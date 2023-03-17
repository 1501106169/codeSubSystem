/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./src/**/*.{html,js,vue,ts,tsx}'],
  theme: { extend: {} },
  plugins: [require('daisyui')],
  safelist: ['inline-block'],
  daisyui: {
    themes: [
      {
        light: {
          primary: '#36D399',
          secondary: '#F000B8',
          accent: '#37CDBE',
          neutral: '#3D4451',
          'base-100': '#FFFFFF',
          info: '#3ABFF8',
          success: '#36D399',
          warning: '#FBBD23',
          error: '#F87272',
        },
      },
    ],
  },
};
