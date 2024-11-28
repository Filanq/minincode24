<template>
  <HeaderComponent />
    <main>
        <section class="section organization__section">
            <div class="container organizations__container gap-50">
                <h2 class="h3 w-700 organizations__title">Откройте для себя новые возможности!</h2>
              <input type="text" class="organization__input input js-s width-100" placeholder="Поиск">
                <div class="organizations__inner gap-25 grid width-100">
                    <div class="organizations__wrap grid grid-column gap-10 ac-s width-100">
                        <div class="organization__item grid grid-column ji-s ac-s">
                            <h3 class="h5 w-500 organization-item__title">Заголовок организации</h3>
                            <span class="h7 w-300 organization-item__address">ул. Пушкина д. Колотушкина</span>
                        </div>
                        <div class="organization__item grid grid-column ji-s ac-s">
                            <h3 class="h5 w-500 organization-item__title">Заголовок организации</h3>
                            <span class="h7 w-300 organization-item__address">ул. Пушкина д. Колотушкина</span>
                        </div>
                        <div class="organization__item grid grid-column ji-s ac-s">
                            <h3 class="h5 w-500 organization-item__title">Заголовок организации</h3>
                            <span class="h7 w-300 organization-item__address">ул. Пушкина д. Колотушкина</span>
                        </div>
                        <div class="organization__item grid grid-column ji-s ac-s">
                            <h3 class="h5 w-500 organization-item__title">Заголовок организации</h3>
                            <span class="h7 w-300 organization-item__address">ул. Пушкина д. Колотушкина</span>
                        </div>
                        <div class="organization__item grid grid-column ji-s ac-s">
                            <h3 class="h5 w-500 organization-item__title">Заголовок организации</h3>
                            <span class="h7 w-300 organization-item__address">ул. Пушкина д. Колотушкина</span>
                        </div>
                        <div class="organization__item grid grid-column ji-s ac-s">
                            <h3 class="h5 w-500 organization-item__title">Заголовок организации</h3>
                            <span class="h7 w-300 organization-item__address">ул. Пушкина д. Колотушкина</span>
                        </div>
                        <div class="organization__item grid grid-column ji-s ac-s">
                            <h3 class="h5 w-500 organization-item__title">Заголовок организации</h3>
                            <span class="h7 w-300 organization-item__address">ул. Пушкина д. Колотушкина</span>
                        </div>
                      <div class="organization__item grid grid-column ji-s ac-s">
                        <h3 class="h5 w-500 organization-item__title">Заголовок организации</h3>
                        <span class="h7 w-300 organization-item__address">ул. Пушкина д. Колотушкина</span>
                      </div>
                      <div class="organization__item grid grid-column ji-s ac-s">
                        <h3 class="h5 w-500 organization-item__title">Заголовок организации</h3>
                        <span class="h7 w-300 organization-item__address">ул. Пушкина д. Колотушкина</span>
                      </div>
                      <div class="organization__item grid grid-column ji-s ac-s">
                        <h3 class="h5 w-500 organization-item__title">Заголовок организации</h3>
                        <span class="h7 w-300 organization-item__address">ул. Пушкина д. Колотушкина</span>
                      </div>
                    </div>
                    <div class="organization__sticky grid grid-column ac-s">
                      <div id="organizations__map" class="width-100 organizations__map"></div>
                    </div>
                </div>
            </div>
        </section>

      <section class="section news__section">
        <div class="container news__container gap-50">
          <h2 class="h3 ta-c"><span class="blue">_</span>Новости</h2>
          <div class="news__main_wrap gap-25">
            <router-link :to="cur_news.link" target="_blank" class="news__main_block" v-for="cur_news in news">
              <img src="#" :key="cur_news.id" :alt="cur_news.title">
              <h5>{{ cur_news.title }}</h5>
              <div class="news__info">
                <div class="news-info__item">{{ cur_news.organization.name }}</div>
                <div class="news-info__item">{{ cur_news.date }}</div>
              </div>
            </router-link>
          </div>
        </div>
      </section>

      <section class="section events__section">
        <div class="container events__container gap-50">
          <h2 class="h3 ta-c"><span class="blue">_</span>События</h2>
          <div class="events__main_wrap gap-25">
            <router-link :to="cur_events.link" target="_blank" class="events__main_block" v-for="cur_events in events">
              <img src="#" :key="cur_events.id" :alt="cur_events.title">
              <h5>{{ cur_events.title }}</h5>
              <div class="events__info">
                <div class="events-info__item">{{ cur_events.organization.name }}</div>
                <div class="events-info__item">{{ cur_events.datetime }}</div>
              </div>
            </router-link>
          </div>
        </div>
      </section>
    </main>
</template>

