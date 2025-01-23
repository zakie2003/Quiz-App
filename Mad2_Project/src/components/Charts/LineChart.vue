<script setup>
import { onMounted, watch } from 'vue';

const props = defineProps({
  line_data: Array
});

const xValues = [];
let yValues = [];

const updateChart = () => {
  if (props.line_data && Array.isArray(props.line_data)) {
    xValues.length = 0;
    yValues.length = 0;
    props.line_data.forEach(item => {
      xValues.push(item.date);
      yValues.push(item.count);
    });
    const ctx = document.getElementById("myChart").getContext("2d");
    const gradient = ctx.createLinearGradient(0, 0, 0, 400);
    gradient.addColorStop(1, "rgba(0,0,0,0)");
    gradient.addColorStop(0, "#4c49ea");
    new Chart(document.getElementById("myChart"), {
      type: "line",
      data: {
        labels: xValues,
        datasets: [{
          backgroundColor: gradient,
          borderColor: "#4c49ea",
          data: yValues
        }]
      },
      options: {
          legend: {
            display: false
          }
      }
    });
  }
};

onMounted(() => {
  if (props.line_data) {
    console.log("Line data on mount:", props.line_data);
    updateChart();
  }
});

watch(() => props.line_data, (newVal) => {
  if (newVal) {
    // console.log("Line data updated:", newVal);
    updateChart();
  }
});
</script>
<template>
  <h1 class="mx-4">User Registration Trend</h1>
  <canvas id="myChart" class="mx-4" style="width:100%;max-width:600px"></canvas>
</template>