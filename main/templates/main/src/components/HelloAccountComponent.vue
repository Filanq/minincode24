<template>
    <h2 class="h3 mb-50"><span style="font-size: inherit;">Личный кабинет</span> <span style="color: var(--colorBlueMain); font-size: inherit;">{{ props.name }}</span></h2>
</template>

<script setup>
    const props = defineProps({
        name: {
            type: String,
            required: true,
        }
    });
</script>

<style scoped>

</style>