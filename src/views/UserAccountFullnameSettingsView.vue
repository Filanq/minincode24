<template>
    <HeaderAdminComponent :buttons="buttons" />
    <div class="container-with-header">
        <HelloAccountComponent :name="'Тайно дернул'" />
        <div class="inner-container">
            <h3 class="h3">Редактирование ФИО</h3>
            <form class="form-container">
                <label>
                    Фамилия
                    <input type="text">
                </label>
                <label>
                    Имя
                    <input type="text">
                </label>
                <label>
                    Отчество
                    <input type="text">
                </label>
                <button type="button">Сохранить</button>
                <span class="green_text hide_green_text">Сохранено</span>
            </form>
        </div>
    </div>
</template>

<script setup>
    import HeaderAdminComponent from "@/components/HeaderAdminComponent.vue";
    import HelloAccountComponent from "@/components/HelloAccountComponent.vue";

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
    .container-with-header {
        width: calc(100% - 300px);
        margin-left: 300px;
        padding: 30px;
    }
    .inner-container {
        width: 100%;
        max-width: 500px;
    }
    form {
        display: flex;
        flex-direction: column;
        gap: 15px;
        margin: 15px 0;
    }
    label {
        display: flex;
        flex-direction: column;
        gap: 8px;
        font-weight: 300;
        font-size: 14px;
    }
    input {
        border-radius: 10px;
        border: solid #000 1px;
        padding: 10px;
    }
    input:focus {
        outline: none;
    }
    button {
        padding: 16px 28px;
        background-color: #000;
        border-radius: 200px;
        border: none;
        color: var(--colorWhite);
        cursor: pointer;
    }
    .green_text {
        color: green;
    }
    .hide_green_text {
        display: none;
    }
</style>