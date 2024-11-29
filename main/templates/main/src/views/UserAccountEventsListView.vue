<template>
    <HeaderAdminComponent :buttons="buttons" />
    <div class="container-with-header">
        <HelloAccountComponent :name="user_name" />
        <div class="inner-container">
            <h3 class="h5">Ваши мероприятия</h3>
            <div class="news__main_wrap gap-25">
                <router-link to="" target="_blank" class="news__main_block" v-for="cur_news in news">
                    <img src="#" :key="cur_news.event_id" :alt="cur_news.event.title">
                    <h5>{{ cur_news.event.title }}</h5>
                    <div class="news__info">
                        <div class="news-info__item">{{ cur_news.event.organization.name }}</div>
                        <div class="news-info__item">{{ cur_news.event.datetime }}</div>
                        <div class="news-info__item delete-event"><img src="@/assets/images/icon/close.svg" alt=""></div>
                    </div>
                </router-link>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
    import HeaderAdminComponent from "@/components/HeaderAdminComponent.vue";
    import HelloAccountComponent from "@/components/HelloAccountComponent.vue";
    import {onMounted, ref} from 'vue';
    import {useUserStore} from "@/stores/user";
    import axios from "axios";

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
    onMounted(() => {

    let user = useUserStore();

    let user_name = ref('');
    axios.get(window.origin + '/api/users/' + user.id).then(res => {
        user_name.value = res.data.firstname;
    });

    const news = ref([]);

    axios.get(window.origin + '/api/events-req').then(res => {
        news.value = res.data.filter((i)=>{return i.user_id === user.id});
    });
    });
</script>

<style scoped>
    .container-with-header {
        width: calc(100% - 300px);
        margin-left: 300px;
        padding: 30px;
    }
    .inner-container {
        width: 100%;
    }
    .news__main_wrap{
        display: grid;
        gap: 15px;
        margin-top: 30px;
        grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    }

    .news__main_block{
        display: flex;
        flex-direction: column;
        gap: 12px;
        text-decoration: none;
    }

    .news__main_block > img{
        width: 100%;
        height: 250px;
        object-fit: cover;
        border-radius: 20px;
        pointer-events: none;
    }

    .news__main_block > h5{
        padding: 0 5px;
    }

    .news__info{
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
    }

    .news-info__item{
        font-size: 18px;
        padding: 7px 14px;
        border-radius: 50px;
        outline: 1px solid rgb(49, 49, 49);
    }
    
    .news-info__item.delete-event {
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 10px;
        background-color: red;
        outline: none;
    }
    
    .news-info__item.delete-event > img {
        filter: invert(100%) sepia(0%) saturate(0%) hue-rotate(257deg) brightness(102%) contrast(104%);
    }
</style>