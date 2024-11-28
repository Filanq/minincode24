<template>
    <h1>Личный кабинет орг, Мероприятия</h1>
    <HeaderComponent :buttons="buttons" />
    <div></div>
</template>

<script setup>
    import HeaderComponent from "@/components/HeaderComponent.vue";

    const buttons = [
        {
            title: 'Основная информация',
            view: 'org_account_data_settings',
        },
        {
            title: 'Мероприятия организации',
            view: 'org_account_events',
        },
        {
            title: 'Новости организации',
            view: 'org_account_news',
        },
        {
            title: 'Гости мероприятия',
            view: 'org_account_guests',
        },
    ];
</script>

<style scoped>

</style>