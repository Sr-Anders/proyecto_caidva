/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: "class",
  content: [
    "./templates/**/*.html",
    "./static/**/*.js"
  ],
  theme: {
    extend: {
      colors: {
        "on-primary": "#ffffff",
        "on-background": "#191c1e",
        "on-secondary": "#ffffff",
        "tertiary-fixed-dim": "#b7c8e1",
        "on-tertiary": "#ffffff",
        "surface-container-low": "#f2f4f6",
        "primary-fixed-dim": "#bec6e0",
        "on-secondary-fixed": "#001a42",
        "surface-bright": "#f7f9fb",
        "on-tertiary-fixed": "#0b1c30",
        "primary-container": "#131b2e",
        "primary-fixed": "#dae2fd",
        "on-tertiary-fixed-variant": "#38485d",
        "surface-container": "#eceef0",
        "surface-container-high": "#e6e8ea",
        "on-surface-variant": "#45464d",
        "outline": "#76777d",
        "error-container": "#ffdad6",
        "inverse-surface": "#2d3133",
        "on-error": "#ffffff",
        "outline-variant": "#c6c6cd",
        "tertiary": "#000000",
        "surface-variant": "#e0e3e5",
        "surface-container-lowest": "#ffffff",
        "on-primary-fixed-variant": "#3f465c",
        "tertiary-container": "#0b1c30",
        "on-primary-container": "#7c839b",
        "surface-container-highest": "#e0e3e5",
        "surface-dim": "#d8dadc",
        "secondary": "#0058be",
        "on-secondary-fixed-variant": "#004395",
        "on-error-container": "#93000a",
        "error": "#ba1a1a",
        "surface-tint": "#565e74",
        "surface": "#f7f9fb",
        "primary": "#000000",
        "on-secondary-container": "#fefcff",
        "on-surface": "#191c1e",
        "on-primary-fixed": "#131b2e",
        "secondary-fixed-dim": "#adc6ff",
        "inverse-primary": "#bec6e0",
        "inverse-on-surface": "#eff1f3",
        "secondary-container": "#2170e4",
        "on-tertiary-container": "#75859d",
        "background": "#f7f9fb",
        "secondary-fixed": "#d8e2ff",
        "tertiary-fixed": "#d3e4fe"
      },
      borderRadius: {
        "DEFAULT": "0.125rem",
        "lg": "0.25rem",
        "xl": "0.5rem",
        "full": "0.75rem"
      },
      spacing: {
        "stack-lg": "32px",
        "card-padding": "20px",
        "stack-sm": "8px",
        "gutter": "16px",
        "base": "4px",
        "container-margin": "24px",
        "stack-md": "16px"
      },
      fontFamily: {
        "label-md": ["Inter"],
        "headline-sm": ["Inter"],
        "headline-lg": ["Inter"],
        "label-sm": ["Inter"],
        "body-md": ["Inter"],
        "headline-md": ["Inter"],
        "headline-lg-mobile": ["Inter"],
        "body-lg": ["Inter"]
      },
      fontSize: {
        "label-md": ["12px", { "lineHeight": "16px", "letterSpacing": "0.05em", "fontWeight": "600" }],
        "headline-sm": ["20px", { "lineHeight": "28px", "fontWeight": "600" }],
        "headline-lg": ["30px", { "lineHeight": "38px", "letterSpacing": "-0.02em", "fontWeight": "700" }],
        "label-sm": ["11px", { "lineHeight": "14px", "fontWeight": "500" }],
        "body-md": ["14px", { "lineHeight": "20px", "fontWeight": "400" }],
        "headline-md": ["24px", { "lineHeight": "32px", "letterSpacing": "-0.01em", "fontWeight": "600" }],
        "headline-lg-mobile": ["24px", { "lineHeight": "32px", "fontWeight": "700" }],
        "body-lg": ["16px", { "lineHeight": "24px", "fontWeight": "400" }]
      }
    }
  },
  plugins: []
};