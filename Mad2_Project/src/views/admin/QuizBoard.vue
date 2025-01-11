<script setup>
import axios from "axios";
import NavAdmin from "@/components/NavBar/NavAdmin.vue";
import QuizCards from "@/components/Cards/QuizCards.vue";
import { onMounted, ref } from "vue";

const data = ref({
  name: "",
  description: "",
  quiz_data: []
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

onMounted(() => {
  fetch_quiz();
});

</script>
<template>
  <nav class="navbar navbar-expand-lg pb-0 bg-body-tertiary">
    <NavAdmin /> 
    <div style="height: 100vh;" class="bg-light w-100">
      <h1 class="m-4">Quiz Dashboard  <button v-on:click="go_to_create_quiz" style="background-color: #4723d9;color: aliceblue;" class="btn">Create Quiz</button></h1> 
      <div v-for="(item, index) in data.quiz_data" :key="index">
        <QuizCards :item="item"/>
      </div>
    </div>
  </nav>
</template>
<style>
@import "../../assets/CSS/nav.css";


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
