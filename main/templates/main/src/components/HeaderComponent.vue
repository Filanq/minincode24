<template>
    <div class="section header__section">
        <div class="container header__container">
            <nav class="header_nav" :class="{'header_nav--open': isBurgerOpen}">
                <div>
                    <span class="header-cursor" :class="{hideHeaderCursor: !headerCursor1.active}" :style="{ width: `${headerCursor1.width}px`, height: `${headerCursor1.height}px`, left: `${headerCursor1.left}px` }"></span>
                    <router-link :to="{name: 'home'}" class="link header_link header-section-1" @click="getClickFromHeader($event, anchors.homeAnch)" ref="homeHeaderBtn">Главная</router-link>
                    <router-link :to="{name: 'news'}" class="link header_link header-section-1" @click="getClickFromHeader($event, anchors.aboutAnch)" ref="aboutHeaderBtn">Новости</router-link>
                    <router-link :to="{name: 'events'}" class="link header_link header-section-1" @click="getClickFromHeader($event, anchors.resumeAnch)" ref="resumeHeaderBtn">События</router-link>
                </div>
                <router-link :to="{name: 'home'}" class="link header_link--logo">MininCode</router-link>
                <div>
                    <span class="header-cursor" :class="{hideHeaderCursor: !headerCursor2.active}" :style="{ width: `${headerCursor2.width}px`, height: `${headerCursor2.height}px`, left: `${headerCursor2.left}px` }"></span>
                    <router-link :to="{name: 'organizations'}" class="link header_link header-section-2" @click="getClickFromHeader($event, anchors.contactsAnch)" ref="contactsHeaderBtn">Организации</router-link>
                    <router-link v-if="user.type !== '' && user.type !== 'admin'" :to="user.type === 'user' ? '/user_account' : '/org_account'" class="link header_link header-section-2" @click="getClickFromHeader($event, anchors.historyAnch)" ref="historyHeaderBtn" href="#history">Личный кабинет</router-link>
                    <router-link v-if="user.type === 'admin'" to="/admin" class="link header_link header-section-2" @click="getClickFromHeader($event, anchors.historyAnch)" ref="historyHeaderBtn" href="#">Адм. панель</router-link>
                    <router-link v-if="user.type === ''" :to="{name: 'login'}" class="link header_link header-section-2" @click="getClickFromHeader($event, anchors.projectsAnch)" ref="projectsHeaderBtn">Вход</router-link>
                    <router-link v-if="user.type === ''" :to="{name: 'registration'}" class="link header_link header-section-2" @click="getClickFromHeader($event, anchors.contactsAnch)" ref="contactsHeaderBtn">Регистрация</router-link>
                    <a v-if="user.type !== ''" href="#" @click.prevent="()=>{user.logout(); $router.push('/')}" class="link header_link header-section-2" @click="getClickFromHeader($event, anchors.contactsAnch)" ref="contactsHeaderBtn">Выход</a>
                </div>
            </nav>
        </div>
    </div>
</template>

<script setup lang="ts">
import {RouterLink, useRouter} from 'vue-router';
    import {reactive, ref, defineProps, onMounted, type Ref} from 'vue';
    import {useUserStore} from "@/stores/user";

    const props = defineProps({
        anchors: Object
    });

    const user = useUserStore();

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

    let isBurgerOpen = ref(false)

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

    .header_nav div{
        display: flex;
        gap: 20px;
    }

    .header_link{
        display: flex;
        align-items: center;
        padding: 10px 24px;
        border-radius: 50px;
        z-index: 2;
    }

    .header_link--active{
        background-color: var(--colorBlue);
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
        background-color: #0069ff;
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
        background-image: url('../assets/images/icon/cross.png');
        width: 50px;
        height: 50px;
        background-position: center;
        background-size: cover
    }

    .burger_menu{
        display: none !important;
        position: relative;
    }

    @media(max-width: 1280px){
        .burger_btn{
            display: block;
        }

        .header_nav div{
            display: none;
        }

        .burger_menu{
            display: grid !important;
            position: absolute;
            right: 0;
            top: 0;
            padding: 20px;
            padding-top: 80px;
            border-radius: 20px;
            background-color: #a6a6a6;
            margin-top: 20px;
            margin-right: 20px;
        }

        .cross{
            position: absolute;
            top: 10px;
            right: 10px;
            background-image: url('../assets/images/icon/burger.png');
            width: 50px;
            height: 50px;
            background-position: center;
            background-size: cover
        }
    }
</style>
