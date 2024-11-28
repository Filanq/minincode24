<template>
    <h1>Личный кабинет, Мероприятия</h1>
    <HeaderAdminComponent :buttons="buttons" />
    <div></div>
</template>

<script setup>
    import HeaderAdminComponent from "@/components/HeaderAdminComponent.vue";

    const buttons = [
        {
            title: 'ФИО',
            view: 'name_settings',
        },
        {
            title: 'Мои мероприятия',
            view: 'events_list',
        },
    ];
</script>

<style scoped>

</style>