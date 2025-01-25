<script setup>
import LineChart from '@/components/Charts/LineChart.vue';
import NavAdmin from '@/components/NavBar/NavAdmin.vue';
import PieChart from '@/components/Charts/PieChart.vue';
import BarChart from '@/components/Charts/BarChart.vue';
import { onMounted, ref } from 'vue';
import axios from 'axios';

const chart_data = ref({
  piechart_data: {},
  user_activity_data: {}
});

const isLoading = ref(true);

const fetchData = async () => {
  await axios.get('http://localhost:5000/user/get_profile_data').then((res) => {
    chart_data.value.piechart_data = res.data.device_data;
    chart_data.value.top_quiz_names = res.data.top_quiz_names;
    chart_data.value.user_activity_data = res.data.user_activity_data;
    isLoading.value = false;
    console.log("Fetched data:", res.data);
  }).catch((err) => {
    console.log(err);
  });
};

onMounted(() => {
  fetchData();
});

</script>
<template>
    <nav class="navbar navbar-expand-lg pb-0 bg-body-tertiary">
      <NavAdmin /> 
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
                    <div class="mb-2"><strong>Name:</strong> Zakie Khan</div>
                    <div><strong>User Type:</strong> Admin</div>
                  </div>
                </div>
              </div>
            </div>
            <div class="col-md-6">
              <h1 class="mx-4">User Login Activity</h1>
              <LineChart :line_data="chart_data.user_activity_data"/>
            </div>
          </div>
          <div class="row m-4">
            <div class="col-md-6">
              <PieChart :pie_data="chart_data.piechart_data"/>
            </div>
            <div class="col-md-6">
              <h1 class="m-4">Top Quizes</h1>
              <BarChart :bar_data="chart_data.top_quiz_names"/>
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
</style>