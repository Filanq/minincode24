<template>
    <div class="section header__section">
        <div class="container header__container">
            <nav class="header_nav" :class="{'header_nav--open': isBurgerOpen}">
                <div>
                    <router-link :to="{name: 'home'}" class="link header_link header-section-2">Главная</router-link>
                    <router-link :to="{name: 'organizations'}" class="link header_link header-section-2">Организации</router-link>
                    <router-link :to="{name: 'news'}" class="link header_link header-section-2">Новости</router-link>
                </div>
                <a class="link header_link--logo" href="#">MininCode</a>
                <div>
                    <router-link :to="{name: 'org_account_data_settings'}" class="link header_link header-section-2">Личный кабинет</router-link>
                    <router-link :to="{name: 'registration'}" class="link header_link header-section-2">Регистрация</router-link>
                    <router-link :to="{name: 'login'}" class="link header_link header-section-2">Вход</router-link>
                </div>
                <span :class="{'open_burger_btn': isBurgerOpen}" class="burger_btn" @click="isBurgerOpen = !isBurgerOpen"></span>
                <div :class="{'open_burger_menu': isBurgerOpen}" class="burger_menu grid grid-column gap-10">
                    <router-link :to="{name: 'home'}" class="link header_link header-section-2">Главная</router-link>
                    <router-link :to="{name: 'organizations'}" class="link header_link header-section-2">Организации</router-link>
                    <router-link :to="{name: 'news'}" class="link header_link header-section-2">Новости</router-link>
                    <router-link :to="{name: 'org_account_data_settings'}" class="link header_link header-section-2">Личный кабинет</router-link>
                    <router-link :to="{name: 'registration'}" class="link header_link header-section-2">Регистрация</router-link>
                    <router-link :to="{name: 'login'}" class="link header_link header-section-2">Вход</router-link>
                </div>
            </nav>
        </div>
    </div>
</template>

<script setup lang="ts">
    import { RouterLink } from 'vue-router';
    import {reactive, ref, defineProps, onMounted, type Ref} from 'vue';

    const props = defineProps({
        anchors: Object
    });

    // Works Cursor Position
    const headerCursor1 = reactive({
        width: 0,
        height: 0,
        left: 0,
        active: false,
    });
    const headerCursor2 = reactive({
        width: 0,
        height: 0,
        left: 0,
        active: false,
    });
    const activeBtn: Ref<any> = ref(null);

    const homeHeaderBtn: Ref<any> = ref(null);
    const aboutHeaderBtn: Ref<any> = ref(null);
    const resumeHeaderBtn: Ref<any> = ref(null);
    const historyHeaderBtn: Ref<any> = ref(null);
    const projectsHeaderBtn: Ref<any> = ref(null);
    const contactsHeaderBtn: Ref<any> = ref(null);

    function scrollTo(view: Ref<HTMLElement | null>) { 
        view.value?.scrollIntoView({ behavior: 'smooth' });
    }

    let timerId: ReturnType<typeof setTimeout>;

    function getClickFromHeader(headerBtnEvent: any, scrollElement: any) {
        headerBtnEvent.preventDefault();
        clearTimeout(timerId);
        scrollCheckerActive = false;
        setHeaderCursor(headerBtnEvent.target);
        if (scrollElement) scrollTo(scrollElement);
        timerId = setTimeout(() => {
            scrollCheckerActive = true;
            scrollChecker();
        }, 1000);
    }

    // Change Header Cursor And Current Section on Click
    function setHeaderCursor(element: HTMLElement): void {
        activeBtn.value = element;
        console.log(1);
        if (element.classList.contains('header-section-1')) {
            if (headerCursor1.active) {
                headerCursor1.width = element.offsetWidth;
                headerCursor1.height = element.offsetHeight;
                headerCursor1.left = element.offsetLeft;
            } else {
                headerCursor1.active = true;
                headerCursor2.active = false;
                headerCursor1.width = element.offsetWidth;
                headerCursor1.height = element.offsetHeight;
                headerCursor1.left = element.offsetLeft;
                headerCursor2.width = element.offsetWidth;
                headerCursor2.height = element.offsetHeight;
                headerCursor2.left = element.offsetLeft;
            }
        } else if (element.classList.contains('header-section-2')) {
            if (headerCursor2.active) {
                headerCursor2.width = element.offsetWidth;
                headerCursor2.height = element.offsetHeight;
                headerCursor2.left = element.offsetLeft;
            } else {
                headerCursor2.active = true;
                headerCursor1.active = false;
                headerCursor2.width = element.offsetWidth;
                headerCursor2.height = element.offsetHeight;
                headerCursor2.left = element.offsetLeft;
                headerCursor1.width = element.offsetWidth;
                headerCursor1.height = element.offsetHeight;
                headerCursor1.left = element.offsetLeft;
            }
        }
    }

    let scrollCheckerActive = true;

    const scrollChecker = () => {
        if (scrollCheckerActive) {
            if (window.pageYOffset >= props.anchors.contactsAnch.value.offsetTop) {
                setHeaderCursor(contactsHeaderBtn.value);
            } else if (window.pageYOffset >= props.anchors.projectsAnch.value.offsetTop) {
                setHeaderCursor(projectsHeaderBtn.value);
            } else if (window.pageYOffset >= props.anchors.historyAnch.value.offsetTop) {
                setHeaderCursor(historyHeaderBtn.value);
            } else if (window.pageYOffset >= props.anchors.resumeAnch.value.offsetTop) {
                setHeaderCursor(resumeHeaderBtn.value);
            } else if (window.pageYOffset >= props.anchors.aboutAnch.value.offsetTop) {
                setHeaderCursor(aboutHeaderBtn.value);
            } else if (window.pageYOffset >= props.anchors.homeAnch.value.offsetTop) {
                setHeaderCursor(homeHeaderBtn.value);
            }
        }
    }

    // On Mounted Clicks Default Cursor Object
    onMounted(() => {
        addEventListener("scroll", scrollChecker);
        addEventListener("DOMContentLoaded", scrollChecker);
        addEventListener("resize", () => setHeaderCursor(activeBtn.value));
    })

    let isBurgerOpen = ref(false);

    // defineProps()
