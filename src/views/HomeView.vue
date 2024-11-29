<template>
    <HeaderComponent :anchors="anchors"/>
    <div class="section banner__section" >
        <div class="container banner__container jc-c">
            <h1 class="h1">MININCODE</h1>
            <p class="h2">Твой путь к успеху в IT</p>
        </div>
        <div class="banner__gradient"></div>
    </div>

    <MarqueComponent />

    <about-component />

    <DirectionsComponent/>

    <NewsComponent/>

    <div class="section">
        <div class="container footer__container grid">
            <h3 class="h2">Спасибо MininCode</h3>
            <p>Проект создан в рамках Всероссийского научно-технического хакатона по программированию MininCode силами команды CodeMakers. Наша команда в составе Федосенко Илья, Черных Владислав и Утяцкий Владислав, узнали много нового в сфере веб-технологий, закрепили имеющиеся навыки работы с фреймворками и получили ценный опыт командной работы. 😊</p>
        </div>
    </div>
</template>

<script setup>  
    import MarqueComponent from '@/components/MarqueComponent.vue';
    import HeaderComponent from '@/components/HeaderComponent.vue';
    import AboutComponent from '@/components/AboutComponent.vue';
    import DirectionsComponent from '@/components/DirectionsComponent.vue';
    import NewsComponent from '@/components/NewsComponent.vue';

    const anchors = {
        homeAnch: null,
        aboutAnch: null,
        resumeAnch: null,
        historyAnch: null,
        projectsAnch: null,
        contactsAnch: null,
    };

    const updateAnchors = newAnchors => {
        anchors.homeAnch = newAnchors.homeAnch;
        anchors.aboutAnch = newAnchors.aboutAnch;
        anchors.resumeAnch = newAnchors.resumeAnch;
        anchors.historyAnch = newAnchors.historyAnch;
        anchors.projectsAnch = newAnchors.projectsAnch;
        anchors.contactsAnch = newAnchors.contactsAnch;
    }
</script>

<style scoped>
    .banner__section{
        width: 100%;
        height: 100vh;
        position: relative;
        z-index: 0;
        position: relative;
    }
    .banner__gradient{
        position: absolute;
        bottom: 0;
        left: 0;
        width: 100%;
        height: 80px;
        background-image: linear-gradient(180deg, rgba(255,255,255,0) 0%, rgba(16,0,43,1) 80%);
    }
    .banner__section::after{
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: url('@/assets/images/bg1.jpg');
        background-position: center top;
        background-size: cover;

        z-index: -1;
    }

    .banner__section::before{
        content: '';
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        position: absolute;
        z-index: 0;
        background-color: rgba(0, 0, 0, 0.4);
    }

    .banner__container > * {
        z-index: 2;
        text-shadow: 1px 1px 2px var(--colorBlueMain);
    }

    .footer__container{
        grid-auto-columns: 1fr 1fr;
        grid-auto-rows: 1fr 1fr;
        gap: 40px;
    }

    .footer__container > p{
        grid-area: 2 / 2;
    }
    
</style>