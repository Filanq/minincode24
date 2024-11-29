<template>
    <header-component></header-component>

    <div class="section news-card__section">
        <div class="container">
            <div class="card__wrap grid gap-50">
                <div class="card__block">
                    <img :src="news.img" alt="img">
                    <div class="grid grid-row jc-sb ai-c">
                        <span>{{ news.title }}</span>
                        <span>{{ news.date }}</span>
                    </div>
                </div>
                <p>{{ news.text }}</p>
            </div>
        </div>
    </div>
</template>

<script setup>
    import HeaderComponent from '@/components/HeaderComponent.vue';
    import {useRoute} from "vue-router";
    import {ref} from "vue";
    import axios from "axios";

    let news = ref({});
    axios.get(window.origin + '/api/news/' + useRoute().params.id).then(res => {
        news.value = res.data;
    });
</script>

<style scoped>
.news-card__section{
    padding-top: 150px;
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