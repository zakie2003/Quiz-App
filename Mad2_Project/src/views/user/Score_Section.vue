<script setup>
import axios from 'axios';
import NavUser from '@/components/NavBar/NavUser.vue';
import Loader from '@/components/Loader/Loader.vue';
import Footer from '@/components/Footer/Footer.vue';
import { onMounted, ref, computed, watch } from 'vue';

const data = ref({
    isLoading: false,
    scores: [],
    user_id: sessionStorage.getItem("id"),
});

const currentPage = ref(1);
const itemsPerPage = ref(5);
const paginatedScores = ref({});
let index = ref(1);

const get_reports = async () => {
    data.value.isLoading = true;
    try {
        const res = await axios.post("https://quiz-app-chz3.onrender.com/user/get_score", { "user_id": data.value.user_id });
//        console.log(res.data);
        paginatedScores.value = res.data.Score_list;
        console.log(res.data.Score_list);
        totalPages.value.total= Object.keys(paginatedScores.value).length;
    } catch (err) {
        console.error(err);
        data.value.scores = [];
    } finally {
        data.value.isLoading = false;
    }
};


const updatePaginatedScores = () => {
    const start = (currentPage.value - 1) * itemsPerPage.value;
    paginatedScores.value = data.value.scores.slice(start, start + itemsPerPage.value);
};

watch([data, currentPage, itemsPerPage], updatePaginatedScores, { immediate: true });

const totalPages = ref({});


const changePage = (direction) => {
  console.log("Index",index.value);
    if (direction === "next" ) {
      index.value= index.value+1;
    } else if (direction === "prev") {
      index.value= index.value-1;
    }
};

const go_to_preview = (chapter_name, quiz_id, date_of_quiz, time) => {
    window.location.href = `/user/quiz_preview/${chapter_name}/${quiz_id}?date=${date_of_quiz}&time=${time}`;
};

onMounted(() => {
    get_reports();
});
</script>

<template>
    <nav class="navbar navbar-expand-lg pb-0 bg-body-tertiary">
        <NavUser />
        <div style="min-height: 100vh;" class="bg-light w-100">
            <div v-if="data.isLoading" class="loader-container">
                <Loader />
            </div>
            <div v-else>
                <h3 class="p-4">Score Dashboard</h3>
                <table class="table container rounded">
                    <thead>
                        <tr>
                            <th class="row_table" scope="col">Chapter</th>
                            <th class="row_table" scope="col">Date</th>
                            <th class="row_table" scope="col">Score</th>
                            <th class="row_table" scope="col">Download</th>
                            <th class="row_table" scope="col">Action</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="(item) in paginatedScores[index]" :key="index">
                            <td scope="row">{{ item.chapter_name }}</td>
                            <td scope="row">{{ item.date }}</td>
                            <td style="font-weight: bold;" scope="row">{{ Math.round(item.score) }}/100</td>
                            <td>
                                <a :href="'https://quiz-app-chz3.onrender.com/celery/get_csv_data?user_id='+ data.user_id +'&quiz_id=' + item.id+'&time='+item.time+'&date='+item.date">Download Transcript</a>
                            </td>
                            <td scope="row"><button v-on:click="go_to_preview(item.chapter_name, item.id, item.date, item.time)" class="btn btn_score">OverView</button></td>
                        </tr>
                    </tbody>
                </table>

                <!-- Pagination Controls -->
                <div class="pagination-container">
                    <button class="btn btn_score" :disabled="index === 1" v-on:click="changePage('prev')">Previous</button>
                    <span>Page {{ index }} of {{ totalPages.total }}</span>
                    <button class="btn btn_score" :disabled="index === totalPages.total" v-on:click="changePage('next')">Next</button>
                </div>
            </div>
        </div>
    </nav>
    <Footer />
</template>

<style>
@import "../../assets/CSS/nav.css";

.row_table {
    color: aliceblue !important;
    background-color: #4723d9 !important;
}

.loader-container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
}

.pagination-container {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 10px;
    padding: 20px;
}

.btn_score{
    background-color: #4723d9 !important;
    color: aliceblue !important;
}
</style>
