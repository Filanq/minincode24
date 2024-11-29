<template>
    <!-- у меня и опыт -->
    <div class="section skills__section">
        <div class="container skills__container">
            <div class="skills_block--sticky_parent">
                <div class="skills_block skills_block--sticky">
                    <h2 class="h2"><span class="blue h2">_</span>Компетенции <span class="h2 blue">&</span> Мероприятия</h2>
                    <div class="skills__inner">
                        <div class="skills-inner__img_wrap">
                            <img class="skills-inner__img" :src="skill_active.icon" :alt="skill_active.title">
                        </div>
                        <p class="skills-inner__text"><span class="w-500 h6">{{ skill_active.title }}</span> <br> {{ skill_active.description }}</p>
                    </div>
                    <h3 class="h3">Компетенции</h3>
                    <div class="skills_wrap-skils">
                        <div @click="setActiveSkill(skills_datum.id)" class="skills_block-skils" :class="{'skills_block-skils_active': skill_active.id === skills_datum.id}" :key="skills_datum.id" v-for="skills_datum in skills_data">
                            <img :src="skills_datum.icon" :alt="skills_datum.title">
                        </div>
                    </div>
                </div>
            </div>

            <div class="skills_block">
                <div class="skills_block-experience">
                    <h3 class="h3">Мероприятия</h3>
                </div>
                <div class="skills_block-experience" v-for="event in events">
                    <div class="experience">
                        <p>{{ event.datetime.split('T')[0] }}</p>
                        <div class="experience_description">
                            <h4 class="h4"><span class="blue">«</span> {{ event.title }} <span class="blue">»</span></h4>
                            <p>{{ event.text }}</p>
                            <router-link :to="{name: 'event_page', params: {id: event.id}}" class="btn">Подробнее ></router-link>
                        </div>
                    </div>
                </div>
<!--                <div class="skills_block-experience">-->
<!--                    <div class="experience">-->
<!--                        <p>16 декабря</p>-->
<!--                        <div class="experience_description">-->
<!--                            <h4 class="h4"><span class="blue">«</span> Основы кибербезопасности <span class="blue">»</span></h4>-->
<!--                            <p>Практический семинар для студентов колледжей, посвященный вопросам защиты информации в интернете. Научитесь защищать свои данные и узнайте, как избежать распространенных угроз. </p>-->
<!--                            <router-link :to="{name: 'home'}" class="btn">Подробнее ></router-link>-->
<!--                        </div>-->
<!--                    </div>-->
<!--                </div>-->
<!--                <div class="skills_block-experience">-->
<!--                    <div class="experience">-->
<!--                        <p>05 декабря</p>-->
<!--                        <div class="experience_description">-->
<!--                            <h4 class="h4"><span class="blue">«</span> JavaScript: от простого к сложному <span class="blue">»</span></h4>-->
<!--                            <p>Онлайн-курс для школьников, желающих освоить один из самых востребованных языков фронтенд-разработки. Начните с азов и постепенно переходите к более сложным концепциям.</p>-->
<!--                            <router-link :to="{name: 'home'}" class="btn">Подробнее ></router-link>-->
<!--                        </div>-->
<!--                    </div>-->
<!--                </div>-->
<!--                <div class="skills_block-experience">-->
<!--                    <div class="experience">-->
<!--                        <p>08 декабря</p>-->
<!--                        <div class="experience_description">-->
<!--                            <h4 class="h4"><span class="blue">«</span> Конференция по искусственному интеллекту <span class="blue">»</span></h4>-->
<!--                            <p>Встреча экспертов и энтузиастов AI, где обсудим последние достижения и перспективы применения технологий искусственного интеллекта. Участие бесплатное, регистрация обязательна. </p>-->
<!--                            <router-link :to="{name: 'home'}" class="btn">Подробнее ></router-link>-->
<!--                        </div>-->
<!--                    </div>-->
<!--                </div>-->
            </div>           
        </div>
    </div>
</template>

