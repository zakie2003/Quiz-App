<script setup>
import { ref, defineExpose, computed, onMounted } from 'vue';
import "@/assets/JS/nav.js";
import axios from "axios";
import NavAdmin from '@/components/NavBar/NavAdmin.vue';
import Cards from '@/components/Cards/Cards.vue';
import Loader from '@/components/Loader/Loader.vue';
import QuizCards from '@/components/Cards/QuizCards.vue';
import User_Profile_Card from '@/components/Cards/User_Profile_Card.vue';
import Footer from '@/components/Footer/Footer.vue';

const search_results = ref({});
let isLoading = ref(true);

let arr=ref([]);

const get_results = async () => {
    let currentLocation = window.location.href.split("/");
    const search = decodeURIComponent(currentLocation[currentLocation.length-1]);
    await axios.post(`http://localhost:5000/admin/search`, { "search": search }).then((res) => {
        search_results.value = res.data;
        arr.value=search_results.value.quiz;
        isLoading.value = false;
    }).catch((err) => {
        console.log(err);
        isLoading.value = false;
    });
}

const change_arr=(value)=>{
    if(value=="quiz"){
        arr.value=search_results.value.quiz;
        option.value="quiz";
    }
    else if(value=="user"){
        arr.value=search_results.value.user;
        option.value="user";
    }
    else if(value=="subject"){
        arr.value=search_results.value.subject;
        option.value="subject";
    }
}

let option=ref("quiz");

const go_to_profile=(email)=>{
    window.location.href="/admin/user_profile/"+email;
}

onMounted(() => {
    get_results();
});

</script>
<template>
    <nav class="navbar navbar-expand-lg pb-0 bg-body-tertiary">
      <NavAdmin /> 
      <div style="min-height: 100vh;" class="bg-light w-100">
        <div v-if="isLoading" style="display: flex;justify-content: center;align-items: center;height: 100vh;"><Loader/></div>
        <div v-else>
            <h1 class="m-4">Search Results</h1>
            <div class="row">
                <div class="col-lg-3 col-sm-12">
                    <div class="search-results m-4 p-4">
                        <div v-on:click="change_arr('user')" class="result-item rounded-top text-white text-center p-3 border" style="background-color: #4723D9;">
                            <h5>User {{ search_results.user.length }}</h5>
                        </div>
                        <div v-on:click="change_arr('quiz')" class="result-item p-3 border text-center text-white" style="background-color: #4723D9;">
                            <h5>Quiz {{ search_results.quiz.length }}</h5>
                        </div>
                        <div v-on:click="change_arr('subject')" class="result-item rounded-bottom text-center text-white p-3 border" style="background-color: #4723D9;">
                            <h5>Subject {{ search_results.subject.length }}</h5>
                        </div>
                    </div>
                </div>
                <div class="col-lg-9 col-sm-12">
                    <div class="ag-courses_box row">
                        <div v-if="arr.length==0" class="text-center w-100">
                            <h1>No Results Found</h1>
                        </div>
                        <div v-else class="row">
                            <div v-if="option=='quiz'" v-for="(item, index) in arr" :key="'quiz-' + index" class="col-md-4" style="width: 100%;">
                                <QuizCards :display_button="false" :item="item"/>
                            </div>
                            <div v-else-if="option=='user'" v-for="(item, index) in arr" :key="'user-' + index" class="col-md-4" style="width: 100%;">
                                <User_Profile_Card v-on:click.stop="go_to_profile(item.email)" :item="item"/>
                            </div>
                            <div v-else-if="option=='subject'" v-for="(item, index) in arr" :key="'subject-' + index" class="col-md-4" style="width: 100%;">
                                <Cards :item="item"/>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
      </div>
    </nav>
    <Footer/>
</template>
<style>
@import "../../assets/CSS/nav.css";

.search-results {
    display: flex;
    flex-direction: column;
}

.result-item {
    background-color: #f8f9fa;
    transition: background-color 0.3s ease;
}

.result-item:hover {
    background-color: #e9ecef;
}

.ag-courses_box {
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-align: start;
    -ms-flex-align: start;
    align-items: flex-start;
    -ms-flex-wrap: wrap;
    flex-wrap: wrap;
    padding: 50px 0;
}
</style>