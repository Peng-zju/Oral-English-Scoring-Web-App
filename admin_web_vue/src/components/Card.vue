<template>
    <el-card>
        <div slot="header" class="head">
            <span>{{card_title}}</span>
            <el-button-group style="float: right">
                <el-button size="small" type="primary" icon="el-icon-plus" @click="openDialog">添加</el-button>
                <el-button size="small" type="primary" icon="el-icon-delete"></el-button>
            </el-button-group>
        </div>
        <slot></slot>

    </el-card>
</template>

<script>
    export default {
        name: "Card",
        props: ['card_title'],
        methods: {
            openDialog() {
                if(this.card_title === '地区管理') {
                    this.$parent.showDialog1();
                }
                else {
                    this.$parent.showDialog2();
                }
            }
        }
    }
</script>

<style scoped>
    .head {
        font-size: 18px;
        font-weight: bold;
        color: #909399;
        padding-left: 6px;
        height: 32px;
    }
</style>