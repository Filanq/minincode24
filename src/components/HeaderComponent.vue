<template>
    <div class="section header__section">
        <div class="container header__container grid grid-column gap-75">
            <span class="logo">MininCode</span>
            <nav class="grid grid-column gap-10 ac-s">
                <!-- заменить name -->
                <router-link :to="{name: 'home'}" class="link header_link">Главная</router-link>
                <router-link :to="{name: 'home'}" class="link header_link">Личный кабинет</router-link>
                <router-link :to="{name: 'home'}" class="link header_link">Организации</router-link>
                <router-link :to="{name: 'home'}" class="link header_link">Мероприятия</router-link>
                <router-link :to="{name: 'home'}" class="link header_link">Новости</router-link>
            </nav>
        </div>
    </div>
</template>

<script setup lang="ts">
    import { RouterLink } from 'vue-router';

    // Set Props
    const props = defineProps(['relative']);
</script>

<style scoped>
    .header__section{
        height: 100vh;
        background-color: white;
        display: flex;
        padding: 40px 0;
    }

    .header__container{
        padding: 0 60px;
    }

    .header_link{
        font-size: 20px;
    }

    .logo{
        font-size: 28px;
        
    }

    
</style>
