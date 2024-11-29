<template>
    <main>
        <section class="left-part">
            <div class="inner-container">
                <h2 class="h3">Вход</h2>
                <p class="mini-text">Еще нет аккаунта? <router-link :to="{name: 'registration'}">Регистрация</router-link></p>
                <form class="form-container">
                    <label>
                        Почта
                        <input type="email">
                    </label>
                    <label>
                        Пароль
                        <input type="password">
                    </label>
                    <button type="button">Войти</button>
                </form>
            </div>
        </section>
        <section class="right-part">
            <img src="@/assets/images/fone.png" alt="">
        </section>
    </main>
</template>

<script setup>

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
    max-width: 600px;
    height: 100%;
    background-color: var(--colorGrey);
    padding: 30px;
}
.left-part > .inner-container {
    width: 100%;
    max-width: 500px;
}
.right-part {
    flex-grow: 1;
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