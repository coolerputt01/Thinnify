<template>
    <div class="todo-card-container">
        <span class="todo-card">
            <span class="desc-info">
                <span class="icon">
                    <div class="border" :style="{ borderColor: categoryColor }" @click="isClicked = !isClicked">
                        <div class="clicked" :class="{ click: isClicked }" :style="{ backgroundColor : categoryColor }"></div>
                    </div>
                </span>
                <span class="todo-card-text">
                    <h2 :class="{ slash :isClicked  }"> {{ todoTask }}</h2>
                    <p>created by {{  todoDate }}</p>
                </span>
            </span>
        </span>
    </div>
</template>
<script>
    import {ref , computed , watch} from 'vue';
    import axios from 'axios';
    export default {
        name: 'TodoComp',
        props: {
            todoCategory: {
                type: String,
                required: true
            },
            todoId :{
                type: Number,
                required:true
            },
            todoTask: {
                type: String,
                required: true
            },
            todoDate: {
                type: String,
                required: true
            },
            completed: {
                type: Boolean,
                required: true
            }
        },
        emits: ['status-updated'],
        setup(props, { emit }) {
            const isClicked = ref(props.completed);

            const categoryColor = computed(() => {
                const colors = {
                    Personal: '#8cc9ff',
                    Productivity: '#f88fff',
                    Fitness: '#9cff8f',
                    Work: '#be8fff',
                    Default: '#cccccc' // Fallback color
                };
                return colors[props.todoCategory] || colors.Default;
            });
            watch(isClicked, async (newVal) => {
            try {
                const response = await axios.put(`http://127.0.0.1:5000/todo/${ props.todoId }`, {
                    completed: newVal
                }, {
                    headers: {
                        Authorization: `Bearer ${localStorage.getItem('access_token')}`
                    }
                });
                console.log('Updated todo status:', response.data);
                emit('status-updated', {
                    task: props.todoTask,
                    completed: newVal
             });
            } catch (error) {
                console.error('Failed to update todo status:', error);
            }
        });
            return { categoryColor,isClicked};
    }
    }
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
        justify-content: flex-start;
        align-items: center;
        width: 100vw;
        margin: 0.5% !important;
        padding: 6% !important;
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
        font-size: 1.3em;
        transition: all 0.3s ease;
    }
    .slash {
        text-decoration: line-through;
        color: grey;
        font-weight: 500;
    }
    .todo-card-text > p {
        color: grey;
        font-size: 0.9em;
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
    .border {
        width: 30px;
        height: 30px;
        border-radius: 50%;
        display: flex;
        justify-content: center;
        align-items: center;
        border: 2px solid; /* Default border color */
        transition: all 0.3s ease;
    }
    .clicked {
        width: 100%;
        height: 100%;
        object-fit: cover;
        border-radius: 50%;
        transition: all 0.3s ease;
        flex: 0 0 auto;
        display: none;
        cursor: pointer;
    }
    .clicked.click {
        display: block;
    }
</style>