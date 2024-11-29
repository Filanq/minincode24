<template>
    <div class="darker" @click="changeCondCreateModal"></div>
    <form class="form-container" @submit.prevent="create()">
        <label>
            Название
            <input type="text" v-model="title">
        </label>
        <label>
            Дата
            <input type="datetime-local" v-model="datetime">
        </label>
        <label>
            Адрес
            <input type="text" v-model="address">
        </label>
        <label>
            Максимум человек
            <input type="number" v-model="count">
        </label>
        <label>
            Текст
            <textarea v-model="text" style="resize: vertical; max-height: 300px; min-height: 100px;"></textarea>
        </label>
        <label>
            Обложка
            <input id="img" type="file">
        </label>
        <button type="submit">Создать</button>
        <span v-show="is_successfuly" class="green_text">Создано</span>
    </form>
</template>

<script setup>
    import {ref} from "vue";
    import axios from "axios";
    import {useUserStore} from "@/stores/user";

    const props = defineProps({
        changeCondCreateModal: {
            type: Function,
        }
    });

    let is_successfuly = ref(false);
    let title = ref('');
    let text = ref('');
    let address = ref('');
    let datetime = ref('');
    let img = ref('')
    let count = ref(0);

    let user = useUserStore();

    const emits = defineEmits(['close']);

    const create = () => {
        let img_f = document.getElementById('img').files[0] ?? null;
        axios.post(window.origin + '/api/events/', {
            title: title.value,
            text: text.value,
            datetime: datetime.value,
            address: address.value,
            img: img_f,
            count: count.value,
            organization: Number(user.id)
        }, {headers: {"Content-Type": 'multipart/form-data', "X-CSRFToken": user.getCookie('csrftoken')}}).then(res => {
            emits('close');
        });
    };
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