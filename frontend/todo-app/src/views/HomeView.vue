<template>
    <section>
        <main>
            <nav class="main-nav">
                <div class="img-container">
                    <!--Image Optimisation-->
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
                        <CircleProgress :percent="(completedTasks.length/filteredTodos.length) * 100" :viewport="true" fill-color="#fff" empty-color="#ff9878" :show-percent="true" :border-width="strokewidth" :border-bg-width="strokewidth" :size="70" />
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
            <NavBar/>
        </main>
    </section>
</template>
<script>
    import "vue3-circle-progress/dist/circle-progress.css";
    import CircleProgress from "vue3-circle-progress";
    import TodoCard from '@/components/TodoCard.vue';
    import VLazyImage from 'v-lazy-image';
    //onBeforeUnmount is used to run piece of code before the component is unmounted.
    import { ref, onMounted,computed ,getCurrentInstance, onBeforeUnmount} from "vue";
    import NavBar from '@/components/NavBar.vue';
    import CarouselItemCard from '@/components/CarouselItemCard.vue';

    export default {
        name: 'HomeView',
        components: {
            CarouselItemCard,
            CircleProgress,
            VLazyImage,
            TodoCard,
            NavBar
        },
        props: ['user'],
        setup() {
            //Arrays i created to manage the todos.
            const filteredTodos = ref([]);
            const completedTasks = ref([]);
            const onGoingTasks = ref([]);
            const personalTasks = ref([]);
            const fitnessTasks = ref([]);
            const productivityTasks = ref([]);
            const workTasks = ref([]);
            const defaultTasks = ref([]);

            const filterByCategory = () => {
                //Clear Arrays first
                completedTasks.value = [];
                onGoingTasks.value = [];
                personalTasks.value = [];
                fitnessTasks.value = [];
                productivityTasks.value = [];
                workTasks.value = [];
                defaultTasks.value = [];

                filteredTodos.value.forEach(todo => {
                    //Filter Todos either Completed or not
                    if (todo.completed === true) {
                        completedTasks.value.push(todo);
                    } else {
                        onGoingTasks.value.push(todo);
                    }

                    //Category check
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
            //GET request.
            const { proxy } = getCurrentInstance();
            const fetchTodos = async () => {
                try {
                    const response = await proxy.$api('/todos', {
                        headers: {
                            Authorization: `Bearer ${localStorage.getItem('access_token')}`
                        }
                    });

                    if (response.data && Array.isArray(response.data)) {
                        filteredTodos.value = response.data;
                        filterByCategory();
                    }
                } catch (err) {
                    console.error("Error fetching todos:", err.message);
                }
            };

            //A Progress Calculation to check the progress of the tasks based on the category.
            const getProgress = (taskList) => {
                if (taskList.length === 0) return 0;
                const completed = taskList.filter(t => t.completed).length;
                return Math.round((completed / taskList.length) * 100);
            };

            //Setting each progress value to the computed properties.
            const personalProgress = computed(() => getProgress(personalTasks.value));
            const fitnessProgress = computed(() => getProgress(fitnessTasks.value));
            const productivityProgress = computed(() => getProgress(productivityTasks.value));
            const workProgress = computed(() => getProgress(workTasks.value));
            const defaultProgress = computed(() => getProgress(defaultTasks.value));

            //Fetch todos when the component is mounted.
            onMounted(() => {
                fetchTodos();
            });

            //I'm trying to style the progress bar to be responsive.
            const strokewidth = ref(8);
            const width = ref(200);
            const height = ref(200);
            const windowWidth = ref(0);

            const updateWindowWidth = () => {
                windowWidth.value = window.innerWidth;
            };

            onMounted(() => {
                updateWindowWidth();
                window.addEventListener('resize', updateWindowWidth);
            });

            onBeforeUnmount(() => {
                window.removeEventListener('resize', updateWindowWidth);
            });
            const circleSize = computed(() => {
    return Math.max(50, Math.min(200, windowWidth.value * 0.1));
});

            return {
                strokewidth,
                width,
                height,
                windowWidth,
                circleSize,

                filteredTodos,
                completedTasks,
                onGoingTasks,
                personalTasks,
                fitnessTasks,
                productivityTasks,
                workTasks,
                defaultTasks,

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
        background-image: linear-gradient(100deg,rgba(211, 211, 211, 0.562),white ,white,white);
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
        gap: 8%;
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
        padding: 3% !important;
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
        justify-content: space-around;
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
        justify-content: center;
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
        justify-content: left;
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
    @media (min-width:768px) {
        .nav-text-container  > h2{
            font-size: 0.9em;
        }
        .nav-text-container  > p{
            font-size: 1.1em;
        }
        .main-nav {
            gap: 2% !important;
        }
        .today-task-card {
            width: 50vw !important;
            height: 25vh !important;
            margin: 0.32% !important;
            padding: 12px !important;
            gap: 1% !important;
        }
        .in-progress-text {
            gap: 0 !important;
            justify-content: flex-start !important;
        }
        .in-progress-head {
            width: 10vw !important;
        }
        .progress-carousel {
            margin-left: 3em !important;
            justify-content: center;
            gap: 3%;
            height: 35vh !important;
        }
        .task-groups {
            margin-bottom: 5% !important;
        }
        .task-groups-list {
            gap: 1% !important;
        }
        .task-group-text {
            gap: 1em !important;
        }
    }
    @keyframes l18 {
        0%   {clip-path:polygon(50% 50%,0 0,0    0,0    0   ,0    0   ,0    0   )}
        25%  {clip-path:polygon(50% 50%,0 0,100% 0,100% 0   ,100% 0   ,100% 0   )}
        50%  {clip-path:polygon(50% 50%,0 0,100% 0,100% 100%,100% 100%,100% 100%)}
        75%  {clip-path:polygon(50% 50%,0 0,100% 0,100% 100%,0    100%,0    100%)}
        100% {clip-path:polygon(50% 50%,0 0,100% 0,100% 100%,0    100%,0    0   )}
    }
</style>
