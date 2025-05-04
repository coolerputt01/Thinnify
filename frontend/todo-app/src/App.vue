<template>
    <router-view />
</template>
<script>
  export default {
    name: "App",
  };
</script>
<style>
* {
  font-family: "Urbanist",sans-serif;
}
/* 🔹 Fix the Toast font issue */
.p-toast {
    font-family: "Urbanist", sans-serif !important;
}
.p-select-dropdown-icon {
    background-image: url("../src/assets/dropdown.svg") !important;
    background-repeat: no-repeat !important;
    background-size: cover !important;
    background-position: center !important;
    width: 1.5em !important;
    height: 1.5em !important;
    color: transparent !important;
}
.p-progressbar {
  width: 90% !important;
  height: 0.7em !important;
  border-radius: 10px !important;
  background-color: #c7c7c7af !important;
}
.p-select {
  border-radius: 50px !important;
  padding: 12px !important;
}

.p-select-label {
  font-weight: 600 !important;
  color: #000 !important;
}
.p-progressbar-value {
  background-color: #ff5d2bbb !important;
  border-radius: 10px !important;
}

.vue3-circular-progressbar {
  display: flex !important;
  justify-content: center !important;
  align-items: center !important;
}
</style>
