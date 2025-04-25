<template>
    <section>
        <nav class="nav-bar">
            <span class="icon-groups">
                <span class="icon-group">
                    <div class="icon-container">
                        <img src="../assets/home.svg" alt="Thinnify Thinnify nav icon home">
                    </div>
                    <div class="icon-container">
                        <img src="../assets/calender.svg" alt="Thinnify Thinnify nav icon calender">
                    </div>
                </span>
                <span class="icon-group">
                    <div class="add-icon-container">
                        <router-link :to="{name:'transition',params:{ page : 'create'}}"><img src="../assets/add.svg" alt="Thinnify Thinnify nav icon Add" class="add-icon"></router-link>
                    </div>
                </span>
                <span class="icon-group">
                    <div class="icon-container">
                        <img src="../assets/paper.svg" alt="Thinnify Thinnify nav icon paper">
                    </div>
                    <div class="icon-container">
                        <img src="../assets/people.svg" alt="Thinnify Thinnify nav icon people">
                    </div>
                </span>
            </span>
        </nav>        
    </section>
</template>
<script>
    export default {
        name: 'NavBar',
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
        height: 7vh !important;
        padding: 22px;
        z-index: 1000;
    }
    /* .add-icon {
        width: 2.7em !important;
        height: 2.7em !important;
    } */
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
    .icon-container > * {
        width: 1.9em;
        height: 1.9em;
        object-fit: cover;
        transition: all 350ms;
        cursor: pointer;
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
    .icon-container > img:hover {
        opacity: 0.8;
        transform: translateY(-15%);
    }
</style>