<template>
    <section>
        <nav class="nav-bar">
            <span class="icon-groups">
                <span class="icon-group">
                    <div class="icon-container">
                        <router-link :to="{name:'transition',params:{ page:'home',user: username}}"><img src="../assets/home.svg" alt="Thinnify Thinnify nav icon home" class="icon"></router-link>
                    </div>
                    <div class="icon-container">
                        <router-link :to="{name:'transition',params:{ page : 'calender' ,user:'/'}}"><img src="../assets/calender.svg" alt="Thinnify Thinnify nav icon calender" class="icon"></router-link>
                    </div>
                </span>
                <span class="icon-group">
                    <div class="add-icon-container">
                        <router-link :to="{name:'transition',params:{ page : 'create' ,user:'/'}}"><img src="../assets/add.svg" alt="Thinnify Thinnify nav icon Add" class="add-icon"></router-link>
                    </div>
                </span>
                <span class="icon-group">
                    <div class="icon-container">
                        <router-link :to="{ name:'transition',params:{ page:'search',user:'/'}}" ><img src="../assets/search.svg" alt="Thinnify Thinnify nav icon paper" class="icon"></router-link>
                    </div>
                    <div class="icon-container">
                        <router-link :to="{ name:'transition',params:{ page:'about',user:'/'} }"><img src="../assets/info.svg" alt="Thinnify Thinnify nav icon info" class="icon"></router-link>
                    </div>
                </span>
            </span>
        </nav>        
    </section>
</template>
<script>
    export default {
        name: 'NavBar',
        data() {
            return {
                username : localStorage.getItem('username'),
            }
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
    .nav-bar {
        display: flex;
        align-items: center;
        justify-content: center;
        backdrop-filter: blur(5px);
        position: fixed;
        bottom: -2px;
        left: 0;
        width: 100% !important;
        height: 7vh ;
        padding: 22px;
        z-index: 1000;
    }
    .icon-group {
        display: flex;
        align-items: center;
        justify-content: space-between;
        width: 50%;
        gap: 35px;
    }
    
    .icon-groups {
        display: flex;
        align-items: center;
        justify-content: space-between;
        width: 100%;
    }
    .icon {
        width: 1.9em;
        height: 1.9em;
        object-fit: cover;
        transition: all 350ms;
        cursor: pointer;
        mix-blend-mode: multiply;
    }
    .add-icon-container {
        display: flex;
        align-items: center;
        justify-content: center;
        width: 100%;
        height: 100%;
    }
    .add-icon {
        width: 3.2em;
        height: 3.2em;
        object-fit: cover;
        transition: all 350ms;
        cursor: pointer;
        transform: translateY(-35%);
    }
    .icon:hover {
        opacity: 0.8;
        transform: translateY(-15%);
    }
    @media (min-width: 768px) {
        .nav-bar {
            height: 10vh;
        }
    }
</style>