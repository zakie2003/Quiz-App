<script setup>
const props = defineProps({
  item: Object
});
</script>
<template>
    <div class="ag-courses_item">
      <div class="ag-courses-item_link">
        <div class="ag-courses-item_bg"></div>
        <div class="ag-courses-item_title">
            <div class="profile-container">
                <img class="profile-image" src="https://upload.wikimedia.org/wikipedia/commons/9/99/Sample_User_Icon.png" alt="">
                <div class="profile-info">
                    <h3>{{ item.name }}</h3>
                    <p>{{ item.email }}</p>
                </div>
                <button style="height: 50px;width: 50px;" class="btn delete-button"><i class='bx bxs-trash'></i></button>
            </div>
        </div>
        <div class="profile-details">
          <table class="details-table">
            <tbody>
            </tbody>
          </table>
        </div>
      </div>
    </div>
</template>
<style>
@import "../../assets/CSS/card.css";

.profile-container {
    display: flex;
    align-items: center;
}

.profile-image {
    width: 100px;
    background-color: aliceblue;
    border-radius: 50%;
}

.profile-info {
    margin-left: 40px;
    margin-top: 5px;
}

.delete-button {
    background-color: aliceblue;
    color: black;
    margin-left: auto;
}

.profile-details {
    z-index: 2;
    position: relative;
    color: white;
}

.details-table {
    background: none;
    width: 100%;
}
</style>