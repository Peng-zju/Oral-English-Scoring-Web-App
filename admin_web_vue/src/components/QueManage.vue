<template>
    <div class="que_manage">
        <div class="toolbox" align="end" >
            <collapse-transition>
                <div v-show="!isDeleteMode && !isEditMode">
                    <el-button-group >
                        <el-button type="primary" icon="el-icon-document-add" @click="openDialog">添加题目</el-button>
                        <el-button type="primary" icon="el-icon-edit" @click="isEditMode = !isEditMode"></el-button>
                        <el-button type="primary" icon="el-icon-delete" @click="isDeleteMode = !isDeleteMode"></el-button>
                    </el-button-group>
                </div>
            </collapse-transition>
            <collapse-transition>
                <div v-show="isDeleteMode">
                    <el-button-group >
                        <el-button @click="isDeleteMode = false">取消</el-button>
                        <el-button type="danger" icon="el-icon-delete" @click="deleteAlertBox">删除</el-button>
                    </el-button-group>
                </div>
            </collapse-transition>
            <collapse-transition>
                <div v-show="isEditMode">
                    <el-button-group >
                        <el-button @click="isEditMode = false">取消</el-button>
                        <el-button type="primary" icon="el-icon-check">保存更改</el-button>
                    </el-button-group>
                </div>
            </collapse-transition>
        </div>
        <el-table
                :data="tableData"
                :stripe="true"
                :border="true"
                ref = "multipleTable "
                @selection-change="handleSelectionChange">
            <el-table-column type="expand">
                <template slot-scope="props">
                    <el-form label-position="left" :inline="true" class="table-expand">
                        <el-form-item label="ID：">
                            <span>{{ props.row.qid }}</span>
                        </el-form-item>
                        <el-form-item label="地区：">
                            <span>{{ props.row.region_name }}</span>
                        </el-form-item>
                        <el-form-item label="题目类型：">
                            <span>{{ props.row.type_name }}</span>
                        </el-form-item>
                    </el-form>
                    <el-form label-position="left" id="table-expand-block" class="table-expand">
                        <el-form-item label="题目要求：">
                            <span>{{ props.row.requirement }}</span>
                        </el-form-item>
                        <el-form-item label="题目内容：">
                            <span>{{ props.row.body }}</span>
                        </el-form-item>
                        <el-form-item label="题目备注：">
                            <span>{{ props.row.comment }}</span>
                        </el-form-item>
                    </el-form>
                </template>
            </el-table-column>
            <el-table-column
                    label="ID"
                    prop="qid"
                    width="100"
                    :show-overflow-tooltip='true'>
            </el-table-column>
            <el-table-column
                    label="地区"
                    width="100">
                <template slot-scope="scope">
                    <el-tag size="medium">{{ scope.row.region_name }}</el-tag>
                </template>
            </el-table-column>
            <el-table-column
                    label="题目类型"
                    prop="type_name"
                    width="100"
                    :show-overflow-tooltip='true'>
            </el-table-column>
            <el-table-column
                    label="题目要求"
                    prop="requirement"
                    width="220"
                    :show-overflow-tooltip='true'>
            </el-table-column>
            <el-table-column
                    label="题目内容"
                    prop="body"
                    width="440"
                    :show-overflow-tooltip='true'>
            </el-table-column>
            <el-table-column
                    label="题目备注"
                    prop="comment"
                    :show-overflow-tooltip='true'>
            </el-table-column>

            <el-table-column
                    v-if="isDeleteMode"
                    type="selection"
                    width="50">
            </el-table-column>

            <el-table-column
                    v-if="isEditMode"
                    width="56">
                <template slot-scope="scope">
                    <el-button type="text" @click="editQu(scope.row)">编辑</el-button>
                </template>
            </el-table-column>
        </el-table>

        <que-dialog ref="child">

        </que-dialog>
    </div>
</template>

<script>
    import CollapseTransition from 'element-ui/lib/transitions/collapse-transition';
    import QueDialog from "@/components/QueDialog";
    export default {
        name: "QueManage",
        data() {
            return {
                tableData: [],
                isDeleteMode: false,
                isEditMode: false,
                multipleSelection: [],
            }
        },
        created: function (){
            this.getAllQuest();
        },
        components: {CollapseTransition, QueDialog},
        methods: {
            getAllQuest() {
                let that = this;
                this.$http.get('get_all_questions')
                    .then(function (response) {
                        that.tableData = response.data
                    })
            },
            deleteAlertBox() {
                this.$confirm('此操作将永久删除已选择的题目, 是否继续?', {
                    confirmButtonText: '确认删除',
                    cancelButtonText: '取消',
                    type: 'warning'
                }).then(() => {
                    this.deleteQuestions();
                    this.isDeleteMode = false;
                }).catch(() => {
                    this.isDeleteMode = false;
                    this.$message({
                        type: 'info',
                        message: '已取消删除'
                    });
                });
            },
            handleSelectionChange(val) {
                this.multipleSelection = val;
            },
            deleteQuestions() {
                let that = this;
                let rids = '';
                for(let item of this.multipleSelection) {
                    rids += item.qid + ', ';
                }
                this.$http.post('delete_questions', rids.substr(0,rids.length - 2))
                    .then(function () {
                        that.$message({
                            type: 'success',
                            message: '删除题目成功！'
                        });
                        that.getAllQuest()
                    })
                    .catch(function(error) {
                        that.$message({
                            type: 'error',
                            message: '删除题目失败！' + error
                        });
                    });
            },
            openDialog() {
                this.$refs.child.open('添加新题目', false);
            },
            editQu(row) {
                this.$refs.child.open('编辑题目', true, row);
            }
        }
    }

</script>

<style scoped>
    .el-table{
        font-size: 12px;
        width: 100%;
        box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04)
    }
    .table-expand label {
        width: 90px;
        color: #99a9bf;
    }
    .table-expand .el-form-item {
        margin-right: 0;
        margin-bottom: 0;
        width: 33%;
    }
    #table-expand-block .el-form-item{
        width: 100%;
    }
    .toolbox{
        margin-top: 20px;
        margin-bottom: 20px;
    }

   /* .v-enter, .v-leave-to {
        opacity: 0;
        transform: translateX(100px);
    }
    .v-enter-active, .v-leave-active {
        transition: all 0.5s ease;
    }*/
</style>