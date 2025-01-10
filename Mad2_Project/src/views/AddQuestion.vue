<script setup>
import axios from "axios";
import NavAdmin from "@/components/NavBar/NavAdmin.vue";

const data={
  name:"",
  description:"",
}


</script>
<template>
  <nav class="navbar navbar-expand-lg pb-0 bg-body-tertiary">
    <NavAdmin /> 
    <div style="height: 100vh;" class="bg-light w-100">
      <h1 class="m-4">Add Question</h1>
      <div class="container">
        <form class="d-flex flex-column w-90"  action="">
          <div class="mb-3">
            <label style="font-size: 30px;" class="form-label my-2" for="chapter">Question Description</label>
            <input style="font-size: 20px;" type="text" name="chapter" class="form-control"  placeholder="Enter Question Description">
          </div>
          <div class="mb-3">
            <label style="font-size: 30px;" class="form-label my-2" for="description">Option 1</label>
            <input style="font-size: 20px;" type="text" name="description" class="form-control"  placeholder="Enter Description">
          </div>
          <div class="mb-3">
            <label style="font-size: 30px;" class="form-label my-2" for="description">Option 2</label>
            <input style="font-size: 20px;" type="text" name="description" class="form-control"  placeholder="Enter Description">
          </div>
          <div class="mb-3">
            <label style="font-size: 30px;" class="form-label my-2" for="description">Option 3</label>
            <input style="font-size: 20px;" type="text" name="description" class="form-control"  placeholder="Enter Description">
          </div>
          <div class="mb-3">
            <label style="font-size: 30px;" class="form-label my-2" for="description">Option 4</label>
            <input style="font-size: 20px;" type="text" name="description" class="form-control"  placeholder="Enter Description">
          </div>
          <div class="mb-3">
            <label style="font-size: 30px;" class="form-label my-2" for="description">Correct Option</label>
            <select style="font-size: 20px;" class="form-select" aria-label="Default select example">
              <option selected>Open this select menu</option>
              <option value="1">One</option>
              <option value="2">Two</option>
              <option value="3">Three</option>
              <option value="4">Four</option>
            </select>
          </div>
          <button style="font-size: 20px;background-color: #4723d9;color: aliceblue;" type="submit" class="m-3 btn  ">Submit</button>
        </form>
      </div>
    </div>
  </nav>
</template>
<style>
@import "../assets/CSS/nav.css";

/* Add custom styles for better form spacing */
form {
  max-width: 600px;
  margin: auto;
}

form .form-label {
  font-weight: bold;
}

form .form-control {
  padding: 10px;
  font-size: 18px;
}

form .btn {
  padding: 10px 20px;
  font-size: 18px;
}
</style>
