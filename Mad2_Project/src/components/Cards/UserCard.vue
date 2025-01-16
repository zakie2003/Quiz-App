<script setup>
import axios from 'axios';
import { onMounted, ref } from 'vue';

const props=defineProps(
  {
    item:Object,
    color:String
  }
)

const data=ref({});

console.log(props)
</script>
<template>
  <div class="ag-courses_item">
    <div class="ag-courses-item_link">
      <div :style="props.color != 'yellow' ? 'background: rgb(116,63,213);background: radial-gradient(circle, rgba(116,63,213,1) 0%, rgba(0,248,251,1) 90%);':'' " class="ag-courses-item_bg"></div>
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
             <th>No of Questions: <span>{{ props.item?.no_of_questions }}</span></th>
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
          <button style="background-color: aliceblue;color: black;width: 100%;" class="btn m-2">Add to Library</button>
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
</style>