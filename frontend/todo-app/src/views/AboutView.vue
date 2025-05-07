<template>
    <div>
        This project was made by coolerputt.
        <NavBar />
    </div>
</template>
<script>
    import NavBar from '../components/NavBar.vue';
    export default {
        name:'AboutView',
        components:{
            NavBar
        },
    }
</script>
<style scoped>
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
        font-family: "Urbanist",sans-serif;
    }
    div {
        display: flex;
        align-items: center;
        justify-content: center;
        width: 100vw;
        height: 100vh;
        background-color: #fff;
        color: #000;
    }
</style>