<template>
    <h1>Личный кабинет, Name</h1>
    <HeaderComponent :buttons="buttons" />
    <div></div>
</template>

<script setup>
    import HeaderComponent from "@/components/HeaderComponent.vue";

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