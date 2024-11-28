<template>
    <div class="section grid grid-column ac-s gap-40">
        <div class="container grid grid-column jc-s ai-s">
            <h2 class="h2 mb-10">Здравствуйте, Name!</h2>
            <p class="width-100">Войди в мир IT вместе с нами...</p>
        </div>

        <div class="organ__container container grid grid-column jc-s ac-s gap-10">
            <div class="organ_block width-100 grid grid-column">
                <h3 class="h3">Учитесь новому, создавайте, творите</h3>
                <div class="btn">Узнать больше</div>
            </div>
            <div class="organ_block width-100 grid grid-column"></div>
        </div>
    </div>


</template>

<script setup>

</script>

<style scoped>
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
</style>