<template>
    <header-component></header-component>

    <div class="section">
        <div class="container">
            <div class="card__wrap grid gap-50">
                <div class="card__block">
                    <img src="../assets/images/news_test.webp" alt="img">
                    <div class="grid grid-row jc-sb ai-c">
                        <span>IT-cube</span>
                        <span>11.11.1111</span>
                    </div>
                </div>
                <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Pariatur vero earum ex eum sequi. Recusandae facilis porro, dolorum perspiciatis vitae minima a officiis? Iusto dicta velit ab vitae nam dolorem. Lorem ipsum dolor sit amet consectetur adipisicing elit. Ea, at! Similique minus mollitia sapiente sit. Nesciunt, possimus adipisci? Maiores at, quod dolor velit nostrum labore modi iure soluta nesciunt pariatur? Lorem ipsum dolor sit amet consectetur adipisicing elit. Fugiat neque ex praesentium veritatis repudiandae corporis quas ducimus qui minima totam dignissimos quod eum dolorem, id ipsum enim sequi? Nemo, magni.</p>
            </div>
        </div>
    </div>
</template>

<script setup>
    import HeaderComponent from '@/components/HeaderComponent.vue';
</script>

<style scoped>
    .card__wrap{
        grid-template-columns: 1fr 2fr;
    }

    .card__block{
        width: 100%;
    }
    
    .card__block > img{
        width: 100%;
        border-radius: 20px;
        object-fit: cover;
        object-position: center;
    }

</style>