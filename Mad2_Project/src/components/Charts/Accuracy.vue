<script setup>
import { onMounted, watch } from 'vue';
import { defineProps } from 'vue';

const props = defineProps({
    right: Number,
    wrong: Number
});

const renderChart = () => {
  const ctx = document.getElementById("accuracy").getContext("2d");
  const labels = ["Correct", "Incorrect"];
  const data = [props.right, props.wrong];
  const barColors = ["green", "red"];

  new Chart(ctx, {
    type: "bar",
    data: {
      labels: labels,
      datasets: [{
        backgroundColor: barColors,
        data: data
      }]
    },
    options: {
      scales: {
        yAxes: [{
          ticks: {
                beginAtZero:true
            }
        }]
      },
      legend: {
        display: false
      }
    }
  });
};

onMounted(() => {
  renderChart();
});

watch(() => props.right + props.wrong, () => {
  renderChart();
});
</script>

<template>
  <canvas id="accuracy" style="width:100%;max-width:600px"></canvas>
</template>