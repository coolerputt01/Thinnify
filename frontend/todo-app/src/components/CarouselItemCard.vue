<template>
    <div class="carousel-item-card" :style="{ backgroundColor: categoryColor }">
        <div class="icon">
            <img :src="src" alt="Thinnify Icon" class="card-icon">
        </div>
        <div class="task-title">
            <h2>{{ category }}</h2>
        </div>
        <ProgressBar :value="progress" :showValue="false"></ProgressBar>
    </div>
</template>

<script>
import { computed } from 'vue';
import ProgressBar from 'primevue/progressbar';

export default {
    name: 'CarouselItemCard',
    components: {
        ProgressBar,
    },
    props: {
        progress: {
            type: Number,
            required: true
        },
        category: {
            type: String,
            required: true
        },
        src: {
            type: String,
            required: true
        }
    },
    setup(props) {
        // Determine background color based on injected category
        const categoryColor = computed(() => {
            const colors = {
                Personal: 'rgba(140, 201, 255,0.3)',
                Productivity: 'rgba(248, 143, 255,0.3)',
                Fitness: 'rgba(156, 255, 143,0.3)',
                Work: 'rgba(190, 143, 255,0.3)',
                Default: 'rgba(204, 204, 204,0.3)' // Fallback color
            };
            return colors[props.category] || colors.Default;
        });

        return { categoryColor };
    }
};
</script>

<style scoped>
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: "Urbanist", sans-serif;
}
.carousel-item-card {
    padding: 25px;
    border-radius: 20px;
    color: white; /* Ensure text is readable */
    transition: background-color 0.3s ease;
    cursor: pointer;
    transition: all 0.3s ease;
    flex: 0 0 auto; 
}
.carousel-item-card:hover {
    transform: scale(1.05);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}
.icon {
    display: flex;
    align-items: center;
    justify-content: flex-end;
    margin-bottom: 10px;
}
.card-icon {
    width: 24px;
    height: 24px;
}
.task-title > h2{
    margin: 15px;
    font-size: 1.3em;
    font-weight: 500;
    text-align: left;
    color: black;
}
.p-progressbar-value {
    background-color: blue !important;
}
</style>
