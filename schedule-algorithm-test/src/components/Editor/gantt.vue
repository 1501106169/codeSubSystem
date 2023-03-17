<script>
const START_X = 30;
const START_Y = 20;
const BAR_WIDTH = 20;
const BAR_GAP = 20;
const PROCESS = 2;
const LINE_WIDTH = 1.0;

const COLOR = [
  "#FF0000", // 红色
  "#00FF00", // 绿色
  "#0000FF", // 蓝色
  "#FF00FF", // 紫色
  "#FFFF00", // 黄色
  "#00FFFF", //
  // "#FFFFFF"	// 白色
  "#000000", // 黑色
];

export default {
  name: "Gantt",
  data() {
    return {
    };
  },
  props: {
    tasks: {
      type: Object,
      default: null,
      required: true
    }
  },

  mounted() {
    this.drawGantt();
  },

  methods: {
    // 左上角起始 横x 竖y

    // 绘制甘特图
    drawGantt() {
      const canvas = this.$refs.gantt;
      const ctx = canvas.getContext("2d");
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      if (this.tasks == null || this.tasks.length == 0) {
        return;
      }
      var maxId = 0;
      var axis = 0;
      this.tasks.forEach((ele) => {
        maxId = maxId > parseInt(ele[0]) ? maxId : parseInt(ele[0]);
        axis =
          axis > parseInt(ele[1]) + parseInt(ele[2])
            ? axis
            : parseInt(ele[1]) + parseInt(ele[2]);
        this.drawBlock(parseInt(ele[0]), parseInt(ele[1]), parseInt(ele[2]));
        this.drawText(parseInt(ele[0]), parseInt(ele[1]) + parseInt(ele[2]));
      });

      this.drawAxis(maxId, axis);
      this.drawTask(maxId);
    },

    // 绘制时间轴
    drawAxis(taskNum, axis) {
      const canvas = this.$refs.gantt;
      const ctx = canvas.getContext("2d");
      for (var i = 0; i <= taskNum; ++i) {
        ctx.beginPath();
        ctx.moveTo(
          START_X,
          START_Y + BAR_WIDTH * (i + 1) + BAR_GAP * i + LINE_WIDTH
        );
        ctx.lineTo(
          START_X + PROCESS * axis,
          START_Y + BAR_WIDTH * (i + 1) + BAR_GAP * i + LINE_WIDTH
        );
        ctx.closePath();
        ctx.strokeStyle = "#000000";
        ctx.lineWidth = 0.5;
        ctx.stroke();
        ctx.beginPath();
        ctx.moveTo(
          START_X - LINE_WIDTH,
          START_Y + BAR_WIDTH * (i + 1) + BAR_GAP * i + LINE_WIDTH + LINE_WIDTH
        );
        ctx.lineTo(
          START_X - LINE_WIDTH,
          START_Y + (BAR_WIDTH + BAR_GAP) * i + LINE_WIDTH - BAR_GAP / 2
        );
        ctx.closePath();
        ctx.strokeStyle = "#000000";
        ctx.lineWidth = 0.5;
        ctx.stroke();
      }
    },

    // 绘制时间块
    drawBlock(id, startTime, execTime) {
      const canvas = this.$refs.gantt;
      const ctx = canvas.getContext("2d");
      ctx.fillStyle = COLOR[id % COLOR.length];
      ctx.fillRect(
        START_X + PROCESS * startTime,
        START_Y + (BAR_WIDTH + BAR_GAP) * id,
        PROCESS * execTime,
        BAR_WIDTH
      );
    },

    // 绘制时间
    drawText(id, endTime) {
      const canvas = this.$refs.gantt;
      const ctx = canvas.getContext("2d");
      ctx.font = "10px serif";
      ctx.fillStyle = "#000000";
      ctx.fillText(
        endTime,
        START_X + PROCESS * endTime,
        START_Y + BAR_WIDTH + (BAR_WIDTH + BAR_GAP) * id + 10
      );
    },

    // 绘制任务编号
    drawTask(taskNum) {
      const canvas = this.$refs.gantt;
      const ctx = canvas.getContext("2d");
      ctx.font = "15px serif";
      ctx.fillStyle = "#000000";
      for (var i = 0; i <= taskNum; ++i) {
        ctx.fillText(
          "T" + i,
          START_X - 25,
          START_Y + (BAR_WIDTH + BAR_GAP) * i + 15
        );
      }
    },
  },
};
</script>

<template>
  <!-- <div style="width: 100%; height: 100%;">
    <canvas ref="gantt" id="gantt" style="width: auto; height: auto; border-width: 2px;"></canvas>
  </div> -->
  <div class="w-full h-[200px] overflow-auto">
    <canvas ref="gantt" id="gantt" :width="1000" :height="400"></canvas>
  </div>
</template>
