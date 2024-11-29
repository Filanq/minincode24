<template>
    <HeaderComponent />
    <main>
        <section class="left-part">
            <div class="inner-container">
                <h1 class="h3">Регистрация</h1>
                <p class="mini-text">Уже есть аккаунт? <router-link :to="{name: 'login'}" class="link">Войти</router-link></p>
                <form @submit.prevent="register" v-if="formType == 'user'" class="form-container">
                    <label>
                        Фамилия
                        <input type="text" v-model="surname">
                    </label>
                    <label>
                        Имя
                        <input type="text" v-model="firstname">
                    </label>
                    <label>
                        Отчество
                        <input type="text" v-model="lastname">
                    </label>
                    <label>
                        Почта
                        <input type="email" v-model="email">
                    </label>
                    <label>
                        Пароль
                        <input type="password" v-model="password">
                    </label>
                    <span style="color: red" v-show="error">{{ error }}</span>
                    <button type="submit">Зарегистрироваться</button>
                </form>
                <form @submit.prevent="register" v-else-if="formType === 'organization'">
                    <label>
                        Имя организации
                        <input type="text" v-model="name">
                    </label>
                    <label>
                        Адрес организации (г.&nbsp;... ул.&nbsp;...)
                        <input type="text" v-model="address">
                    </label>
                    <label>
                        Сайт организации
                        <input type="text" v-model="website">
                    </label>
                    <label>
                        Почта организации
                        <input type="email" v-model="email2">
                    </label>
                    <label>
                        Пароль
                        <input type="password" v-model="password2">
                    </label>
                    <span style="color: red" v-show="error2">{{ error2 }}</span>
                    <button type="submit">Зарегистрировать</button>
                </form>
                <div class="select-formType-container">
                    <div @click="changeFormType('user')" :class="{'selected-formType-btn': formType == 'user'}" class="ta-c">Гость</div>
                    <div @click="changeFormType('organization')" :class="{'selected-formType-btn': formType == 'organization'}" class="ta-c">Организация</div>
                </div>
            </div>
        </section>
        <section class="right-part">
            <img src="@/assets/images/fone.png" alt="">
        </section>
    </main>
</template>

<script setup>
    import {ref} from "vue";
    import axios from "axios";
    import {useRouter} from "vue-router";
    import {useUserStore} from "@/stores/user";
    import HeaderComponent from "@/components/HeaderComponent.vue";

    const formType = ref('user');

    function changeFormType(newFormType) {
        formType.value = newFormType;
    }

    let firstname = ref('');
    let surname = ref('');
    let lastname = ref('');
    let name = ref('');
    let website = ref('');
    let address = ref('');
    let email = ref('');
    let email2 = ref('');
    let password = ref('');
    let password2 = ref('');
    let error = ref('');
    let error2 = ref('');

    const register = () => {
        if(formType.value === 'user'){
            axios.post(window.origin + '/api/register', {
                firstname: firstname.value,
                surname: surname.value,
                lastname: lastname.value,
                name: name.value,
                website: website.value,
                address: address.value,
                email: email.value,
                password: password.value,
                type: formType.value
            }, {headers: {"X-CSRFToken": useUserStore().getCookie('csrftoken')}}).then(res => {
                if(res.data['result']){
                    window.location.href = '/';
                    error.value = '';
                }
                else{
                    error.value = res.data['error'];
                }
            });
        }
        else{
            axios.post(window.origin + '/api/register', {
                firstname: firstname.value,
                surname: surname.value,
                lastname: lastname.value,
                name: name.value,
                website: website.value,
                address: address.value,
                email: email2.value,
                password: password2.value,
                type: formType.value
            }, {headers: {"X-CSRFToken": useUserStore().getCookie('csrftoken')}}).then(res => {
                if(res.data['result']){
                    alert("В скором времени вашу заявку на регистрацию рассмотрят");
                    error2.value = '';
                }
                else{
                    error2.value = res.data['error'];
                }
            });
        }
    };
</script>

<style scoped>
main {
    display: flex;
    width: 100%;
    height: 100vh;
}
.left-part {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    width: 50%;
    height: 100%;
    background-color: var(--colorGrey);
    padding: 30px;
}
.left-part > .inner-container {
    width: 100%;
    max-width: 500px;
}
.right-part {
    width: 50%;
    height: 100%;
    background-color: var(--colorWhite);
}
.right-part > img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}
.left-part .mini-text {
    font-weight: 300;
    margin: 10px 0;
}
.left-part .mini-text > a {
    font-weight: 500;
    color: var(--colorBlueLight);
}
.select-formType-container {
    display: flex;
    gap: 3px;
    margin-top: 20px;
    border: solid #000 1px;
    border-radius: 10px;
    padding: 3px;
}
.select-formType-container > div {
    width: calc((100% - 3px) / 2);
    padding: 10px;
    border-radius: 7px;
    background-color: var(--colorGrey);
    transition: all .3s ease;
    cursor: pointer;
}
.selected-formType-btn {
    background-color: var(--colorBlueLight)!important;
    color: #000;
}
form {
    display: flex;
    flex-direction: column;
    gap: 15px;
    margin: 15px 0;
}
label {
    display: flex;
    flex-direction: column;
    gap: 8px;
    font-weight: 300;
    font-size: 14px;
}
input {
    border-radius: 10px;
    border: solid #000 1px;
    padding: 10px;
    background-color: #FFFFFF10;
    color: var(--colorWhite);
}
input:focus {
    outline: none;
}
button {
    padding: 16px 28px;
    background-color: var(--colorBlueLight);
    border-radius: 200px;
    border: none;
    color: #000;
    cursor: pointer;
}
</style>