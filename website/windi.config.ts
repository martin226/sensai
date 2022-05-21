import { defineConfig } from '@windicss/plugin-utils';

export default defineConfig({
  /**
   * Write windi classes in html attributes.
   * @see https://windicss.org/features/attributify.html
   */
  attributify: true,
  plugins: [require('windicss/plugin/forms')],
  theme: {
    extend: {
      colors: {
        primary: '#5C946E',
        secondary: '#FFFFFF',
        tertiary: '#2A2D34',
      },
    },
  },
});
