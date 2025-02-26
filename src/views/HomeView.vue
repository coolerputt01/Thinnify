<template>
  <NavBar />
  <section class="home-view">
    <div class="home-view-text">
      <h2 class="home-view-text-head">Welcome Joy!</h2>
    </div>
    <div class="home-view-categorized-card-container">
      <h2 class="category-header">CATEGORIES</h2>
      <div class="home-view-categorized-card-container-item">
        <div class="category-card-carousel">
          <CategorizedCard task-category="Personal" task-no="12" />
          <CategorizedCard task-category="Productivity" task-no="15" />
          <CategorizedCard task-category="Goals" task-no="31" />
          <CategorizedCard task-category="Home" task-no="20" />
          <CategorizedCard task-category="Others" task-no="122" />
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import NavBar from "../components/NavBar.vue";
import CategorizedCard from "../components/CategorizedCard.vue";

export default {
  name: "HomeView",
  components: {
    NavBar,
    CategorizedCard, // Added missing component reference
  },
};
</script>

<style scoped>
* {
  font-family: "Urbanist", sans-serif !important;
  box-sizing: border-box;
  padding: 0; /* Changed 'none' to '0' */
  margin: 0; /* Changed 'none' to '0' */
}
.home-view-categorized-card-container-item{
  display: flex;
  justify-content: flex-start;
  align-items: center;
  padding: 1.1em;
  overflow: auto;
  width:100%;
  white-space: nowrap;
}
.category-card-carousel {
  display: flex;
  justify-content: flex;
  align-items: center;
  width: max-content;
  overflow-x: auto;
  scroll-snap-type: x mandatory;
  padding: 1em 0;
}
.category-card-carousel::-webkit-scrollbar {
  height: 8px;
}

.category-card-carousel::-webkit-scrollbar-thumb {
  background: #888;
  border-radius: 40px;
}

.category-card-carousel::-webkit-scrollbar-track {
  background: #f1f1f1;
}
.category-header {
  font-size: 0.8em;
  font-weight: bolder;
  color: grey;
  padding: 1.1em;
}
.home-view {
  margin-top: 2.3em;
}

.home-view-text {
  padding: 1.1em;
}

.home-view-text-head {
  font-size: 2.1em;
}
</style>
