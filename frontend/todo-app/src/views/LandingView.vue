<!--Landing View HTMl codes-->
<template>
    <!--I had to put more than one container has good practice-->
    <section>
        <main>
            <!--Then I added the elemental features in containers. PS: I tried to get my SEO skills running well.-->
            <div class="main-image-container">
                <VLazyImage  src="https://i.ibb.co/4nNgvGNm/Thinnfy-Landing-page-image.gif" alt="Thinnify Thinnify Lady Sitting down." class="main-image" />
            </div>
            <span class="text-container">
                <h1 class="text-head">Task Management & To-Do List</h1>
                <p class="text">This productive tool is designed to help you better manage your daily life conveniently!</p>
            </span>
            <div class="button-container">
                <button class="redirect-btn" @click="this.$router.push('/signup')">Let's Start <img src="../assets/right-arrow.svg" alt="Thinnify Thinnify Right Arrow" class="icon"></button>
            </div>
            <div class="circles">

            </div>
        </main>
    </section>
</template>
<!--Nothing much as a script but just to export the name of the model component.-->
<script>
    import VLazyImage from "v-lazy-image";
    export default {
        name: "LandingView",
        components: {
            VLazyImage,
        }
    }
</script>
<!--These are the CSS codes for the already declared HTML elements.-->
<style scoped>
    /*Before you continue reading , I want you to know that I am very mucb obessessed with flexboxes when I code CSS .*/
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
        font-family: "Urbanist",sans-serif;
    }
    main {
        display: flex;
        align-items: center;
        justify-content: center;
        flex-direction: column;
        column-gap: 50px;
        flex-wrap: wrap;
        overflow: hidden;
        position: relative;
    }
    .main-image-container {
        max-width: 85vw;
        max-height: 45vh;
        position: relative;
    }
    .main-image {
        width: 100%;
        height: 100%;
        object-fit: cover;
    }
    .text-container {
        display: flex;
        align-items: center;
        justify-content: center;
        flex-direction: column;
        margin-top: 20%;
    }
    .text-container > * {
        margin: 3%;
    }
    .text-head {
        text-align: center;
        font-size: 2.2em;
    }
    .text {
        color: grey;
        max-width: 90%;
        text-align: center;
    }
    .button-container {
        margin: 2%;
        position: relative;
        display: flex;
        overflow: hidden;
        background-clip: cover;
    }
    /*I had an issue here trying to add a special hover effect but I later discarded it */
    .redirect-btn {
        outline: none;
        border: none;
        background-color: #ff5d2b;
        color: #fff !important;
        font-size: 1.2em;
        width: 70vw !important;
        padding: 5px;
        border-radius: 50px;
        cursor: pointer;
        transition: all 250ms;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 10%;
    }
    .redirect-btn:hover {
        opacity: 0.8;
    }
    .icon {
        width: 2.3em;
        height: 2.3em;
    }
    .redirect-btn:hover .icon {
        transform: translateX(15px);
        transition: all 250ms;
    }
    .main-image-container::before {
        content: '';
        position: absolute;
        top: 15%;
        left: 15%;
        width: 16em;
        height: 16em;
        background-color: #ff5d2b;
        opacity: 0.1;
        border-radius: 50%;
    }
    @media (min-width: 768px) {
        .main-image {
            max-width: 50vw;
            max-height: 50vh;
        }
        .circles {
            position: absolute;
            top: 1em;
            left: 1em;
            width: 14em;
            height: 14em;
            background-color: #ff5d2b;
            border-radius: 50%;
            opacity: 0.6;
        }
        .text-container {
            margin-top: 5%;
        }
        .text-head {
            font-size: 1.7em;
            margin: 0.3em;
        }
        .redirect-btn {
            width: 25vw !important;
            padding: 8px;
            height: 2em;
        }
        .redirect-btn:hover {
            opacity: 1;
        }
        main::after {
            content: '';
            position: absolute;
            top: 35%;
            left: 16em;
            width: 9em;
            height: 9em;
            opacity: 0.2;
            background-color: #ff5d2b;
            border-radius: 50%;
        }
        main::before {
            content: '';
            position: absolute;
            top: 18%;
            right: 8em;
            width: 9em;
            height: 9em;
            opacity: 0.5;
            background-color: #ff5d2b;
            border-radius: 50%;
        }
    }
</style>
