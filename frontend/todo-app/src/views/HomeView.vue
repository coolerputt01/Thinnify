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
                <div class="today-task">
                    <h2 class="today-head">Today's Task</h2>
                    <button class="view-btn">View Tasks</button>
                </div>
                <n-config-provider>
                    <n-progress type="line" :percentage="70" :height="10" color="#00ff9c" />
                </n-config-provider>
            </div>
            <div class="in-progress">
                <span class="progress-card">
                    <span class="in-progress-text">
                        <h2 class="in-progress-head">In Progress</h2>
                        <small>6</small>
                    </span>
                    <div class="progress-carousel">
                        <CarouselItemCard  category="Personal" :src="require('../assets/personal.svg')" :progress="70"/>
                    </div>
                </span>
            </div>
            <NavBar />
        </main>
    </section>
</template>
<script>
    import VLazyImage from 'v-lazy-image';
    import axios from "axios";
    axios.defaults.withCredentials = true;
    import NavBar from '@/components/NavBar.vue';
    import CarouselItemCard from '@/components/CarouselItemCard.vue';
    export default {
        name:'HomeView',
        components:{
            NavBar,
            CarouselItemCard,
            VLazyImage,
        },props:['user'],
        methods: {
            async fetchTodoFromDate(){
                try{
                    const response = await axios.get('http://127.0.0.1:5000/check-session');
                    console.log(response);
                }catch(err){
                    console.error("Pele bro, e dey happen",err.message);
                }
            },
        },async mounted(){
            await this.fetchTodoFromDate();
        }
    }
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
    .profile {
        width: 3em !important;
        height: 3em !important;
        object-fit: cover;
    }
    .today-task-card {
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 10%;
        width: 80vw !important;
        height: 20vh !important;
        background-color: #ff5d2b !important;
        color: #fff !important;
        border-radius: 14px !important;
        margin: 12px;
        -webkit-box-shadow: 5px 5px 26px 0px rgba(0,0,0,0.24); 
        box-shadow: 5px 5px 26px 0px rgba(0,0,0,0.24);
    }
    .today-task {
        display: flex;
        justify-content: flex-start;
        align-items: center;
        width: 100%;
        margin: 5% !important;
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