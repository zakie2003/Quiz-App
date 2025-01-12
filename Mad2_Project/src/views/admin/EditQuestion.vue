<script setup>
import axios from "axios";
import NavAdmin from "@/components/NavBar/NavAdmin.vue";
import { onMounted, reactive } from "vue";

let urlParams = new URLSearchParams(window.location.search);
const data = reactive({
  chapter_name: urlParams.get('chapter_name'),
  quiz_id: urlParams.get('quiz_id'),
  question: "",
  option_a: "",
  option_b: "",
  option_c: "",
  option_d: "",
  correct_option: "",
});

const get_question = async () => {
  let urlPath = window.location.pathname;
  const parts = urlPath.split('/');
  const question_id = parts[parts.length - 1]; // Extract the question_id

  try {
    const res = await axios.post("http://localhost:5000/admin/get_question", { question_id });
    // Ensure the API response matches the structure of `data`
    if (res.data && res.data.data) {
      Object.assign(data, res.data.data);
      console.log(data);
    } else {
      console.error("Invalid API response:", res.data);
    }
  } catch (err) {
    console.error("Error fetching question:", err);
  }
};

const add_question = async () => {
  let urlPath = window.location.pathname;
  const parts = urlPath.split('/');
  const question_id = parts[parts.length - 1]; 
  const formData = {
    id: question_id,
    chapter_name: data.chapter_name,
    quiz_id: data.quiz_id,
    question_description: data.question,
    option_1: data.option_a,
    option_2: data.option_b,
    option_3: data.option_c,
    option_4: data.option_d,
    correct_option: data.correct_option,
  };

  try {
     await axios.post("http://localhost:5000/admin/edit_question", formData).then((res) => {
       console.log(res);
       window.location.href = "/admin/quiz_dashboard";
     }).catch((err) => {
       console.log(err);
     })
    // window.location.href = "/admin/quiz_dashboard";
  } catch (err) {
    console.error("Error updating question:", err);
    alert("Failed to update question.");
  }
};

onMounted(() => {
  get_question();
});
</script>

<template>
  <nav class="navbar navbar-expand-lg pb-0 bg-body-tertiary">
    <NavAdmin />
    <div style="height: 100vh;" class="bg-light w-100">
      <h1 class="m-4">Edit Question</h1>
      <div class="container">
        <form
          class="d-flex flex-column w-90"
          @submit.prevent="add_question"
          action=""
        >
          <div class="mb-3">
            <label class="form-label my-2" for="chapter">Question Description</label>
            <input
              v-model="data.question"
              type="text"
              class="form-control"
              required
              placeholder="Enter Question Description"
            />
          </div>
          <div class="mb-3">
            <label class="form-label my-2" for="option_1">Option 1</label>
            <input
              v-model="data.option_a"
              type="text"
              class="form-control"
              required
              placeholder="Enter Option 1"
            />
          </div>
          <div class="mb-3">
            <label class="form-label my-2" for="option_2">Option 2</label>
            <input
              v-model="data.option_b"
              type="text"
              class="form-control"
              required
              placeholder="Enter Option 2"
            />
          </div>
          <div class="mb-3">
            <label class="form-label my-2" for="option_3">Option 3</label>
            <input
              v-model="data.option_c"
              type="text"
              class="form-control"
              required
              placeholder="Enter Option 3"
            />
          </div>
          <div class="mb-3">
            <label class="form-label my-2" for="option_4">Option 4</label>
            <input
              v-model="data.option_d"
              type="text"
              class="form-control"
              required
              placeholder="Enter Option 4"
            />
          </div>
          <div class="mb-3">
            <label class="form-label my-2" for="description">Correct Option</label>
            <select
              v-model="data.correct_option"
              class="form-select"
              required
            >
              <option value="" disabled>Select Correct Option</option>
              <option value="1">One</option>
              <option value="2">Two</option>
              <option value="3">Three</option>
              <option value="4">Four</option>
            </select>
          </div>
          <button type="submit" class="btn btn-primary m-3">Edit</button>
        </form>
      </div>
    </div>
  </nav>
</template>

<style>
@import "../../assets/CSS/nav.css";

/* Add custom styles for better form spacing */
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
