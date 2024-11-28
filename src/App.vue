<template>
    <div class="main-app_grid">
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

</style>