<template>
    <main>
        <section class="section organization__section ac-s">
            <div class="container organizations__container gap-50">
                <h2 class="h3 w-700 organizations__title">Откройте для себя новые возможности!</h2>
                <div class="organizations__inner gap-25 grid width-100">
                    <div class="organizations__wrap grid grid-column gap-10 ac-s width-100">
                        <div class="organization__item grid grid-column ji-s ac-s">
                            <h3 class="h4 w-500 organization-item__title">Заголовок организации</h3>
                            <span class="h7 w-300 organization-item__address">ул. Пушкина д. Колотушкина</span>
                        </div>
                        <div class="organization__item grid grid-column ji-s ac-s">
                            <h3 class="h4 w-500 organization-item__title">Заголовок организации</h3>
                            <span class="h7 w-300 organization-item__address">ул. Пушкина д. Колотушкина</span>
                        </div>
                        <div class="organization__item grid grid-column ji-s ac-s">
                            <h3 class="h4 w-500 organization-item__title">Заголовок организации</h3>
                            <span class="h7 w-300 organization-item__address">ул. Пушкина д. Колотушкина</span>
                        </div>
                        <div class="organization__item grid grid-column ji-s ac-s">
                            <h3 class="h4 w-500 organization-item__title">Заголовок организации</h3>
                            <span class="h7 w-300 organization-item__address">ул. Пушкина д. Колотушкина</span>
                        </div>
                        <div class="organization__item grid grid-column ji-s ac-s">
                            <h3 class="h4 w-500 organization-item__title">Заголовок организации</h3>
                            <span class="h7 w-300 organization-item__address">ул. Пушкина д. Колотушкина</span>
                        </div>
                        <div class="organization__item grid grid-column ji-s ac-s">
                            <h3 class="h4 w-500 organization-item__title">Заголовок организации</h3>
                            <span class="h7 w-300 organization-item__address">ул. Пушкина д. Колотушкина</span>
                        </div>
                        <div class="organization__item grid grid-column ji-s ac-s">
                            <h3 class="h4 w-500 organization-item__title">Заголовок организации</h3>
                            <span class="h7 w-300 organization-item__address">ул. Пушкина д. Колотушкина</span>
                        </div>
                    </div>
                    <div class="organization__sticky">
                        <div id="yandex-map"></div>
                        <div id="organizations__map" class="organizations__map"></div>
                    </div>
                </div>
            </div>
        </section>
    </main>
</template>

<script setup>
    import {onMounted, ref} from "vue";

    let coordinates = ref([56.297462, 43.919970]);
    let zoom = ref(11);
    let map = ref(null);
    onMounted(() => {
        function initializeYandexMap() {
            ymaps.ready(async () => {
                map.value = new ymaps.Map("yandex-map", {
                    center: coordinates.value,
                    zoom: zoom.value,
                    controls: ['fullscreenControl'],
                });
                let myGeoObject = new ymaps.GeoObject({
                    geometry: {
                        type: "Point", // тип геометрии - точка
                        coordinates: [55.8, 37.8] // координаты точки
                    }
                });

                map.value.geoObjects.add(myGeoObject);
            });
        }

        let scriptYandexMap = document.createElement('script');
        scriptYandexMap.setAttribute('src', 'https://api-maps.yandex.ru/2.1/?lang=ru_RU&apikey=465efea3-a9a7-4ee1-93e8-83044cbd69ab');
        document.head.appendChild(scriptYandexMap);

        // Инициализировать яндекс карту
        scriptYandexMap.addEventListener("load", initializeYandexMap);
    });
</script>

<style scoped>
    .organizations__inner{
        grid-template-columns: 1fr 1fr;
    }
    .organization__item{
        background-color: var(--colorWhite);
        padding: 20px;
        border-radius: 10px;
        box-shadow: var(--colorBlueLight) 0 0 50px -30px;
        cursor: pointer;
        gap: 5px;
        transition: transform .3s ease;
    }
    .organization__item:hover{
        transform: scale(1.01);
    }
    .organization__sticky{
        position: relative;
    }
    #yandex-map {
        border-radius: 10px;
        height: 80vh;
        position: sticky;
        top: 10vh;
    }
</style>