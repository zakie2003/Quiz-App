<script setup>
import "@/assets/JS/nav.js";
import Loader from "@/components/Loader/Loader.vue";
import axios from "axios";
import { onMounted,ref } from "vue";
import MarkdownIt from 'vue3-markdown-it';

const quiz_data=ref({
  quiz: {
    quiz_name: '',
    time_duration: '',
    chapter_name: '',
    questions:[]
  }
});

const user_options=ref({});

const pointer=ref({index:0});
const loading = ref(true);
const showSolutionModal = ref(false);
const solutionText = ref("");
const solutionExplanation = ref("");

const get_quiz=async()=>{
  const urlParams=window.location.pathname;
  const parts=urlParams.split('/');
  const quiz_id=parts[parts.length-1];
  await axios.post("http://localhost:5000/admin/get_quiz",{"quiz_id":quiz_id}).then((res)=>{
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
  await axios.post("http://localhost:5000/user/get_questions",{"chapter_name":decodeURI(chapter_name),"quiz_id":quiz_id}).then((res)=>{
    quiz_data.value.questions=res.data.data;
    console.log(quiz_data.value);
    loading.value = false;
  }).catch((err)=>{
    console.log(err);
    loading.value = false;
  })
}

const get_user_anser = () => {
  const urlParams = new URLSearchParams(window.location.search);
  const date_of_quiz = urlParams.get('date');
  const time = urlParams.get('time');
  const parts = window.location.pathname.split('/');
  const quiz_id = parts[parts.length - 1];
  const chapter_name = parts[parts.length - 2];
  console.log(sessionStorage.getItem("id"));
  axios.post("http://localhost:5000/user/get_user_answer", {
    chapter_name: decodeURI(chapter_name),
    quiz_id: quiz_id,
    user_id: sessionStorage.getItem("id"),
    date: date_of_quiz,
    time: time
  }, { headers: { "Content-Type": "application/json" } })
  .then((res) =>{
    user_options.value = res.data;
    console.log(user_options.value.user_answers[pointer.value.index]);
  } 
)
  .catch((err) => console.log(err));
};

onMounted(async()=>{
  await get_quiz();
  await get_questions();
  get_user_anser();
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

const get_Solution=async(question)=>{
  console.log(question);
  await axios.post("http://localhost:5000/user/summerize_question", {
    question: question
  }).then((res) => {
    // Assume res.data.summary is the generated text, and res.data.explanation is how it was generated
    solutionText.value = res.data.summary;
    solutionExplanation.value = res.data.explanation || "This solution was generated using an AI model based on the question context.";
    showSolutionModal.value = true;
  }).catch((err) => {
    console.log(err);
    alert("Error fetching solution");
  });
}

const go_to_this_question=(index)=>{
  pointer.value.index=index;
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
          <button class="btn gemini_btn text-white" v-on:click="get_Solution(quiz_data.questions[pointer.index].question)">
            <svg  xmlns="http://www.w3.org/2000/svg" width="24" height="24"  
              fill="currentColor" viewBox="0 0 24 24" >
              <path d="M12 2c-.78 5.16-4.84 9.22-10 10 5.16.78 9.22 4.84 10 10 .78-5.16 4.84-9.22 10-10-5.16-.78-9.22-4.84-10-10" class="b"></path>
              </svg>
              Generate Solution
          </button>
        </div>
        <span class="p-2 d-block" style="font-size: larger;">
           {{ quiz_data.questions[pointer.index].question }}
        </span>
        <h3 class="pt-4">Options</h3>
        <div class="py-2">
          <div class="option-container">
            <input type="radio" :checked="user_options.user_answers[pointer.index].user_answer == '1'" disabled>
            <button :class="{'correct_answer':quiz_data.questions[pointer.index].correct_option=='1', 'selected_option': user_options.user_answers[pointer.index].user_answer == '1'}" style="font-size: larger;" class="btn w-100 my-2 text-start border">{{ quiz_data.questions[pointer.index].option_a }}</button>
          </div>
          <div class="option-container">
            <input type="radio" :checked="user_options.user_answers[pointer.index].user_answer == '2'" disabled>
            <button :class="{'correct_answer':quiz_data.questions[pointer.index].correct_option=='2', 'selected_option': user_options.user_answers[pointer.index].user_answer == '2'}" style="font-size: larger;" class="btn w-100 my-2 text-start border">{{ quiz_data.questions[pointer.index].option_b }}</button>
          </div>
          <div class="option-container">
            <input type="radio" :checked="user_options.user_answers[pointer.index].user_answer == '3'" disabled>
            <button :class="{'correct_answer':quiz_data.questions[pointer.index].correct_option=='3', 'selected_option': user_options.user_answers[pointer.index].user_answer == '3'}" style="font-size: larger;" class="btn w-100 my-2 text-start border">{{ quiz_data.questions[pointer.index].option_c }}</button>
          </div>
          <div class="option-container">
            <input type="radio" :checked="user_options.user_answers[pointer.index].user_answer == '4'" disabled>
            <button :class="{'correct_answer':quiz_data.questions[pointer.index].correct_option=='4', 'selected_option': user_options.user_answers[pointer.index].user_answer == '4', 'wrong_answer': user_options.user_answers[pointer.index].user_answer != quiz_data.questions[pointer.index].correct_option, 'blank_answer': user_options.user_answers[pointer.index].user_answer == ''}" style="font-size: larger;" class="btn w-100 my-2 text-start border">{{ quiz_data.questions[pointer.index].option_d }}</button>
          </div>
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
  <div v-if="showSolutionModal" class="modal-overlay">
    <div class="modal-content themed-modal scrollable-modal">
      <button class="modal-close" @click="showSolutionModal = false">&times;</button>
      <h4 class="modal-title">AI Generated Solution</h4>
      <MarkdownIt :source="solutionText" class="modal-html" />
      <hr />
      <button class="btn nav_bar text-white mt-3 w-100" @click="showSolutionModal = false">Close</button>
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

.gemini_btn {
  background: linear-gradient(45deg, #4723D9, #8A2BE2, #5F9DF7);
  color: aliceblue;
  border: 1px solid #fff;
  padding: 10px 20px;
  border-radius: 8px;
  cursor: pointer;
  transition: background-position 0.5s ease, transform 0.3s ease;
  background-size: 200% 200%;
}

.gemini_btn:hover {
  background-position: right center;
  transform: scale(1.05);
}

.correct_answer{
  background-color: green !important;
  color: aliceblue !important;
}
.wrong_answer{
  background-color: red !important;
  color: aliceblue !important;
}
.blank_answer{
  background-color: #F8F9FA !important;
  color: #2C3034 !important;
}
.selected_option {
  border: 2px solid blue !important;
}
.option-container {
  display: flex;
  align-items: center;
}
.option-container input {
  margin-right: 10px;
}
.modal-overlay {
  position: fixed;
  top: 0; left: 0; right: 0; bottom: 0;
  background: rgba(44,48,52,0.6);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
}
.themed-modal {
  background: #fff;
  border: 3px solid #4723D9;
  border-radius: 16px;
  max-width: 540px;
  width: 95%;
  box-shadow: 0 4px 32px rgba(71,35,217,0.15);
  padding: 2.5rem 2rem 2rem 2rem;
  position: relative;
  color: #2C3034;
}
.scrollable-modal {
  max-height: 80vh;
  overflow-y: auto;
}
.modal-title {
  color: #4723D9;
  font-weight: bold;
  margin-bottom: 1rem;
}
.modal-subtitle {
  color: #4723D9;
  margin-top: 1.5rem;
  margin-bottom: 0.5rem;
}
.modal-html {
  font-size: 1.08em;
  color: #2C3034;
  margin-bottom: 0.5rem;
}
.modal-html.explanation {
  font-size: 0.98em;
  color: #555;
}
.modal-close {
  position: absolute;
  top: 12px;
  right: 18px;
  background: none;
  border: none;
  font-size: 2rem;
  color: #4723D9;
  cursor: pointer;
  transition: color 0.2s;
  z-index: 10;
}
.modal-close:hover {
  color: #2C3034;
}
</style>
