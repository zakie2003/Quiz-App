<script setup>
import "@/assets/JS/nav.js";
import Loader from "@/components/Loader/Loader.vue";
import axios from "axios";
import { onMounted, ref, computed } from "vue";
import Footer from "@/components/Footer/Footer.vue";

const quiz_data = ref({
  quiz: {
    quiz_name: '',
    time_duration: '',
    chapter_name: '',
    questions: []
  }
});

const user_data = ref({
  name: sessionStorage.getItem('name'),
  profile_url: sessionStorage.getItem('profile_url') || "https://upload.wikimedia.org/wikipedia/commons/9/99/Sample_User_Icon.png"
});

const pointer = ref({ index: 0 });
const loading = ref(true);
const remainingTime = ref(0);
const minute = ref(0);
const second = ref(0);
const correct_options = ref([]);
const user_option = ref([]);
const question_ids = ref([]);
let timer;

const sidebarVisible = ref(false);

const toggleSidebar = () => {
  sidebarVisible.value = !sidebarVisible.value;
};

const get_quiz = async () => {
  const urlParams = window.location.pathname;
  const parts = urlParams.split('/');
  const quiz_id = parts[parts.length - 1];
  await axios.post("http://localhost:5000/admin/get_quiz", { "quiz_id": quiz_id }).then((res) => {
    quiz_data.value = res.data;
  }).catch((err) => {
    console.log(err);
  });
};

const get_questions = async () => {
  const urlParams = window.location.pathname;
  const parts = urlParams.split('/');
  const quiz_id = parts[parts.length - 1];
  const chapter_name = decodeURIComponent(parts[parts.length - 2]);
  await axios.post("http://localhost:5000/user/get_questions", { "chapter_name": chapter_name, "quiz_id": quiz_id }).then((res) => {
    quiz_data.value.questions = res.data.data.map(question => ({ ...question, isVisited: false }));
    correct_options.value = quiz_data.value.questions.map((question) => question.correct_option);
    user_option.value = quiz_data.value.questions.map((question) => '');
    question_ids.value = quiz_data.value.questions.map((question) => question.id);
  }).catch((err) => {
    console.log(err);
  });
};

const start_quiz = async () => {
  await axios.post("http://localhost:5000/user/start_quiz", {
    "quiz_id": quiz_data.value.quiz.id,
    "time_duration": quiz_data.value.quiz.time_duration,
    "user_id": sessionStorage.getItem("id")
  }).then((res) => {
    console.log(res);
  }).catch((err) => {
    console.log(err);
  });
};

const fetchRemainingTime = async () => {
  try {
    const response = await axios.post("http://localhost:5000/user/remaining_time", {
      "user_id": sessionStorage.getItem("id"),
      "quiz_id": quiz_data.value.quiz.id
    });
    const data = response.data;
    remainingTime.value = data.remainingTime;
    console.log(remainingTime.value);
    minute.value = Math.floor(remainingTime.value / 60);
    second.value = remainingTime.value % 60;
    if (remainingTime.value <= 0) {
      clearInterval(timer);
      await submit_quiz();
      window.location.href = "/user/library";
    }
  } catch (err) {
    console.log(err);
  }
};

const submit_quiz = async () => {
  try {
    await axios.post("http://localhost:5000/user/submit_quiz", {
      "user_id": sessionStorage.getItem("id"),
      "quiz_id": quiz_data.value.quiz.id,
      "user_answers": user_option.value,
      "correct_answers": correct_options.value,
      "question_ids": question_ids.value
    }).then((res) => {
      console.log(res);
    }).catch((err) => {
      console.log(err);
    });
  } catch (err) {
    console.log(err);
  }
};

const startLocalCountdown = () => {
  if (remainingTime.value > 0) {
    remainingTime.value = (remainingTime.value - 1);
  }
};

const click_option = (index, value) => {
  user_option.value[index] = value;
  quiz_data.value.questions[index].isVisited = true;
  console.log(user_option.value);
};

onMounted(async () => {
  await get_quiz();
  await get_questions();
  await start_quiz();
  loading.value = false;
  timer = setInterval(() => {
    startLocalCountdown();
  }, 1000);
  setInterval(fetchRemainingTime, 2000);
});

const next = () => {
  if (pointer.value.index < quiz_data.value.questions.length - 1) {
    pointer.value.index = pointer.value.index + 1;
    quiz_data.value.questions[pointer.value.index].isVisited = true;
  }
};

const prev = () => {
  if (pointer.value.index > 0) {
    pointer.value.index = pointer.value.index - 1;
    quiz_data.value.questions[pointer.value.index].isVisited = true;
  }
};

const go_to_this_question = (index) => {
  pointer.value.index = index;
  quiz_data.value.questions[index].isVisited = true;
};

const submit_button = async () => {
  await submit_quiz();
  clearInterval(timer);
  window.location.href = "/user/library";
};

const questionsLeft = computed(() => {
  return quiz_data.value.questions.filter(question => !question.isVisited).length;
});

const questionsAttempted = computed(() => {
  return quiz_data.value.questions.filter(question => question.isVisited && user_option.value[quiz_data.value.questions.indexOf(question)] !== '').length;
});

const questionsUnattempted = computed(() => {
  return quiz_data.value.questions.filter(question => question.isVisited && user_option.value[quiz_data.value.questions.indexOf(question)] === '').length;
});

