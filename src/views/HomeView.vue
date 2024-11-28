<template>
    <HeaderComponent :anchors="anchors"/>
    <div class="section banner__section" >
        <div class="container banner__container jc-c">
            <h1 class="h1">MININCODE</h1>
        </div>
    </div>

    <MarqueComponent/>

    <about-component/>

    <DirectionsComponent/>

    <NewsComponent/>
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
        width: 100vw;
        height: 100vh;
        position: relative;
        z-index: 0;
    }

    
</style>