<template>
    <HeaderAdminComponent :buttons="buttons" />
    <div class="container-with-header">
        <HelloAccountComponent :name="user_name" />
        <div class="inner-container">
            <h3 class="h5">Редактирование данных</h3>
            <form class="form-container">
                <label>
                    Название организации
                    <input v-model="name" type="text">
                </label>
                <label>
                    Сайт организации
                    <input v-model="website" type="text">
                </label>
                <label>
                    Адрес организации
                    <input v-model="address" type="text">
                </label>
                <label>
                    Информация
                    <textarea v-model="text" style="resize: vertical; max-height: 300px; min-height: 100px;"></textarea>
                </label>
                <label>
                    Контакты
                    <input v-model="contacts" type="text">
                </label>
                <button type="button">Сохранить</button>
                <span class="green_text hide_green_text">Сохранено</span>
            </form>
        </div>
    </div>
</template>

<script setup>
    import HeaderAdminComponent from "@/components/HeaderAdminComponent.vue";
    import HelloAccountComponent from "@/components/HelloAccountComponent.vue";
    import {ref} from "vue";
    import axios from "axios";
    import {useUserStore} from "@/stores/user";

    const buttons = [
        {
            title: 'Основная информация',
            view: 'org_account_data_settings',
        },
        {
            title: 'Мероприятия организации',
            view: 'org_account_events',
        },
        {
            title: 'Новости организации',
            view: 'org_account_news',
        },
        {
            title: 'Гости мероприятия',
            view: 'org_account_guests',
        },
    ];

    let user = useUserStore();

    let is_successfuly = ref(false);

    const name = ref('');
    const website = ref('');
    const address = ref('');
    const text = ref('');
    const contacts = ref('');
    let org_id = 0;

    user.login().then(() => {
        axios.get(window.origin + '/api/users/' + user.id).then(res => {
            name.value = res.data.name;
            website.value = res.data.website;
            address.value = res.data.address;
        });

        axios.get(window.origin + '/api/organization').then(res => {
            let info = res.data.filter(i => {return i.user === Number(user.id)});
            contacts.value = res.data.filter(i => {return i.user === Number(user.id)})[0].contacts;
            text.value = res.data.filter(i => {return i.user === Number(user.id)})[0].text;
            org_id = res.data.filter(i => {return i.user === Number(user.id)})[0].id;
        });
    });

    const save = () => {
        if(is_successfuly.value){
            return;
        }
        axios.patch(window.origin + '/api/users/' + user.id + '/', {
            name: name.value,
            website: website.value,
            address: address.value
        }, {headers: {"X-CSRFToken": user.getCookie('csrftoken')}}).then(res => {
            axios.patch(window.origin + '/api/organization/' + org_id + '/', {
                text: text.value,
                contacts: contacts.value
            }, {headers: {"X-CSRFToken": user.getCookie('csrftoken')}}).then(() => {
                is_successfuly.value = true;
                setTimeout(()=>{
                    is_successfuly.value = false;
                }, 2000);
            });

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
    input, textarea {
        border-radius: 10px;
        border: solid #000 1px;
        padding: 10px;
        background-color: #FFFFFF15;
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