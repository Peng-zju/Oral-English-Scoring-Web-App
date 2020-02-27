<template>
    <div class="login_box">
        <el-form :model="userForm" :rules="rules" ref="ruleFormRef" class="login_form">
            <el-form-item><h3>管理员登陆</h3></el-form-item>
            <el-form-item prop="account">
                <el-input prefix-icon="el-icon-user-solid" placeholder="管理员账号" v-model.number="userForm.account"></el-input>
            </el-form-item>
            <el-form-item prop="password">
                <el-input prefix-icon="el-icon-lock" type="password" placeholder="密码" v-model="userForm.password" autocomplete="off" show-password></el-input>
            </el-form-item>
            <el-form-item>
                <el-button style="width: 100%" type="primary" @click="submitForm">登录</el-button>
            </el-form-item>
        </el-form>

    </div>
</template>

<script>
    export default {
        name: "Login",
        data() {
            return {
                userForm: {
                    account: '',
                    password: '',
                },
                rules: {
                    account: [
                        { required: true, message: "账号不能为空", trigger: 'blur' }
                    ],
                    password: [
                        { required: true, message: "密码不能为空", trigger: 'blur' }
                    ]
                }
            };
        },
        methods: {
            submitForm() {
                let that = this;
                this.$refs.ruleFormRef.validate((valid) => {
                    if (valid) {
                        that.$router.push("/main")
                        /*this.$http.post('login', this.userForm)
                            .then(function () {

                            that.$message({
                                type: 'success',
                                message: '登陆成功'
                            });

                            })
                            .catch(function(error) {
                                that.$message({
                                    type: 'error',
                                    message: '用户名或密码错误，请检查后重试' + error
                                });
                            });*/
                    } else {
                        return false;
                    }
                });
            }
        }
    }
</script>

<style scoped>
    .login_box {
        width: 450px;
        height: 350px;
        margin: 0 auto;
        position: relative;
        border-radius: 4px;
        top: 50%;
        transform: translateY(-50%);
        box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
        display: flex;
        align-items:center;
    }
    .login_form {
        width: 85%;
        margin: 0 auto;
        box-sizing: border-box;
    }
</style>