<template>
  <div class="create-todo-container">
    <div class="cancel-todo-create" @click="this.$router.push({ name: 'todo-transition', params: { page: '/' } });">
      <i class="fa-solid fa-x"></i>
    </div>
    <div class="form-container">
      <form class="form" action="">
        <input type="text" placeholder="Enter new task" v-model="task" class="task-input">
        <div class="selection-div">
        <button class="enter-edate" @click.prevent="">
          <i class="fa-solid fa-calendar-week"></i>
          <p>Today</p>
        </button>
        <div class="dropdown">
          <button class="dropdown-button" @click.prevent="">
            category
          </button>
          <div class="dropdown-content">
            <div class="category">Personal</div>
            <div class="category">Productivity</div>
            <div class="category">Goals</div>
            <div class="category">Others</div>
          </div>
        </div>
        </div>
        <div class="submit-button">New Task</div>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: "CreateView",
}
</script>

<style scoped>
* {
  font-family: "Urbanist", sans-serif !important;
  box-sizing: border-box;
  padding: 0;
  margin: 0;
}
.task-input {
  width:70vw;
  height: 5vh;
  border-radius: 50px;
  padding: 1.5em;
  box-shadow:5px 5px 15px -3px rgba(0,0,0,0.15);
  border:none;
  outline:none;
}
.task-input::placeholder {
  font-size:1.2em;
}
.task-input:focus {
  outline:none;
}
.cancel-todo-create {
  font-family: "Font Awesome 5 Free" !important;
  width: 24px;
  height: 24px;
  position: absolute;
  top:5%;
  right:9%;
}
.cancel-todo-create > i {
  border: 2px solid grey;
  border-radius: 56px;
  padding:0.5em;
  font-size: 1.1em;
}
.form-container{
  display: flex;
  justify-content: center;
  align-items: center;
  padding:2.5em;
  flex-direction:column;
}
.submit-button{
  background-color: #3498db;
  color: white;
  padding: 10px 15px;
  border: none;
  width:40vw;
  position:fixed;
  bottom:15%;
  right:15%;
  text-align:center;
  cursor: pointer;
  font-size: 16px;
  border-radius: 56px;
  transition:all 0.3s;
  -webkit-box-shadow: 5px 5px 15px 2px rgba(41,13,255,0.31); 
  box-shadow: 5px 5px 15px 2px rgba(41,13,255,0.31);
}
.enter-edate {
  padding:1em;
  display: flex;
  justify-content: center;
  align-items: center;
  gap:1em;
  background-color:#fff;
  box-shadow:5px 5px 15px -3px rgba(0,0,0,0.15);
  border-radius:50px;
  border:none;
  outline:none;
}
.enter-edate:focus {
  border:none;
  outline:none;
}
.enter-edate > i {
  font-family: "Font Awesome 5 Free" !important;
  -webkit-text-stroke:2px grey;
  color:transparent;
}
.enter-edate > p{
  color:grey;
}
.form{
  padding:1.1em;
}
.create-todo-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 97vh;
  position: relative;
  overflow-x: hidden;
  background-color: #f9f9f9;
}

.selection-div{
  display: flex;
  justify-content: space-between;
  align-ditems: center;
  width:100%;
  margin:4em 0em 4em 0em;
}
.dropdown {
      position: relative;
      display: inline-block;
    }

    .dropdown-button {
      background-color: #3498db;
      color: white;
      padding: 10px 15px;
      border: none;
      cursor: pointer;
      font-size: 16px;
      border-radius: 56px;
      transition:all 0.3s;
      -webkit-box-shadow: 5px 5px 15px 2px rgba(41,13,255,0.31); 
      box-shadow: 5px 5px 15px 2px rgba(41,13,255,0.31);
    }

    .dropdown-button:hover {
      background-color: #fff;
      color:#2980b9 !important
    }

    .dropdown-content {
      position: absolute;
      top: 100%;
      left: 0;
      background-color: white;
      min-width: 150px;
      border-radius: 5px;
      box-shadow: 0px 5px 10px rgba(0, 0, 0, 0.2);
      overflow: hidden;
      opacity: 0;
      visibility: hidden;
      transform: translateY(-10px);
      transition: opacity 0.3s ease, transform 0.3s ease, visibility 0.3s;
    }

.dropdown-content div {
      display: block;
      padding: 10px;
      color: black;
      text-decoration: none;
      transition: background 0.3s;
}

.dropdown-content div:hover {
      background-color: #f1f1f1;
}
.dropdown:hover .dropdown-content {
      opacity: 1;
      visibility: visible;
      transform: translateY(0);
}
</style>