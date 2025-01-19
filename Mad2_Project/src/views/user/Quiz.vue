<script setup>
import "@/assets/JS/nav.js";
import Loader from "@/components/Loader/Loader.vue";
import axios from "axios";
import { onMounted,ref } from "vue";

const quiz_data=ref({
  quiz: {
    quiz_name: '',
    time_duration: '',
    chapter_name: '',
    questions:[]
  }
});

const pointer=ref({index:0});
const loading = ref(true);
const remainingTime = ref(0);
const minute=ref(0);
const second=ref(0);
let timer;

const get_quiz=async()=>{
  const urlParams=window.location.pathname;
  const parts=urlParams.split('/');
  const quiz_id=parts[parts.length-1];
  await axios.post("http://localhost:5000/admin/get_quiz",{"quiz_id":quiz_id}).then((res)=>{
    quiz_data.value=res.data;
  }).catch((err)=>{
    console.log(err);
  })
}

const get_questions=async()=>{
  const urlParams=window.location.pathname;
  const parts=urlParams.split('/');
  const quiz_id=parts[parts.length-1];
  const chapter_name=parts[parts.length-2];
  await axios.post("http://localhost:5000/user/get_questions",{"chapter_name":chapter_name,"quiz_id":quiz_id}).then((res)=>{
    quiz_data.value.questions=res.data.data;
    loading.value = false;
  }).catch((err)=>{
    console.log(err);
    loading.value = false;
  })
}

const start_quiz=async()=>{
  console.log("Quiz data",quiz_data.value.quiz);
  await axios.post("http://localhost:5000/user/start_quiz",{
    "quiz_id": quiz_data.value.quiz.id,
    "time_duration": quiz_data.value.quiz.time_duration,
    "user_id": sessionStorage.getItem("id")
  }).then((res)=>{
    console.log(res);
  }).catch((err)=>{
    console.log(err);
  })
}

const fetchRemainingTime = async () => {
  try {
    const response = await axios.post("http://localhost:5000/user/remaining_time", {
      "user_id": sessionStorage.getItem("id"),
      "quiz_id": quiz_data.value.quiz.id
    });
    const data = response.data;
    remainingTime.value = data.remainingTime;
    console.log(remainingTime.value);
    minute.value = Math.floor(remainingTime.value / 60);
    second.value = remainingTime.value % 60;
    if (remainingTime.value <= 0) {
      clearInterval(timer);
      await submit_quiz();
      window.location.href = "/user/library";
    }
  } catch (err) {
    console.log(err);
  }
}

const submit_quiz = async () => {
  try {
    await axios.post("http://localhost:5000/user/submit_quiz", {
      "user_id": sessionStorage.getItem("id"),
      "quiz_id": quiz_data.value.quiz.id
    }).then((res) => {
      console.log(res);
    }).catch((err) => {
      console.log(err);
    });
  } catch (err) {
    console.log(err);
  }
}

const startLocalCountdown = () => {
  if (remainingTime.value > 0) {
    remainingTime.value = (remainingTime.value - 1);
  }
}

onMounted(async()=>{
  await get_quiz();
  await get_questions();
  await start_quiz();
  timer = setInterval(() => {
    startLocalCountdown();
  }, 1000);
  setInterval(fetchRemainingTime, 2000); 
})


const next=()=>{
  if(pointer.value.index<quiz_data.value.questions.length-1){
    pointer.value.index=pointer.value.index+1;
  }
}

const prev=()=>{
  if(pointer.value.index>0){
    pointer.value.index=pointer.value.index-1;
  }
}

const go_to_this_question=(index)=>{
  pointer.value.index=index;
}



</script>
<template>
  <header  class="header bg-light p-3 mb-3 nav_bar text-white" id="header">
    <h3 class="pt-2">Quiz Preview: {{ quiz_data.quiz.quiz_name }} </h3>
    <h3 class="pt-2">Time: {{ minute }}:{{ second }}</h3>
    <h3 class="pt-2">Chapter Name: {{ quiz_data.quiz.chapter_name }}</h3>
  </header>
  <div class="row" style="align-items: center;justify-content: center;display: flex;height: 100vh;" v-if="loading">
    <Loader/>
  </div>
  <div class="row" v-else>
    <div class="row" style="display: flex;justify-content: center;align-items: center;height: 80vh;" v-if="quiz_data.questions.length==0">
      <h3 class="col-7 mx-2 my-4 rounded p-4 bg-light" style="text-align: center;">No questions found</h3>  
    </div>
    <div class="row" v-else>
    <div  class="col-7 mx-1 my-4 rounded p-4 bg-light">
      <div class="py-4 text-left">
        <div class="d-flex justify-content-between align-items-center">
          <h3>Question No {{ pointer.index+1 }}</h3>
        </div>
        <span class="p-2 d-block" style="font-size: larger;">
           {{ quiz_data.questions[pointer.index].question }}
        </span>
        <h3 class="pt-4">Options</h3>
        <div class="py-2">
          <button style="font-size: larger;" class="btn w-100 my-2 text-start border">{{ quiz_data.questions[pointer.index].option_a }}</button>
          <button style="font-size: larger;" class="btn w-100 my-2 text-start border">{{ quiz_data.questions[pointer.index].option_b }}</button>
          <button style="font-size: larger;" class="btn w-100 my-2 text-start border">{{ quiz_data.questions[pointer.index].option_c }}</button>
          <button style="font-size: larger;" class="btn w-100 my-2 text-start border">{{ quiz_data.questions[pointer.index].option_d }}</button>
        </div>
        <div class="d-flex justify-content-between pt-4">
          <button class="btn nav_bar text-white" v-on:click="prev">Previous</button>
          <button class="btn nav_bar text-white" v-on:click="next">Next</button>
        </div>
      </div>
    </div>
    <div class="col-4 mx-1 my-4 rounded p-4 bg-light">
      <h3 class="py-4">Questions</h3>
      <div class="row justify-content-center">
        <button v-on:click="go_to_this_question(i-1)" class="btn col-3 py-3 m-2 border" :class="{'nav_bar':pointer.index==i-1}"  v-for="i in quiz_data.questions.length" :key="i">{{ i }}</button>
      </div>
    </div>
    </div>
  </div>
</template>
<style>
@import "../../assets/CSS/nav.css";
.nav_bar{
  background-color: #4723D9 !important;
  color: aliceblue !important;
  border:2px solid #fff !important;
}
</style>
