<script setup>
import axios from 'axios';
import { onMounted, ref } from 'vue';

const props = defineProps({
  item: Object,
  color: String
});

const quiz_data = ref({});
const isInLibrary = ref(false);
const isLoading = ref(true);

const checkLibrary = async () => {
  try {
    await axios.post("http://localhost:5000/user/check_quiz_in_library", {
      "user_id": sessionStorage.getItem("id"),
      "quiz_id": props.item.quiz_id
    }).then((res) => {
        console.log(res.data.quiz_data)
        quiz_data.value = res.data.quiz_data;
        isInLibrary.value = res.data.is_in_library;
        isLoading.value = false;
    })
  } catch (err) {
    console.log('Error:', err);
    isLoading.value = false;
  }
};

const attempt_quiz=(quiz_data)=>{
  window.location.href="/user/quiz/"+quiz_data.chapter_name+"/"+quiz_data.id;
}

onMounted(() => {
  checkLibrary();
});
</script>
<template>
  <div class="ag-courses_item">
    <div class="ag-courses-item_link">
      <div :style="props.color !== 'yellow' ? 'background: rgb(116,63,213);background: radial-gradient(circle, rgba(116,63,213,1) 0%, rgba(0,248,251,1) 90%);' : ''" class="ag-courses-item_bg"></div>
      <div v-if="isLoading" class="loader">Loading...</div>
      <div v-else>
        <div class="ag-courses-item_title">
          {{ quiz_data?.quiz_name }}
        </div>
        <div style="z-index: 2;position: relative;" class="text-white">
          <table style="background: none; width: 100%;">
            <thead>
              <tr>
                <th>Chapter: <span>{{ quiz_data?.chapter_name }}</span></th>
              </tr>
              <tr>
               <th>Date of Creation: <span>{{ quiz_data?.date_of_quiz }}</span></th>
              </tr>
              <tr>
                  <th>
                      Duration: <span>{{ quiz_data?.time_duration }}</span>
                  </th>
              </tr>
            </thead>
            <tbody>
            </tbody>
          </table>
          <div class="button-container">
            <button v-on:click="attempt_quiz(quiz_data)"v-if="isInLibrary" style="background-color: aliceblue;color: black;width: 100%;" class="btn m-2">Attempt Quiz</button>
            <button v-else style="background-color: aliceblue;color: black;width: 100%;" class="btn m-2">Add to Library</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<style>
@import "../../assets/CSS/card.css";
.ag-courses_item {
    flex: 1 1 300px;
    margin: 10px;
    min-width: 300px; /* Set the minimum width for the card */
}

.button-container {
    display: flex;
    justify-content: center;
    align-items: center;
}

.loader {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100px;
    color: white;
}
</style>