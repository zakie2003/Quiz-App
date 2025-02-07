<script setup>
import { onMounted, watch } from 'vue';
import { defineProps } from 'vue';

const props = defineProps({
  radar_data: Array
});

// Store the chart instance for cleanup on re-render
let radarChartInstance = null;

const renderChart = () => {
  if (!props.radar_data || props.radar_data.length === 0) {
    return;
  }

  // If a chart instance already exists, destroy it before re-rendering
  if (radarChartInstance) {
    radarChartInstance.destroy();
  }

  const labels = props.radar_data.map(item => item.quiz_name);
  const data = props.radar_data.map(item => item.average_score);

  radarChartInstance = new Chart("radarChart", {
    type: "radar",
    data: {
      labels: labels,
      datasets: [{
        label: "Average Score",
        data: data,
        backgroundColor: "rgba(71, 35, 217, 0.2)",
        borderColor: "rgba(71, 35, 217, 1)",
        borderWidth: 1
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      scale: {
        ticks: {
          beginAtZero: true,
          max: 100
        }
      }
    }
  });
};

onMounted(() => {
  renderChart();
});

watch(() => props.radar_data, () => {
  renderChart();
});
</script>

<template>
  <!-- Wrap your canvas in a container with a defined height -->
  <div style="width:100%;max-width:600px;height:400px;">
    <canvas id="radarChart"></canvas>
  </div>
</template>
