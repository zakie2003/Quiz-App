<script setup>
import LineChart from '@/components/Charts/LineChart.vue';
import Accuracy from '@/components/Charts/Accuracy.vue';
import BarChart from '@/components/Charts/BarChart.vue';
import { onMounted, ref } from 'vue';
import axios from 'axios';
import NavUser from '@/components/NavBar/NavUser.vue';

const chart_data = ref({
  line_data: {},
  right: 0,
  wrong: 0,
  user_activity_data: {},
  top_chapter_names:{}
});

const user_data=ref({
  name:sessionStorage.getItem('name'),
  email:sessionStorage.getItem('email')
})

const get_user_chart=async()=>{
  await axios.post("http://localhost:5000/user/get_user_chart",{"user_id":sessionStorage.getItem("id")}).then((res)=>{
    chart_data.value.line_data=res.data.line_chart;
    chart_data.value.top_chapter_names=res.data.top_chapter_names;
    chart_data.value.right=res.data.right;
    chart_data.value.wrong=res.data.wrong;
    console.log(chart_data)
  }).catch((err)=>{
    console.log(err);
  })
}

const isLoading = ref(false);

onMounted(()=>{
  get_user_chart();
  console.log(chart_data.value.line_data);
})

</script>

<template>
  <nav class="navbar navbar-expand-lg pb-0 bg-body-tertiary">
    <NavUser/> 
    <div style="min-height: 100vh;" class="bg-light w-100">
      <div v-if="isLoading" class="text-center mt-5">
        <p>Loading...</p>
      </div>
      <div v-else>
        <div class="row m-4">
          <div class="col-md-6">
            <div class="p-2 rounded mt-4 text-white"  style="background-color: #4723d9;">
              <h1 class="mx-4  mt-4">Profile</h1>
              <div class="row g-3 align-items-center mt-4 mb-5">
                <div class="col-4 text-center">
                  <img class="profile_img" src="https://upload.wikimedia.org/wikipedia/commons/9/99/Sample_User_Icon.png" alt="Error">
                </div>
                <div style="font-size:xx-large;" class="col-8">
                  <div class="mb-2"><strong>Name:</strong> {{ user_data.name }}</div>
                  <div><strong>User Type:</strong> Student</div>
                  <div><strong>Email:</strong> {{ user_data.email }}</div>
                </div>
              </div>
            </div>
          </div>
          <div class="col-md-6">
            <h1 class="mx-4 mb-5">Quiz Participation Trends</h1>
            <LineChart :line_data="chart_data.line_data"/>
          </div>
        </div>
        <div class="row m-4">
          <div class="col-md-6">
            <h1 class="mx-4 mb-5">Student Accuracy</h1>
            <Accuracy :wrong="chart_data.wrong" :right="chart_data.right"/>
          </div>
          <div class="col-md-6">
            <h1 class="mx-4 mb-5">Your Popular Chapters</h1>
            <BarChart :bar_data="chart_data.top_chapter_names"/>
          </div>
        </div>
      </div>
    </div>
  </nav>
</template>

<style>
.profile_img {
  width: 125px;
  border-radius: 50%;
  background-color: aliceblue;
}

.col-8 {
  word-wrap: break-word;
}
</style>