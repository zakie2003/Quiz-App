<script setup>
import axios from 'axios';
import { onMounted, ref } from 'vue';

const props=defineProps(
  {
    item:Object
  }
)

const data=ref({})

const get_chapters=async()=>{
  await axios("https://quiz-app-chz3.onrender.com/admin/get_chapter?subject_id="+props.item.id).then((res)=>{
    console.log(res.data.data);
    data.value=res.data.data;
  }).catch((err)=>{
    console.log(err);
  })
}

const go_to_edit=(name,numberofquestion)=>{
  window.location.href="/admin/edit_chapter?id="+props.item.id+"&name="+name+"&numberofquestion="+numberofquestion;
}

const delete_chapter=async(name)=>{
  await axios("https://quiz-app-chz3.onrender.com/admin/delete_chapter?name="+name).then((res)=>{
    get_chapters();
  }).catch((err)=>{
    console.log(err);
  })
}

const delete_subject=async(chap_name)=>{
  console.log(chap_name);
  await axios.post("https://quiz-app-chz3.onrender.com/admin/delete_subject",{"name":chap_name}).then((res)=>{
    console.log(res);
    if(res.data.message=="Can't delete subject with Chapters,delete Chapters first"){
      alert(res.data.message);
    }
    else{
      alert(res.data.message);
      window.location.reload();
    }
  }).catch((err)=>{
    console.log(err);
  })
}

onMounted(()=>{
  get_chapters();
})

const url=ref(`/admin/create_chapter/?id=${props.item.id}`);

</script>
<template>
  <div class="ag-courses_item">
    <div class="ag-courses-item_link">
      <div class="ag-courses-item_bg"></div>
      <div class="ag-courses-item_title">
        {{props.item.name}}  
        <a :href="url">
          <button style="background-color: aliceblue;color: black;" class="btn m-2">Add Chapter</button>
        </a>
        <button v-on:click="delete_subject(props.item.name)" style="background-color: aliceblue;color: black;" class="btn m-2">Delete</button>
      </div>
      <div style="z-index: 2;position: relative;" class="text-white">
        <table style="background: none; width: 100%;">
          <thead>
            <tr>
              <th>Chapter</th>
              <th>No of Questions</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            
            <tr v-for="(item, index) in data" :key="index">
              <td>{{item.name}}</td>
              <td>{{item.number_of_questions}}</td>
              <td>
                <button v-on:click="go_to_edit(item.name,item.number_of_questions)" class="btn my-1 button_option"><i class='bx bxs-edit-alt'></i></button> &nbsp;
                <button v-on:click="delete_chapter(item.name)" class="btn my-1 button_option"><i class='bx bx-trash'></i></button>
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

.button_option{
  background-color: aliceblue;
  color: black;
}

.button_option:hover{
  background-color: black;
  color: aliceblue;
}
.ag-courses-item_bg{
  background: rgb(116,63,213);background: radial-gradient(circle, rgba(116,63,213,1) 0%, rgba(0,248,251,1) 90%) !important;
}

</style>