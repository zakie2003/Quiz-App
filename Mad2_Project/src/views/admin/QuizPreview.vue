<script setup>
import "@/assets/JS/nav.js";
</script>
<template>
  <header  class="header bg-light p-3 mb-3 nav_bar text-white" id="header">
    <h3 class="pt-2">Quiz Preview</h3>
  </header>
  <div class="row">
    <div class="col-7 mx-2 my-4 rounded p-4 bg-light">
      <div class="py-4 text-left">
        <h3>Question No 1</h3>
        <span class="p-2 d-block" style="font-size: larger;">
          4 men and 7 women can do a work in 8 days.
          7 men and 4 women can do the same work in 5 days.
          Find the number of days in which 8 women can finish the work.
        </span>
        <h3 class="pt-4">Options</h3>
        <div class="py-2">
          <button style="font-size: larger;" class="btn w-100 my-2 text-start border">4 days</button>
          <button style="font-size: larger;" class="btn w-100 my-2 text-start border">5 days</button>
          <button style="font-size: larger;" class="btn w-100 my-2 text-start border">6 days</button>
          <button style="font-size: larger;" class="btn w-100 my-2 text-start border">7 days</button>
        </div>
        <div class="d-flex justify-content-between pt-4">
          <button class="btn nav_bar text-white">Previous</button>
          <button class="btn nav_bar text-white">Next</button>
        </div>
      </div>
    </div>
    <div class="col-4 mx-2 my-4 rounded p-4 bg-light">
      <h3 class="py-4">Questions</h3>
      <div class="row justify-content-center">
        <button class="btn col-3 py-3 m-2 nav_bar text-white" v-for="i in 10" :key="i">{{ i }}</button>
      </div>
    </div>
  </div>
</template>
<style>
@import "../../assets/CSS/nav.css";
.nav_bar{
  background-color: #4723D9 !important;
}
</style>
