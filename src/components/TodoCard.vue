<template>
  <div class="todo-app-card">
    <label>
      <input type="checkbox" id="circularCheckbox" v-model="isChecked">
      <span class="custom-checkbox" :style="checkboxStyle"></span>
    </label>
    <div class="todo-text" :class="{ completed: isChecked }">{{ todoText }}</div>
  </div>
</template>

<script>
export default {
  name: "TodoCard",
  props: {
    category: {
      type: String,
      required: true, // Must pass "work", "personal", "home", "goals", etc.
    },
    todoText: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      isChecked: false, // Checkbox state
      categoryColors: {
        productivity: "green",  // Red
        personal: "blue", // Blue
        home: "purple", // Green
        goals: "red", // Orange
        others: "gray", // Purple
      },
    };
  },
  computed: {
    checkboxStyle() {
      const color = this.categoryColors[this.category] || "#576574";
       // Default gray if category not found
      return {
        backgroundColor: this.isChecked ? color : "transparent",
        borderColor: color,
      };
    },
  },
};
</script>

<style scoped>
* {
  font-family: "Urbanist", sans-serif !important;
  box-sizing: border-box;
  padding: 0;
  margin: 0;
}
/* Hide default checkbox */
input[type="checkbox"] {
  display: none;
}
.completed {
  text-decoration: line-through;
  color: gray;
}
.custom-checkbox {
  display: inline-block;
  width: 24px;
  height: 24px;
  border-radius: 50%;
  position: relative;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow:5px 5px 15px -3px rgba(0,0,0,0.15);
  border: 2px solid #333; 
}

.todo-app-card {
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 3em;
  align-items: center;
  flex-direction: row;
  padding: 1em;
  background-color:#fff;
  border-radius: 20px;
  border-bottom: 1px solid #e9ecef;
  width: 100%;
  height: 7vh;
  -webkit-box-shadow: 5px 5px 15px -3px rgba(0,0,0,0.15); 
  box-shadow: 5px 5px 15px -3px rgba(0,0,0,0.15);
  margin: 1em;
  flex: 0 0 auto;
  transition: all 0.3s;
}
.todo-app-card:hover{
    transform:scale(1.05);
    box-shadow: 5px 3px 32px 5px rgba(0,0,0,0.1);
    .progress-value{
        box-shadow: 0 0 15px blue;
    }
}
.todo-text{
    font-size: 1.1em;
    font-weight: bolder;
}
</style>
