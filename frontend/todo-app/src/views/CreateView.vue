<template>
    <section>
      <main>
        <nav class="nav-bar">
          <div class="icon">
            <img src="../assets/leftarrow.svg" alt="Back Icon" class="back-icon" />
          </div>
          <h1>Add Project</h1>
        </nav>
  
        <section class="form">
          <Select
            v-model="title"
            :options="categories"
            optionLabel="name"
            placeholder="Select Category"
            fluid=true
          >
            <!-- Selected value display -->
            <template #value="slotProps">
              <div v-if="slotProps.value" class="select-option">
                <img :src="slotProps.value.icon" alt="" class="option-icon" :style="{backgroundColor:slotProps.value.color}"/>
                <span>{{ slotProps.value.name }}</span>
              </div>
              <span v-else class="select-placeholder">Select Category</span>
            </template>
  
            <!-- Dropdown options -->
            <template #option="slotProps">
              <div class="select-option">
                <img :src="slotProps.option.icon" alt="" class="option-icon" :style="{backgroundColor:slotProps.option.color}"/>
                <span>{{ slotProps.option.name }}</span>
              </div>
            </template>
          </Select>
          <div class="input-container">
            <p>Task Name</p>
            <input type="text" class="input-field" />
          </div>
        </section>
      </main>
    </section>
  </template>
  
  <script>
  import { ref } from 'vue'
  import Select from 'primevue/select'
  
  export default {
    name: 'CreateView',
    props: ['user'],
    components: {
      Select
    },
    setup() {
      const title = ref(null)
  
      const categories = [
        { name: 'Personal', icon: require('../assets/personal.svg'), color: 'rgba(140, 201, 255,0.3)' },
        { name: 'Productivity', icon: require('../assets/productivity.svg'), color: 'rgba(248, 143, 255,0.3)' },
        { name: 'Fitness', icon: require('../assets/fitness.svg'), color: 'rgba(156, 255, 143,0.3)' },
        { name: 'Work', icon: require('../assets/work.svg'), color: 'rgba(190, 143, 255,0.3)' },
        { name: 'Default', icon: require('../assets/default.svg'), color: 'rgba(204, 204, 204,0.3)' }
    ]

  
      return {
        title,
        categories
      }
    }
  }
  </script>
  
  <style scoped>
  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: "Urbanist", sans-serif;
  }
  .input-container {
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    box-shadow: -16px 15px 22px 11px rgba(0,0,0,0.05);
    border-radius: 28px !important;
    padding: 12px;
    width: 85vw;
    margin-top: 20px;
    background-color: #fff;
    flex: 0 0 auto;
  }
  .input-container > * {
    margin-left: 8%;
  }
  .input-container > p {
    font-size: 0.9em;
    font-weight: 400 !important;
    color: grey;
    width: 100%;
    text-align: left;
    padding: 12px !important;
  }
  .input-container > input {
    width: 100%;
    height: 3vh;
    padding: 5px;
    border-radius: 5px;
    border: none;
    font-size: 1.4em;
    font-weight: 500;
    outline: none;
    transition: border-color 0.3s ease;
  }
  .nav-bar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    backdrop-filter: blur(5px);
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 12vh;
    padding: 22px;
    z-index: 1000;
  }
  
  .icon {
    display: flex;
    align-items: center;
    justify-content: flex-start;
  }
  
  .icon > * {
    width: 3em;
    height: 3em;
  }
  .nav-bar > h1 {
    font-size: 1.5em;
    font-weight: 600;
    width: 100%;
    text-align: center;
    margin: 0;
  }
  .option-icon {
    padding: 5px !important;
    border-radius: 50% !important;
  }
  
  .form {
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    background-color: #fff;
    max-width: 100vw;
    border-radius: 8px;
    padding: 30px;
    margin-top: 15vh;
  }
  
  .select-option {
    display: flex;
    align-items: center;
    gap: 10px;
  }
  
  .option-icon {
    width: 30px;
    height: 30px;
  }
  
  .select-placeholder {
    color: #aaa;
  }
  </style>
  