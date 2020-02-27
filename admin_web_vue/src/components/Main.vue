<template>
    <el-container class="main">
        <el-header class="header">
            <h3 style="display: inline-block; color: #909399" >Winter Project 后台管理系统</h3>
            <el-menu router default-active="que_manage" mode="horizontal" @select="handleSelect" active-text-color="#409EFF">
                <el-menu-item index="que_manage">题库管理</el-menu-item>
                <el-menu-item index="region_manage">地区题型管理</el-menu-item>
            </el-menu>
        </el-header>
        <router-view/>
    </el-container>
</template>

<script>
    export default {
        name: "Main",
        methods: {
            handleSelect(){
            }
        }
    }
</script>

<style scoped>
    .el-menu .el-menu-item {
        float: right;
    }
    .el-menu{
        width: 75%;
        display: inline-block;
        float: right;
    }
    .header {
        margin-bottom: 20px;
        box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
    }
</style>