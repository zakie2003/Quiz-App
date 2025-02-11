<script setup>
import axios from "axios";
import NavAdmin from "@/components/NavBar/NavAdmin.vue";
import ErrorMessage from "@/components/Message/ErrorMessage.vue";
import { ref } from "vue";
const data={
  name:"",
  description:"",
}

const message=ref({
  "message":"",
  "status":""
})

const addSubject = async(data)=>{
  await axios("http://localhost:5000/admin/add_subject",{
    method:"POST",
    data:JSON.stringify(data),
    headers:{"Content-Type":"application/json"}
  }).then((res)=>{
    console.log(res.data);
    if(res.data.status===200){
      window.location.href="/admin/home";
    }
    if(res.data.message=="Subject already exists"){
      message.value.message=res.data.message;
      message.value.status="401";
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
      <h1 class="m-4">Create Chapter</h1>
      <div class="container">
        <ErrorMessage v-if="message.message" :message="message.message" :status="message.status"/>
        <form class="d-flex flex-column w-90" @submit.prevent="addSubject(data)" action="">
          <div class="mb-3">
            <label style="font-size: 30px;" class="form-label my-2" for="chapter">Chapter</label>
            <input style="font-size: 20px;" type="text" name="chapter" class="form-control"  v-model="data.name" placeholder="Enter Chapter Name">
          </div>
          <div class="mb-3">
            <label style="font-size: 30px;" class="form-label my-2" for="description">Description</label>
            <input style="font-size: 20px;" type="text" name="description" class="form-control" v-model="data.description" placeholder="Enter Description">
          </div>
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
