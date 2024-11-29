<template>
    <div class="darker" @click="changeCondCreateModal"></div>
    <form class="form-container">
        <label>
            Название
            <input type="text">
        </label>
        <label>
            Дата
            <input type="date">
        </label>
        <label>
            Текст
            <textarea style="resize: vertical; max-height: 300px; min-height: 100px;"></textarea>
        </label>
        <label>
            Обложка
            <input type="file">
        </label>
        <button type="button">Создать</button>
        <span class="green_text hide_green_text">Создано</span>
    </form>
</template>

<script setup>
    const props = defineProps({
        changeCondCreateModal: {
            type: Function,
        }
    });
</script>

<style scoped>
    .darker {
        position: fixed;
        inset: 0;
        background-color: #00000080;
        width: 100%;
        height: 100%;
        z-index: 9;
    }
    form {
        position: fixed;
        inset: 50% auto auto 50%;
        transform: translate(-50%, -50%);
        display: flex;
        flex-direction: column;
        gap: 15px;
        margin: 15px 0;
        background-color: var(--colorGrey);
        padding: 20px;
        border-radius: 20px;
        z-index: 10;
    }
    label {
        display: flex;
        flex-direction: column;
        gap: 8px;
        font-weight: 300;
        font-size: 14px;
    }
    input, textarea {
        border-radius: 10px;
        border: solid #000 1px;
        padding: 10px;
        background-color: #FFFFFF15;
        color: var(--colorWhite);
    }
    input:focus,
    textarea:focus {
        outline: none;
    }
    button {
        padding: 16px 28px;
        background-color: var(--colorBlueLight);
        border-radius: 200px;
        border: none;
        color: #000;
        cursor: pointer;
    }
    .green_text {
        color: green;
    }
    .hide_green_text {
        display: none;
    }
</style>