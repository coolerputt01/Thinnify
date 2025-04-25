<template>
    <div class="transition-container">
        <div class="transition-circle" @animationend="onAnimationEnd"></div>
    </div>
</template>

<style scoped>
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
        font-family: "Urbanist", sans-serif;
    }

    .transition-container {
        display: flex;
        align-items: center;
        justify-content: center;
        width: 100vw;
        height: 100vh;
        background-color: #fff;
    }

    .transition-circle {
        position: absolute;
        bottom: 7vh;
        left: 50%;
        width: 100px;
        height: 100px;
        border-radius: 50%;
        background-color: #ff5d2b;
        animation: scale 2s ease-in-out forwards;
    }

    @keyframes scale {
        to {
            transform: scale(150);
            opacity: 0;
        }
    }
</style>

<script>
export default {
    name: 'TransitionView',
    props: ['page'],
    methods: {
        onAnimationEnd() {
            // Once the animation ends, redirect to the page passed via props
            this.$router.push({ name: this.page });
        }
    }
}
</script>
