import { createVNode, render } from 'vue';
import template from './index.vue';

export const showAlert = ({ message, type = 'info', duration = 2000 }) => {
  const root = document.querySelector('#app');
  if (!root) {
    return;
  }

  const container = document.createElement('div');
  const instance = createVNode(template, {
    message,
    type,
  });
  render(instance, container);

  root.appendChild(container);
  setTimeout(() => {
    root.removeChild(container);
  }, duration);
};
