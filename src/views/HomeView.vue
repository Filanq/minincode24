<template>
    <div class="section grid grid-column ac-s gap-40">
        <div class="container grid grid-column jc-s ai-s">
            <h2 class="h2 mb-10">Здравствуйте, Name!</h2>
            <p class="width-100">Войди в мир IT вместе с нами...</p>
        </div>

        <div class="organ__container container grid grid-column jc-s ac-s gap-25">
            <div class="organ_block width-100 grid grid-column gap-25">
                <h3 class="h3">Учитесь новому, создавайте, творите</h3>
                <router-link :to="{name: 'home'}" class="link btn organ_btn">Узнать больше</router-link>
            </div>
            <div class="organ_block width-100 grid grid-column"></div>
        </div>

        <div class="container grid grid-row jc-s ac-s gap-25">
            <router-link :to="{name: 'home'}" class="link event_link events_link grid grid-row gap-10">
                <img src="../assets/images/icon/event.svg" alt="event">
                <div class="grid grid-column gap-10">
                    <p class="event_time">22.06.2025</p>
                    <h4>Собрание</h4>
                </div>
            </router-link>
            <router-link :to="{name: 'home'}" class="link event_link events_link grid grid-row gap-10">
                <img src="../assets/images/icon/event.svg" alt="event">
                <div class="grid grid-column gap-10">
                    <p class="event_time">22.06.2025</p>
                    <h4>Собрание</h4>
                </div>
            </router-link>
            <router-link :to="{name: 'home'}" class="link event_link events_link grid grid-row gap-10">
                <img src="../assets/images/icon/event.svg" alt="event">
                <div class="grid grid-column gap-10">
                    <p class="event_time">22.06.2025</p>
                    <h4>Собрание</h4>
                </div>
            </router-link>
            <router-link :to="{name: 'home'}" class="link event_link events_link grid grid-row gap-10">
                <img src="../assets/images/icon/event.svg" alt="event">
                <div class="grid grid-column gap-10">
                    <p class="event_time">22.06.2025</p>
                    <h4>Собрание</h4>
                </div>
            </router-link>
            <router-link :to="{name: 'home'}" class="link event_link events_link grid grid-row gap-10">
                <img src="../assets/images/icon/event.svg" alt="event">
                <div class="grid grid-column gap-10">
                    <p class="event_time">22.06.2025</p>
                    <h4>Собрание</h4>
                </div>
            </router-link>
        </div>

        <div class="container grid grid-column jc-s ac-s ai-s gap-25">
            <h3 class="h3">Новости</h3>
            <div class="news_wrap grid grid-row gap-25">
                <div class="news_block grid grid-column gap-10">
                    <img src="../assets/images/news_test.webp" alt="news">
                    <h4>Не пенить Александра</h4>
                    <div class="grid grid-row jc-sb">
                        <p class="event_time">22.06.2025</p>
                        <p class="event_time">IT-новости</p>
                    </div>
                    <p class="event__name_organ">Кванториум</p>
                </div>

                <div class="news_block grid grid-column gap-10">
                    <img src="../assets/images/news_test.webp" alt="news">
                    <h4>Не пенить Александра</h4>
                    <div class="grid grid-row jc-sb">
                        <p class="event_time">22.06.2025</p>
                        <p class="event_time">IT-новости</p>
                    </div>
                    <p class="event__name_organ">IT-cube</p>
                </div>

                <div class="news_block grid grid-column gap-10">
                    <img src="../assets/images/news_test.webp" alt="news">
                    <h4>Не пенить Александра</h4>
                    <div class="grid grid-row jc-sb">
                        <p class="event_time">22.06.2025</p>
                        <p class="event_time">IT-новости</p>
                    </div>
                    <p class="event__name_organ">IT-cube</p>
                </div>

                <div class="news_block grid grid-column gap-10">
                    <img src="../assets/images/news_test.webp" alt="news">
                    <h4>Не пенить Александра</h4>
                    <div class="grid grid-row jc-sb">
                        <p class="event_time">22.06.2025</p>
                        <p class="event_time">IT-новости</p>
                    </div>
                    <p class="event__name_organ">IT-cube</p>
                </div>
            </div>
        </div>
    </div>


</template>

<script setup>

</script>

<style scoped>
    h2{
        text-align: start;
    }

    .organ__container{
        grid-template-columns: 2fr 1fr;
    }

    .organ_block{
        padding: 30px;
        background-color: var(--colorBlueLight);
        color: #fff;
        border-radius: 20px;
    }

    .organ_btn{
        background-color: white;
        color: black;
    }

    .events_link{
        padding: 20px;
        background-color: white;
        border-radius: 15px;
    }

    .events_link > div{
        gap: 5px;
    }

    .event_time{
        font-size: 14px;
        color: #858585;
    }

    .event_link > img{
        height: 100%;
    }

    .news_wrap{
        grid-template-columns: repeat(4, 1fr)
    }

    .news_block > img{
        width: 100%;
        height: 160px;
        border-radius: 20px;
        object-fit: cover;
        object-position: center;
    }

    .news_block{
        position: relative;
    }

    .event__name_organ{
        position: absolute;
        z-index: 2;
        padding: 6px 10px;
        background-color: white;
        border-radius: 200px;
        font-size: 14px;
        top: 8px;
        left: 8px;
    }

</style>    