<template>
    <HeaderComponent :buttons="buttons" />
    Заявки
</template>

<script setup>
    import HeaderComponent from "@/components/HeaderComponent.vue";

    const buttons = [
        {
            title: 'Заявки организаций',
            view: 'organizations_requests',
        }
    ];
</script>

<style scoped>

</style>