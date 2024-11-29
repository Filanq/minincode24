<template>
    <HeaderAdminComponent :buttons="buttons" />
    <ModalRedactComponent v-if="showRedactModal" :changeCondRedactModal="changeCondRedactModal" />
    <ModalCreateComponent v-if="showCreateModal" :changeCondCreateModal="changeCondCreateModal" />  
    <div class="container-with-header">
        <HelloAccountComponent :name="'«Тайно дернул»'" />
        <div class="inner-container">
            <div class="title-add-container">
                <h3 class="h3">Новости организации</h3>
                <div @click="changeCondCreateModal" class="add-btn">
                    <img src="@/assets/images/icon/plus.svg" alt="">
                    Добавить
                </div>
            </div>
            <div class="news__main_wrap gap-25">
                <router-link :to="cur_news.link" target="_blank" class="news__main_block" v-for="cur_news in news">
                    <img src="#" :key="cur_news.id" :alt="cur_news.title">
                    <h5>{{ cur_news.title }}</h5>
                    <div class="news__info">
                        <div class="news-info__item">{{ cur_news.organization.name }}</div>
                        <div class="news-info__item">{{ cur_news.date }}</div>
                        <div @click="changeCondRedactModal" class="news-info__item edit-event"><img src="@/assets/images/icon/edit.svg" alt=""></div>
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
    import ModalRedactComponent from "@/components/ModalRedactComponent.vue";
    import ModalCreateComponent from "@/components/ModalCreateComponent.vue";
    import {ref} from 'vue';

    const showRedactModal = ref(false);
    const showCreateModal = ref(false);
    function changeCondRedactModal(e) {
        e.preventDefault();
        showRedactModal.value = !showRedactModal.value;
    }
    function changeCondCreateModal(e) {
        e.preventDefault();
        showCreateModal.value = !showCreateModal.value;
    }

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

    const news = ref([{id: 0, title: 'title', img: '', organization: {name: 'it-cube'}, date: '11-11-1111'}]);

    function getNews(): void {
        news.value = [
            {id: 0, title: 'title', img: '', organization: {name: 'it-cube'}, date: '11-11-1111'},
            {id: 0, title: 'title', img: '', organization: {name: 'it-cube'}, date: '11-11-1111'},
            {id: 0, title: 'title', img: '', organization: {name: 'it-cube'}, date: '11-11-1111'},
        ];
    }
    getNews();
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
        grid-template-columns: repeat(auto-fill, minmax(290px, 1fr));
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

    .news-info__item.delete-event > img,
    .news-info__item.edit-event > img {
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
        background-color: var(--colorBlueLight);
        color: #000;
        cursor: pointer;
    }
    .add-btn > img {
        width: 20px;
        height: auto;
    }
</style>