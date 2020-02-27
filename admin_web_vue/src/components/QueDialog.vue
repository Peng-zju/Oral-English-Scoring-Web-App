<template>
    <el-dialog :title="title" :visible.sync="dialogFormVisible" :close-on-click-modal="false" width="30%">
        <el-form ref="qu_form" label-position="left" :model="form" label-width="80px">
            <el-form-item label="题目信息">
                <el-col :span="12">
                    <el-select :disabled="disabled" v-model="form.rid" placeholder="请选择地区" @click.native="getAllRegions">
                        <el-option
                                v-for="item in regions"
                                :key="item.rid"
                                :label="item.region_name"
                                :value="item.rid">
                            <span style="float: left">{{ item.region_name }}</span>
                            <span style="float: right; color: #8492a6; font-size: 13px">{{ item.rid }}</span>
                        </el-option>
                    </el-select>
                </el-col>
                <el-col :span="12">
                    <el-select :disabled="disabled" label="题目类型" v-model="form.type_id" placeholder="请选择题目类型" @click.native="getTypes">
                        <el-option
                                v-for="item in question_types"
                                :key="item.type_id"
                                :label="item.type_name"
                                :value="item.type_id">
                        </el-option>
                    </el-select>
                </el-col>
            </el-form-item>
            <br>
            <el-form-item label="题目要求">
                <el-input v-model="form.requirement"></el-input>
            </el-form-item>
            <br>
            <el-form-item label="题目内容">
                <el-input :rows="7" type="textarea" v-model="form.body"></el-input>
            </el-form-item>
            <br>
            <el-form-item label="备注">
                <el-input v-model="form.comment"></el-input>
            </el-form-item>

        </el-form>
        <div slot="footer" class="dialog-footer">
            <el-button @click="dialogFormVisible = false">取 消</el-button>
            <el-button type="primary" @click="dialogFormVisible = false" @click.native="disabled === true ? editQuestion() : postNewQuestion()">确 定</el-button>
        </div>
    </el-dialog>
</template>

<script>
    export default {
        name: "QueDialog",
        data() {
            return {
                dialogFormVisible: false,
                form: {
                    qid: '',
                    rid: '',
                    type_id:'',
                    requirement: '',
                    body: '',
                    comment: ''
                },
                regions: [],
                question_types: [],
                title: '',
                disabled: false
            }
        },
        methods: {
            open(title, isEdit, form) {
                this.title = title;
                this.disabled = false;
                if(isEdit) {
                    this.disabled = true;
                    this.form = form;
                }
                this.dialogFormVisible = true;
            },
            getAllRegions() {
                let that = this;
                this.$http.get('get_all_regions')
                    .then(function (response) {
                        that.regions = response.data
                    })
            },
            getTypes() {
                let that = this;
                this.$http.get('get_types/' + this.form.rid)
                    .then(function (response) {
                        that.question_types = response.data
                    })
            },
            postNewQuestion() {
                let that = this;
                this.$http.post('post_question', this.form)
                    .then(function () {
                        that.$message({
                            type: 'success',
                            message: '添加题目成功！'
                        });
                        that.$parent.getAllQuest();
                        that.$refs.qu_form.resetFields();
                    })
                    .catch(function(error) {
                        that.$message({
                            type: 'error',
                            message: '添加题目失败！' + error
                        });
                    });
            },
            editQuestion() {
                let that = this;
                this.$http.post('edit_question', this.form)
                    .then(function () {
                        that.$message({
                            type: 'success',
                            message: '修改题目成功！'
                        });
                        that.$parent.getAllQuest();
                        that.$refs.qu_form.resetFields();
                    })
                    .catch(function(error) {
                        that.$message({
                            type: 'error',
                            message: '修改题目失败！' + error
                        });
                    });
            }
        }
    }
</script>

<style scoped>
    .el-form {
        margin: 0 auto;
        width: 90%;
    }
</style>