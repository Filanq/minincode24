<template>
    <HeaderAdminComponent :buttons="buttons" />
    <div class="container-with-header">
        <HelloAccountComponent :name="user_name" />
        <div class="inner-container">
            <h3 class="h5">Модерация заявок на создание организаций</h3>
            <div class="requests-container">

                <div class="request" v-for="org in orgs">
                    <div class="left">
                        <h5 class="h5">{{ org.name }}</h5>
                        <p>Сайт: <a :href="org.website" target="_blank">{{ org.website }}</a></p>
                        <p>Адрес: {{ org.address }}</p>
                    </div>
                    <div class="right">
                        <div class="cancel-btn" @click="decline(org.id)">
                            <img src="@/assets/images/icon/close.svg" alt="">
                        </div>
                        <div class="ok-btn" @click="accept(org.id)">
                            <img src="@/assets/images/icon/check.svg" alt="">
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
    import HeaderAdminComponent from "@/components/HeaderAdminComponent.vue";
    import HelloAccountComponent from "@/components/HelloAccountComponent.vue";
    import {onMounted, ref} from "vue";
    import axios from "axios";
    import {useUserStore} from "@/stores/user";

    const buttons = [
        {
            title: 'Заявки организаций',
            view: 'organizations_requests',
        }
    ];
    let user = useUserStore();
    let user_name = ref('');
    user.login().then(() => {
        axios.get(window.origin + '/api/users/' + user.id).then(res => {
            user_name.value = res.data.firstname;
        });
    });

    let orgs = ref([]);
    axios.get(window.origin + '/api/users').then(res => {
        console.log(res);
        orgs.value = res.data.filter((item)=>{return item.type === 'organization' && !item.verified});
    });

    const decline = (id) => {
        axios.delete(window.origin + '/api/users/' + String(id));
        orgs.value.splice(orgs.value.indexOf(orgs.value.filter((item)=>{return item.id == id})[0]), 1);
    };
    const accept = (id) => {
        axios.post(window.origin + '/api/accept-org', {
            id: id
        }, {headers: {"X-CSRFToken": user.getCookie('csrftoken')}});
        orgs.value.splice(orgs.value.indexOf(orgs.value.filter((item)=>{return item.id == id})[0]), 1);
    };
</script>

<style scoped>
    .container-with-header {
        width: calc(100% - 300px);
        margin-left: 300px;
        padding: 30px;
    }
    .inner-container {
        width: 100%;
    }
    .requests-container {
        display: flex;
        flex-direction: column;
        gap: 10px;
        margin-top: 20px;
    }
    .request {
        display: flex;
        justify-content: space-between;
        align-items: flex-end;
        border: solid var(--colorWhite) 1px;
        border-radius: 20px;
        padding: 20px;
    }
    .request > .left {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        gap: 10px;
    }
    .request > .left > p {
        color: #858585;
        font-size: 14px;
    }
    .request > .right {
        display: flex;
        gap: 10px;
    }
    .request > .right > div {
        display: flex;
        justify-content: center;
        align-items: center;
        width: 40px;
        height: 40px;
        border-radius: 50px;
        cursor: pointer;
    }
    .cancel-btn {
        background-color: red;
    }
    .ok-btn {
        background-color: green;
    }
    .request > .right img {
        width: 20px;
        height: auto;
        filter: invert(100%) sepia(0%) saturate(7500%) hue-rotate(207deg) brightness(107%) contrast(100%);
    }
</style>