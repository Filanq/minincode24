<template>
    <HeaderAdminComponent :buttons="buttons" />
    <div class="container-with-header">
        <HelloAccountComponent :name="user_name" />
        <div class="inner-container">
            <h3 class="h5">Редактирование ФИО</h3>
            <form @submit.prevent="save()" class="form-container">
                <label>
                    Фамилия
                    <input v-model="user_sur" type="text">
                </label>
                <label>
                    Имя
                    <input v-model="user_name" type="text">
                </label>
                <label>
                    Отчество
                    <input v-model="user_last" type="text">
                </label>
                <button type="submit">Сохранить</button>
                <span v-show="is_successfuly" class="green_text">Сохранено</span>
            </form>
        </div>
    </div>
</template>

<script setup>
    import HeaderAdminComponent from "@/components/HeaderAdminComponent.vue";
    import HelloAccountComponent from "@/components/HelloAccountComponent.vue";
    import {useUserStore} from "@/stores/user";
    import {onMounted, ref} from "vue";
    import axios from "axios";

    let is_successfuly = ref(false);

    const buttons = [
        {
            title: 'ФИО',
            view: 'name_settings',
        },
        {
            title: 'Мои мероприятия',
            view: 'events_list',
        },
    ];
    let user = useUserStore();

    let user_name = ref('');
    let user_last = ref('');
    let user_sur = ref('');

    const news = ref([]);
    user.login().then(() => {
        axios.get(window.origin + '/api/users/' + user.id).then(res => {
            user_name.value = res.data.firstname;
            user_sur.value = res.data.surname;
            user_last.value = res.data.lastname;
        });
        axios.get(window.origin + '/api/events-req').then(res => {
            news.value = res.data.filter((i)=>{return i.user_id === user.id});
        });
    });



    const save = () => {
        if(is_successfuly.value){
            return;
        }
        axios.patch(window.origin + '/api/users/' + user.id + '/', {
            surname: user_sur.value,
            lastname: user_last.value,
            firstname: user_name.value
        }, {headers: {"X-CSRFToken": user.getCookie('csrftoken')}}).then(res => {
            is_successfuly.value = true;
            setTimeout(()=>{
                is_successfuly.value = false;
            }, 2000);
        }).catch(err => {
            alert(err.data);
        });
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
        max-width: 500px;
    }
    form {
        display: flex;
        flex-direction: column;
        gap: 15px;
        margin: 15px 0;
    }
    label {
        display: flex;
        flex-direction: column;
        gap: 8px;
        font-weight: 300;
        font-size: 14px;
    }
    input {
        border-radius: 10px;
        border: solid #000 1px;
        padding: 10px;
        background-color: #FFFFFF10;
        color: var(--colorWhite);
    }
    input:focus {
        outline: none;
    }
    button {
        padding: 16px 28px;
        background-color: #000;
        border-radius: 200px;
        border: none;
        color: var(--colorWhite);
        cursor: pointer;
    }
    .green_text {
        color: green;
    }
    .hide_green_text {
        display: none;
    }
</style>