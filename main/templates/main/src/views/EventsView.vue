<template>
    <header-component />
    <section class="section events__section">
        <div class="container events__container gap-50">
            <h2 class="h2 ta-c"><span class="blue">_</span>События</h2>
            <div class="events__main_wrap gap-25">
                <router-link :to="{name: 'event_page', params: {id: event.id}}" class="events__main_block" v-for="event in events">
                    <img :src="event.img" :key="event.id" :alt="event.title">
                    <h5>{{ event.title }}</h5>
                    <div class="events__info">
                        <div class="events-info__item">{{ organizations.filter(i => {return i.id == event.organization})[0].name }}</div>
                        <div class="events-info__item">{{ event.datetime }}</div>
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
import axios from "axios";

const events: Ref<Object[]> = ref([{}]);
const organizations: Ref<Object[]> = ref([{}]);

axios.get(window.origin + '/api/events').then(res => {
    events.value = res.data;
});
axios.get(window.origin + '/api/users').then(res => {
    organizations.value = res.data;
});
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
