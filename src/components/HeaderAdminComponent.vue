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
            <div class="grid grid-column gap-10">
                <router-link :to="{name: 'home'}" class="link header_link">← Главная</router-link>
            </div>
            <!-- TODO: ДЛЯ beckend -->
            <!-- <div class="link header_link header_link--red">Выйти</div> -->
        </div>
    </div>
</template>

<script setup lang="ts">
    import { RouterLink } from 'vue-router';

    defineProps({
        buttons: {
            type: Array,
            required: true,
        },
    });
</script>

<style scoped>
    .header__section{
        height: 100vh;
        background-color: white;
        display: flex;
        position: fixed;
        left: 0;
        top: 0;
        z-index: 9;
        width: 300px;
        padding: 40px 0;
    }

    .header__container{
        padding: 0 60px;
    }

    .header_link{
        font-size: 18px;
    }

    .logo{
        font-size: 28px;
        font-weight: 700;
    }

    .header_link--red{
        color: rgb(255, 18, 0);
    }

    .header_link--blue{
        color: var(--colorBlueMain);
    }

    
</style>
