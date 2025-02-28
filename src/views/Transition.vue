<template>
    <div class="transition-container">
        <div class="transition-circle" @animationend="onAnimationEnd"></div>
    </div>
</template>

<script>
export default {
    name: "Transition",
    methods: {
        onAnimationEnd() {
            var page = this.$route.params.page;
            // After the animation ends, navigate to the desired page
            this.$router.push(`/${page}`);
        }
    },
}
</script>

<style scoped>
* {
    font-family: "Urbanist", sans-serif;
    box-sizing: border-box;
    padding: none;
    margin: none;
}

.transition-container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    width: 100vw;
    background: #fff;
    position: relative;
}

.transition-circle {
    width: 100px;
    height: 100px;
    border-radius: 50%;
    background-color: grey;
    box-shadow: 5px 5px 15px -3px rgba(0, 0, 0, 0.5);
    position: absolute;
    bottom: -8px;
    right: -8px;
    opacity: 1;
    animation: zoom-out 1s ease-in forwards;
}

@keyframes zoom-out {
    to {
        transform: scale(360);
        opacity: 0.2;
    }
}
</style>
