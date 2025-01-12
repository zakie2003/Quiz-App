<script setup>
import axios from "axios";
import NavAdmin from "@/components/NavBar/NavAdmin.vue";
import { onMounted,ref } from "vue";
import ErrorMessage from "@/components/Message/ErrorMessage.vue";
let urlParams = new URLSearchParams(window.location.search);
const data={
  chapter_name:urlParams.get('chapter_name'),
  quiz_id:urlParams.get('quiz_id'),
  question_description:"",
  option_1:"",
  option_2:"",
  option_3:"",
  option_4:"",
  answer:""
}

const msg=ref({});

const add_question=async(data)=>{
  await axios.post("http://localhost:5000/admin/add_question",data).then((response)=>{
    if(response.data.message=="Question limit reached"){
      msg.value.message=response.data.message;
    }
    else{
      window.location.href="/admin/quiz_dashboard";
    }
  }).catch((err)=>{
    console.log(err);
  })
}


</script>
<template>
  <nav class="navbar navbar-expand-lg pb-0 bg-body-tertiary">
    <NavAdmin /> 
    <div style="height: 100vh;" class="bg-light w-100">
      <h1 class="m-4">Add Question</h1>
      <div class="container">
        <form class="d-flex flex-column w-90" @submit.prevent="add_question(data)"  action="">
          <div class="mb-3">
            <label style="font-size: 30px;" class="form-label my-2" for="chapter">Question Description</label>
            <input v-model="data.question_description" style="font-size: 20px;" type="text" name="chapter" class="form-control" required  placeholder="Enter Question Description">
          </div>
          <div class="mb-3">
            <label style="font-size: 30px;" class="form-label my-2" for="option_1">Option 1</label>
            <input v-model="data.option_1" style="font-size: 20px;" type="text" name="option_1" class="form-control" required  placeholder="Enter Option 1">
          </div>
          <div class="mb-3">
            <label style="font-size: 30px;" class="form-label my-2" for="option_2">Option 2</label>
            <input  v-model="data.option_2" style="font-size: 20px;" type="text" name="option_2" class="form-control" required  placeholder="Enter Option 2">
          </div>
          <div class="mb-3">
            <label style="font-size: 30px;" class="form-label my-2" for="option_3">Option 3</label>
            <input v-model="data.option_3" style="font-size: 20px;" type="text" name="option_3" class="form-control" required  placeholder="Enter Option 3">
          </div>
          <div class="mb-3">
            <label style="font-size: 30px;" class="form-label my-2" for="option_4">Option 4</label>
            <input  v-model="data.option_4" style="font-size: 20px;" type="text" name="option_4" class="form-control" required  placeholder="Enter Option 4">
          </div>
          <div class="mb-3">
            <label style="font-size: 30px;" class="form-label my-2" for="description">Correct Option</label>
            <select v-model="data.answer" style="font-size: 20px;" class="form-select" aria-label="Default select example">
              <option selected value="">Select Correct Option</option>
              <option value="1">One</option>
              <option value="2">Two</option>
              <option value="3">Three</option>
              <option value="4">Four</option>
            </select>
          </div>
          <ErrorMessage v-if="msg.message" :message="msg.message" />
          <button style="font-size: 20px;background-color: #4723d9;color: aliceblue;" type="submit" class="m-3 btn  ">Submit</button>
        </form>
      </div>
    </div>
  </nav>
</template>
<style>
@import "../../assets/CSS/nav.css";

/* Add custom styles for better form spacing */
form {
  max-width: 600px;
  margin: auto;
}

form .form-label {
  font-weight: bold;
}

form .form-control {
  padding: 10px;
  font-size: 18px;
}

form .btn {
  padding: 10px 20px;
  font-size: 18px;
}
</style>
