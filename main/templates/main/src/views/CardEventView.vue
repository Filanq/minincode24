<template>
    <header-component></header-component>

    <div class="section news-card__section">
        <div class="container">
            <div class="card__wrap grid gap-50">
                <div class="card__block">
                    <img :src="event.img" alt="img">
                    <div class="grid grid-row jc-sb ai-c">
                        <span>{{ event.title }}</span>
                        <span>{{ event.datetime }}</span>
                        <span>{{ event.date }}</span>
                    </div>
                </div>
                <p>{{ event.text }}</p>
                    <div v-if="user.type !== ''" @click="write()" class="add-btn">
                        Записаться
                    </div>

                <p class="w-700 h6">{{ event.address }}</p>
            </div>
        </div>
    </div>
</template>

<script setup>
    import HeaderComponent from '@/components/HeaderComponent.vue';
    import {useRoute} from "vue-router";
    import {ref} from "vue";
    import axios from "axios";
    import {useUserStore} from "@/stores/user";

    let user = useUserStore();

    let event = ref({});
    axios.get(window.origin + '/api/events/' + useRoute().params.id).then(res => {
        event.value = res.data;
    });

    const write = () => {
        axios.post(window.origin + '/api/events-req/', {
            user: Number(user.id),
            event: Number(event.value.id)
        }, {headers: {"X-CSRFToken": user.getCookie('csrftoken')}}).then(()=>{
            document.querySelector('.add-btn').textContent = 'Вы успешно записались!';
        });
    }
</script>

<style scoped>
.news-card__section{
    padding-top: 150px;
}
    .add-btn {
        display: flex;
        align-items: center;
        gap: 7px;
        border-radius: 50px;
        padding: 10px 16px;
        background-color: var(--colorBlueLight);
        color: #000;
        cursor: pointer;
    }
    .card__wrap{
        grid-template-columns: 4fr 5fr;
    }

    .card__block{
        width: 100%;
    }
    
    .card__block > img{
        width: 100%;
        border-radius: 20px;
        object-fit: cover;
        object-position: center;
    }

    @media(max-width: 768px){
        .card__wrap{
            grid-template-columns: 1fr;
        }
    }
</style>