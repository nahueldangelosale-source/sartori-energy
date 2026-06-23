/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./*.html", "./es/*.html"],
  theme: {
    extend: {
      colors: {
        sartori: {
          'navy-deep': '#00072D',
          'navy': '#051650',
          'blue': '#0A2472',
          'teal': '#2A7B88',
          'teal-light': '#92B4BA',
          'amber': '#F59E0B',
          'amber-hover': '#D97706',
        }
      },
      fontFamily: {
        heading: ['Montserrat', 'sans-serif'],
        body: ['Lato', 'sans-serif'],
      },
    },
  },
  plugins: [],
}
