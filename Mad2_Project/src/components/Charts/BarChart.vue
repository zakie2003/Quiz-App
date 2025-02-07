<script setup>
import { onMounted, watch } from 'vue';
import { defineProps } from 'vue';

const props = defineProps({
  bar_data: Object
});

const renderChart = () => {
  if (!props.bar_data) {
    return;
  }

  const labels = Object.keys(props.bar_data);
  const data = Object.values(props.bar_data);
  const barColors = ["#F77F00", "#6C63FF", "#4E89FF", "#FFD166", "#29292C"];

  new Chart("barChart", {
    type: "bar",
    data: {
      labels: labels,
      datasets: [{
        backgroundColor: barColors,
        data: data
      }]
    },
    options: {
      legend: {
        display: false
      },
      scales: {
        yAxes: [{
          ticks: {
            beginAtZero: true,
            callback: function(value) { if (Number.isInteger(value)) { return value; }
            }
          }
        }]
      }
    }
  });
};

onMounted(() => {
  renderChart();
});

watch(() => props.bar_data, () => {
  renderChart();
});
</script>

<template>
  <canvas id="barChart" style="width:100%;max-width:600px"></canvas>
</template>