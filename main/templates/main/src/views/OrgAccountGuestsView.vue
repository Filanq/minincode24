<template>
    <HeaderAdminComponent :buttons="buttons" />
    <div class="container-with-header">
        <HelloAccountComponent :name="user_name" />
        <div class="inner-container">
            <h3 class="h5">Гости мероприятий</h3>
            <div class="news__main_wrap gap-25">
                <div class="news__main_block" v-for="event in events">
                    <h5>{{ event.title }}</h5>
                    <div class="guests-container">
                        <b>Участники:</b>
                        <span v-for="req in requests.filter((i)=>{return event.id === i.event_id})">{{ users.filter(i=>{return i.id === req.user})[0].lastname + users.filter(i=>{return i.id === req.user})[0].firstname }}</span>
                    </div>
                    <div class="news__info">
                        <div class="news-info__item">{{ event.organization.name }}</div>
                        <div class="news-info__item">{{ event.datetime }}</div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
    import HeaderAdminComponent from "@/components/HeaderAdminComponent.vue";
    import HelloAccountComponent from "@/components/HelloAccountComponent.vue";
    import {onMounted, ref} from 'vue';
    import {useUserStore} from "@/stores/user";
    import axios, {get} from "axios";

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
        let user = useUserStore();

    let user_name = ref('');

    const events = ref([]);
    const requests = ref([]);
    const users = ref([]);
    user.login().then(() => {
        axios.get(window.origin + '/api/users/' + user.id).then(res => {
            user_name.value = res.data.firstname;
        });


        axios.get(window.origin + '/api/users').then(res => {
            users.value = res.data;
        });

        axios.get(window.origin + '/api/events').then(res => {
            events.value = res.data.filter((i)=>{return i.organization == user.id});
        });

        axios.get(window.origin + '/api/events-req').then(res => {
            requests.value = res.data;
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
        grid-template-columns: 1fr;
    }

    .news__main_block{
        display: flex;
        flex-direction: column;
        gap: 12px;
        text-decoration: none;
    }

    .news__main_block > img{
        width: 100%;
        height: 290px;
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

    .news-info__item.edit-event,
    .news-info__item.delete-event {
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 10px;
    }

    .news-info__item.delete-event {
        background-color: red;
        outline: none;
    }

    .news-info__item.delete-event > img {
        filter: invert(100%) sepia(0%) saturate(0%) hue-rotate(257deg) brightness(102%) contrast(104%);
    }
    .title-add-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .add-btn {
        display: flex;
        align-items: center;
        gap: 7px;
        border-radius: 50px;
        padding: 10px 16px;
        background-color: #000;
        color: var(--colorWhite);
        cursor: pointer;
    }
    .add-btn > img {
        width: 18px;
        height: auto;
        filter: invert(100%) sepia(0%) saturate(0%) hue-rotate(257deg) brightness(102%) contrast(104%);
    }
    .guests-container {
        display: flex;
        flex-direction: column;
    }
    .guests-container > span::before {
        content: '- ';
    }
</style>