# Client

 * [Chinese Manual](https://github.com/1501106169/codeSubSystem/tree/master/schedule-algorithm-test)
 * [English Manual](https://github.com/1501106169/codeSubSystem/blob/master/schedule-algorithm-test/README-en.md)

## Development

### Development Environment

 * npm v7.18.1
 * vue v3.2.37

### Running

1. Enter `npm install` in terminal to install the dependency package.
2. Enter `npm run dev` to run the project.
3. The project uses a third-party `monaco-editor` package。If it causes an error about `monaco-editor`, you can try to solve it with the following command.
```
npm install -g cnpm
npm install monaco-editor --save
npm install monaco-editor-webpack-plugin --save
cnpm install vite-plugin-monaco-editor --save-dev
```

### Third Party Library

- CSS and UI Solution

  - [https://tailwindcss.com/](https://tailwindcss.com/)
  - [https://daisyui.com/](https://daisyui.com/)

- Icon Solution

  The icon is already configured in `vite.config.js` and can be used in the page without introducing it. Such as：`<i-mdi-home/>`，icon set reference [https://icon-sets.iconify.design/mdi/](https://icon-sets.iconify.design/mdi/)


## Deployment

Technical documentation for the deployment is not available at this time.
