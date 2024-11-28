<template>
    <div class="main-app_grid">
        <HeaderComponent v-if="true" :relative="header_relative" class="mb-25"/>
        <RouterView />
    </div>
    
</template>

<script setup lang="ts">
    import HeaderComponent from "@/components/HeaderComponent.vue";
    import { RouterView } from 'vue-router';
    import type {Ref} from "vue";
    import {ref} from "vue";

    // Is Header Relative
    const header_relative: Ref<boolean> = ref(true);

    // Define Emits
    const emits = defineEmits(['authorize_or_registrze_modal']);
</script>

<style scoped>
    .main-app_grid{
        display: grid;
        grid-template-columns: auto 1fr;
        position: relative;
    }
</style>