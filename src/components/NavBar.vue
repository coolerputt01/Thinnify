<template>
  <nav class="nav-bar">
    <div class="bread-crumb">
      <i class="fa-solid fa-bars-staggered"></i>
    </div>
    <div class="user-interactions">
      <i class="fa-solid fa-search"></i>
      <i class="fa-solid fa-bell"></i>
    </div>
  </nav>
</template>

<script>
export default {
  name: "NavBar",
};
</script>

<style scoped>
* {
  font-family: "Urbanist", sans-serif;
  box-sizing: border-box;
  padding: none;
  margin: none;
}

i {
  font-family: "Font Awesome 5 Free" !important;
  font-weight: 900; /* Needed for solid icons */
}

.nav-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1em;
  background-color: #f9f9f9;
  border-radius: 50px;
  border-bottom: 1px solid #e9ecef;
  height: 7vh;
  -webkit-box-shadow: 5px 5px 31px 8px rgba(0, 0, 0, 0.07);
  box-shadow: 5px 5px 31px 8px rgba(0, 0, 0, 0.07);
  margin-top: 3em;
}
.user-interactions > i {
  color: transparent !important;
  -webkit-text-stroke: 1px #000 !important;
  transition: 0.3s;
}
.user-interactions {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 3em;
}
.user-interactions > i:hover {
  color: #000 !important;
  cursor: pointer;
}
</style>
