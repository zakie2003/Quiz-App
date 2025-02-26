<script setup>
import axios from "axios";
import NavAdmin from "@/components/NavBar/NavAdmin.vue";
import QuizCards from "@/components/Cards/QuizCards.vue";
import { onMounted, ref } from "vue";
import ErrorMessage from "@/components/Message/ErrorMessage.vue";

const data = ref({
  name: "",
  description: "",
  quiz_data: [],
  ready_quiz_data: [],
  alert_msg: "",
});

const go_to_create_quiz = () => {
  window.location.href = "/admin/create_quiz";
};

const fetch_quiz = async () => {
  await axios("http://localhost:5000/admin/get_quizes")
    .then((res) => {
      data.value.quiz_data = res.data.quiz_data;
      console.log(data.value.quiz_data);
    })
    .catch((err) => {
      console.log(err);
    });
};

const fetch_ready_quiz = async () => {
  await axios("http://localhost:5000/admin/get_ready_quizes")
    .then((res) => {
      data.value.ready_quiz_data = res.data.ready_quiz_data;
      console.log(data.value.ready_quiz_data);
    })
    .catch((err) => {
      data.value.alert_msg = err.response.data.message;
      console.log(err);
    });
};

const refresh_quizzes = () => {
  fetch_quiz();
  fetch_ready_quiz();
};

onMounted(() => {
  refresh_quizzes();
});

</script>
<template>
  <nav class="navbar navbar-expand-lg pb-0 bg-body-tertiary">
    <NavAdmin /> 
    <div :style="{ minHeight: '100vh' }" class="bg-light w-100">
      <ErrorMessage v-if="data.alert_msg" :message="data.alert_msg" />
      <h1 class="m-4">Quiz Dashboard  <button v-on:click="go_to_create_quiz" style="background-color: #4723d9;color: aliceblue;" class="btn">Create Quiz</button></h1> 
      <div class="ag-courses_box row">
        <div v-for="(item, index) in data.quiz_data" :key="index" class="col-md-4">
          <QuizCards :display_button="true" :item="item" :isready="false"/>
        </div>
      </div>
      <h1 class="p-4">Ready Quiz</h1>
      <div class="ag-courses_box row">
        <div v-for="(item, index) in data.ready_quiz_data" :key="index" class="col-md-4">
          <QuizCards :display_button=true :item="item" :isready="true"/>
        </div>
      </div>
    </div>
  </nav>
</template>
<style>
@import "../../assets/CSS/nav.css";
@import "../../assets//CSS/login.css";

.ag-courses_box {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
}

.ag-courses_item {
  min-width: 300px; /* Set the minimum width for the card */
}

form {
  max-width: 600px;
  margin: auto;
}

form .form-label {
  font-weight: bold;
}

form .form-control {
  padding: 10px;
  font-size: 18px;
}

form .btn {
  padding: 10px 20px;
  font-size: 18px;
}
</style>
