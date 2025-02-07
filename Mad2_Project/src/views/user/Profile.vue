<script setup>
import LineChart from '@/components/Charts/LineChart.vue';
import Accuracy from '@/components/Charts/Accuracy.vue';
import BarChart from '@/components/Charts/BarChart.vue';
import Footer from '@/components/Footer/Footer.vue';
import { onMounted, ref } from 'vue';
import axios from 'axios';
import NavUser from '@/components/NavBar/NavUser.vue';
import Radar from '@/components/Charts/Radar.vue';

const chart_data = ref({
  line_data: {},
  right: 0,
  wrong: 0,
  user_activity_data: {},
  top_chapter_names: {}
});

const default_img_url = "https://upload.wikimedia.org/wikipedia/commons/9/99/Sample_User_Icon.png";

const user_data = ref({
  name: sessionStorage.getItem('name') || '',
  email: sessionStorage.getItem('email') || '',
  img_url: sessionStorage.getItem('profile_url') || default_img_url
});


const get_user_chart = async () => {
  try {
    const res = await axios.post("http://localhost:5000/user/get_user_chart", {
      user_id: sessionStorage.getItem("id")
    });
    chart_data.value.line_data = res.data.line_chart;
    chart_data.value.top_chapter_names = res.data.top_chapter_names;
    chart_data.value.right = res.data.right;
    chart_data.value.wrong = res.data.wrong;
    chart_data.value.radar_chart=res.data.radar_chart;
    // console.log(chart_data.value);
  } catch (err) {
    console.error(err);
  }
};

const save_img=async()=>{
  try{
    await axios("http://localhost:5000/user/save_img",{
      method: 'POST',
      data: {
        user_id: sessionStorage.getItem("id"),
        img_url: user_data.value.img_url
      }
    }).then((res)=>{
      console.log(res.data);
    });
  }catch(err){
    console.error(err);
  }
}

const upload_image = async (event) => {
  const img1 = event.target.files[0];
  if (!img1) {
    console.error('No file selected');
    return;
  }
  const form_data = new FormData();
  form_data.append('file', img1);
  form_data.append('upload_preset', 'cloud_demo'); 
  form_data.append('cloud_name', 'dyt00fcs6');
  try {
    const res = await axios.post("https://api.cloudinary.com/v1_1/dyt00fcs6/image/upload", form_data, {
      headers: { 'Content-Type': 'multipart/form-data' }
    });
    user_data.value.img_url = res.data.secure_url;
    save_img();
    sessionStorage.setItem('profile_url', res.data.secure_url);
  } catch (error) {
    console.error('Error uploading image:', error.response ? error.response.data : error.message);
  }
};

onMounted(() => {
  get_user_chart();
});
</script>

<template>
  <nav class="navbar navbar-expand-lg pb-0 bg-body-tertiary">
    <NavUser />
    <div style="min-height: 100vh;" class="bg-light w-100">
      <div v-if="isLoading" class="text-center mt-5">
        <p>Loading...</p>
      </div>
      <div v-else>
        <div class="row m-4 w-100" >
          <!-- Profile Card -->
          <div class="col-md-6">
            <div class="p-2 rounded mt-4 text-white profile-card" style="background-color: #4723d9;">
              <div class="d-flex justify-content-between align-items-center">
                <h1 class="mx-4 mt-4">Profile</h1>
                <button class="btn edit-button"><i class='bx bx-edit-alt'></i></button>
              </div>
              <div class="row g-3 align-items-center mt-4 mb-5">
                <div  class="col-4 text-center">
                  <input type="file" @change="upload_image" style="display: none;" ref="fileInput">
                  <div class="profile_img_container" @click="$refs.fileInput.click()">
                    <img
                      class="profile_img"
                      :src="user_data.img_url || default_img_url"
                      alt="Profile"
                    />
                    <div class="edit_overlay">Edit</div>
                  </div>
                </div>
                <div class="col-8 profile-text" style="font-size:x-large;">
                  <div class="mb-2"><strong>Name:</strong> {{ user_data.name }}</div>
                  <div class="mb-2"><strong>User Type:</strong> Student</div>
                  <div class="mb-2"><strong>Email:</strong> {{ user_data.email }}</div>
                </div>
              </div>
            </div>
          </div>

          <!-- Quiz Participation Trends -->
          <div class="col-md-6">
            <h1 class="mx-4 mb-5">Quiz Participation Trends</h1>
            <LineChart :line_data="chart_data.line_data" />
          </div>
        </div>

        <!-- Additional Charts -->
        <div class="row m-4">
          <div class="col-md-4">
            <h1 class="mx-4 mb-5">Student Accuracy</h1>
            <Accuracy :wrong="chart_data.wrong" :right="chart_data.right" />
          </div>
          <div class="col-md-4">
            <h1 class="mx-4 mb-5">Domain Growth</h1>
            <div style="width: 300px;">
                <Radar :radar_data="chart_data.radar_chart"/>
            </div>
          </div>

          <div class="col-md-4">
            <h1 class="mx-4 mb-5">Popular Chapters</h1>
            <BarChart :bar_data="chart_data.top_chapter_names" />
          </div>
        </div>
      </div>
    </div>
  </nav>
  <Footer />
</template>

<style>
.profile_img_container {
  position: relative;
  display: inline-block;
}

.profile_img {
  width: 125px;
  border-radius: 50%;
  background-color: aliceblue;
}

.edit_overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  background-color: rgba(0, 0, 0, 0.5);
  border-radius: 50%;
  opacity: 0;
  transition: opacity 0.3s;
}

.profile_img_container:hover .edit_overlay {
  opacity: 1;
}

.col-8 {
  word-wrap: break-word;
}

.profile-card {
  font-size: medium;
}

.profile-text {
  font-size: xx-large;
}

.edit-button {
  color: aliceblue;
  border: 1px solid aliceblue;
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-right:15px;
}

@media (max-width: 768px) {
  .profile-card {
    font-size: medium;
  }
  .profile-text {
    font-size: large;
  }
  .profile_img {
    width: 55px;
  }
}
</style>
