<script setup>
import { ref, defineExpose, computed, onMounted } from 'vue';
import "@/assets/JS/nav.js";
import axios from "axios";
import NavAdmin from '@/components/NavBar/NavAdmin.vue';
import Cards from '@/components/Cards/Cards.vue';

// Example of making an authenticated request
const token = sessionStorage.getItem('token');
const name = sessionStorage.getItem('name');
const id = sessionStorage.getItem('id');
const password = sessionStorage.getItem('password');
const email = sessionStorage.getItem('email');

const data = ref({
  email: email,
  password: password,
  type: "Admin",
  token: token,
  name: name,
  chapters: []
});

const isLoading = ref(false);

const dynamicHeight = computed(() => {
  return '100vh';
});

axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;

defineExpose({
  data,
  isLoading,
  dynamicHeight
});

function go_to_create(){
  window.location.href="/admin/create_subject";
}

const fetchChapters = async () => {
  isLoading.value = true;
  try {
    const res = await axios("http://localhost:5000/admin/get_subject", {
      method: "GET",
      headers: { "Content-Type": "application/json" }
    });

    data.value.chapters = res.data.data;
    isLoading.value = false;
  } catch (err) {
    isLoading.value = false;
    console.log('Error:', err);
  }
};

onMounted(() => {
  fetchChapters();
});

</script>
<template>
  <nav class="navbar navbar-expand-lg pb-0 bg-body-tertiary">
    <NavAdmin /> 
    <div :style="{ minHeight: dynamicHeight }" class="bg-light w-100">
      <div v-if="isLoading">Loading</div>
      <div v-else>
        <h1 class="m-4">Welcome to Admin Dashboard, {{ data.name }}</h1> 
        <button v-on:click="go_to_create" type="button" style="background-color: #4723d9;color: aliceblue;" class="btn  m-4">Add Subject</button>
        <div v-for="(item, index) in data.chapters" :key="index">
          <Cards :item="item"/>
        </div>
      </div>
    </div>
  </nav>
</template>
<style>
@import "../assets/CSS/nav.css";
.ag-courses_box {
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-align: start;
    -ms-flex-align: start;
    align-items: flex-start;
    -ms-flex-wrap: wrap;
    flex-wrap: wrap;
    padding: 50px 0;
  }
</style>