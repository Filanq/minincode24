<template>
    <HeaderComponent :relative="header_relative" class="mb-25"/>

    <RouterView />
</template>

<script setup lang="ts">
    import HeaderComponent from "@/components/HeaderComponent.vue";
    import { RouterView } from 'vue-router';
    import type {Ref} from "vue";
    import {ref} from "vue";

    // Is Header Relative
    const header_relative: Ref<boolean> = ref(true);
</script>