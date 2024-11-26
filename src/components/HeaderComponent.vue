<template>
    <header>
        <router-link :to="{name: 'home'}">home</router-link>
        <router-link :to="{name: 'home'}">about</router-link>
    </header>
</template>

<script setup lang="ts">
    import { RouterLink } from 'vue-router'
</script>

<style scoped>
    header{
        line-height: 1.5;
        max-height: 100vh;
    }
</style>
