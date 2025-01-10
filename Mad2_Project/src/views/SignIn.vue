<script setup>
import "@/assets/JS/nav.js";
import Signin from "@/components/SignIn.vue";
import NavBar from "@/components/NavBar/Nav.vue"; // Import NavBar component
</script>
<template>
  <nav class="pb-0 navbar navbar-expand-lg bg-body-tertiary">
    <NavBar /> <!-- Use NavBar component -->
    <div class="height-100 bg-light w-100">
      <Signin/>
    </div>
  </nav>
</template>
<style>
@import "../assets/CSS/nav.css";
</style>