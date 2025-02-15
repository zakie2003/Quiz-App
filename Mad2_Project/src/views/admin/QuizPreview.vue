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

const get_quiz=async()=>{
  const urlParams=window.location.pathname;
  const parts=urlParams.split('/');
  const quiz_id=parts[parts.length-1];
  await axios.post("https://quiz-app-chz3.onrender.com/admin/get_quiz",{"quiz_id":quiz_id}).then((res)=>{
    quiz_data.value=res.data;
    loading.value = false;
  }).catch((err)=>{
    console.log(err);
    loading.value = false;
  })
}

const get_questions=async()=>{
  const urlParams=window.location.pathname;
  const parts=urlParams.split('/');
  const quiz_id=parts[parts.length-1];
  const chapter_name=parts[parts.length-2];
  await axios.post("https://quiz-app-chz3.onrender.com/admin/get_questions",{"chapter_name":chapter_name,"quiz_id":quiz_id}).then((res)=>{
    quiz_data.value.questions=res.data.data;
    console.log(quiz_data.value);
    loading.value = false;
  }).catch((err)=>{
    console.log(err);
    loading.value = false;
  })
}

onMounted(()=>{
  get_quiz();
  get_questions();
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

const edit_question=(id)=>{
  window.location.href="/admin/edit_question/"+id;
}

const delete_question=async(id)=>{
  await axios.post("https://quiz-app-chz3.onrender.com/admin/delete_question",{"id":id}).then((res)=>{
    console.log(res);
    get_questions();
  }).then((err)=>{
    console.log(err);
  })
}

</script>
<template>
  <header  class="header bg-light p-3 mb-3 nav_bar text-white" id="header">
    <h3 class="pt-2">Quiz Preview: {{ quiz_data.quiz.quiz_name }} </h3>
    <h3 class="pt-2">Time: {{ quiz_data.quiz.time_duration }}</h3>
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
          <div>
            <button class="btn nav_bar mx-1" v-on:click="edit_question(quiz_data.questions[pointer.index].id)">Edit</button>
            <button  class="btn nav_bar mx-1" v-on:click="delete_question(quiz_data.questions[pointer.index].id)">Delete</button>
          </div>
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
