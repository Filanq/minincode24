<template>
    <div class="section header__section">
        <div class="container">
            <nav class="grid grid-column gap-10">
                <router-link :to="{name: 'home'}" class="link header_link">MininCode</router-link>
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
    }

    .header_link{
        font-size: 22px;
    }

    
</style>