</script>
<template>
  <header class="header bg-light p-3 mb-3 nav_bar text-white" id="header">
    <h3 class="pt-2 is_visible">Quiz Preview: {{ quiz_data.quiz.quiz_name }}</h3>
    <div class="make_center">
      <h3 class="pt-2">Time: {{ minute }}:{{ second }} <button class="btn pt-2 submit_option" style="font-weight: bold;" v-on:click="submit_button">Submit</button></h3>
    </div>
    <h3 class="pt-2 is_visible">Chapter Name: {{ quiz_data.quiz.chapter_name }}</h3>
    <button class="btn nav_bar text-white toggle-sidebar d-md-none" v-on:click="toggleSidebar"><i class='bx bx-menu mt-1'></i></button>
  </header>
  <div class="row loader-container" v-if="loading">
    <Loader/>
  </div>
  <div class="row" v-else>
    <div class="row no-questions" v-if="quiz_data.questions.length==0">
      <h3 class="col-7 mx-2 my-4 rounded p-4 bg-light text-center">No questions found</h3>  
    </div>
    <div class="row" v-else>
        <div class="col-12 col-md-7 mx-1 my-4 rounded p-4 bg-light question-container">
          <div class="py-4 text-left">
            <div class="d-flex justify-content-between align-items-center">
              <h3>Question No {{ pointer.index + 1 }}</h3>
            </div>
            <span class="p-2 d-block question-text">
              {{ quiz_data.questions[pointer.index].question }}
            </span>
            <h3 class="pt-4">Options</h3>
            <div class="py-2">
              <div class="option" v-for="(option, index) in ['a', 'b', 'c', 'd']" :key="index">
                <input type="radio" :id="'option_' + option" name="option" :value="index + 1" v-model="user_option[pointer.index]" @change="click_option(pointer.index, (index + 1).toString())">
                <label :for="'option_' + option">{{ quiz_data.questions[pointer.index]['option_' + option] }}</label>
              </div>
            </div>
            <div class="d-flex justify-content-between pt-4">
              <button class="btn nav_bar text-white" v-on:click="prev">Previous</button>
              <button class="btn nav_bar text-white" v-on:click="next">Save and Next</button>
            </div>
          </div>
        </div>
        <div class="col-12 col-md-4 mx-1 rounded p-4 sidebar" :class="{ 'sidebar-visible': sidebarVisible }">
          <div class="profile_box p-4 rounded">
            <div class="d-flex justify-content-center align-items-center">
              <img class="profile_img" :src="user_data.profile_url" alt="error">
              <h4 class="my-3 mx-4" style="font-weight: bold;">{{ user_data.name }}</h4>
            </div>
            <div class="mt-4 mb-3">
              <p><strong>No of Questions Left:</strong> <span class="box white text-right">{{ questionsLeft }}</span></p>
              <p><strong>No of Questions Attempted:</strong> <span class="box green text-right">{{ questionsAttempted }}</span></p>
              <p><strong>No of Questions Unattempted:</strong> <span class="box red text-right">{{ questionsUnattempted }}</span></p>
            </div>
          </div>
          <div class="index_box p-2 rounded my-4">
            <h3 class="py-4">Questions</h3>
            <div class="row justify-content-center">
              <button v-on:click="go_to_this_question(i - 1)" class="btn col-3 py-3 m-2 border" :class="{'nav_bar': pointer.index == i - 1}" v-for="i in quiz_data.questions.length" :key="i">{{ i }}</button>
            </div>
          </div>
        </div>
      </div>
  </div>
</template>
<style>
@import "../../assets/CSS/nav.css";

.nav_bar {
  background-color: #4723D9 !important;
  color: aliceblue !important;
  border: 2px solid #fff !important;
}

.loader-container {
  align-items: center;
  justify-content: center;
  display: flex;
  height: 100vh;
}

.no-questions {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 80vh;
}

.question-container {
  background-color: #f8f9fa;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.question-text {
  font-size: larger;
  padding: 10px;
  background-color: #fff;
  border-radius: 4px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.option {
  display: flex;
  align-items: center;
  margin-bottom: 10px;
}

.option input[type="radio"] {
  margin-right: 10px;
}

.submit_option {
  background-color: black;
  color: aliceblue;
}

.submit_option:hover {
  background-color: aliceblue;
  color: black;
}

.option label {
  font-size: larger;
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  cursor: pointer;
}

.option input[type="radio"]:checked + label {
  background-color: #4723D9;
  color: aliceblue;
  border-color: #4723D9;
}

@media screen and (max-width: 730px) {
  .is_visible {
    display: none;
  }
  .make_center {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100%;
  }
  .toggle-sidebar {
    display: block;
  }
  .sidebar {
    position: fixed;
    top: 0;
    left: -250px;
    width: 250px;
    height: 100%;
    background-color: #000;
    color: #fff;
    z-index: 1000;
    overflow-y: auto;
    padding: 20px;
    transition: left 0.3s ease;
  }
  .sidebar-visible {
    left: 0;
  }
  .sidebar .profile_box, .sidebar .index_box {
    background-color: #000;
  }
  .sidebar .profile_img {
    width: 50px;
    height: 50px;
  }
}

@media screen and (min-width: 731px) {
  .toggle-sidebar {
    display: none;
  }
}

.profile_img {
  width: 70px;
  height: 70px;
  border-radius: 50%;
  background-color: #fff;
}

.profile_box {
  background-color: #000000;
  color: aliceblue;
}

.index_box {
  background-color: #F8F9FA;
}

.box {
  display: inline-block;
  padding: 5px 10px;
  border-radius: 4px;
  color: #fff;
  font-weight: bold;
  text-align: right;
}

.box.white {
  background-color: #ffffff;
  color: #000;
  border: 1px solid #ccc;
}

.box.green {
  background-color: #28a745;
}

.box.red {
  background-color: #dc3545;
}

.text-right {
  float: right;
}
</style>
