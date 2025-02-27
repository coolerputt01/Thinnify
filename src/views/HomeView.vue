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
    <div class="todo-app-card">
      <div class="todo-app-header">TASKS</div>
      <div class="todo-app-container">
        <TodoCard category="productivity" todo-text="Wash the dishes." />
        <TodoCard category="personal" todo-text="Wash the dishes." />
        <TodoCard category="others" todo-text="Wash the dishes." />
        <TodoCard category="home" todo-text="Wash the dishes." />
        <TodoCard category="goals" todo-text="Wash the dishes." />
      </div>
    </div>
    <div class="add-todo-btn" @click="addTodo">
      <i class="fa fa-plus"></i>
    </div>
  </section>
</template>

<script>
import NavBar from "../components/NavBar.vue";
import CategorizedCard from "../components/CategorizedCard.vue";
import TodoCard from "../components/TodoCard.vue";

export default {
  name: "HomeView",
  components: {
    NavBar,
    CategorizedCard, // Added missing component reference
    TodoCard,
  },
  methods:{
    addTodo(){
      this.$router.push('/create-todo');
    }
  }
};
</script>

<style scoped>
* {
  font-family: "Urbanist", sans-serif !important;
  box-sizing: border-box;
  padding: 0; /* Changed 'none' to '0' */
  margin: 0; /* Changed 'none' to '0' */
}
.todo-app-container{
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 1.1em;
  overflow-x: hidden;
  flex-direction: column;
  width:100%;
  border-radius: 50px;
  white-space: nowrap;
  background-color: #f9f9f9;
}
.add-todo-btn {
  position: fixed;
  bottom: 2em;
  right: 2em;
  padding: 2em !important;
  background-color: blue;
  border-radius: 50%;
  width: 3em;
  height: 3em;
  display: flex;
  justify-content: center;
  align-items: center;
  color: #fff;
  -webkit-box-shadow: 5px 5px 15px -3px rgba(0,0,0,0.67);
  box-shadow: 5px 5px 15px -3px rgba(0,0,0,0.67);
}
.add-todo-btn:hover {
  background-color: #000;
  cursor: pointer;
}
.add-todo-btn > i {
  font-size: 2em !important;
  font-weight: normal;
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
.category-header{
  font-size: 0.8em !important;
  font-weight: bolder !important;
  color: grey !important;
  padding: 1.1em !important;
}
.todo-app-header {
  font-size: 0.8em !important;
  font-weight: bolder !important;
  color: grey !important;
  padding: 1.1em !important;
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
