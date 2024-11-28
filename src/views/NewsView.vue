<template>
    <section class="section grid grid-column ac-s gap-40">
        <div class="container">
            <h3 class="h3 mb-10">Новости</h3>
            <span class="mini-text">Что-то</span>
        </div>
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
    </section>
</template>

<script setup>

</script>

<style scoped>
    h3 {
        align-self: start;
    }
    .mini-text {
        display: inline;
        font-weight: 300;
        color: #858585;
        font-size: 14px;
    }
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
        cursor: pointer;
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
