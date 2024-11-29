<template>
    <div v-if="$route.name !== 'login' && $route.name !== 'registration'" class="section header__section">
        <div class="container header__container grid grid-column ac-sb">
            <div class="grid grid-column gap-75">
                <span class="logo">MininCode</span>
                <nav class="grid grid-column gap-25 ac-s">
                    <!-- заменить name -->
                    <router-link v-for="button in buttons" :to="{name: button.view}" class="link header_link">{{ button.title }}</router-link>
                </nav>
            </div>
            <div class="grid grid-column gap-10 ac-s ji-c">
                <div class="grid grid-column gap-10">
                    <router-link :to="{name: 'home'}" class="link header_link">← Главная</router-link>
                </div>
                <!-- TODO: ДЛЯ beckend -->
                 <a href="#" @click.prevent="()=>{user.logout(); $router.push('/');}" class="link header_link header_link--red">Выйти</a>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
    import { RouterLink } from 'vue-router';
    import {useUserStore} from "@/stores/user";

    defineProps({
        buttons: {
            type: Array,
            required: true,
        },
    });

    let user = useUserStore();
</script>

<style scoped>
    .header__section{
        height: 100vh;
        background-color: var(--colorBlueMain);
        display: flex;
        position: fixed;
        left: 0;
        top: 0;
        z-index: 9;
        width: 300px;
        padding: 40px 0;
    }

    .header__container{
        padding: 0 20px;
    }

    .header__container > div:first-child > nav {
        gap: 20px;
    }

    .header_link{
        font-size: 18px;
        color: var(--colorWhite);
        border-radius: 15px;
        padding: 10px 20px;
    }

    .logo{
        font-size: 28px;
        font-weight: 700;
        text-align: center;
    }

    .header_link--red{
        color: #ea827b;
        font-weight: 700;
    }

    .header_link--blue{
        color: var(--colorWhite);
    }

    .router-link-exact-active {
        background-color: var(--colorBlueLight);
        color: #000;
    }
</style>
