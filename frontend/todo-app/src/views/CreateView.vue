<template>
    <section>
      <main>
        <nav class="nav-bar">
          <div class="icon">
            <img src="../assets/leftarrow.svg" alt="Back Icon" class="back-icon" @click="goHome"/>
          </div>
          <h1>Add Task</h1>
        </nav>
        <Toast />
        <section class="form">
          <Select
            v-model="category"
            :options="categories"
            optionLabel="name"
            placeholder="Select Category"
            :fluid="true"
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
            <input type="text" class="input-field" v-model="task"/>
          </div>
          <div class="date">
            <div class="date-input">
                <div class="date-info-text">
                  <p class="date-mini-text">Start Date</p>
                  <p> {{ new Date().toLocaleDateString() }}</p>
                </div>
                <img src="../assets/calender.svg" alt="slotProps.option.label" class="option-icon" />
            </div>
            <div class="date-input" @click="visible = true" label="Show">
                <div class="date-info-text">
                  <p class="date-mini-text">End Date</p>
                  <p> {{ date ? date.toLocaleDateString() : 'Select a date' }}</p>
                </div>
                <img src="../assets/calender.svg" alt="slotProps.option.label" class="option-icon" />
            </div>
            <Dialog v-model:visible="visible" modal header="Choose a Date" :style="{ width: '25rem' }">
              <VDatePicker v-model="date" />
            </Dialog>
          </div>
          <div class="button-container">
            <button class="submit-button" @click="postTask()"><p v-if="!isLoading">Add Task</p> <ProgressSpinner v-else style="width: 32px; height: 32px" strokeWidth="8" fill="transparent" strokeColor="#fff"
              animationDuration=".5s" aria-label="Custom ProgressSpinner" /></button>
          </div>
        </section>
      </main>
    </section>
  </template>
  
  <script>
  import { ref , getCurrentInstance } from 'vue';
  import Select from 'primevue/select';
  import Dialog from 'primevue/dialog';
  import Toast from 'primevue/toast';
  import ProgressSpinner from 'primevue/progressspinner';
  import { useToast } from 'primevue/usetoast';
  import { useRouter } from 'vue-router';
  
  export default {
    name: 'CreateView',
    props: ['user'],
    components: {
      Select,
      Dialog,
      ProgressSpinner,
      Toast,
    },
    setup() {
      //State to check if loading state has ended or started.
      const visible = ref(false);
      const category = ref('');
      const date = ref(null);
      const task = ref('');
      //same here
      const isLoading = ref(false);
      const username = ref(localStorage.getItem('username'));
      const router = useRouter();
      const toast = useToast();
      const { proxy } = getCurrentInstance();

      const postTask = async () => {
          try {
              isLoading.value = true;
              if(task.value < 3) {
                toast.add({severity: "error",
                    summary: "Invalid Details",
                    detail: "Enter a valid task_name",
                    life: 3000});
              } else {
                  await proxy.$api.post('/todo',{
                    title: task.value,
                    category: category.value.name,
                    endate: date.value,
                },{
                    headers: {
                        Authorization: `Bearer ${localStorage.getItem('access_token')}`
                    }
                });
                toast.add({
                      severity: "success",
                      summary: "Todo Created",
                      detail: "Todo has been created successfully.",
                      life: 3000
                  });
                isLoading.value = false;
                task.value = '';
                category.value = '';
                date.value = null;
            }
          }catch (error) {
              isLoading.value = false;
              toast.add(
                    {severity: "error",
                    summary: "Error Occured",
                    detail: "Try again later",
                    life: 3000}
                );
          }
        }
        const goHome = () => {
          const username = localStorage.getItem('username');
          console.log(username);
          router.push({ 
            name: 'transition', 
            params: { page : 'home',user: username } 
          });
        };
        const categories = [
          { name: 'Personal', icon: require('../assets/personal.svg'), color: 'rgba(140, 201, 255,0.3)' },
          { name: 'Productivity', icon: require('../assets/productivity.svg'), color: 'rgba(248, 143, 255,0.3)' },
          { name: 'Fitness', icon: require('../assets/fitness.svg'), color: 'rgba(156, 255, 143,0.3)' },
          { name: 'Work', icon: require('../assets/work.svg'), color: 'rgba(190, 143, 255,0.3)' },
          { name: 'Default', icon: require('../assets/default.svg'), color: 'rgba(204, 204, 204,0.3)' }
      ]

    
        return {
          categories,
          username,
          goHome,
          visible,
          date,
          postTask,
          task,
          category,
          isLoading,
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
  main {
    background-image: linear-gradient(100deg,rgba(211, 211, 211, 0.562),white ,white,white);
  }
  .input-container {
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    box-shadow: -16px 15px 22px 11px rgba(0,0,0,0.01);
    border: 1px solid rgba(0, 0, 0, 0.1);
    border-radius: 28px !important;
    padding: 12px;
    width: 85vw;
    margin-top: 20px;
    background-color: #fff;
    flex: 0 0 auto;
  }
  .button-container {
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    border-radius: 28px !important;
    padding: px;
    width: 85vw;
    margin-top: 8%;
    flex: 0 0 auto;
  }
  .button-container > button {
    width: 100%;
    padding: 12px;
    border-radius: 50px;
    border: none;
    font-size: 1.5em;
    font-weight: 600;
    outline: none;
    transition: border-color 0.3s ease;
    background-color: #ff5d2b;
    color: white;
    cursor: pointer;
  }
  .date-input {
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-direction: row;
    border: 1px solid rgba(0, 0, 0, 0.1);
    border-radius: 28px !important;
    padding: 12px;
    width: 85vw;
    margin-top: 20px;
    background-color: #fff;
    flex: 0 0 auto;
    background-color: rgba(226, 226, 255, 0.226);
  }
  .date-input > p {
    font-weight: 600;
  }
  .date {
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    padding: 12px;
    width: 95vw;
    height: 50% !important;
    margin-top: 10%;
    background-color: #fff;
    flex: 0 0 auto;
  }
  .date > * {
    margin: 3%;
  }
  .date-input:hover {
    opacity: 0.8;
    filter: contrast(40%);
    transition: all 0.3s ease-in-out;
  }
  .date-info-text > .date-mini-text {
    font-size: 0.8em;
    font-weight: 500 !important;
    color: grey;
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
  }
  .input-container > input {
    width: 100%;
    height: 3vh;
    padding: 5px;
    border-radius: 5px;
    border: none;
    font-size: 1.2em;
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
  @media (min-width: 768px) {
    .input-container {
      width: 95vw;
    }
    .date-input {
      width: 95vw;
      margin: 1%;
      cursor: pointer;
    }
    .date {
      margin-top: 1.5%;
    }
    .button-container {
      margin-top: 1%;
      width: 52vw;
    }
    .button-container:hover {
      cursor: pointer;
    }
    .form {
      overflow: hidden;
    }
  }
  </style>
  