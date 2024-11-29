<template>
    <section class="section news__section">
        <div class="container news__container">
            <h2 class="h2"><span class="blue h2">_</span>Новости</h2>
            <div class="news__main_wrap">
                <router-link :to="{name: 'news_page', params: {id: cur_news.id}}" class="news__main_block" v-for="cur_news in news">
                    <img :src="cur_news.img" :key="cur_news.id" :alt="cur_news.title">
                    <h5>{{ cur_news.title }}</h5>
                    <div class="news__info">
                        <div class="news-info__item">{{ organizations.filter(i => {return i.id == cur_news.organization})[0].name }}</div>
                        <div class="news-info__item">{{ cur_news.date }}</div>
                    </div>
                </router-link>
            </div>
        </div>
    </section>
</template>

<script setup lang="ts">
import type {Ref} from "vue";
import {ref} from "vue";
import axios from "axios";

const news: Ref<Object[]> = ref([{}]);
const organizations: Ref<Object[]> = ref([{}]);

axios.get(window.origin + '/api/news').then(res => {
    news.value = res.data.slice(0, 6);
});
axios.get(window.origin + '/api/users').then(res => {
    organizations.value = res.data;
});
</script>

<style scoped>
.news__container{
    display: flex;
    flex-direction: column;
    gap: 50px;
}

.news__main_wrap{
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(400px, 1fr));
    gap: 30px;
}

.news__main_block{
    display: flex;
    flex-direction: column;
    gap: 12px;
    text-decoration: none;
}

.news__main_block > img{
    width: 100%;
    height: 300px;
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
</style>