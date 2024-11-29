<template>
    <HeaderComponent/>

    <div class="section">
        <div class="container grid grid-column gap-25">
            <div class="organization_wrap grid grid-row gap-25">
                <div class="grid grid-column gap-25 ac-s">
                    <img src="../assets/images/news_test.webp" alt="img">
                </div>
                <div class="grid grid-column gap-25">
                    <h3 class="h4">IT-Cube</h3>
                    <p>МЫ компания со стажем 20 лет. Учим молодых и заинтересованных. Lorem ipsum dolor sit amet consectetur adipisicing elit. Nihil nostrum dicta ab molestias ipsum saepe, debitis repellat nulla tenetur quis minus facere numquam aut dolor omnis, et distinctio eaque sed.</p>
                    <div style="width: fit-content" class="grid grid-row gap-10 ac-c">
                        <a href="https://telegram.org" class="btn">Telegramm</a>
                        <a href="https://whatsapp" class="btn">WhatsApp</a>
                        <a href="https://vk" class="btn">VK</a>

                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
    import HeaderComponent from '@/components/HeaderComponent.vue';
</script>

<style scoped>
    .organization_wrap{
        grid-template-columns: 1fr 1fr;
    }

    .organization_wrap > div > img{
        width: 100%;
        border-radius: 20px;
        height: fit-content
    }

    .competents__wrap{
        display: flex;
        gap: 25px;
        flex-wrap: wrap;
    }

    .competents__block{
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        align-items: center;
        width: fit-content;
        gap: 10px;

        padding: 15px;
        border: 1px solid var(--colorBlueMain);
        border-radius: 20px;
    }

    .btn--mini{
        padding: 8px 18px;
    }

    .link{
        font-size: 18px;
        display: flex;
        justify-content: center;
        justify-content: center;

        padding: 7px 14px;
        border-radius: 50px;
        outline: 1px solid rgb(49, 49, 49);
        width: fit-content;
        color: white;
    }
</style>