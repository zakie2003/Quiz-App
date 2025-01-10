<script setup>
import "@/assets/JS/nav.js"
</script>
<template>
  <header class="header" id="header">
    <div class="header_toggle"> <i class='bx bx-menu' id="header-toggle"></i> </div>
    <div class="header_img"> <img src="https://upload.wikimedia.org/wikipedia/commons/9/99/Sample_User_Icon.png" alt=""> </div>
  </header>
  <div class="l-navbar" id="nav-bar">
    <nav class="nav">
      <div>
        <a href="#" class="nav_logo"> <i class='bx bx-layer nav_logo-icon'></i> <span class="nav_logo-name">Quiz Master</span> </a>
        <div class="nav_list">
          <a href="/" class="nav_link"> <i class='bx bx-user-check nav_icon'></i> <span class="nav_name">Login</span> </a>
          <a href="/signin" class="nav_link"><i class='bx bx-user nav_icon'></i> <span class="nav_name">SignUp</span> </a>
          <button style="background: none;border: none;" class="nav_link "><i class='bx bx-moon' ></i> <span>Theme</span></button>
        </div>
      </div>
    </nav>
  </div>
</template>
<style>
@import "../../assets/CSS/nav.css";
</style>
