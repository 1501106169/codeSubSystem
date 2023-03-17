<script setup>
import Editor from '@/components/Editor/editor.vue';
import TheHeader from './components/the-header.vue';
import QuestionPanel from './components/question-panel.vue';
import { createConditionalExpression } from '@vue/compiler-core';

const questionArr = [
  "周期任务调度",
  "非周期任务调度",
  "偶发任务调度",
  "Round-Robin",
  "FIFO",
  "LIFO",
  "抢占式EDF",
  "抢占式LST",
  "抢占式RM",
  "抢占式DM",
  "SRTF",
  "LRTF",
  "EDF",
  "LST",
  "RM",
  "DM",
  "SJF",
  "LJF"
];

const question = {
  title: '周期性任务调度',
  difficulty: '中等',
  tags: ['周期性任务', "不可抢占"],
  passRate: 40.21,
  timeLimit: 1,
  memoryLimit: 64,
  detail: {
    // text: 'Culpa laborum et. Ad veniam iste incidunt aut autem ducimus nemo. Voluptatem officiis est est nobis explicabo. \n Velit ut possimus necessitatibus sunt facere voluptas excepturi dolores. Nemo qui sint nisi sequi rerum repellendus. Voluptatem laborum voluptas doloribus dicta ut in accusantium error. Consectetur saepe praesentium blanditiis ratione sint ad at. Dignissimos est eligendi possimus repudiandae rerum ipsam suscipit necessitatibus odit.\nAccusantium provident tenetur aspernatur ipsum corrupti vitae officiis. Qui quasi sapiente. Dolorem est eveniet.',
    text: '给定一组实时任务, 请你编写出一种可以有效调度该组实时任务的实时调度算法。\n类SchedulingAlgorithm中的成员变量在代码模板中已给出, 你需要实现继承自SchedulingAlgorithm类的Algorithm类, 并重写其中的doSchedule()方法。\n * taskSet: 一组实时任务\n * runEndTime: 算法运行截止时间\n * timeAxis: 算法运行时间轴\n * schedulingResult: 算法执行结果\n',
    img: '',
  },
  cases: [
    {
      input: "\nt0: (0, 40, 10, 40)\nt1: (0, 50, 18, 50)\nt2: (0, 200, 10, 200)\nt3: (0, 200, 20, 200)",
      output: "(0, 0, 10), (1, 10, 18), (2, 28, 10), (3, 38, 20), (0, 58, 10), (1, 68, 18), (0, 86, 10), (1, 100, 18), (0, 120, 10), (1, 150, 18), (0, 168, 10)",
    },
    // {
    //   input: [2, 4, 5, 4, 5, 3, 239, 372, 30, 3, 4],
    //   output: [4, 3, 30, 372, 239, 3, 5, 4, 5, 4, 2],
    // },
  ],
};
</script>

<template>
  <div class="h-screen flex flex-col">
    <TheHeader />
    <main class="flex-1 min-h-[1px] flex bg-base-200">
      <QuestionPanel :question="question" :questionArr="questionArr" />
      <div class="m-[20px] bg-base-100 rounded w-[calc(50%-20px)] m-[20px] ml-0">
        <Editor></Editor>
      </div>
    </main>
  </div>
</template>
