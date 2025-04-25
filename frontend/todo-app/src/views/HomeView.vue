<template>
    <section>
        <main>
            <nav class="main-nav">
                <div class="img-container">
                    <VLazyImage src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRTxoOGOgrf6j8wBO_t92ryv2tnseAPM78vFw&s" class="profile"></VLazyImage>
                </div>
                <div class="nav-text-container">
                    <h2>Hello!</h2>
                    <p>{{ user }}</p>
                </div>
            </nav>
            <div class="today-task-card">
                <div class="container">
                    <div class="today-task">
                        <h2 class="today-head">Today's Task</h2>
                        <button class="view-btn">View Tasks</button>
                    </div>
                    <div class="c-prog">
                        <CircleProgress :percent="(completedTasks.length/filteredTodos.length) * 100" :viewport="false" fill-color="#fff" empty-color="#ff9878" :show-percent="true"/>
                    </div>
                </div>
            </div>
            <div class="in-progress">
                <span class="progress-card">
                    <span class="in-progress-text">
                        <h2 class="in-progress-head">In Progress</h2>
                        <small>{{ filteredTodos.length - completedTasks.length }}</small>
                    </span>
                    <div class="progress-carousel">
                        <CarouselItemCard  category="Personal" :src="require('../assets/personal.svg')" :progress="personalProgress"/>
                        <CarouselItemCard  category="Fitness" :src="require('../assets/fitness.svg')" :progress="fitnessProgress"/>
                        <CarouselItemCard  category="Productivity" :src="require('../assets/productivity.svg')" :progress="productivityProgress"/>
                        <CarouselItemCard  category="Work" :src="require('../assets/work.svg')" :progress="workProgress"/>
                        <CarouselItemCard  category="Default" :src="require('../assets/default.svg')" :progress="defaultProgress"/>
                    </div>
                </span>
                <span class="task-groups">
                    <span class="task-group-text">
                        <h2 class="task-group-head">Task Group</h2>
                        <small>{{ filteredTodos.length }}</small>
                    </span> 
                    <div class="task-groups-list">
                        <TodoCard v-if="personalTasks.length > 0" todoText="Personal" :todoNumber="personalTasks.length" :icon="require('../assets/personal.svg')" :numberCompleted="personalProgress"/>
                        <TodoCard v-if="fitnessTasks.length > 0" todoText="Fitness" :todoNumber="fitnessTasks.length" :icon="require('../assets/fitness.svg')" :numberCompleted="fitnessProgress"/>
                        <TodoCard v-if="productivityTasks.length" todoText="Productivity" :todoNumber="productivityTasks.length" :icon="require('../assets/productivity.svg')" :numberCompleted="productivityProgress"/>
                        <TodoCard v-if="workTasks.length > 0" todoText="Work" :todoNumber="workTasks.length" :icon="require('../assets/work.svg')" :numberCompleted="workProgress"/>
                        <TodoCard v-if="defaultTasks.length > 0" todoText="Default" :todoNumber="defaultTasks.length" :icon="require('../assets/default.svg')" :numberCompleted="defaultProgress"/>
                    </div>
                </span>
            </div>
            <NavBar />
        </main>
    </section>
