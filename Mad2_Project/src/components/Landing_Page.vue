<script setup>
import { onMounted } from 'vue';
import Footer from './Footer/Footer.vue';

const go_to_signin=()=>{
    window.location.href="/signin";
}

const go_to_login=()=>{
    window.location.href="/login";
}

const add_css=()=>{
    document.getElementById("body-pd").style.padding="0";
    document.getElementById("body-pd").style.margin="0";
}

onMounted(()=>{
    add_css();
});

</script>

<template>
    <nav  class="navbar navbar-expand-lg landing-nav">
        <div class="container-fluid">
            <div class="h2 font-weight-bold text-white">
                MindSpark
            </div>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent"
                aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>

            <div class="collapse navbar-collapse justify-content-end" id="navbarSupportedContent">
                <ul class="navbar-nav">
                    <li class="nav-item active">
                        <a class="nav-link text-white" href="#home">Home</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link text-white" href="#features">Features</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link text-white" href="#contact">Contact</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link text-white" href="#faq">Faq </a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link text-white" href="/login">Login</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link text-white" href="/signin">Signin</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
    <div class="p-6">
        <section id="home" class="bg-white py-5 conatainer">
            <div class="container d-flex flex-column flex-md-row align-items-center">
                <div class="col-md-6">
                <h1 class="display-4 font-weight-bold mb-4">
                    Welcome to MindSpark
                </h1>
                <p class="lead mb-4">
                Create, share, and take quizzes on any topic. Enhance your learning experience with our easy-to-use platform.
                </p>
                <button v-on:click="go_to_login" style="background-color: #4723d9;color: aliceblue;" class="btn">Login</button> &nbsp;
                <button v-on:click="go_to_signin" style="background-color: #4723d9;color: aliceblue;" class="btn">Signin</button>
                </div>
                <div class="col-md-6 mt-4 mt-md-0">
                <img alt="Illustration of people taking quizzes" style="padding-right: 110px;padding-left: 110px;" class="img-fluid" src="https://storage.googleapis.com/a1aa/image/jNjID8UlarlSD2FKAsPmmV2xmYt9XskxoduXzoUhBjI.jpg"/>
                </div>
            </div>
        </section>
  <!-- Features Section -->
        <section id="features" class="bg-light py-5">
        <div class="container">
            <h2 style="font-weight: bolder;" class="text-center mb-5">
            Features
            </h2>
            <div class="row">
            <div class="col-md-4 mb-4">
            <div class="card h-100 text-center feature-card">
            <div class="card-body">
                <i style="font-weight: bolder;" class='bx bx-edit display-3 mb-4'></i>
                <h5 style="font-weight: bolder;" class="card-title font-weight-bold">
                    Attempt Quizzes
                </h5>
                <p class="card-text">
                Create quizzes with multiple question types and share them with your audience.
                </p>
            </div>
            </div>
            </div>
            <div class="col-md-4 mb-4">
            <div class="card h-100 text-center feature-card">
            <div class="card-body">
                <i style="font-weight: bolder;" class='bx bxs-chevrons-up display-3 mb-4'></i>
                <h5 style="font-weight: bolder;" class="card-title font-weight-bold">
                    Up Scale Your Self
                </h5>
                <p class="card-text">
                    Share your quizzes with friends, students, or colleagues with just a few clicks.
                </p>
            </div>
            </div>
            </div>
            <div class="col-md-4 mb-4">
            <div class="card h-100 text-center feature-card">
            <div class="card-body">
                <i style="font-weight: bolder;" class='bx bx-trending-up display-3 mb-4' ></i>
                <h5 style="font-weight: bolder;" class="card-title">
                Track Progress
                </h5>
                <p class="card-text">
                Track your progress and see how well you and others are doing on quizzes.
                </p>
            </div>
            </div>
            </div>
            </div>
        </div>
        </section>

        <section id="faq" class="bg-white py-5">
            <div class="container">
                <h2 style="font-weight: bolder;" class="text-center font-weight-bold mb-5">
                    Frequently Asked Questions
                </h2>
                <div class="accordion" id="faqAccordion">
                    <div class="card">
                        <div class="card-header" id="headingOne">
                            <h5 class="mb-0">
                                <button class="btn btn-link faq_large" data-bs-toggle="collapse" data-bs-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
                                    How do I create a quiz?
                                </button>
                            </h5>
                        </div>
                        <div id="collapseOne" class="collapse show w-100" aria-labelledby="headingOne" data-bs-parent="#faqAccordion">
                            <div class="card-body faq_large">
                                Only admin can create quizes as of now.
                            </div>
                        </div>
                    </div>
                    <div class="card">
                        <div class="card-header" id="headingTwo">
                            <h5 class="mb-0">
                                <button class="btn btn-link collapsed faq_large" data-bs-toggle="collapse" data-bs-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
                                    Is the platform fully free?
                                </button>
                            </h5>
                        </div>
                        <div id="collapseTwo" class="collapse w-100" aria-labelledby="headingTwo" data-bs-parent="#faqAccordion">
                            <div class="card-body faq_large">
                                Yes, the platform is currently free, but it may introduce paid features or plans in the future.
                            </div>
                        </div>
                    </div>
                    <div class="card">
                        <div class="card-header" id="headingThree">
                            <h5 class="mb-0">
                                <button class="btn btn-link collapsed faq_large" data-bs-toggle="collapse" data-bs-target="#collapseThree" aria-expanded="false" aria-controls="collapseThree">
                                    Is there a limit to the number of quizzes I can attempt?
                                </button>
                            </h5>
                        </div>
                        <div id="collapseThree" class="collapse w-100" aria-labelledby="headingThree" data-bs-parent="#faqAccordion">
                            <div class="card-body faq_large">
                                No, there is no limit to the number of quizzes you can attempt. Feel free to attempt as many quizzes as you like!
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>


    </div>
    <div id="contact">
        <Footer/>
    </div>
</template>

<style>

.landing-nav {
    padding: 10px 20px !important;
    background-color: #4723d9 !important;
}

.navbar-nav .nav-link {
    font-size: 16px;
    font-weight: 500;
    margin: 0 10px;
    transition: color 0.3s ease-in-out;
}

.card-header .btn-link {
    text-decoration: none;
    font-weight: bold;
    color: #4723d9;
}

.card-header .btn-link:hover {
    text-decoration: underline;
}

.card-body {
    font-size: 14px;
    color: #333;
}

.accordion, .card {
    width: 100% !important;
}

.faq_large{
    font-size: large;
}

.feature-card:hover {
    transform: scale(1.05);
    transition: transform 0.3s ease-in-out;
    background-color: #4723d9;
}

.card-body:hover {
    background-color: #4723d9;
    color: aliceblue;
    transition: transform 0.3s ease-in-out;
}

</style>
