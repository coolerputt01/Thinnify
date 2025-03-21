<template>
    <!--Using Containers is a very good code practice and I had to use span and other semantic tags because of SEO.-->
    <section>
        <main>
            <!--I found out you can declare components like this.-->
            <ErrorCard ></ErrorCard>
            <div class="form">
                <span class="form-head-container">
                    <h1 class="form-head">SignUp</h1>
                </span>
                <div class="input-group">
                    <input type="text" name="username" placeholder="Username" class="username" v-model="username" required>
                    <input type="password" name ="password" placeholder="Password" class="password" v-model="password" required>
                    <input type="password" name ="cpassword" placeholder="Confirm Password" class="cpassword" v-model="cpassword" required>
                </div>
                <span class="info-container">
                    <p>Already have an account?</p>
                    <!--This is how you use the router component in Vue 3. Btw I used this inplace of <a @click="this.$router.push('/')"> Login </a>-->
                    <RouterLink to="/">Login</RouterLink>
                </span>
                <span class="button-container">
                    <button class="form-submit" @click="signUpUser">Sign Up</button>
                </span>
            </div>
        </main>
    </section>
</template>
<!--I used Options API before then because i had to use the provide/inject API from Vue whivh are basically Compostion API tools I had to switch.-->
<script>
    import { ref ,provide} from 'vue';
    //I guess I never knew you could import Router component until now.Before I always used this.$router.push('/route').
    import { useRouter } from 'vue-router';
    import axios from 'axios';
    import ErrorCard from '../components/ErrorCard.vue';
    export default {
        name:"SignupView",
        components:{
            ErrorCard,
        },
        setup(){
            let router = useRouter();
            const password = ref("");
            const cpassword = ref("");
            const username = ref("");
            const errorOccured = ref(false)
            const signUpUser = async () => {
                try{
                    if(!(password.value.length > 6 && password.value ===cpassword.value)){
                        errorOccured.value = true;
                        return
                    }
                    const postRequest = axios.post('http://127.0.0.1:5000/register',{username:username.value,password:password.value});
                    console.log(postRequest);
                    router.push('/');
                }catch(error) {
                    errorOccured.value = true;
                    console.error(error.message);
                }
            }
            provide("errorOccured",errorOccured);
            return {
                password,
                cpassword,
                username,
                errorOccured,
                signUpUser,
            }
        },
    }
</script>
<!--I didn't do much stuff for the styles, but basically the design for the page is really an inspiration from uiverse.io-->
<style scoped>
    * {
        margin: 0;
        padding: 0; 
        box-sizing: border-box;
        font-family: "Urbanist",sans-serif;
    }
    main {
        display: flex;
        align-items: center;
        justify-content: center;
        flex-direction: column;
        overflow: hidden;
        height: 100vh !important;
        width: 100vw !important;
        background-color: #adacac;
    }
    section {
        overflow: hidden;
    }
    .form {
        display: flex;
        align-items: center;
        justify-content: center;
        flex-direction: column;
        column-gap: 50px;
        flex-wrap: wrap;
        overflow: hidden;
        background-color: #fff;
        max-width: 88vw;
        border-radius: 3%;
        padding: 30px;
        flex-shrink: 0;
    }
    .form-head-container {
        width: 95% !important;
        text-align: left;
        margin: 5%;
    }
    .input-group {
        display: flex;
        align-items: center;
        justify-content: center;
        flex-direction: column;
    }
    .input-group > * {
        width: 40vw;
        height: 5vh;
        outline: none;
        border: none;
        background-color: #cccccc;
        margin: 5%;
        border-radius: 50px;
        padding: 8px;
        flex-shrink: 0;
    }
    @media (min-width:1024px) {
        .form-head-container {
            margin: 2% !important;
        }
        .form {
            padding: 24px !important;
        }
        .form-submit {
            width: 25vw !important;
        }
        .input-group > * {
            width: 25vw !important;
            height: 5vh !important;
        }
    }
    .input-group > input:focus {
        outline: none;
        border: none;
    }
    .info-container {
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 3%;
        width: 100%;
    }
    .info-container > * {
        font-size:0.9em;
    }
    .button-container {
        margin: 3%;
        display: flex;
        overflow: hidden;
        background-clip: cover;
    }
    .form-submit {
        outline: none;
        border: none;
        background-color: #ff5d2b;
        color: #fff !important;
        font-size: 1em;
        width: 50vw ;
        padding: 8px;
        border-radius: 50px;
        cursor: pointer;
        transition: all 250ms;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 10%;
    }
    .form-submit:hover {
        opacity: 0.8;
    }
</style>