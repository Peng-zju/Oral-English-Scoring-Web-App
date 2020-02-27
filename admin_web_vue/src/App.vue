<template>
  <div id="app">
    <router-view/>
  </div>
</template>
<script>
  export default {
    name: "app",
  }
</script>
<style>
  #app{
    height: 100%;
    width: 1280px;
    margin: 0 auto;
  }
  html,body{
    height: 100%;
    margin: 0;}
  .el-dialog__body{
    padding-bottom: 0 !important;
  }
  .el-divider__text{
    font-size: 8px!important;
    color: #909399!important;
    width: 160px;
    text-align: center;
  }
</style>
