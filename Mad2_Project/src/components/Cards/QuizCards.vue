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

const get_questions=async()=>{
  await axios.post("http://localhost:5000/admin/get_questions",{"quiz_id":props.item.id,"chapter_name":props.item.chapter_name}).then((res)=>{
    data.value=res.data.data;
  }).then((err)=>{
    console.log(err);
  })
}

const delete_question=async(id)=>{
  await axios.post("http://localhost:5000/admin/delete_question",{"id":id}).then((res)=>{
    console.log(res);
    get_questions();
  }).then((err)=>{
    console.log(err);
  })
}

const go_to_edit_question=(id)=>{
  window.location.href="/admin/edit_question/"+id;
}

const go_to_preview=()=>{
  window.location.href="/admin/quiz_preview/";
}

onMounted(()=>{
  console.log(props);
  get_questions();
})

</script>
<template>
  <div v-on:click="go_to_preview" class="ag-courses_item">
    <div class="ag-courses-item_link">
      <div class="ag-courses-item_bg"></div>
      <div class="ag-courses-item_title">
        {{ props.item.quiz_name }}  
        <a>
          <button v-on:click.stop="go_to_add_question" style="background-color: aliceblue;color: black;" class="btn m-2">Add Question</button>
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
              <td>{{ item.id }}</td>
              <td>{{ item.question }}</td>
              <td>
                <button style="background-color: #f38d04;" v-on:click.stop="go_to_edit_question(item.id)" class="btn my-1">Edit</button> &nbsp;
                <button style="background-color: #f38d04;" v-on:click.stop="delete_question(item.id)" class="btn my-1">Delete</button>
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