<template>
    <header :class="{'header_relative': relative}" class="grid grid-row gap-10 jc-s ai-c">
        <router-link :to="{name: 'home'}">home</router-link>
        <router-link :to="{name: 'about'}">about</router-link>
    </header>
</template>

<script setup lang="ts">
    import { RouterLink } from 'vue-router';

    // Set Props
    const props = defineProps(['relative']);
</script>

<style scoped>
    header{
        max-height: 100vh;
    }
</style>
