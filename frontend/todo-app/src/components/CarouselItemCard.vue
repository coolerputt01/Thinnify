<template>
    <div class="carousel-item-card">
        <div class="icon">
            <img :src="src" alt="Thinnify Thinnify Thinnify Icon" class="card-icon">
        </div>
        <div class="task-title"><h2>{{ category }}</h2></div>
        <ProgressBar :value="progress"></ProgressBar>
    </div>
</template>
<script>
    export default {
        name:'CarouselItemCard',
        props: {
            category: {
                type:String,
                required:true
            },
            progress: {
                type: Number,
                required: true,
            },
            src: {
                type: String,
                required: true,
            },
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
    .p-progressbar-value {
        background-color: blue !important;
    }
</style>