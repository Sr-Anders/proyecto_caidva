from flask import Flask, render_template, request, redirect, url_for, session, flash, send_file
import mysql.connector
import os
from werkzeug.utils import secure_filename
from reportlab.pdfgen import canvas

app = Flask(__name__)
app.secret_key = 'clave_secreta_segura_caidva'

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '*/NiGG4/M4n/102/*',
    'database': 'caidva_db'
}

def get_db():
    return mysql.connector.connect(**db_config)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        correo = request.form['correo']
        password = request.form['password']
        
        conn = get_db()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM usuario WHERE correo = %s AND password = %s", (correo, password))
        user = cursor.fetchone()
        cursor.close()
        conn.close()
        
        if user:
            session['user_id'] = user['id']
            session['rol'] = user['rol']
            session['correo'] = user['correo']
            if user['rol'] == 'administrador':
                return redirect(url_for('dashboard'))
            else:
                return redirect(url_for('index'))
        else:
            flash('Correo o contraseña incorrectos.', 'danger')
    return render_template('login.html')

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        correo = request.form['correo']
        password = request.form['password']
        ced_alum = request.form['ced_alum']
        fec_nac = request.form['fec_nac']
        linea_atencion = request.form['linea_atencion']
        tel_alum = request.form['tel_alum']
        
        # Manejo del archivo del informe médico
        file = request.files.get('informe_medico')
        inf_med_path = ""
        
        if file and file.filename != '':
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            inf_med_path = file_path
        
        conn = get_db()
        cursor = conn.cursor()
        try:
            # 1. Crear el usuario para poder iniciar sesión posteriormente
            cursor.execute("""
                INSERT INTO usuario (correo, password, rol) 
                VALUES (%s, %s, %s)
            """, (correo, password, 'usuario'))

            cod_ins_edu = None
            grado_con_alum = linea_atencion

            # 2. Si seleccionó Integración Escolar, guardamos los datos del instituto
            if linea_atencion == "Integración Escolar":
                nom_ins = request.form['nom_ins']
                rif_ins = request.form['rif_ins']
                grado_escolar = request.form['grado_escolar']
                grado_con_alum = f"Integración: {grado_escolar}"

                cursor.execute("""
                    INSERT INTO instituto (NomInsEdu, RifInsEdu, NumTellInsEdu) 
                    VALUES (%s, %s, %s)
                """, (nom_ins, rif_ins, tel_alum))
                cod_ins_edu = cursor.lastrowid

            # 3. Guardar los datos del estudiante
            cursor.execute("""
                INSERT INTO alumno (CedAlum, CodInsEdu, FecNacAlum, GradoConAlum, InfMedAlum, NumTelAlum) 
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (ced_alum, cod_ins_edu, fec_nac, grado_con_alum, inf_med_path, tel_alum))
            
            conn.commit()
            flash('¡Registro completado con éxito! Ahora puede iniciar sesión con su correo y contraseña.', 'success')
            return redirect(url_for('login'))
        except Exception as e:
            conn.rollback()
            flash(f'Error en el registro: {e}', 'danger')
        finally:
            cursor.close()
            conn.close()
            
    return render_template('registro.html')

@app.route('/dashboard')
def dashboard():
    if 'rol' in session and session['rol'] == 'administrador':
        conn = get_db()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM alumno")
        alumnos = cursor.fetchall()
        cursor.close()
        conn.close()
        return render_template('dashboard.html', alumnos=alumnos)
    return redirect(url_for('login'))

@app.route('/generar_pdf')
def generar_pdf():
    if 'rol' in session and session['rol'] == 'administrador':
        buffer = io.BytesIO()
        p = canvas.Canvas(buffer, pagesize=letter)
        
        p.drawString(100, 750, "REPÚBLICA BOLIVARIANA DE VENEZUELA")
        p.drawString(100, 735, "CENTRO DE ATENCIÓN INTEGRAL DE DEFICIENCIAS VISUALES ANZOÁTEGUI (CAIDVA)")
        p.drawString(100, 710, "REPORTE OFICIAL DE MATRÍCULA Y ESTUDIANTES")
        
        conn = get_db()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM alumno")
        alumnos = cursor.fetchall()
        cursor.close()
        conn.close()
        
        y = 670
        for alum in alumnos:
            p.drawString(100, y, f"Cédula: {alum['CedAlum']} - Grado/Línea: {alum['GradoConAlum']} - Tel: {alum['NumTelAlum']}")
            y -= 25
            if y < 50:
                p.showPage()
                y = 750
                
        p.save()
        buffer.seek(0)
        return send_file(buffer, as_attachment=True, download_name="reporte_caidva.pdf", mimetype='application/pdf')
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)