<template>
    <HeaderComponent/>
    <div class="section banner__section grid jc-c ac-c" >
        <div class="container grid jc-c">
            <h1 class="h1">MININCODE</h1>
            <!-- <img class="banner_img" src="#" alt="img"> -->
        </div>
    </div>

    <MarqueComponent/>
</template>

<script setup>
    import MarqueComponent from '@/components/MarqueComponent.vue';
    import HeaderComponent from '@/components/HeaderComponent.vue';
</script>

<style scoped>
    .banner__section{
        width: 100vw;
        height: 100vh;
        position: relative;
        z-index: 0;
    }

    
</style>