const { addDynamicIconSelectors } = require('@iconify/tailwind')

module.exports = {
  content: [
    "./templates/**/*.html",
  ],
  theme: {
    extend: {}
  },
  variants: {},
  plugins: [
    require("flyonui"),
    require('@tailwindcss/typography'),
    addDynamicIconSelectors()
  ]
};