<script setup>
import {onMounted, ref} from "vue";
import HeaderComponent from "@/components/HeaderComponent.vue";

let map = null;

onMounted(() => {
  function initializeYandexMap() {
    ymaps.ready(async () => {
      map = new ymaps.Map("organizations__map", {
        center: [56.297462, 43.919970],
        zoom: 11
      });
      let geocoder = ymaps.geocode("г. Нижний Новгород, ул. Белинского д. 4");
      geocoder.then(
          function (res) {
            // Получаем первую найденную позицию
            let firstGeoObject = res.geoObjects.get(0);

            if (firstGeoObject) {
              // Получаем координаты
              let coordinates = firstGeoObject.geometry._coordinates;

              var placemark = new ymaps.Placemark(coordinates, {
                balloonContent: "asdfasfsdf",
              }, {
                iconImageHref: '/img/organization.svg',
                iconLayout: 'default#imageWithContent',
                iconImageSize: [36, 36],
                iconImageOffset: [-24, -24],
                iconContentOffset: [15, 15]
              });

              // Добавление метки на карту
              map.geoObjects.add(placemark);
            } else {
              alert('Адрес не найден');
            }
          },
          function (err) {
            console.error('Ошибка геокодирования:', err);
          }
      );
    });
  }

  let scriptYandexMap = document.createElement('script');
  scriptYandexMap.setAttribute('src', 'https://api-maps.yandex.ru/2.1/?lang=ru_RU&apikey=465efea3-a9a7-4ee1-93e8-83044cbd69ab');
  document.head.appendChild(scriptYandexMap);

  // Инициализировать яндекс карту
  scriptYandexMap.addEventListener("load", initializeYandexMap);
});

const news = ref([{id: 0, title: 'title', img: '', organization: {name: 'it-cube'}, date: '11-11-1111'}]);

function getNews() {
  news.value = [
    {id: 0, title: 'title', img: '', organization: {name: 'it-cube'}, date: '11-11-1111'},
    {id: 0, title: 'title', img: '', organization: {name: 'it-cube'}, date: '11-11-1111'},
    {id: 0, title: 'title', img: '', organization: {name: 'it-cube'}, date: '11-11-1111'},
  ];
}
getNews();


const events = ref([{id: 0, title: 'title', img: '', organization: {name: 'it-cube'}, datetime: '11-11-1111'}]);

function getEvents() {
  events.value = [
    {id: 0, title: 'title', img: '', organization: {name: 'it-cube'}, datetime: '11-11-1111'},
    {id: 0, title: 'title', img: '', organization: {name: 'it-cube'}, datetime: '11-11-1111'},
    {id: 0, title: 'title', img: '', organization: {name: 'it-cube'}, datetime: '11-11-1111'},
  ];
}
getEvents();
</script>

<style scoped>
  .organization__section{
    padding-top: 150px;
  }
    .organizations__inner{
        grid-template-columns: 1fr 1fr;
    }
    .organization__item{
        border: 1px solid var(--colorBlueMain);
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
    .organizations__map{
        height: 80vh;
        position: sticky;
        top: 15vh;
      border-radius: 10px;
      overflow: hidden;
    }

  input {
    border-radius: 10px;
    border: solid #000 1px;
    padding: 10px;
    background-color: rgba(157, 78, 221, 0.2);
    color: white;
  }
  input:focus {
    outline: none;
  }
  .events__section{
    padding-top: 150px;
  }
  .events__container{
    display: flex;
    flex-direction: column;
    gap: 50px;
  }

  .events__main_wrap{
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  }

  .events__main_block{
    display: flex;
    flex-direction: column;
    gap: 12px;
    text-decoration: none;
  }

  .events__main_block > img{
    width: 100%;
    height: 300px;
    object-fit: cover;
    border-radius: 20px;
    pointer-events: none;
  }

  .events__main_block > h5{
    padding: 0 5px;
  }

  .events__info{
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
  }

  .events-info__item{
    font-size: 18px;
    padding: 7px 14px;
    border-radius: 50px;
    outline: 1px solid rgb(49, 49, 49);
  }
  .news__section{
    padding-top: 150px;
  }
  .news__container{
    display: flex;
    flex-direction: column;
    gap: 50px;
  }

  .news__main_wrap{
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  }

  .news__main_block{
    display: flex;
    flex-direction: column;
    gap: 12px;
    text-decoration: none;
  }

  .news__main_block > img{
    width: 100%;
    height: 300px;
    object-fit: cover;
    border-radius: 20px;
    pointer-events: none;
  }

  .news__main_block > h5{
    padding: 0 5px;
  }

  .news__info{
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
  }

  .news-info__item{
    font-size: 18px;
    padding: 7px 14px;
    border-radius: 50px;
    outline: 1px solid rgb(49, 49, 49);
  }
</style>