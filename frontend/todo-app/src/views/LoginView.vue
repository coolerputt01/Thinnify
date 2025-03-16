<template>
    <div class="create-view">
        <h1>Create a New Todo</h1>
        <form @submit.prevent="createTodo">
            <div>
                <label for="title">Title:</label>
                <input type="text" v-model="title" id="title" required />
            </div>
            <div>
                <label for="description">Description:</label>
                <textarea v-model="description" id="description" required></textarea>
            </div>
            <button type="submit">Create</button>
        </form>
    </div>
</template>

<script>
export default {
    data() {
        return {
            title: '',
            description: ''
        };
    },
    methods: {
        createTodo() {
            // Logic to create a new todo
            console.log('Todo created:', this.title, this.description);
            // Reset form fields
            this.title = '';
            this.description = '';
        }
    }
};
</script>

<style scoped>
.create-view {
    max-width: 600px;
    margin: 0 auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 4px;
}
.create-view h1 {
    margin-bottom: 20px;
}
.create-view form div {
    margin-bottom: 10px;
}
.create-view form label {
    display: block;
    margin-bottom: 5px;
}
.create-view form input,
.create-view form textarea {
    width: 100%;
    padding: 8px;
    box-sizing: border-box;
}
.create-view form button {
    padding: 10px 15px;
    background-color: #28a745;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}
.create-view form button:hover {
    background-color: #218838;
}
</style>