<script setup>
import axios from 'axios';
import { onMounted, ref } from 'vue';

const props = defineProps({
  item: Object,
  isready: Boolean,
  display_button: Boolean
})

const data = ref({})

const go_to_add_question = () => {
  window.location.href = "/admin/add_question?quiz_id=" + props.item.id + "&chapter_name=" + props.item.chapter_name;
}

const get_questions = async () => {
  await axios.post("http://localhost:5000/admin/get_questions", { "quiz_id": props.item.id, "chapter_name": props.item.chapter_name }).then((res) => {
    data.value = res.data.data;
  }).then((err) => {
    console.log(err);
  })
}

const delete_question = async (id) => {
  await axios.post("http://localhost:5000/admin/delete_question", { "id": id }).then((res) => {
    console.log(res);
    get_questions();
  }).then((err) => {
    console.log(err);
  })
}

const go_to_edit_question = (id) => {
  window.location.href = "/admin/edit_question/" + id;
}

const go_to_preview = (event, chapter_name, quiz_id) => {
  event.preventDefault();
  window.location.href = "/admin/quiz_preview/" + chapter_name + "/" + quiz_id;
}

onMounted(() => {
  // console.log(props);
  get_questions();
})

const add_to_ready_quiz = async (id) => {
  await axios.post("http://localhost:5000/admin/add_ready_quiz", { "quiz_id": id }).then((res) => {
    console.log(res);
    window.location.reload();
  }).then((err) => {
    console.log(err);
  })
}

const remove_from_ready_quiz = async (id) => {
  await axios.post("http://localhost:5000/admin/remove_ready_quiz", { "quiz_id": id }).then((res) => {
    console.log(res);
    window.location.reload();
  }).catch((err) => {
    console.log(err);
  })
}

</script>
<template>
  <div class="ag-courses_item">
    <div class="ag-courses-item_link">
      <div class="ag-courses-item_bg"></div>
      <div class="ag-courses-item_title">
        {{ props.item.quiz_name }}  
        <a>
          <button v-if="!props.isready" v-on:click.stop="go_to_add_question(props.item.id)" style="background-color: aliceblue;color: black;" class="btn m-2">Add Question</button>
        </a>
      </div>
      <div style="z-index: 2;position: relative;" class="text-white">
        <table style="background: none; width: 100%;">
          <thead>
            <tr>
              <th>ID</th>
              <th>Question Title</th>
              <th v-if="!props.isready">Actions</th>
            </tr>
          </thead>
          <tbody>
            
            <tr v-for="(item, index) in data" :key="index">
              <td>{{ item.id }}</td>
              <td>{{ item.question }}</td>
              <td v-if="!props.isready">
                <button style="background-color: aliceblue;" v-on:click.stop="go_to_edit_question(item.id)" class="btn my-1"><i class='bx bxs-edit-alt'></i></button> &nbsp;
                <button style="background-color: aliceblue;" v-on:click.stop="delete_question(item.id)" class="btn my-1"><i class='bx bx-trash'></i></button>
              </td>
            </tr>
          </tbody>
        </table>
        <div v-if="props.display_button==true">
          <button v-if="!props.isready" v-on:click.stop="add_to_ready_quiz(props.item.id)" style="background-color: aliceblue;color: black;width: 100%;" class="btn my-2">Add to Ready Quiz</button>
          <button v-else v-on:click.stop="remove_from_ready_quiz(props.item.id)" style="background-color: aliceblue;color: black;width: 100%;" class="btn my-2">Go Back</button>
        </div>
      </div>
    </div>
  </div>
</template>
<style>
@import "../../assets/CSS/card.css";
.ag-courses-item_bg{
  background: rgb(116,63,213);background: radial-gradient(circle, rgba(116,63,213,1) 0%, rgba(0,248,251,1) 90%);
}
</style>