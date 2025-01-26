<script setup>
import axios from 'axios';
import { ref } from 'vue';

let input_search= ref('');

const search=async()=>{
  if(input_search.value){
    window.location.href=`/user/search/${input_search.value}`;
  }
}

</script>
<template>
<div class="search">
        <input v-model="input_search" placeholder="Search..." type="text">
        <button v-on:click="search" type="submit">Go</button>
</div>
</template>
<style>

.search {
  display: inline-block;
  position: relative;
}

.search input[type="text"] {
  width: 300px;
  padding: 10px;
  border: none;
  border-radius: 20px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.search button[type="submit"] {
  background-color: #4723D9;
  border: none;
  color: #fff;
  cursor: pointer;
  padding: 10px 20px;
  border-radius: 20px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  position: absolute;
  top: 0;
  right: 0;
  transition: .9s ease;
}

.search button[type="submit"]:hover {
  transform: scale(1.1);
  color: rgb(255, 255, 255);
  background-color: rgb(132, 0, 255);
}

</style>