</template>
<script>
    import "vue3-circle-progress/dist/circle-progress.css";
    import CircleProgress from "vue3-circle-progress";
    import TodoCard from '@/components/TodoCard.vue';
    import VLazyImage from 'v-lazy-image';
    import { ref, onMounted,computed } from "vue";
    import axios from "axios";
    axios.defaults.withCredentials = true;

    import NavBar from '@/components/NavBar.vue';
    import CarouselItemCard from '@/components/CarouselItemCard.vue';

    export default {
        name: 'HomeView',
        components: {
            NavBar,
            CarouselItemCard,
            CircleProgress,
            VLazyImage,
            TodoCard,
        },
        props: ['user'],
        setup() {
    const filteredTodos = ref([]);
    const completedTasks = ref([]);
    const onGoingTasks = ref([]);
    const personalTasks = ref([]);
    const fitnessTasks = ref([]);
    const productivityTasks = ref([]);
    const workTasks = ref([]);
    const defaultTasks = ref([]);

    const filterByCategory = () => {
        // Clear arrays first (important!)
        completedTasks.value = [];
        onGoingTasks.value = [];
        personalTasks.value = [];
        fitnessTasks.value = [];
        productivityTasks.value = [];
        workTasks.value = [];
        defaultTasks.value = [];

        filteredTodos.value.forEach(todo => {
            // Completed or not
            if (todo.completed === true) {
                completedTasks.value.push(todo);
            } else {
                onGoingTasks.value.push(todo);
            }

            // Category check
            switch (todo.category) {
                case "Personal":
                    personalTasks.value.push(todo);
                    break;
                case "Fitness":
                    fitnessTasks.value.push(todo);
                    break;
                case "Productivity":
                    productivityTasks.value.push(todo);
                    break;
                case "Work":
                    workTasks.value.push(todo);
                    break;
                default:
                    defaultTasks.value.push(todo);
            }
        });
    };

    const fetchTodos = async () => {
        try {
            const response = await axios.get('http://127.0.0.1:5000/todos', {
                headers: {
                    Authorization: `Bearer ${localStorage.getItem('access_token')}`
                }
            });

            if (response.data && Array.isArray(response.data)) {
                filteredTodos.value = response.data;
                console.log("Fetched todos:", filteredTodos.value);
                filterByCategory();
            }
        } catch (err) {
            console.error("Error fetching todos:", err.message);
        }
    };

    // 👇 Progress Calculators
    const getProgress = (taskList) => {
        if (taskList.length === 0) return 0;
        const completed = taskList.filter(t => t.completed).length;
        return Math.round((completed / taskList.length) * 100);
    };

    const personalProgress = computed(() => getProgress(personalTasks.value));
    const fitnessProgress = computed(() => getProgress(fitnessTasks.value));
    const productivityProgress = computed(() => getProgress(productivityTasks.value));
    const workProgress = computed(() => getProgress(workTasks.value));
    const defaultProgress = computed(() => getProgress(defaultTasks.value));

    onMounted(() => {
        fetchTodos();
    });

    return {
        filteredTodos,
        completedTasks,
        onGoingTasks,
        personalTasks,
        fitnessTasks,
        productivityTasks,
        workTasks,
        defaultTasks,

        // Progress values (hook these into your carousel)
        personalProgress,
        fitnessProgress,
        productivityProgress,
        workProgress,
        defaultProgress
    };
}
    };
</script>


