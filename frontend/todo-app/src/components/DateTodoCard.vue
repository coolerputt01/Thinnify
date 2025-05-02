<template>
    <div class="todo-card">
        <div class="date-container">
            <p class="todo-group" :style="{ color:categoryColor }"> {{ categoryName }} </p>
            <div class="card-groups" v-if="todos.length > 0">
                <TodoComp v-for="todo in todos" :key="todo.id" :completed="todo.completed" :todo-id="todo.id" :todo-task="todo.title" :todo-date="new Date(todo.created).toLocaleDateString()" :todo-category="categoryName"  @status-updated="handleStatusChange"/>
            </div>
            <div v-else class="empty-todo">
                <p class="none">No Tasks</p>
            </div>
        </div>
    </div>
</template>
<script>
    import { computed} from 'vue';
    import TodoComp from './TodoComp.vue';
    export default {
        name: 'DateTodoCard',
        props: {
            user: String,
            todos: {
                type: Array,
                required: true
            },
            categoryName: {
                type:String,
                required:true
            }
        },
        components: {
            TodoComp
        },
        emits: ['todo-status-updated'],
        setup(props, { emit }) {
            // This is reactive and safe to use right away
            const handleStatusChange = (payload) => {
                emit('todo-status-updated', payload);
            };
            const categoryColor = computed(() => {
                const colors = {
                    Personal: '#8cc9ff',
                    Productivity: '#f88fff',
                    Fitness: '#9cff8f',
                    Work: '#be8fff',
                    Default: '#cccccc'
                };
                return colors[props.categoryName] || colors.Default;
            });

            return {
                categoryColor,
                handleStatusChange
            };
        }
    }
</script>
<style scoped>
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
        font-family: "Urbanist", sans-serif;
    }
    .todo-card {
        margin: 2%;
    }
    .todo-group {
        padding: 12px;
        font-size: 1.7em;
        font-weight: 700;
    }
    .none {
        font-size: 1.5em;
        font-weight: 500;
        color: grey;
        text-align: center;
        padding: 18px;
    }
</style>