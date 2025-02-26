<script setup>
import axios from "axios";
import NavAdmin from "@/components/NavBar/NavAdmin.vue";
import ErrorMessage from "@/components/Message/ErrorMessage.vue";
import { ref } from "vue";

let urlParams = new URLSearchParams(window.location.search);
const data={
  name:urlParams.get('name'),
  numberofquestion:urlParams.get('numberofquestion'),
  subject_id:urlParams.get('id')
}

let alert_message=ref("");

const edit_chapter=async(data)=>{
    await axios("http://localhost:5000/admin/edit_chapter",{
        method:"POST",
        data:JSON.stringify(data),
        headers:{"Content-Type":"application/json"}
    }).then((res)=>{
        console.log(res.data);
        if(res.data.status===200){
            window.location.href="/admin/home";
        }
        else{
          alert_message.value=res.data.message;
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
      <div class="container">
        <ErrorMessage v-if="alert_message" :message="alert_message"/>
      </div>
      <h1 class="m-4">Edit Subject</h1>
      <div class="container">
        <form class="d-flex flex-column w-90" @submit.prevent="edit_chapter(data)" action="">
          <div class="mb-3">
            <label style="font-size: 30px;" class="form-label my-2" for="subject">Subject Name</label>
            <input style="font-size: 20px;" type="text" name="subject" class="form-control"  v-model="data.name" placeholder="Enter Subject Name">
          </div>
          <div class="mb-3">
            <label style="font-size: 30px;" class="form-label my-2" for="max_questions">Maxiumum Questions</label>
            <input style="font-size: 20px;" type="number" name="max_questions" class="form-control" v-model="data.numberofquestion" placeholder="Enter Maximum Questions">
          </div>
          <button style="font-size: 20px;background-color: #4723d9;color: aliceblue;" type="submit" class="m-3 btn  ">Edit</button>
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
