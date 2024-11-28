<template>
    <main>
        <section class='left-part'>
            <h1 class="h1">Войти в аккаунт</h1>
            <p class="mini-text">Уже есть аккаунт? <router-link to="/account/registration">Зарегистрироваться</router-link></p>
        </section>
        <section class='right-part'>
            <img src="@/assets/images/fone.svg" alt="">
        </section>
    </main>
</template>

<script setup>

</script>

<style scoped>
main {
    display: flex;
}
.left-part {
    width: 50%;
    height: 100%;
    background-color: var(--colorWhite);
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
</style>