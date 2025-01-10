<script setup>
import axios from 'axios';
import { onMounted, ref } from 'vue';

const props=defineProps(
  {
    item:Object
  }
)

const data=ref({})

const go_to_add_question=()=>{
  window.location.href="/admin/add_question?quiz_id="+props.item.id+"&chapter_name="+props.item.chapter_name;
}



</script>
<template>
  <div class="ag-courses_item">
    <div class="ag-courses-item_link">
      <div class="ag-courses-item_bg"></div>
      <div class="ag-courses-item_title">
        {{ props.item.quiz_name }}  
        <a>
          <button v-on:click="go_to_add_question" style="background-color: aliceblue;color: black;" class="btn m-2">Add Question</button>
        </a>
      </div>
      <div style="z-index: 2;position: relative;" class="text-white">
        <table style="background: none; width: 100%;">
          <thead>
            <tr>
              <th>ID</th>
              <th>Question Title</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            
            <tr v-for="(item, index) in data" :key="index">
              <td>mkmom</td>
              <td>0</td>
              <td>
                <button v-on:click="go_to_edit(item.name,item.number_of_questions)" style="background-color: #f38d04;" class="btn my-1">Edit</button> &nbsp;
                <button v-on:click="delete_chapter(item.name)" style="background-color: #f38d04;" class="btn my-1">Delete</button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>
<style>
@import "../../assets/CSS/card.css";
.ag-courses-item_bg{
  background-color: #2399d9 !important;
}
</style>