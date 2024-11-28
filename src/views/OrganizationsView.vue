<template>
    <main>
        <section class="section organization__section">
            <div class="container organizations__container">
                <h2 class="h2 w-600"></h2>
            </div>
        </section>
    </main>
</template>

<script setup>

</script>

<style scoped>
main {
    display: flex;
}
.left-part {
    width: 50%;
    height: 100%;
    background-color: var(--colorWhite);
}
.right-part {
    width: 50%;
    height: 100%;
    background-color: var(--colorGrey);
}
.right-part > img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}
</style>