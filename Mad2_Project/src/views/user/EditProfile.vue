<script setup>
import "@/assets/JS/nav.js";
import NavUser from "@/components/NavBar/NavUser.vue";
import axios from "axios";
import { onMounted, ref } from "vue";

const user_data=ref({
  email: sessionStorage.getItem('email') || ''
})

const data=ref({
  name:'',
  dob:'',
  qualification:''
})

const get_user_data=async()=>{
  await axios.post("https://quiz-app-chz3.onrender.com/user/get_user_data",{"email":user_data.value.email}).then((res)=>{
    data.value.name=res.data.user_data.name;
    data.value.dob=res.data.user_data.dob;
    data.value.qualification=res.data.user_data.qualification;
  }).catch((err)=>{
    console.log(err);
  })
}

const edit_profile=async()=>{
  await axios.post("https://quiz-app-chz3.onrender.com/user/edit_profile",{"email":user_data.value.email,"name":data.value.name,"dob":data.value.dob,"qualification":data.value.qualification}).then((res)=>{
    console.log(res.data);
    sessionStorage.setItem('name',data.value.name);
    sessionStorage.setItem('dob',data.value.dob);
    sessionStorage.setItem('qualification',data.value.qualification);
    window.location.href="/user/profile/"+user_data.value.email;
  }).catch((err)=>{
    console.log(err);
  })
}

onMounted(()=>{
  get_user_data();
})

</script>
<template>
  <nav class="pb-0 navbar navbar-expand-lg bg-body-tertiary">
    <NavUser/>
    <div style="min-height: 100vh;" class="bg-light w-100">
      <h1 class="m-4">Edit Profile</h1>
      <div class="container">
        <form
          class="d-flex flex-column w-90"
          @submit.prevent="add_question"
          action=""
        >
          <div class="mb-3">
            <label class="form-label my-2" for="chapter">Name</label>
            <input
              type="text"
              class="form-control"
              required
              placeholder="Enter Name" v-model="data.name"
            />
          </div>
          <div class="mb-3">
            <label class="form-label my-2" for="chapter">Date of Birth</label>
            <input
              type="date"
              class="form-control"
              required
              placeholder="Enter Date of Birth" v-model="data.dob"
            />
          </div>

          <div class="mb-3">
            <label class="form-label my-2" for="chapter">Qualification</label>
            <input
              type="text"
              class="form-control"
              required
              placeholder="Enter Qualification" v-model="data.qualification"
            />
          </div>

          <button v-on:click="edit_profile()" type="submit" style="background-color: #4723d9;color: aliceblue;" class="btn m-3">Edit</button>
        </form>
      </div>
    </div>
  </nav>
</template>
<style>
@import "../../assets/CSS/nav.css";
</style>