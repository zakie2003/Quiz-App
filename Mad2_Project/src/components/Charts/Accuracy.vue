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
    type: "doughnut",
    data: {
      labels: labels,
      datasets: [{
        backgroundColor: barColors,
        data: data
      }]
    },
    options: {
      options: {
            rotation: 1 * Math.PI,/** This is where you need to work out where 89% is */
            circumference: 1 * Math.PI,/** put in a much smaller amount  so it does not take up an entire semi circle */
            legend: {
                display: false
            },
            tooltip: {
                enabled: false
            },
            cutoutPercentage: 95
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