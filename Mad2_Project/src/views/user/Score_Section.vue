<script setup>
import axios from 'axios';
import NavUser from '@/components/NavBar/NavUser.vue';
import Loader from '@/components/Loader/Loader.vue';
import { onMounted, ref } from 'vue';
import UserLibraryCard from '@/components/Cards/UserLibraryCard.vue';
import Footer from '@/components/Footer/Footer.vue';
const data=ref({
    isLoading: false,
    scores:[]
})

const get_reports=async()=>{
    data.value.isLoading=true;
    axios.post("http://localhost:5000/user/get_score",{"user_id":sessionStorage.getItem("id")}).then((res)=>{
        console.log(res.data);
        data.value.scores=res.data.Score_list;
        data.value.isLoading=false;
    }).catch((err)=>{
      console.log(err);
    })
}

onMounted(()=>{
  get_reports();
})

</script>
<template>
    <nav class="navbar navbar-expand-lg pb-0 bg-body-tertiary">
      <NavUser/> 
      <div style="min-height: 100vh;" class="bg-light w-100">
        <div v-if="data.isLoading" style="display: flex;justify-content: center;align-items: center;height: 100vh;"><Loader/></div>
        <div v-else>
          <h3 class="p-4">Score Dashboard</h3>
          <table class="table container rounded">
            <thead>
              <tr>
                <th class="row_table" scope="col">Quiz Name</th>
                <th class="row_table" scope="col">Date</th>
                <th class="row_table" scope="col">Score</th>
                <th class="row_table" scope="col">Action</th>
              </tr>
            </thead>
            <tbody>
                <tr v-for="(item, index) in data.scores" :key="index">
                  <td scope="row">{{ item.quiz_name }}</td>
                  <td scope="row">{{ item.date }}</td>
                  <td scope="row">{{ Math.round(item.score) }}</td>
                  <td>
                    <a href="#">Download Report</a>
                  </td>
                </tr>
            </tbody>
          </table>
        </div>
      </div>
    </nav>
    <Footer/>
  </template>
  <style>
  @import "../../assets/CSS/nav.css";
.row_table{
    color: aliceblue !important;
    background-color: #4723d9 !important;
}
  </style>