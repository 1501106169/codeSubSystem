<script setup>
import { defineProps, toRef } from 'vue';
import { copyText, showAlert } from '@/utils/index';

const props = defineProps({
  question: {
    type: Object,
    required: true,
  },
  questionArr: {
    type: Object,
    required: true,
  },
});

const question = toRef(props, 'question');

const onHandleCopy = async (text) => {
  const isSuccess = copyText(
    typeof text === 'string' ? text : JSON.stringify(text, null, 2)
  );
  if (isSuccess) {
    showAlert({
      message: '已复制到剪贴板',
      type: 'success',
      duration: 20000,
    });
  } else {
    showAlert({
      message: '复制失败',
      type: 'error',
    });
  }
};

const selectChange = async (event) => {
  // 拿到任务序号
  console.log(event.target.value);
  question = null;
};

</script>

<template>
  <div class="flex-1 m-[20px] p-[20px] bg-base-100 rounded flex flex-col">
    <div>
      <div class="flex justify-between items-center">
        <!-- <h1 class="text-xl font-bold">{{ question.title }}</h1> -->
        <select class="select select-ghost w-full max-w-xs select-lg" style="font-size: 22px; font-weight: bold;" @change="selectChange">
          <option v-for="(item, index) in questionArr" v-bind:value="index">{{ item }}</option>
        </select>
        <div>
          <button class="btn btn-sm btn-circle btn-outline mr-1"><i-mdi-edit /></button>
          <button class="btn btn-sm btn-circle btn-outline mr-1"><i-mdi-star-outline /></button>
          <button class="btn btn-sm btn-circle btn-outline mr-1"><i-mdi-share /></button>
          <button class="btn btn-sm btn-circle btn-outline"><i-mdi-warning /></button>
        </div>
      </div>
      <div class="btn-group my-[10px]">
        <input type="radio" name="options" data-title="题目" class="btn btn-outline" checked />
        <input type="radio" name="options" data-title="解题" class="btn btn-outline" />
        <input type="radio" name="options" data-title="讨论" class="btn btn-outline" />
        <input type="radio" name="options" data-title="排名" class="btn btn-outline" />
        <input type="radio" name="options" data-title="面经" class="btn btn-outline" />
      </div>
    </div>
    <div class="flex-1 h-full overflow-auto grid grid-cols-[1fr] gap-y-[20px]">
      <div class="opacity-[0.5]">
        <div class="flex justify-between">
          <span>难度：{{ question.difficulty }}</span>
          <span class="flex items-center">
            <i-mdi-send-check />
            通过率：{{ question.passRate }}%
          </span>
          <span class="flex items-center">
            <i-mdi-timer-outline /> 时间限制：{{ question.timeLimit }} 秒
          </span>
          <span class="flex items-center">
            <i-mdi-memory /> 内存限制：{{ question.memoryLimit }} MB
          </span>
        </div>
        <div>
          知识点：
          <span class="badge badge-outline" v-for="(tag, index) in question.tags" :key="index">{{ tag }}</span>
        </div>
      </div>
      <div>
        <h2 class="text-xl">描述</h2>
        <div v-if="question.detail.text" v-html="question.detail.text.replace(/\n/g, '<br/>')" />
        <img v-if="question.detail.img" :src="question.detail.img" />
      </div>
      <div v-for="(item, index) in question.cases" :key="index">
        <h2 class="text-xl">示例{{ index + 1 }}</h2>
        <div class="p-[10px] bg-base-200">
          <div style="white-space: pre-wrap;">
            输入：{{ item.input }}
            <button @click="onHandleCopy(item.input)">
              <i-mdi-content-copy />
            </button>
          </div>
          <div style="white-space: pre-wrap;">
            输出：{{ item.output }}
            <button @click="onHandleCopy(item.output)">
              <i-mdi-content-copy />
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
