<script>
import gantt from 'dhtmlx-gantt';
import 'dhtmlx-gantt/codebase/dhtmlxgantt.css';

export default {
  name: 'Gantt',
  props: {
    tasks: {
      type: Object,
      default() {
        return { data: [], links: [] }
      }
    }
  },
  
  mounted() {
    gantt.i18n.setLocale('cn');

    //自适应甘特图的尺寸大小, 使得在不出现滚动条的情况下, 显示全部任务
    gantt.config.autosize = true;
    //只读模式：打开后不可以操作甘特图
    gantt.config.readonly = true;
    //是否显示左侧树表格
    gantt.config.show_grid = true;
    //表格列设置：我们在后台获取数据后，会解析到这个表格列中，这里面会含有很多隐藏列，作用是甘特图中不需要看隐藏列，但当我们获取甘特图的任务时，这些隐藏列会跟随任务方便使用
    gantt.config.columns = [
      {
        //最左侧新增符号列，甘特图内置可选使用列
        name: 'add',
        hide: true
      },
      {
        name: 'id',
        label: '任务编号',
        hide: true,
        align: 'center',
        // tree: true,
        width: '100'
      },
      {
        name: 'text',
        label: '任务编号',
        align: 'center',
        width: '100'
      },
      {
        name: 'start_date',
        label: '开始时间',
        align: 'center',
        width: '100'
      },
      {
        name: 'duration',
        label: '执行时间',
        align: 'center',
        width: '100'
      }
    ];
    //自适应
    //gantt.config.fit_tasks = true;

    //表头高度
    // gantt.config.scale_height = 50;

    //开启提示：鼠标悬浮在gantt行上显示
    gantt.plugins({
      tooltip: true
    });

    //禁用双击事件
    // gantt.config.details_on_dblclick = false;
    //关闭所有错误提示信息：gantt有自己的异常消息，如果不关闭可能页面会弹出异常消息
    gantt.config.show_errors = false;
    //禁止拖动任务
    // gantt.config.drag_move = false;
    //禁止拖动任务进度
    // gantt.config.drag_progress = false;
    //禁止拖放添加Link
    // gantt.config.drag_links = false;

    //开启标记
    gantt.plugins({
      marker: true
    });

    // gantt.config.xml_data = '%Y-%m-%d';
    gantt.init(this.$refs.gantt);
    gantt.parse(this.$props.tasks);
  },

  methods: { },
};
</script>

<template>
  <div ref="gantt"></div>
</template>
