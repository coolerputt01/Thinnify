<template>
    <section>
        <main>
            <Toast />
            <div class="search-container">
                <div class="search-bar">
                    <input type="text" placeholder="Search..." class="search-input" v-model="search"/>
                    <VLazyImage src="../assets/search.svg" alt="Thinnify Thinnify nav icon search" class="search-icon" @click="fetchTodos" />
                </div>
            </div>
            <div class="card-container" v-if="todos.length > 0">
                <TodoComp v-for="todo in todos" :key="todo.id" :completed="todo.completed" :todo-id="todo.id" :todo-task="todo.title" :todo-date="new Date(todo.created).toLocaleDateString()" :todo-category="todo.category"  @status-updated="showToast" />
            </div>
            <div class="empty-todo" v-else>
                <VLazyImage src="../assets/animate.gif" alt="Thinnify Thinnify No Tasks" class="empty-todo-gif" />
                <p class="none">No Tasks</p>
            </div>
            <NavBar />
        </main>
    </section>
</template>
<script>
    import NavBar from '@/components/NavBar.vue';
    import { ref ,watch,onBeforeUnmount ,getCurrentInstance} from 'vue';
    import TodoComp from '@/components/TodoComp.vue';
    import { Toast } from 'primevue';
    import { useToast } from 'primevue/usetoast';
    import VLazyImage from "v-lazy-image";
    export default {
        name: 'SearchView',
        components:{
            NavBar,
            TodoComp,
            Toast,
            VLazyImage
        },
        props: {
            user: String
        },
        emits: ['todo-status-updated'],
        setup() {
            const showToast = ({ task, completed }) => {
                toast.add({
                    severity: completed ? 'success' : 'info',
                    summary: completed ? 'Task Completed' : 'Task Marked Incomplete',
                    detail: completed ? `"${task}" has been marked as complete.` : `"${task}" has been marked as incomplete.`,
                    life: 3000
                });
            };
            const todos = ref([]);
            const toast = useToast();
            const search = ref('');
            const { proxy } = getCurrentInstance();
            const fetchTodos = async () => {
                try {
                    if(search.value && search.value.length > 3){
                        const response = await proxy.$api.get('/todos/search?q='+search.value, {
                            headers: {
                                Authorization: `Bearer ${localStorage.getItem('access_token')}`
                            }
                        });
                        todos.value = response.data;
                        console.log(todos.value);
                    }else {
                        toast.add({ severity: 'error', summary: 'Invalid Input', detail: 'Enter a valid search', life: 3000 });
                    }
                }
                catch(error){
                    console.error("Failed to fetch todos:", error);
                    toast.add({ severity: 'error', summary: 'Failed to Fetch', detail: 'Error Occured', life: 3000 });
                }
            };
            let debounceTimer;
            watch(search, () => {
                clearTimeout(debounceTimer);
                debounceTimer = setTimeout(() => {
                    if(search.value.length > 3) {
                        fetchTodos();
                    }else if(search.value.length === 0 || search.value.length < 3) {
                        todos.value = [];
                    }
                }, 400); // 400ms delay
            });
            onBeforeUnmount(() => {
                clearTimeout(debounceTimer);
            });
            return {
                fetchTodos,
                search,
                todos,
                showToast,
            }
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
    .search-icon {
        width: 1.7em;
        height: 1.7em;
        object-fit: cover;
        cursor: pointer;
        position: absolute;
        right: 15%;
        top: 30%;
    }
    main {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        width: 100vw;
        overflow-x: hidden;
        overflow-y: auto;
        scroll-behavior: smooth;
    }
    .empty-todo-gif {
        width: 20em;
        height: 20em;
        object-fit: cover;
        margin: 2em;
    }
    .none {
        font-size: 1.4em;
        font-weight: 500;
        color: grey;
    }
    .search-container {
        display: flex;
        align-items: center;
        justify-content: center;
        flex-direction: row;
        width: 100vw;
        height: 7vh;
        padding: 22px;
        margin-top: 2.3em;
        position: relative;
    }
    .empty-todo {
        display: flex;
        align-items: center;
        justify-content: center;
        flex-direction: column;
        width: 100vw;
        height: 80vh;
        overflow: hidden;
    }
    .card-container{
        display: flex;
        align-items: center;
        justify-content: center;
        flex-direction: column;
        width: 100vw;
        margin-top: 2.3em;
        overflow-x: hidden;
    }
    .search-input {
        width: 80vw;
        height: 5vh;
        border-radius: 50px;
        outline: none;
        border: 1px solid #000;
        font-size: 1.12em;
        padding: 1em;
        font-weight: 500;
    }
    .search-input:active {
        outline: none;
    }
    .search-input:focus {
        outline: none;
    }
    @media (min-width:768px) {
        .search-icon {
            right: 10em;
            width: 1.2em;
            height: 1.2em;
        }
        .card-container {
            margin-top: 1%;
        }
    }
</style>