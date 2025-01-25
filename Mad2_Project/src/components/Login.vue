<script setup>
    import { onMounted, reactive,ref } from 'vue';
    import axios from "axios";
    import ErrorMessage from "./Message/ErrorMessage.vue";
    const device_data=ref({});
    function detectDeviceType() {
        if (navigator.userAgentData) {

            if (navigator.userAgentData.mobile) {

            return navigator.userAgentData.platform === "Android" && window.screen.width >= 600 ? "Tablet" : "Mobile";
            } else {
            return "Desktop/Laptop";
            }
        } 
        else {
            const userAgent = navigator.userAgent.toLowerCase();
            const isTablet = /(ipad|tablet|(android(?!.*mobile))|(windows(?!.*phone)(.*touch))|kindle|playbook|silk|(puffin(?!.*(IP|AP|WP))))/.test(userAgent);
            const isMobile = /Mobile|Android|iP(hone|od)|IEMobile|BlackBerry|Kindle|Silk-Accelerated|(hpw|web)OS|Opera M(obi|ini)/.test(userAgent);
            
            if (isTablet) {
            return "Tablet";
            } else if (isMobile) {
            return "Mobile";
            } else {
            return "Desktop/Laptop";
            }
        }
        }
onMounted(()=>{
    const deviceType = detectDeviceType();
    device_data.value=deviceType;
})
    const data = reactive({
        email: "",
        password: "",
        type: "Admin",
        message: ""
    });

    async function login(data) {
        sessionStorage.clear();

        await axios.post("http://localhost:5000/user/add_device",{"device":device_data.value}).then((res) => {
            console.log(res);
        }).catch((err) => {
            console.log(err);
        })
        var url="";
        var location="";
        if(data.type==="Admin"){
            url="http://localhost:5000/admin/authorize";
            location="/admin/home";
        }
        else{
            url="http://localhost:5000/user/user_authorize";
            location="/user/home";
        }

        await axios(url, {
            method: "POST",
            data: data,
            headers: { "Content-Type": "application/json" }
        }).then((res) => {
            console.log(res.data);
            if (res.data.token !== undefined) {
                sessionStorage.setItem('token', res.data.token);
                sessionStorage.setItem('name', res.data.name);
                sessionStorage.setItem('id', res.data.id);
                sessionStorage.setItem('password', res.data.password);
                sessionStorage.setItem('email', res.data.email);
                window.location.href = location;
            } else {
                data.message = res.data.message;
            }
        }).catch((err) => {
            console.log(err);
            data.message = "Login failed. Please try again.";
        });
    }
</script>
<template>
    <section class="vh-100">
        <div class="container-fluid h-custom">
            <div>
                <ErrorMessage v-if="data.message" :message="data.message" />
            </div>
            <div class="row d-flex justify-content-center align-items-center h-100">
                <div class="col-md-9 col-lg-6 col-xl-5">
                    <img src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-login-form/draw2.webp"
                        class="img-fluid" alt="Sample image">
                </div>
                <div class="col-md-8 col-lg-6 col-xl-4 offset-xl-1">
                    <form method="post">
                        <div class="d-flex flex-row align-items-center justify-content-center justify-content-lg-start">
                            <p class="lead fw-normal mb-0 me-3 mb-3">Login Page</p>
                        </div>


                        <!-- Email input -->
                        <div data-mdb-input-init class="form-outline mb-4">
                            <label class="form-label" for="emailInput">Email address</label>
                            <input type="email" id="emailInput" class="form-control form-control-lg"
                                placeholder="Enter a valid email address" v-model="data.email" />

                        </div>

                        <div data-mdb-input-init class="form-outline mb-4">
                            <label class="form-label" for="typeSelect">Member Type</label>
                            <select name="type" id="typeSelect" class="form-control form-control-lg" v-model="data.type">
                                <option value="Admin">Admin</option>
                                <option value="Student">Student</option>
                            </select>
                        </div>

                        <!-- Password input -->
                        <div data-mdb-input-init class="form-outline mb-3">
                            <label class="form-label" for="passwordInput">Password</label>
                            <input v-model="data.password" type="password" id="passwordInput" class="form-control form-control-lg"
                                placeholder="Enter password" />

                        </div>

                        <div class="d-flex justify-content-between align-items-center">
                            <!-- Checkbox -->
                            <div class="form-check mb-0">
                                <input class="form-check-input me-2" type="checkbox" value="" id="rememberMeCheckbox" />
                                <label class="form-check-label" for="rememberMeCheckbox">
                                    Remember me
                                </label>
                            </div>
                            <a href="#!" class="text-body">Forgot password?</a>
                        </div>

                        <div class="text-center text-lg-start mt-4 pt-2">
                            <button type="button" data-mdb-button-init data-mdb-ripple-init class="btn btn-lg" @click="login(data)"
                                style="padding-left: 2.5rem; padding-right: 2.5rem; background-color:#4723d9;color: aliceblue;">Login</button>
                            <p class="small fw-bold mt-2 pt-1 mb-0">Don't have an account? <a href="/signin" class="link-danger">Register</a></p>
                        </div>

                    </form>
                </div>
            </div>
        </div>
        <div style="background-color: #4723d9;" class="d-flex flex-column flex-md-row text-center text-md-start justify-content-between py-4 px-4 px-xl-5 ">
            <!-- Copyright -->
            <div class="text-white mb-3 mb-md-0">
                Copyright © 2020. All rights reserved.
            </div>
            <!-- Copyright -->

            <!-- Right -->
            <div>
                <a href="#!" class="text-white me-4">
                    <i class="fab fa-facebook-f"></i>
                </a>
                <a href="#!" class="text-white me-4">
                    <i class="fab fa-twitter"></i>
                </a>
                <a href="#!" class="text-white me-4">
                    <i class="fab fa-google"></i>
                </a>
                <a href="#!" class="text-white">
                    <i class="fab fa-linkedin-in"></i>
                </a>
            </div>
            <!-- Right -->
        </div>
    </section>
</template>
<style>
    @import "../assets/CSS/login.css";
</style>