</script>

<style scoped>
    .header__section{
        padding: 20px 0;   
        z-index: 10;
        background-color: rgba(0, 0, 0, 0);
        position: fixed;
    }
    .header_nav{
        padding: 8px 10px ;
        background-color: var(--colorBlueLight);
        border-radius: 100px;
        display: flex;
        justify-content: space-between;
        gap: 30px;
        z-index: 10;
        width: 100%;
    }

    .header_nav div:nth-child(1),
    .header_nav div:nth-child(3){
        display: flex;
        gap: 20px;
    }

    .header_link{
        display: flex;
        align-items: center;
        padding: 10px 24px;
        border-radius: 50px;
        z-index: 2;
        transition: all .2s ease;
        white-space: nowrap;
    }

    .header_link:hover{
        background-color: var(--colorBlueMain);
        color: var(--colorWhite);
    }

    .header_link--logo{
        display: flex;
        align-items: center;
        font-size: 26px;
    }
    .project__container{
        display: flex;
        flex-direction: column;
        gap: 50px;
    }

    .choosing-person_wrap{
        position: relative;
        inset: 0;
        display: flex;
        gap: 18px;
        align-items: center;
        background-color: rgb(49, 49, 49);
        border-radius: 50px;
        padding: 8px 10px;
        width: fit-content;
    }

    .person-cursor {
        position: absolute;
        top: 8px;
        left: 10px;
        /* width: 129px; */
        height: 44px;
        border-radius: 50px;
        background-color: #0069ff;
        z-index: 1;
        transition: all .3s ease-in-out;
    }

    .header-cursor {
        position: absolute;
        left: 10px;
        /* width: 129px; */
        height: 41px;
        border-radius: 50px;
        /* background-color: #0069ff; */
        background-color: #00000000;
        z-index: 1;
        transition: opacity .3s cubic-bezier(.5, 0, .5, 0), left .3s ease-in-out, width .3s ease-in-out, height .3s ease-in-out;
    }

    .hideHeaderCursor {
        opacity: 0;
        transition: opacity .3s cubic-bezier(0, .5, 0, .5), left .3s ease-in-out, width .3s ease-in-out, height .3s ease-in-out;
    }

    .person-btn{
        cursor: pointer;
        font-size: 20px;
        padding: 10px 20px;
        border-radius: 50px;
        z-index: 2;
    }

    /* .person-btn:hover{
        outline: var(--colorBlue) 2px solid;
    } */

    .person-btn--active{
        background-color: blue;
        outline: blue 2px solid;
    }

    .burger_btn{
        display: none;
        background-image: url('../assets/images/icon/burger.svg');
        width: 30px;
        height: auto;
        padding: 10px;
        background-position: center;
        background-size: cover;
        cursor: pointer;
    }

    .open_burger_btn {
        background-image: url('../assets/images/icon/close.svg');
    }

    .burger_menu{
        display: none;
        position: relative;
    }

    @media(max-width: 1280px){
        .burger_btn{
            display: block;
        }

        .header_nav div:nth-child(1),
        .header_nav div:nth-child(3){
            display: none;
        }

        .burger_menu{
            display: none;
            position: absolute;
            right: 0;
            top: 80px;
            padding: 20px;
            border-radius: 20px;
            background-color: var(--colorBlueLight);
            margin-right: 25px;
        }

        .burger_menu > a {
            color: #000;
            text-decoration: none;
        }

        .open_burger_menu {
            display: grid;
        }
    }
</style>
