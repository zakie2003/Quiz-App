<script setup>
import axios from 'axios';
import Footer from './Footer/Footer.vue';
import { reactive } from 'vue';
import ErrorMessage from './Message/ErrorMessage.vue';
const data=reactive({
    email:"",
    password:"",
    type:"User",
    dob:"",
    qualification:"",
    name:"",
    profile_url:"",
    otp:"",
    isoptsent:false
})

const resp_status=reactive({
    status:"",message:""
})

const generate_opt=()=>{
    let str="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
    var otp="";
    for(var i=0;i<6;i++){
        otp+=str.charAt(Math.floor(Math.random()*str.length));
    }
    return otp;
}

const send_opt=async()=>{
    var otp=generate_opt();
    await axios.post("http://localhost:5000/user/send_otp",{"email":data.email,"otp":otp}).then((res)=>{
        console.log(res);
        resp_status.status=res.data.status;
        resp_status.message=res.data.message;
    }).catch((err)=>{
        console.log(err);
    })
    data.isoptsent=true;
}

const resend_opt=async()=>{
    var otp=generate_opt();
    await axios.post("http://localhost:5000/user/resend_otp",{"email":data.email,"otp":otp}).then((res)=>{
        console.log(res);
        resp_status.status=res.data.status;
        resp_status.message=res.data.message;
    }).catch((err)=>{
        console.log(err);
    })
    data.isoptsent=true;
}

const handle_submit=async()=>{
    await axios.post("http://localhost:5000/user/create_user",data).then((res)=>{
        console.log(res);
        resp_status.status=res.data.status;
        resp_status.message=res.data.message;
    }).catch((err)=>{
        console.log(err);
    })
}
</script>

<template>
    <section style="min-height: 100vh;margin-top: 60px;">
    <div class="container">
        <ErrorMessage v-if="resp_status.status" :status="resp_status.status" :message="resp_status.message"/>
    </div>
    <div class="container-fluid h-custom"> 
        <div style="min-height: 100vh;" class="row d-flex justify-content-center align-items-center ">
        <div class="col-md-9 col-lg-6 col-xl-5">
            <img src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-login-form/draw2.webp"
            class="img-fluid" alt="Sample image">
        </div>
        <div class="col-md-8 col-lg-6 col-xl-4 offset-xl-1">
            <form method="post">
            <div class="d-flex flex-row align-items-center justify-content-center justify-content-lg-start">
                <p class="lead fw-normal mb-0 me-3 mb-3">Signin Page</p>
            </div>


            <!-- Email input -->
            <div data-mdb-input-init class="form-outline mb-4">
                <input v-model="data.email" type="email" id="emailInput" class="form-control form-control-lg"
                placeholder="Enter a valid email address" />
                <label class="form-label" for="emailInput">Email address</label>
            </div>

            <!-- Password input -->
            <div data-mdb-input-init class="form-outline mb-3">
                <input v-model="data.password" type="password" id="passwordInput" class="form-control form-control-lg"
                placeholder="Enter password" />
                <label class="form-label" for="passwordInput">Password</label>
            </div>

            <div data-mdb-input-init class="form-outline mb-4">
                <input v-model="data.name" type="text" id="usernameInput" class="form-control form-control-lg"
                placeholder="Enter a valid User Name" />
                <label class="form-label" for="usernameInput">User Name</label>
            </div>

            <div data-mdb-input-init class="form-outline mb-4">
                <input v-model="data.qualification" type="text" id="qualificationInput" class="form-control form-control-lg"
                placeholder="Enter qualification" />
                <label class="form-label" for="qualificationInput">Qualification</label>
            </div>

            <div data-mdb-input-init class="form-outline mb-4">
                <input v-model="data.dob" type="date" id="dobInput" class="form-control form-control-lg"
                placeholder="Enter Date of Birth" />
                <label class="form-label" for="dobInput">Date of Birth</label>
            </div>


            <div v-if="data.isoptsent" data-mdb-input-init class="form-outline mb-4">
                <div style="display: flex;">
                    <input v-model="data.otp" type="text" id="otp" style="border-radius: 0;" class="otp_form form-control form-control-lg" placeholder="Enter OTP" />
                    <button v-on:click.prevent="resend_opt()" class="btn" style="background-color: #4723d9;color: aliceblue;border-radius: 0;">Resend</button>
                </div>
                <label class="form-label" style="color: #4723d9;" for="otp">Otp</label>
            </div>

            <div class="d-flex justify-content-between align-items-center">
                <!-- Checkbox
                <div class="form-check mb-0">
                <input class="form-check-input me-2" type="checkbox" value="" id="rememberMeCheckbox" />
                <label class="form-check-label" for="rememberMeCheckbox">
                    Remember me
                </label>
                </div>
                <a href="#!" class="text-body">Forgot password?</a> -->
            </div>

            <div class="text-center text-lg-start mt-4 pt-2">
                <button v-if="data.isoptsent"  type="button" data-mdb-button-init data-mdb-ripple-init class="btn btn-lg" v-on:click="handle_submit()"
                style="padding-left: 2.5rem; padding-right: 2.5rem; background-color:#4723d9;color: aliceblue;">Signin</button>
                <button v-else type="button" data-mdb-button-init data-mdb-ripple-init class="btn btn-lg" v-on:click="send_opt()"
                style="padding-left: 2.5rem; padding-right: 2.5rem; background-color:#4723d9;color: aliceblue;">Send OTP</button>
                <p class="small fw-bold mt-2 pt-1 mb-0">Already have an account? <a href="/login"
                    class="link-danger">Login</a>
                </p>
            </div>

            </form>
        </div>
        </div>
    </div>
    <Footer/>
    </section>
</template>
<style>
    @import "../assets/CSS/login.css";
    .otp_form{
        border-color: #4723d9 !important;
        background-color: #f4f1ff !important;   
    }
</style>