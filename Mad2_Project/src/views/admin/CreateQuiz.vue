<script setup>
import axios from "axios";
import NavAdmin from "@/components/NavBar/NavAdmin.vue";
import { onMounted, ref } from 'vue';

const data={
  quiz_name:"",
  chapter_name:"",
  date_of_conduction:"",
  minute:"",
  second:"",
  remark:""
}

let chapter=ref({});

const add_quiz=async(data)=>{
  await axios("http://localhost:5000/admin/add_quiz",{
    method:"POST",
    data:JSON.stringify(data),
    headers:{"Content-Type":"application/json"}
  }).then((res)=>{
    console.log(res);
    window.location.href="/admin/quiz_dashboard";
  }).catch((err)=>{
    console.log(err);
  })
}


const get_chapter=async()=>{
  await axios("http://localhost:5000/admin/get_chapter").then((res)=>{
    chapter.value=res.data.data;
    console.log(chapter);
  }).catch((err)=>{
    console.log(err);
  })
}

onMounted(()=>{
  get_chapter();
})

</script>
<template>
  <nav class="navbar navbar-expand-lg pb-0 bg-body-tertiary">
    <NavAdmin /> 
    <div style="min-height: 100vh;" class="bg-light w-100">
      <h1 class="m-4">Create Quiz</h1>
      <div class="container">
        <form class="d-flex flex-column w-90" action="" @submit.prevent="add_quiz(data)">
          <div class="mb-3">
            <label style="font-size: 20px;" class="form-label " for="subject">Quiz Name</label>
            <input style="font-size: 20px;" type="text" name="subject" class="form-control" required v-model="data.quiz_name" placeholder="Enter Quiz Name">
          </div>
          <div data-mdb-input-init class="form-outline mb-3">
                <label style="font-size: 20px;" class="form-label" for="typeSelect">Chapter</label>
                <select v-model="data.chapter_name"  name="type" id="typeSelect" class="form-control form-control-lg">
                    <option value="">Select Chapter</option>
                    <option v-for="item in chapter" :value="item.name">{{item.name}}</option>
                </select>
            </div>
            <div class="mb-3">
                <label style="font-size: 20px;" class="form-label " for="subject">Date of Conduction</label>
                <input v-model="data.date_of_conduction" style="font-size: 20px;" type="date" required name="subject" class="form-control" placeholder="Enter Date of Conduction">
            </div>
            <div class="mb-3">
                <label style="font-size: 20px;" class="form-label " for="subject">Quiz Duration</label>
                <div class="d-flex">
                    <input v-model="data.minute" style="font-size: 20px;" type="number" required name="subject" class="form-control" placeholder="Enter Minute">
                    <input v-model="data.second" style="font-size: 20px;" type="number" required name="subject" class="form-control" max="60" placeholder="Enter Second">
                </div>
            </div>
            <div class="mb-3">
                <label style="font-size: 20px;" class="form-label " for="remark">Quiz Remark</label>
                <input v-model="data.remark" style="font-size: 20px;" type="text" required name="remark" class="form-control" placeholder="Enter Remark">
            </div>
          <button style="font-size: 20px;background-color: #4723d9;color: aliceblue;" type="submit" class="m-3 btn  ">Create Quiz</button>
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
