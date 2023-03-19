# 客户端

 * [中文文档](https://github.com/1501106169/codeSubSystem/tree/master/schedule-algorithm-test)
 * [英文文档](https://github.com/1501106169/codeSubSystem/blob/master/schedule-algorithm-test/README-en.md)

## 开发

### 开发环境

 * npm v7.18.1
 * vue v3.2.37

### 开发运行

1. 在terminal输入`npm install`安装依赖包。
2. 输入`npm run dev`运行项目。
3. 项目使用第三方`monaco-editor`插件。若引起有关`monaco-editor`的错误问题，可以尝试使用如下命令解决。
```
npm install -g cnpm
npm install monaco-editor --save
npm install monaco-editor-webpack-plugin --save
cnpm install vite-plugin-monaco-editor --save-dev
```

### 第三方库

- CSS 和 UI 解决方案

  - [https://tailwindcss.com/](https://tailwindcss.com/)
  - [https://daisyui.com/](https://daisyui.com/)

- Icon 解决方案

  已在 vite.config.js 中配置，无需引入直接在页面中使用即可。如：`<i-mdi-home/>`，图标集参考 [https://icon-sets.iconify.design/mdi/](https://icon-sets.iconify.design/mdi/)


## 部署

暂不提供部署技术文档。
