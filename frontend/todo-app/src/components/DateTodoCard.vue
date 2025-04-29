<template>
    <div class="todo-card">
        <div class="date-container">
            <p></p>
            <div class="card-groups">
                
            </div>
        </div>
    </div>
</template>
<script>
    export default {
        name: 'DateTodoCard',
        props: ['user'],
    }
</script>
<style scoped>
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
        font-family: "Urbanist", sans-serif;
    }
</style>