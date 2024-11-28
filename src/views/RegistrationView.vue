<template>
    <main>
        <section class="left-part">
            <div class="inner-container">
                <h1 class="h1">Регистрация</h1>
                <p class="mini-text">Уже есть аккаунт? <router-link :to="{name: 'login'}">Войти</router-link></p>
                <form v-if="formType == 'user'" class="form-container">
                    <label>
                        Фамилия
                        <input type="text">
                    </label>
                    <label>
                        Имя
                        <input type="text">
                    </label>
                    <label>
                        Отчество
                        <input type="text">
                    </label>
                    <label>
                        Почта
                        <input type="email">
                    </label>
                    <label>
                        Пароль
                        <input type="password">
                    </label>
                    <button type="button">Зарегистрироваться</button>
                </form>
                <form v-else-if="formType == 'organization'">
                    <label>
                        Имя организации
                        <input type="text">
                    </label>
                    <label>
                        Адрес организации
                        <input type="text">
                    </label>
                    <label>
                        Сайт организации
                        <input type="text">
                    </label>
                    <label>
                        Почта организации
                        <input type="email">
                    </label>
                    <label>
                        Пароль
                        <input type="password">
                    </label>
                    <button type="button">Зарегистрировать</button>
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

    const formType = ref('user');

    function changeFormType(newFormType) {
        formType.value = newFormType;
    }
</script>

<style scoped>
main {
    display: flex;
    height: 100vh;
}
.left-part {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    width: 50%;
    height: 100%;
    background-color: var(--colorWhite);
    padding: 30px;
}
.left-part > .inner-container {
    width: 100%;
    max-width: 500px;
}
.right-part {
    width: 50%;
    height: 100%;
    background-color: var(--colorGrey);
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
    transition: background-color .3s ease;
    cursor: pointer;
}
.selected-formType-btn {
    background-color: var(--colorBlueLight)!important;
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
}
input:focus {
    outline: none;
}
button {
    padding: 16px 28px;
    background-color: #000;
    border-radius: 200px;
    border: none;
    color: var(--colorWhite);
    cursor: pointer;
}
</style>