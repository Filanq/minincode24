<template>
    <HeaderAdminComponent :buttons="buttons" />
    
</template>

<script setup>
    import HeaderAdminComponent from "@/components/HeaderAdminComponent.vue";

    const buttons = [
        {
            title: 'Заявки организаций',
            view: 'organizations_requests',
        }
    ];
</script>

<style scoped>

</style>