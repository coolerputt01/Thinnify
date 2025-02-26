<template>
  <div class="categorized-card">
    <div class="card-task-no">
      <p class="card-task-no-value">{{ taskNo }} tasks</p>
    </div>
    <div class="card-task-category">
      <p class="card-task-category-value">{{ taskCategory }}</p>
    </div>
    <div class="progress-bar">
        <div class="progress-value"></div>
    </div>
  </div>
</template>

<script>
export default {
  name: "CategorizedCard",
  props: {
    taskCategory: {
        type:String,
        required:true
    },
    taskNo: {
        type:Number,
        required:true
        },
    progressValue: {
        type:Number,
        required:true,
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
.progress-bar{
    position: absolute;
    bottom: 1%;
    background: lightgrey;
    width: 100%;
    height: 3px !important;
}
.progress-value{
    width:50%;
    height: 100%;
    background: blue;
}
.card-task-category-value {
    font-size: 1.5em;
    font-weight: bolder;
    color: #000;
}
.card-task-no-value {
    font-size: 0,9em;
    color:grey;
}
.categorized-card {
    position:relative;
    width:50vw;
    height:18vh;
    background-color:#f9f9f9;
    border-radius: 28px;
    display:flex;
    justify-content:space-between;
    align-items:center;
    padding: 1.3em;
    margin: 1em;
    flex-direction:column;
    flex: 0 0 auto;
    scroll-snap-align: center;
    overflow:hidden;
    transition: all 0.3s;
}
.categorized-card:hover{
    transform:scale(1.05);
    box-shadow: 5px 3px 32px 5px rgba(0,0,0,0.05);
    .progress-value{
        box-shadow: 0 0 15px blue;
    }
}
.categorized-card > div{
    width:100%;
    height:50%;
}
</style>