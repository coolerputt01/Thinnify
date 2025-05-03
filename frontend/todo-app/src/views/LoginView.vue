<template>
    <section>
        <main>
            <Toast />
            <div class="form">
                <span class="form-head-container">
                    <h1 class="form-head">Login</h1>
                </span>
                <div class="input-group">
                    <input type="text" name="username" placeholder="Username" class="username" v-model="username" required>
                    <input type="password" name ="password" placeholder="Password" class="password" v-model="password" required>
                </div>
                <span class="info-container">
                    <p>Don't have an account?</p>
                    <RouterLink to="/signup">Signup</RouterLink>
                </span>
                <span class="button-container">
                    <button class="form-submit" @click="LogInUser">
                        <p v-if="!isLoading">Login</p>
                        <ProgressSpinner v-else style="width: 32px; height: 32px" :strokeWidth="8" fill="transparent" strokeColor="#fff"
    animationDuration=".5s" aria-label="Custom ProgressSpinner" />
                    </button>
                </span>
            </div>
        </main>
    </section>
</template>
<script>
    import { ref , getCurrentInstance} from 'vue';
    import { useRouter } from 'vue-router';
    import Toast from 'primevue/toast';
    import { useToast } from 'primevue/usetoast';
    import ProgressSpinner from 'primevue/progressspinner';
    export default {
        name:"LoginView",
        components:{
            Toast,
            ProgressSpinner,
        },
        setup(){
            let router = useRouter();
            const password = ref("");
            const username = ref("");
            const isLoading = ref(false);
            const toast = useToast();
            const user = ref("");
            const { proxy } = getCurrentInstance();
            const LogInUser = async () => {
                try{
                    isLoading.value = true;
                    const postRequest = await proxy.$api.post('/login',{username:username.value,password:password.value});
                    const { access_token, userName } = postRequest.data;
                    user.value = userName;
                    console.log(user.value)
                    localStorage.setItem("access_token", access_token);
                    localStorage.setItem("username", userName);
                    router.push({name:'home',params:{user : user.value}});
                }catch(error) {
                    toast.add({
                    severity: "error",
                    summary: "Login Failed",
                    detail: "Invalid username or password. Please try again.",
                    life: 3000
                });
                isLoading.value = false;
                console.error(error.message,"How far bro?");
                }
            }
            return {
                password,
                username,
                isLoading,
                LogInUser,
            }
        },
    }
</script>
<style scoped>
    * {
        margin: 0;
        padding: 0; 
        box-sizing: border-box;
        font-family: "Urbanist",sans-serif !important;
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
    .white{
        color: #fff !important;
        background-color: #fff !important;
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
    @media (max-width: 480px) {
        .form-head-container {
            margin: 2% !important;
        }
        .form {
            padding: 24px !important;
        }
        .form-submit {
            width: 50vw !important;
        }
        .input-group > * {
            width: 50vw !important;
            height: 4vh !important;
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