<style scoped>
    * {
        margin: 0;
        padding: 0; 
        box-sizing: border-box;
        font-family: "Urbanist",sans-serif;
    }
    main {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        width: 100vw !important;
        overflow-x: hidden;
    }
    section {
        overflow-x: hidden;
        overflow-y: scroll;
        background-image: linear-gradient(30deg, lightgrey,white ,white);
    }

        /* For WebKit browsers (Chrome, Safari, Edge) */
    .progress-carousel::-webkit-scrollbar {
        height: 5px;
    }

    .progress-carousel::-webkit-scrollbar-track {
        background: transparent; /* Light gray track */
        border-radius: 8px;
    }

    .progress-carousel::-webkit-scrollbar-thumb {
        background-color: #ff5d2b; /* Customize to match your theme */
        border-radius: 8px;
    }

    .main-nav {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: row;
        width: 90% !important;
        gap: 4%;
        padding: 19.5px;
        margin: 12px;
    }
    .img-container {
        width: 3em !important;
        height: 3em !important;
    }
    .nav-text-container {
        width: 100% !important;
    }
    .c-prog {
        display: flex;
        justify-content: center;
        align-items: center !important;
        width: 30%;
        position: relative;
    }
    .progress-carousel {
        display: flex;
        justify-content: flex-start;
        align-items: center !important;
        width: 100%;
        height: 100%;
        overflow-x: auto;
        overflow-y: hidden;
        margin: 5% !important;
        gap: 10%;
        scroll-behavior: smooth;
        -webkit-overflow-scrolling: touch;
        margin-right: 14% !important;
    }
    .task-group-text {
        display: flex;
        justify-content: left;
        align-items: center !important;
        width: 100%;
        height: 100%;
        gap: 5%;
        margin: 5% !important;
    }
    .task-groups {
        display: flex;
        justify-content: center;
        align-items: center !important;
        width: 100vw !important;
        padding: 5% !important;
        flex-direction: column;
        margin-bottom: 15% !important;
    }
    .container{
        display: flex;
        justify-content: center;
        align-items: center !important;
        width: 100%;
        height: 70%;
        margin: 10% !important;
    }
    .task-group-head {
        text-align: left;
    }
    .nav-text-container > * {
        text-align: left;
    }
    .nav-text-container > h2 {
        font-weight: normal;
        font-size: 1.2em;
    }
    .nav-text-container > p {
        font-weight: bold;
        font-size: 1.3em;
    }
    .task-groups-list {
        display: flex;
        justify-content: center;
        align-items: center !important;
        width: 100%;
        height: 100%;
        gap: 15%;
        margin: 0 auto;
        scroll-behavior: smooth;
        flex-direction: column;
    }
    .progress-card {
        display: flex;
        justify-content: center;
        align-items: center !important;
        width: 95vw !important;
        flex-direction: column;
        margin: 5% !important;
    }
    .profile {
        width: 3em !important;
        height: 3em !important;
        object-fit: cover;
    }
    .today-task-card {
        display: flex;
        justify-content: space-between;
        align-items: center !important;
        gap: 10%;
        width: 80vw !important;
        height: 20vh !important;
        background-color: #ff5d2b !important;
        color: #fff !important;
        border-radius: 20px !important;
        margin: 12px;
        -webkit-box-shadow: 5px 5px 26px 0px rgba(0,0,0,0.24); 
        box-shadow: 5px 5px 26px 0px rgba(0,0,0,0.24);
    }
    .today-task {
        display: flex;
        justify-content: flex-start;
        align-items: center;
        width: 100%;
        flex-direction: column;
    }
    .view-btn {
        outline: none;
        border: none;
        background-color: #fff !important;
        color: #ff5d2b !important;
        font-size: 0.8em !important;
        padding: 10px;
        border-radius: 50px;
        cursor: pointer;
        transition: all 250ms;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 10%;
        align-self: flex-start;
    }
    .loaded {
        margin: 8% !important;
    }
    .view-btn:hover {
        opacity: 0.8; 
    }
    .today-head {
        font-weight: bold;
        font-size: 1.5em !important;
        width: 100% !important;
        margin-bottom: 10% !important;
    }

    .in-progress-text {
        display: flex;
        justify-content: flex-start;
        align-items: center !important;
        gap: 5%;
        width: 100% !important;
    }
    .in-progress-head {
        width: 29vw !important;
    }

    .in-progress-text > small {
        color: #ff5d2b !important;
        padding: 6px;
        background-color:#d4d4d4;
        border-radius: 50%;
    }
    .task-group-text > small {
        color: #ff5d2b !important;
        padding: 6px;
        background-color:#d4d4d4;
        border-radius: 50%;
    }
    /* HTML: <div class="loader"></div> */
    .loader {
    width: 80px;
    aspect-ratio: 1;
    border: 10px solid #ffa185;
    border-radius: 50%;
    position: relative;
    transform: rotate(45deg);
    }
    .loader::before {
    content: "";
    position: absolute;
    inset: -12px;
    border-radius: 50%;
    border: 10px solid #fff;
    animation: l18 2s infinite linear;
    }
    @keyframes l18 {
        0%   {clip-path:polygon(50% 50%,0 0,0    0,0    0   ,0    0   ,0    0   )}
        25%  {clip-path:polygon(50% 50%,0 0,100% 0,100% 0   ,100% 0   ,100% 0   )}
        50%  {clip-path:polygon(50% 50%,0 0,100% 0,100% 100%,100% 100%,100% 100%)}
        75%  {clip-path:polygon(50% 50%,0 0,100% 0,100% 100%,0    100%,0    100%)}
        100% {clip-path:polygon(50% 50%,0 0,100% 0,100% 100%,0    100%,0    0   )}
    }
</style>