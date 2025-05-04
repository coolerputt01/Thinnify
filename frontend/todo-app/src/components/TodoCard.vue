<template>
    <div class="todo-card-container">
        <span class="todo-card">
            <span class="desc-info">
                <span class="icon">
                    <img :src="icon" :alt="todoText" class="todo-icon" :style="{ backgroundColor : categoryColor }"/>
                </span>
                <span class="todo-card-text">
                    <h2> {{ todoText }}</h2>
                    <p> {{ todoNumber }} tasks</p>
                </span>
            </span>
            <span class="progress-bar">
                <CircleProgress :percent="progress" :viewport="false" :size="60" :border-width="7" :border-bg-width="7" :fill-color="categoryColor" empty-color="#c7c7c7af" :show-percent="true"/>
            </span>
        </span>
    </div>
</template>
<script>
    import "vue3-circle-progress/dist/circle-progress.css";
    import CircleProgress from "vue3-circle-progress";
    import { computed } from "vue";
    export default {
        name: "TodoCard",
        components: {
            CircleProgress,
        },
        props: {
            todoText: {
                type: String,
                required: true
            },
            todoNumber: {
                type: Number,
                required: true
            },
            icon: {
                type: String, 
                required: true
            },
            numberCompleted: {
                type: Number,
                required: true
            },
        },
        setup(props){
            const progress = computed(() => {
                if (props.todoNumber === 0) return 0;
                return props.numberCompleted;
            });

            const categoryColor = computed(() => {
                const colors = {
                    Personal: '#8cc9ff',
                    Productivity: '#f88fff',
                    Fitness: '#9cff8f',
                    Work: '#be8fff',
                    Default: '#cccccc' // Fallback color
                };
                return colors[props.todoText] || colors.Default;
            });
            console.log(props.todoNumber,props.numberCompleted)
            return { categoryColor ,progress};
    }
    };
</script>
<style scoped>
    * {
        margin: 0;
        padding: 0; 
        box-sizing: border-box;
        font-family: "Urbanist",sans-serif !important;
    }
    .todo-card-container {
        display: flex;
        justify-content: center;
        align-items: center;
        width: 100vw;
        padding: 6% !important;
    }
    .todo-card:hover {
        transform: scale(1.01);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.05);
        transition: all 0.5s ease;
        opacity: 0.9;
        cursor: pointer;
    }
    .desc-info {
        display: flex;
        justify-content: flex-start;
        align-items: center;
        width: 100%;
        height: 100%;
        gap: 10px;
    }
    .todo-card-text > h2 {
        font-weight: 550;
    }
    .todo-card-text > p {
        color: grey;
    }
    .todo-card {
        display: flex;
        justify-content: space-between;
        align-items: center;
        width: 100%;
        height: 100%;
        background-color: #fff;
        border-radius: 14px;
        padding: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    .icon {
        padding: 8px;
    }
    .icon > * {
        width: 30px;
        height: 30px;
        padding: 5px;
        border-radius: 50%;
    }
    @media (min-width: 768px) {
        .todo-card-container {
            width: 100%;
            justify-content: left;
        }
        .todo-card {
            width: 60vw;
            border-radius: 50px;
        }
    }
</style>