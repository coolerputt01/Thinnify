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
                    <div class="icon-container">
                        <img src="../assets/add.svg" alt="Thinnify Thinnify nav icon Add" class="add-icon">
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
        backdrop-filter: blur(10px);
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100% !important;
        padding: 22px;
        z-index: 1000;
    }
    .add-icon {
        width: 2.7em !important;
        height: 2.7em !important;
        transform: translateY(-30%);
    }
    .icon-group {
        display: flex;
        align-items: center;
        justify-content: space-around;
        width: 40%;
    }
    .icon-groups {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 30px;
        width: 100%;
    }
    .icon-container > * {
        width: 1.7em;
        height: 1.7em;
        object-fit: cover;
        transition: all 350ms;
        cursor: pointer;
    }
    .icon-container > img:hover {
        opacity: 0.8;
        transform: translateY(-15%);
    }
</style>