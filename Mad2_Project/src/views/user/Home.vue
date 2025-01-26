<script setup>
import axios from 'axios';
import NavUser from '@/components/NavBar/NavUser.vue';
import Loader from '@/components/Loader/Loader.vue';
import UserCard from '@/components/Cards/UserCard.vue';
import Footer from '@/components/Footer/Footer.vue';
import { onMounted, ref } from 'vue';
const data=ref({
    isLoading: false,
    free_quizes:[]
})
const get_ready_quizes=async()=>{
  await axios("http://localhost:5000/user/get_ready_quizes").then((res)=>{
    data.value.free_quizes=res.data.ready_quiz_data;
  }).catch((err)=>{
    console.log(err);
  })
}

onMounted(()=>{
  get_ready_quizes();
})
</script>
<template>
    <nav class="navbar navbar-expand-lg pb-0 bg-body-tertiary">
      <NavUser/> 
      <div style="min-height: 100vh;" class="bg-light w-100">
        <div v-if="data.isLoading" style="display: flex;justify-content: center;align-items: center;height: 100vh;"><Loader/></div>
        <div v-else>
          <h3 class="p-4">Quiz Recommendations</h3>
          <div class="ag-courses_box px-4">
            <div v-for="item in data.free_quizes" :key="item.id">
                <UserCard :item="item"/>
            </div> 
        </div>
        <!-- <h3 class="p-4">Paid Quizzes</h3>
        <div class="ag-courses_box">
            <div v-for="i in 4" :key="i">
                <UserCard color='yellow'/>
            </div> 
        </div> -->
        </div>
      </div>
    </nav>
    <Footer/>
  </template>
  <style>
  @import "../../assets/CSS/nav.css";
  .ag-courses_box {
    display: flex;
    flex-wrap: wrap;
    justify-content: flex-start; 
    width: 100%;

  }
  .ag-courses_item {
    flex: 1 1 300px;
    margin: 10px;
    min-width: 300px;
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
      padding: 0px 0px !important;
    }
  </style>