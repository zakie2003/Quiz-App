<script setup>
import { onMounted } from 'vue';

const props = defineProps({
    pie_data: Object
});

onMounted(() => {
    if (props.pie_data) {
        var xValues = ["Laptop", "Phone", "Others"];
        var yValues = [props.pie_data[0].count, props.pie_data[1].count, props.pie_data[2].count];
        var barColors = [
            "#6C63FF",
            "#e8c3b9",
            "#29292C"
        ];
        new Chart(document.getElementById("pieChart"), {
            type: "doughnut",
            data: {
                labels: xValues,
                datasets: [{
                    backgroundColor: barColors,
                    data: yValues
                }]
            },
            options: {
                title: {
                    display: true,
                    text: "Users Devices"
                }
            }
        });
    } else {
        console.error("pie_data is not defined");
    }
    console.log(props.pie_data[0].count);
});
</script>
<template>
    <h1 class="m-4">Session Devices</h1>
    <canvas id="pieChart" style="width:100%;max-width:600px"></canvas>
</template>