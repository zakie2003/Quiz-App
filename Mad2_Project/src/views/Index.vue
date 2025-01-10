<script setup>
import "@/assets/JS/nav.js";
import Login from "@/components/Login.vue";
import NavBar from "@/components/NavBar/Nav.vue"; // Import NavBar component
</script>
<template>
  <nav class="navbar navbar-expand-lg pb-0 bg-body-tertiary">
    <NavBar /> <!-- Use NavBar component -->
    <div class="height-100 bg-light w-100">
      <Login/>
    </div>
  </nav>
</template>
<style>
@import "../assets/CSS/nav.css";
</style>