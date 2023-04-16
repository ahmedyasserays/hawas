/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./**/*.{html,js}"],
  theme: {
    extend: {
      fontFamily: {
        'roboto': ['Roboto', 'sans-serif']
      },
      colors: {
        dominant: "#fb923c",
        secondary: "#f6f1ef",
        third: "#795548",

        pri: "#e3caab",
        cone: "#E0C097",
        ctwo: "#B85C38",
        cthree: "#5C3D2E",
        cfour: "#2D2424",

        facebook: "#3b5998",
        google: "#CF5844"
      },
      container: {
        center: true,
        padding: "1rem",
      },
    },
  },
  plugins: [],
}