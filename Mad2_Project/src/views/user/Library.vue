<script setup>
import axios from 'axios';
import NavUser from '@/components/NavBar/NavUser.vue';
import Loader from '@/components/Loader/Loader.vue';
import { onMounted, ref } from 'vue';
import UserLibraryCard from '@/components/Cards/UserLibraryCard.vue';
import Footer from '@/components/Footer/Footer.vue';
const data=ref({
    isLoading: false,
    quizes:[]
})

const get_my_quizes=async()=>{
  data.value.isLoading=true;
  try {
    const res = await axios("https://quiz-app-chz3.onrender.com/user/get_my_quizes", {
      method: "POST",
      data:{"user_id":sessionStorage.getItem("id")},
      headers: { "Content-Type": "application/json" }
    });
    data.value.quizes=res.data.quiz_library_data;
    data.value.isLoading=false;
  } catch (err) {
    data.value.isLoading=false;
    console.log('Error:', err);
  }
}

onMounted(()=>{
    get_my_quizes();
})
</script>
<template>
    <nav class="navbar navbar-expand-lg pb-0 bg-body-tertiary">
      <NavUser/> 
      <div style="min-height: 100vh;" class="bg-light w-100">
        <div v-if="data.isLoading" style="display: flex;justify-content: center;align-items: center;height: 100vh;"><Loader/></div>
        <div v-else>
          <h3 class="p-4">My Quizzes</h3>
          <div class="ag-courses_box">
            <div v-for="item in data.quizes" :key="item.id">
                <UserLibraryCard :item="item"/>
            </div> 
        </div>
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
    justify-content: flex-start; /* Changed from space-around to flex-start */
  }
  .ag-courses_item {
    flex: 1 1 300px;
    margin: 10px;
    min-width: 300px; /* Set the minimum width for the card */
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