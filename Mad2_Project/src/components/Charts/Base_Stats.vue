<script setup>
import axios from 'axios';
import { onMounted,ref } from 'vue';


const user_stats=ref({
    "email":sessionStorage.getItem("email"),
    "visits":0,
    "accuracy":0,
    "quiz_attempted":0
})

const get_stats=async()=>{
    await axios.post("http://localhost:5000/user/get_stats",{"email":user_stats.value.email}).then((res)=>{
        console.log(res.data);
        user_stats.value.accuracy=res.data.stats.accuracy;
        user_stats.value.quiz_attempted=res.data.stats.quiz_attempted;
    }).catch((err)=>{
        console.log(err);
    })
}

onMounted(()=>{
    get_stats();
})

</script>

<template>
        <div class="row mx-4 my-6">
            <div class="col-md-4">
                <div class="card shadow-sm">
                    <div class="card-body">
                        <div class="d-flex align-items-center">
                            <i style="color: blue;" class="bx bx-line-chart display-1"></i>
                            <div class="ms-3">
                                <p class="h1 mb-0">3</p>
                                <p class="h4 text-muted mb-0">Total Visits</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="col-md-4">
                <div class="card shadow-sm">
                    <div class="card-body">
                        <div class="d-flex align-items-center">
                            <i style="color: red;" class='bx bx-target-lock display-1'></i>
                            <div class="ms-3">
                                <p class="h1 mb-0">{{ user_stats.accuracy }} %</p>
                                <p class="h4 text-muted mb-0">Accuracy</p>
                            </div>
                        </div>
                        <!-- <div class="progress mt-3" style="height: 5px;">
                            <div class="progress-bar bg-pink" role="progressbar" style="width: 50%;" aria-valuenow="50" aria-valuemin="0" aria-valuemax="100"></div>
                        </div> -->
                    </div>
                </div>
            </div>


            <div class="col-md-4">
                <div class="card shadow-sm">
                    <div class="card-body">
                        <div class="d-flex align-items-center">
                          <i style="color: green;" class='bx bxs-edit-alt display-1'></i>
                            <div class="ms-3">
                                <p class="h1 mb-0">{{ user_stats.quiz_attempted }}</p>
                                <p class="h4 text-muted mb-0">Assignment Completed</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

        </div>

</template>