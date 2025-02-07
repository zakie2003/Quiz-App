<script setup>
import "@/assets/JS/nav.js";

function logout() {
    sessionStorage.clear();
    window.location.href = "/";
}

// Add mounted lifecycle hook
import { onMounted, ref } from 'vue';
import User_Search from "../SearchBar/User_Search.vue";
const user_data=ref({
    name:sessionStorage.getItem('name'),
    email:sessionStorage.getItem('email'),
    profile_url:sessionStorage.getItem('profile_url') || "https://upload.wikimedia.org/wikipedia/commons/9/99/Sample_User_Icon.png"
})


onMounted(() => {
    const toggle = document.getElementById('header-toggle');
    const nav = document.getElementById('nav-bar');
    const closeBtn = document.getElementById('nav-close');
    if (toggle && nav) {
        toggle.addEventListener('click', () => {
            nav.classList.toggle('show');
        });
    }
    if (closeBtn && nav) {
        closeBtn.addEventListener('click', () => {
            nav.classList.remove('show');
        });
    }
});

const go_to_profile=()=>{
  window.location.href='/user/profile/' + user_data.email;
}

</script>
<template>
  <header class="header" id="header">
    <div class="header_toggle"> <i class='bx bx-menu' id="header-toggle"></i> </div>
    <User_Search/>
    <div v-on:click="go_to_profile" class="header_img"> <img :src="user_data.profile_url" alt="Err"> </div>
  </header>
  <div class="l-navbar" id="nav-bar">
    <nav class="nav">
      <div>
        <a href="#" class="nav_logo"> <i class='bx bx-layer nav_logo-icon'></i> <span class="nav_logo-name">MindSpark</span> </a>
        <div class="nav_list">
          <a href="/user/home" class="nav_link"> <i class='bx bx-home nav_icon'></i> <span class="nav_name">Home</span> </a>
          <a href="/user/library" class="nav_link"><i class='bx bx-library nav_icon'></i> <span class="nav_name">Library</span> </a>
          <a href="/user/score" class="nav_link"><i class='bx bx-file-blank nav_icon'></i> <span class="nav_name">Score</span> </a>
          <a :href="'/user/profile/' + user_data.email" class="nav_link"><i class='bx bx-bar-chart-square nav_icon'></i> <span class="nav_name">Statistics</span> </a>
          <!-- <button style="background: none;border: none;" class="nav_link "><i class='bx bx-moon' ></i> <span>Theme</span></button> -->
          <button @click="logout" style="background: none;border: none;" class="nav_link "><i class='bx bx-door-open' ></i> <span>Logout</span></button>
          <button  style="background: none;border: none;" class="nav_close nav_link" id="nav-close"> <i  class='bx bx-x nav_icon'></i> Close</button>
        </div>
      </div>

    </nav>
  </div>
</template>
<style>
@import "../../assets/CSS/nav.css";
.header_name{
    align-items: end;
    font-weight: bolder;
}
</style>