<script setup lang="ts">
    import { type Ref, ref } from "vue";
    import axios from "axios";

    // Skills Array
    const skills_data: Ref<Object[]> = ref([]);

    // Active Skill
    const skill_active: Ref<Object> = ref({id: 0, title: '', icon: '', description: ''});

    const getSkillsData = (): void => {
        skills_data.value = [
            { id: 1, title: 'Разработка VR/AR-приложений', icon: '/assets/skills/vr-goggles.svg', description: 'Погружает участников в мир виртуальной реальности, где они учатся создавать и управлять своими собственными 3D-средами. Используется современное программное обеспечение и технические средства.' },
            { id: 2, title: 'Программирование роботов', icon: '/assets/skills/roboto.svg', description: 'Программа раскрывает творческий потенциал детей, помогает понять окружающий мир и стимулирует интерес к техническим профессиям. Участники учатся конструировать и программировать роботов.' },
            { id: 3, title: 'Программирование на Python', icon: '/assets/skills/3d.svg', description: 'Курс посвящен изучению популярного языка Python, который используется во многих отраслях, от веб-разработки до машинного обучения. Рассматриваются основные преимущества языка и его применение.' },
            { id: 4, title: 'Мобильная разработка', icon: '/assets/skills/mobile.svg', description: 'Для любителей компьютерных игр, желающих попробовать себя в создании собственных проектов. Курс сочетает творчество и технические аспекты разработки игр.' },
            { id: 5, title: 'Системное администрирование', icon: '/assets/skills/secure-shield.svg', description: 'Обучает навыкам работы с компьютерным и сетевым оборудованием, установке операционной системы и устранению неисправностей. Программа полезна для тех, кто хочет лучше понимать устройство компьютеров' },
            { id: 6, title: 'Программирование на Scratch', icon: '/assets/skills/scratch.svg', description: 'Дети осваивают визуальное программирование через игровые задания, развивая логику и креативность. Итогом становится собственная игра, мультфильм или интерактивная книга.' },
            { id: 7, title: 'Основы программирования на языке С++', icon: '/assets/skills/marketing.svg', description: 'Изучение одного из старейших и наиболее мощных языков программирования. Курс подходит для начинающих программистов, заинтересованных в создании сложных программных продуктов.' },
            { id: 8, title: 'Искусственный интеллект ', icon: '/assets/skills/AI.svg', description: 'Введение в основы ИИ, включая знакомство с ключевыми технологиями и использованием Python для практических задач. Подходит для подростков, увлеченных современными технологиями.' },
            { id: 9, title: 'Графический дизайн', icon: '/assets/skills/dexign.svg', description: 'Осваиваются инструменты для создания графики, таких как векторные и растровые редакторы. Учащиеся разрабатывают элементы фирменного стиля, упаковки и верстки.' },
            { id: 10, title: 'Веб-технологии', icon: '/assets/skills/web.svg', description: 'Участники изучают инструменты для дизайна и верстки веб-сайтов, такие как Photoshop, Illustrator, Figma и другие. Они учатся создавать макеты, адаптивные дизайны и анимации.' }
        ];

        // Set Active Skill
        skill_active.value = Object.assign(skills_data.value[0], {});
    };

    // Get Skills
    getSkillsData();
    const events: Ref<Object[]> = ref([{}]);

    axios.get(window.origin + '/api/events').then(res => {
        events.value = res.data.slice(0, 5);
    });


    // Set Active Skill on Click Function
    function setActiveSkill(id: number): void {
        skill_active.value = Object.assign(skills_data.value.filter((skill: Skill) => {
            return skill.id === id;
        })[0], {});
    }
</script>
<style>
    .skills__container{
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 100px;
    }

    .skills_block{
        display: flex;
        flex-direction: column;
        gap: 30px;
    }

    .skills_block--sticky{
        position: sticky;
    }

    .skills_wrap-skils{
        display: flex;
        width: 90%;
        flex-wrap: wrap;
        /* grid-template-columns: repeat(7, 1fr); */
        gap: 15px;
    }

    .skills_block-skils{
        width: 70px;
        height: 70px;
        border: 3px solid var(--colorWhite);
        border-radius: 18px;
        display: flex;
        justify-content: center;
        align-items: center;
        cursor: pointer;
        position: relative;
        overflow: hidden;
        transition: .5s;
    }

    .skills_block-skils:hover, .skills_block-skils_active{
        border: 3px solid var(--colorBlueMain);
    }

    .skills_block-skils::before {
        content: "";
        position: absolute;
        top: 50%;
        left: 50%;
        width: 0px;
        height: 0px;
        border-radius: 18px;
        background: var(--colorBlueMain);
        transition: .5s;
        z-index: 2;
    }

    .skills_block-skils:hover::before, .skills_block-skils_active::before {
        width: 130%;
        height: 130%;
        top: -10px;
        left: -10px;
        transition: .5s;
    }

    .skills_block-skils > img{
        width: 50%;
        z-index: 3;
    }

    .skills_block-experience{
        border-bottom: 3px solid var(--colorBlueMain);
        padding-bottom: 50px;
    }

    .experience{
        display: flex;
        gap: 50px;
    }

    .experience_description{
        display: flex;
        flex-direction: column;
        gap: 20px;
    }

    .experience > p{
        margin-top: 10px;
}

    .skills_block--sticky_parent{
        position: relative;
    }
    .skills_block--sticky{
        top: 15vh;
    }
    .skills-inner__img_wrap{
        width: 100px;
        height: 100px;
        border: 3px solid var(--colorWhite);
        border-radius: 18px;
        display: grid;
        grid-auto-flow: row;
        align-content: center;
        justify-items: center;
    }
    .skills-inner__img{
        width: 60%;
    }
    .skills__inner{
        display: grid;
        grid-auto-flow: row;
        justify-items: start;
        align-content: start;
        gap: 25px;
    }
    .skills-inner__text{
        font-size: 20px;
    }

    @media(max-width: 1280px){
        .experience{
            flex-direction: column;
        }

        .skills__container{
            gap: 40px;
        }

        .skills__container{
            grid-template-columns: 1fr;
        }
    }
</style>
