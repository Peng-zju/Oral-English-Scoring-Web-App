<template>
    <div class="navBar">
        <h3 style="display: inline-block; color: #909399" >Winter Project 后台管理系统</h3>
        <el-menu default-active="1" mode="horizontal" @select="handleSelect" active-text-color="#409EFF">
            <el-menu-item index="1">题库管理</el-menu-item>
            <el-menu-item index="2">题目类型管理</el-menu-item>
            <el-menu-item index="3">地区管理</el-menu-item>
        </el-menu>
    </div>
</template>

<script>
    export default {
        name: "NavBar"
    }
</script>

<style scoped>

</style>