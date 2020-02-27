<template>
    <div class="region_manage" >
        <div>
            <card class="card1" card_title="地区管理">
                <el-table
                        :data="tableData"
                        max-height="600"
                        highlight-current-row
                        @current-change="handleCurrentChange">
                    <el-table-column
                            prop="rid"
                            label="地区编号"
                            width="100">
                    </el-table-column>
                    <el-table-column
                            prop="region_name"
                            label="地区名称"
                            width="100">
                    </el-table-column>
                    <el-table-column
                            prop="bank_count"
                            label="题型类别"
                            width="100">
                    </el-table-column>
                </el-table>
            </card>

            <card class="card2" card_title="题型管理" button_title="添加新题型">
                <el-table
                        :data="tableData2"
                        max-height="600">
                    <el-table-column
                            prop="type_id" label="题型编号"
                            width="100">
                    </el-table-column>
                    <el-table-column
                            prop="type_name"
                            label="题型名称"
                            width="100">
                    </el-table-column>
                    <el-table-column
                            label="操作"
                            width="100">
                        <template slot-scope="scope">
                            <el-button @click="handleClick(scope.row)" type="text" size="small">查看</el-button>
                            <el-button type="text" size="small">编辑</el-button>
                        </template>
                    </el-table-column>
                </el-table>
            </card>
        </div>

        <el-dialog title="添加地区" :visible.sync="dialog1FormVisible" :close-on-click-modal="false" width="350px">
            <div slot="footer">
                <el-button @click="dialog1FormVisible = false">取 消</el-button>
                <el-button type="primary" @click="dialog1FormVisible = false" @click.native="postNewRegion">确 定</el-button>
            </div>
            <el-form label-position="left" :model="form" label-width="80px">
                <el-form-item label="地区编号">
                    <el-input v-model="form.rid" placeholder="建议使用当地电话区号"></el-input>
                </el-form-item>
                <el-form-item label="地区名称">
                    <el-input v-model="form.region_name"></el-input>
                </el-form-item>
                <el-divider>请为该地区添加至少一种题型</el-divider>
                <el-form-item label="题型编号">
                    <el-input v-model="form2.type_id" placeholder="请输入"></el-input>
                </el-form-item>
                <el-form-item label="题型名称">
                    <el-input v-model="form2.type_name" placeholder="请输入"></el-input>
                </el-form-item>
            </el-form>
        </el-dialog>

        <el-dialog title="添加新题型" :visible.sync="dialog2FormVisible" :close-on-click-modal="false" width="330px">
            <div slot="footer">
                <el-button @click="dialog2FormVisible = false">取 消</el-button>
                <el-button type="primary" @click="dialog2FormVisible = false" @click.native="postNewType">确 定</el-button>
            </div>
            <el-form label-position="left" :model="form2" label-width="80px">
                <el-form-item label="地区">
                    <el-select  v-model="form2.rid" placeholder="请选择" @click.native="getAllRegions">
                        <el-option
                                v-for="item in tableData"
                                :key="item.rid"
                                :label="item.region_name"
                                :value="item.rid">
                            <span style="float: left">{{ item.region_name }}</span>
                            <span style="float: right; color: #8492a6; font-size: 13px">{{ item.rid }}</span>
                        </el-option>
                    </el-select>
                </el-form-item>
                <el-form-item label="题型编号">
                    <el-input v-model="form2.type_id" placeholder="请输入"></el-input>
                </el-form-item>
                <el-form-item label="题型名称">
                    <el-input v-model="form2.type_name" placeholder="请输入"></el-input>
                </el-form-item>
            </el-form>
        </el-dialog>
    </div>
</template>

<script>
    import Card from "@/components/Card";
    export default {
        name: "RegionManage",
        data() {
            return {
                tableData: [],
                tableData2: [],
                form: {
                    rid: '',
                    region_name: ''
                },
                form2: {
                    rid: '',
                    type_id: '',
                    type_name: ''
                },

                dialog1FormVisible: false,
                dialog2FormVisible: false,
                isDeleteMode: false,
                isEditMode: false,
                multipleSelection: [],
                currentRow: null
            }
        },
        created: function (){
            this.getAllRegions();
        },
        components: {Card},
        methods: {
            getAllRegions() {
                let that = this;
                this.$http.get('get_all_regions_details')
                    .then(function (response) {
                        that.tableData = response.data;
                    })
            },
            showDialog1() {
                this.dialog1FormVisible = true
            },
            showDialog2() {
                this.dialog2FormVisible = true
            },
            postNewRegion() {
                let that = this;
                this.$http.post('post_region', this.form)
                    .then(function () {
                        that.$message({
                            type: 'success',
                            message: '添加地区成功！'
                        });
                        that.form2.rid = that.form.rid;
                        that.postNewType();
                    })
                    .catch(function(error) {
                        that.$message({
                            type: 'error',
                            message: '添加地区失败！' + error
                        });
                    });
            },
            postNewType() {
                let that = this;
                this.$http.post('post_question_bank', this.form2)
                    .then(function () {
                        that.$message({
                            type: 'success',
                            message: '添加题型成功！'
                        });
                        that.getAllRegions();
                    })
                    .catch(function(error) {
                        that.$message({
                            type: 'error',
                            message: '添加题型失败！' + error
                        });
                    });
            },
            getTypes() {
                let that = this;
                this.$http.get('get_types/' + this.currentRow.rid)
                    .then(function (response) {
                        that.tableData2 = response.data
                    })
            },
            handleCurrentChange(val) {
                this.currentRow = val;
                this.getTypes();
            }
        }
    }
</script>

<style scoped>
    .card1{
        display: inline-block;
        width: 500px;
        float: left;
    }
    .card2{
        display: inline-block;
        width: 500px;
        float: right;
    }
</style>