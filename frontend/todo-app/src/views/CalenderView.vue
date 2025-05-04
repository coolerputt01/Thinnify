<template>
    <section>
        <main>
            <Toast />
            <!--Note that my Card here make use of emit events to rendet dynamic data which in this case is the data ised in the Toast.-->
            <DateTodoCard category-name="Personal" :todos="personalTodos" @todo-status-updated="showToast"/>
            <DateTodoCard category-name="Productivity" :todos="productivityTodos" @todo-status-updated="showToast"/>
            <DateTodoCard category-name="Fitness" :todos="fitnessTodos" @todo-status-updated="showToast"/>
            <DateTodoCard category-name="Work" :todos="workTodos" @todo-status-updated="showToast"/>
            <DateTodoCard category-name="Default" :todos="defaultTodos" @todo-status-updated="showToast"/>
            <NavBar />
        </main>
    </section>
</template>
<script>
import { ref, onMounted, computed, getCurrentInstance } from 'vue';
import Toast from 'primevue/toast';
import DateTodoCard from '@/components/DateTodoCard.vue';
import NavBar from '@/components/NavBar.vue';
import { useToast } from 'primevue/usetoast';

export default {
    name: 'CalenderView',
    props: ['user'],
    components: {
        DateTodoCard,
        NavBar,
        Toast
    },
    setup() {
        //I plan to pass an array of data as a prop into my compoenent.
        const dataArray = ref([]);
        const toast = useToast();
        const { proxy } = getCurrentInstance();
        const showToast = ({ task, completed }) => {
            toast.add({
                severity: completed ? 'success' : 'info',
                summary: completed ? 'Task Completed' : 'Task Marked Incomplete',
                detail: completed ? `"${task}" has been marked as complete.` : `"${task}" has been marked as incomplete.`,
                life: 3000
            });
        };
        const fetchTodos = async () => {
            try {
                const response = await proxy.$api.get('/todos', {
                    headers: {
                        Authorization: `Bearer ${localStorage.getItem('access_token')}`
                    }
                });
                dataArray.value = response.data;
            } catch (error) {
                console.error("Failed to fetch todos:", error);
            }
        };

        //Split arrays by category
        const personalTodos = computed(() => dataArray.value.filter(todo => todo.category === 'Personal'));
        const productivityTodos = computed(() => dataArray.value.filter(todo => todo.category === 'Productivity'));
        const fitnessTodos = computed(() => dataArray.value.filter(todo => todo.category === 'Fitness'));
        const workTodos = computed(() => dataArray.value.filter(todo => todo.category === 'Work'));
        const defaultTodos = computed(() => dataArray.value.filter(todo => !['Personal', 'Productivity', 'Fitness', 'Work'].includes(todo.category)));

        onMounted(fetchTodos);

        return {
            personalTodos,
            productivityTodos,
            fitnessTodos,
            workTodos,
            defaultTodos,
            showToast,
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
    main {
        overflow-x: hidden;
        width: 100vw;
        margin-bottom: 2em;
        background-image: linear-gradient(100deg,rgba(211, 211, 211, 0.185),white ,white,white);
    }
    section {
        overflow: hidden;
    }
</style>