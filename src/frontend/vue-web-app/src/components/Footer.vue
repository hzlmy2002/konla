<template>
    <footer class="page-footer py-3 footer-style" :style="footerStyle">
        <div class="px-3">
            <p class="small">KONLA | Copyright &copy; 2021-{{ currentYear }} | Team: Suraj Kothari, Bartosz Grabek, Harry Lei</p>
        </div>
    </footer>
</template>

<script>
export default {
    name: "PageFooter",
    props: {
        footerStyle: Object
    },

    data() {
        return {
            currentYear: new Date().getFullYear()
        }
    }
};
</script>

<style scoped>
.footer-style {
    position: relative;
    bottom: 0;
    left: 0;
    right: 0;
    background-color: #607D8B;
    color: #ECEFF1;
}

.small {
    font-size: 14px;
}
</style>
