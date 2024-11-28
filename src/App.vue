<template>
    <div :class="{'main-app_grid': $route.name !== 'login' && $route.name !== 'registration'}">
        <HeaderComponent 
            :relative="header_relative"
            />
        <RouterView/>
    </div>
    
</template>

<script setup lang="ts">
    import HeaderComponent from "@/components/HeaderComponent.vue";
    import { RouterView  } from 'vue-router';
    import type {Ref} from "vue";
    import {ref} from "vue";

    // Is Header Relative   
    const header_relative: Ref<boolean> = ref(true);

</script>

<style scoped>
    .main-app_grid{
        display: grid;
        grid-template-columns: auto 1fr;
        position: relative;
        margin-left: 300px;
    }
</style>