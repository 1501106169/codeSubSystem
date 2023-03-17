<script>
import * as monaco from "monaco-editor";
import { Text, toRaw } from "vue";
import http from "/src/dao/index";
import Gantt from "./gantt.vue";

const originCode = "import java.util.Vector;\n\nimport pers.han.scheduler.task.TimeBlock;\nimport pers.han.scheduler.scheduling.SchedulingAlgorithm;\nimport pers.han.scheduler.task.PeriodicTask;\nimport pers.han.scheduler.task.Task;\n\npublic class Algorithm extends SchedulingAlgorithm {\n    /**\n     * 一组实时任务\n     * Vector<Task> taskSet\n     *\n     * 算法运行结束时间\n     * int runEndTime\n     *\n     * 算法运行的时间轴\n     * int timeAxis\n     *\n     * 调度结果\n     * Vector<TimeBlock> schedulingResult\n    */\n    @Override\n    public Vector<TimeBlock> doSchedule() {\n        // write your code in here \n    }\n}\n\n";
// const resDemo = "TIME USAGE: 0.8539325842696629\nAVERAGE RESPONSE TIME: 126.0\nRESPONSE TIME VARIANCE: 148.42975206611575\nFEASIBILITY: FEASIBLE\nEXECTION TIME: 1\nSCHEDULE TIME:\n0--0--10\n1--10--18\n2--28--10\n3--38--20\n0--58--10\n1--68--10\n0--86--10\n1--100--18\n0--120--10\n1--150--18\n0--168--10";

// const resDemo = "FEASIBILITY: FEASIBLE\nEXECTION TIME: 1\nTIME USAGE: 0.8539325842696629\nRESPONSE TIME AVERAGE: 126.0\nRESPONSE TIME VARIANCE: 148.42975206611575\nSUCCESS RATE: 100.0\nFAILURE RATE: 0.0\nSCHEDULE TIME:\n0--0--10\n1--10--18\n2--28--10\n3--38--20\n0--58--10\n1--68--18\n0--86--10\n1--100--18\n0--120--10\n1--150--18\n0--168--10"

export default {
  name: "Edior",
  data() {
    return {
      code: "",
      result: null,
      outShow: false,
      process: false,
      gantt: false,
      editor: null,
      languageList: [
        "Java",
        "C",
        "C++",
        "C#",
        "Go",
        "JavaScript",
        "TypeScript",
      ],
      tasks: null,
    };
  },
  mounted() {
    this.init();
  },
  methods: {
    async onHandelFullscreen() {
      /** 全屏 */
      await this.$refs.container?.requestFullscreen();
      // this.editor.layout();
    },
    async onHandelReduction() {
      /** 还原代码模板 */
      toRaw(this.editor).setValue(originCode);
    },
    init() {
      this.editor = monaco.editor.create(this.$refs.container, {
        value: originCode,
        theme: "vs-dark",
        language: "java",
        autoIndent: "full",
        tabSize: 4,
        automaticLayout: true,
      });
      // 设置代码提示
      // this.editor.language.registerCompletionItemProvider("java", {
      //     provideCompletionItems() {
      //     },
      //     triggerCharacters: ['_', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
      //     'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
      //     'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
      // });
      /** editor内容变化事件 */
      this.editor.onDidChangeModelContent(() => { });
    },
    /** 获取edit内容 */
    getCodeContent() {
      return toRaw(this.editor).getValue();
    },
    changeEditorModel(model) {
      if (this.editor === null) {
        this.init();
      }
      const oldModel = this.editor.getModel();
      const newModel = monaco.editor.createModel(this.code, model);
      this.editor.setModel(newModel);
      if (oldModel) {
        oldModel.dispatch();
      }
    },

    // 将系统返回数据转化为Gant数据
    dealResult(res) {
      // 获取调度部分
      var schedulingRes = res.split('SCHEDULE TIME:')[1].trim();
      var schedulingResArr = schedulingRes.split('\n');
      var tasks = new Array();
      for (var i = 0; i < schedulingResArr.length; ++i) {
        tasks.push(schedulingResArr[i].trim().split('--'));
      }
      return tasks;
    },

    /** 代码调试 */
    onclickDebug(event) {
      this.outShow = true;
      this.process = false;
      this.gantt = true;
    },
    /** 自测执行 */
    selfTestRun(event) {
      this.result = null;
      this.gantt = false;
      this.outShow = true;
      this.process = true;
      let res = http
        .request({
          method: "post",
          url: "/",
          data: {
            codeType: "java",
            code: toRaw(this.editor).getValue(),
          },
        })
        .then((response) => {
          this.result = response.data;
          this.tasks = this.dealResult(this.result);
          console.log(this.tasks);
          this.process = false;
          this.gantt = true;
        })
        .catch((err) => {
          console.log(err);
          this.result = "连接服务器超时！";
          this.process = false;
          this.gantt = false;
        });
    },
    /** 设置输出面板是否显示 */
    onOutResult() {
      this.outShow = !this.outShow;
    },
  },
  components: { Text, Gantt },
};
</script>

<template>
  <div class="h-full flex flex-col">
    <div class="px-[20px] py-[10px] flex justify-between items-center">
      <div>
        <select class="select select-bordered mr-1">
          <option v-for="(lang, index) in languageList" :key="index">
            {{ lang }}
          </option>
        </select>
        <span>核心代码模式</span>
      </div>
      <div>
        <button class="btn btn-sm btn-circle btn-outline mr-1">
          <i-mdi-help-circle />
        </button>
        <button class="btn btn-sm btn-circle btn-outline mr-1">
          <i-mdi-format-list-bulleted />
        </button>
        <button class="btn btn-sm btn-circle btn-outline mr-1">
          <i-mdi-download />
        </button>
        <button class="btn btn-sm btn-circle btn-outline mr-1" @click="onHandelReduction">
          <i-mdi-restart />
        </button>
        <button class="btn btn-sm btn-circle btn-outline" @click="onHandelFullscreen">
          <i-mdi-fullscreen />
        </button>
      </div>
    </div>
    <div ref="container" class="flex-1 min-h-[1px]"></div>
    <div v-if="this.outShow" class="px-[20px] py-[10px] flex" style="
        font-size: 12px;
        border: 2px solid #f0f0f0;
        max-height: 360px;
        overflow: auto;
        flex-direction: column;
      ">
      <progress v-if="this.process == true" class="progress progress-success w-56" style="width: 100%"></progress>
      <div v-if="this.gantt == true" style="height: auto; width: 100%; margin-left: auto; margin-right: auto">
        <!-- <Gantt style="overflow: hidden; max-height: 250px;" :data="tasks"></Gantt> -->
        <Gantt v-bind:tasks="tasks"></Gantt>
      </div>
      <div v-if="this.process == false" style="white-space: pre-wrap; width: 100%">
        <p>{{ result }}</p>
      </div>
    </div>
    <div class="px-[20px] py-[10px] flex">
      <div class="flex-1 btn-group">
        <button class="btn btn-outline btn-sm" @click="onOutResult">
          输出结果
        </button>
        <button class="btn btn-outline btn-sm">运行结果</button>
        <button class="btn btn-outline btn-sm">自测输入</button>
        <button class="btn btn-outline btn-sm">提交记录</button>
      </div>
      <div class="btn-group">
        <button class="btn btn-outline btn-sm" @click="onclickDebug">
          进入调试
        </button>
        <button class="btn btn-success btn-sm" @click="selfTestRun">
          自测运行
        </button>
      </div>
    </div>
  </div>
</template>
