<template>
    <header-component />
    <section class="section events__section">
        <div class="container events__container gap-50">
            <h2 class="h2 ta-c"><span class="blue">_</span>События</h2>
            <div class="events__main_wrap gap-25">
                <router-link :to="cur_events.link" target="_blank" class="events__main_block" v-for="cur_events in events">
                    <img src="#" :key="cur_events.id" :alt="cur_events.title">
                    <h5>{{ cur_events.title }}</h5>
                    <div class="events__info">
                        <div class="events-info__item">{{ cur_events.organization.name }}</div>
                        <div class="events-info__item">{{ cur_events.datetime }}</div>
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

const events: Ref<Object[]> = ref([{id: 0, title: 'title', img: '', organization: {name: 'it-cube'}, datetime: '11-11-1111'}]);

function getEvents(): void {
    events.value = [
        {id: 0, title: 'title', img: '', organization: {name: 'it-cube'}, datetime: '11-11-1111'},
        {id: 0, title: 'title', img: '', organization: {name: 'it-cube'}, datetime: '11-11-1111'},
        {id: 0, title: 'title', img: '', organization: {name: 'it-cube'}, datetime: '11-11-1111'},
    ];
}
getEvents();
</script>

<style scoped>
.events__section{
    padding-top: 150px;
}
.events__container{
    display: flex;
    flex-direction: column;
    gap: 50px;
}

.events__main_wrap{
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
}

.events__main_block{
    display: flex;
    flex-direction: column;
    gap: 12px;
    text-decoration: none;
}

.events__main_block > img{
    width: 100%;
    height: 300px;
    object-fit: cover;
    border-radius: 20px;
    pointer-events: none;
}

.events__main_block > h5{
    padding: 0 5px;
}

.events__info{
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
}

.events-info__item{
    font-size: 18px;
    padding: 7px 14px;
    border-radius: 50px;
    outline: 1px solid rgb(49, 49, 49);
}
</style>
