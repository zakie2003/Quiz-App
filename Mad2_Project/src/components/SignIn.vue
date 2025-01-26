<script setup>
import axios from 'axios';
import Footer from './Footer/Footer.vue';
import { reactive } from 'vue';
const data=reactive({
    email:"",
    password:"",
    type:"User",
    dob:"",
    qualification:"",
    name:"",
    profile_url:""
})

const handle_submit=async()=>{
    await axios.post("http://localhost:5000/user/create_user",data).then((res)=>{
        console.log(res);
    }).catch((err)=>{
        console.log(err);
    })
}
</script>

<template>
    <section style="min-height: 100vh;">
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
                <button  type="button" data-mdb-button-init data-mdb-ripple-init class="btn btn-lg" v-on:click="handle_submit()"
                style="padding-left: 2.5rem; padding-right: 2.5rem; background-color:#4723d9;color: aliceblue;">Signin</button>
                <p class="small fw-bold mt-2 pt-1 mb-0">Already have an account? <a href="/"
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
</style>