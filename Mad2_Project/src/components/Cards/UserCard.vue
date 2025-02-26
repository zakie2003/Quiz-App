<script setup>
import axios from 'axios';
import { onMounted, ref } from 'vue';

const props = defineProps({
  item: Object,
  color: String,
});

const data = ref({});
const isInLibrary = ref(false);
const isLoading = ref(true);

const add_to_library = async () => {
  await axios.post("http://localhost:5000/user/add_to_library", {
    "quiz_id": props.item.id,
    "user_id": sessionStorage.getItem("id")
  }).then((res) => {
    console.log(res);
    checkLibrary();
  }).catch((err) => {
    console.log(err);
  });
};

const checkLibrary = async () => {
  try {
    await axios.post("http://localhost:5000/user/check_quiz_in_library", {
      "user_id": sessionStorage.getItem("id"),
      "quiz_id": props.item.id
    }).then((res) => {
      console.log("Data:", res);
      isInLibrary.value = res.data.is_in_library;
      isLoading.value = false;
    });
  } catch (err) {
    console.log('Error:', err);
    isLoading.value = false;
  }
};

onMounted(() => {
  console.log(props);
  checkLibrary();
});
</script>
<template>
  <div class="ag-courses_item">
    <div class="ag-courses-item_link">
      <div :style="props.color != 'yellow' ? 'background: rgb(116,63,213);background: radial-gradient(circle, rgba(116,63,213,1) 0%, rgba(0,248,251,1) 90%);' : ''" class="ag-courses-item_bg"></div>
      <div v-if="isLoading" class="loader">Loading...</div>
      <div v-else>
        <div class="ag-courses-item_title">
          {{ props.item?.quiz_name }}
        </div>
        <div style="z-index: 2;position: relative;" class="text-white">
          <table style="background: none; width: 100%;">
            <thead>
              <tr>
                <th>Chapter: <span>{{ props.item?.chapter_name }}</span></th>
              </tr>
              <tr>
               <th>Date of Creation: <span>{{ props.item?.date_of_quiz }}</span></th>
              </tr>
              <tr>
                  <th>
                      Duration: <span>{{ props.item?.time_duration }}</span>
                  </th>
              </tr>
            </thead>
            <tbody>
            </tbody>
          </table>
          <div class="button-container">
            <button v-if="!isInLibrary" v-on:click="add_to_library" style="background-color: aliceblue;color: black;width: 100%;" class="btn m-2">Add to Library</button>
            <button v-else style="background-color: grey;color: aliceblue;width: 100%;" class="btn m-2">In Library</button>
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