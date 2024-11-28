<template>
    
</template>

<script setup lang="ts">
    import { RouterLink } from 'vue-router';
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
