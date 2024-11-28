<template>
    <header-component />
    <section class="section news__section">
        <div class="container news__container gap-50">
            <h2 class="h2 ta-c"><span class="blue">_</span>Новости</h2>
            <div class="news__main_wrap gap-25">
                <router-link :to="cur_news.link" target="_blank" class="news__main_block" v-for="cur_news in news">
                    <img src="#" :key="cur_news.id" :alt="cur_news.title">
                    <h5>{{ cur_news.title }}</h5>
                    <div class="news__info">
                        <div class="news-info__item">{{ cur_news.organization.name }}</div>
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
import HeaderComponent from "@/components/HeaderComponent.vue";

const news: Ref<Object[]> = ref([{id: 0, title: 'title', img: '', organization: {name: 'it-cube'}, date: '11-11-1111'}]);

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
.news__section{
    padding-top: 150px;
}
.news__container{
    display: flex;
    flex-direction: column;
    gap: 50px;
}

.news__main_wrap{
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
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
