<script setup>
import { onMounted,ref } from 'vue';

const props = defineProps({
    message: {
        type: String,
        required: true
    },
    status:{
        type:String,
        required:true
    }
});

let styling=ref("alert alert-danger");
onMounted(()=>{
    if(props.status=="200"){
        styling.value="alert alert-success";
    }
    console.log(props.status);
})
</script>
<template>
    <div :class="styling" role="alert">
        {{ message }}
    </div>
</template>