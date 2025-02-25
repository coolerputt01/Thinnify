<template>
  <NavBar />
  <section class="home-view">
    <div class="home-view-text">
      <h2 class="home-view-text-head">Welcome Joy!</h2>
    </div>
  </section>
</template>

<script>
import NavBar from "../components/NavBar.vue";
export default {
  name: "HomeView",
  components: {
    NavBar,
  },
};
</script>

<style scoped>
* {
  font-family: "Urbanist", sans-serif !important;
  box-sizing: border-box;
  padding: none;
  margin: none;
}
.home-view {
  margin-top: 3em;
}
.home-view-text {
  padding: 1.1em;
}
.home-view-text-head {
  font-size: 1.5em;
}
</style>
