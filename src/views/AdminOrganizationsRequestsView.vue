<template>
    <HeaderAdminComponent :buttons="buttons" />
    <div class="container-with-header">
        <HelloAccountComponent :name="'«Тайно дернул»'" />
        <div class="inner-container">
            <h3 class="h3">Модерация заявок на создание организаций</h3>
            <div class="requests-container">

                <div class="request">
                    <div class="left">
                        <h5 class="h5">Название</h5>
                        <p>Сайт: <a href="google.com">google.com</a></p>
                        <p>Адрес: ул. Ммжукмбю 09</p>
                    </div>
                    <div class="right">
                        <div class="cancel-btn">
                            <img src="@/assets/images/icon/close.svg" alt="">
                        </div>
                        <div class="ok-btn">
                            <img src="@/assets/images/icon/check.svg" alt="">
                        </div>
                    </div>
                </div>

                <div class="request">
                    <div class="left">
                        <h5 class="h5">Название</h5>
                        <p>Сайт: <a href="google.com">google.com</a></p>
                        <p>Адрес: ул. Ммжукмбю 09</p>
                    </div>
                    <div class="right">
                        <div class="cancel-btn">
                            <img src="@/assets/images/icon/close.svg" alt="">
                        </div>
                        <div class="ok-btn">
                            <img src="@/assets/images/icon/check.svg" alt="">
                        </div>
                    </div>
                </div>

                <div class="request">
                    <div class="left">
                        <h5 class="h5">Название</h5>
                        <p>Сайт: <a href="google.com">google.com</a></p>
                        <p>Адрес: ул. Ммжукмбю 09</p>
                    </div>
                    <div class="right">
                        <div class="cancel-btn">
                            <img src="@/assets/images/icon/close.svg" alt="">
                        </div>
                        <div class="ok-btn">
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

    const buttons = [
        {
            title: 'Заявки организаций',
            view: 'organizations_requests',
        }
    ];
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