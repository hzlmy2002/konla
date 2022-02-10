<template>
    <footer class="page-footer footer-style">
        <div class="px-4">
            <p class="small">KONLA | Copyright &copy; 2021-{{ currentYear }} | Team: Suraj Kothari, Bartosz Grabek, Harry Lei</p>
        </div>
    </footer>
</template>

<script>
export default {
    name: "PageFooter",
    data() {
        return {
            currentYear: new Date().getFullYear()
        }
    }
};
</script>

<style scoped>
.footer-style {
    height: 60px;
    line-height: 60px;
    background-color: #607D8B;
    color: #ECEFF1;
}

.small {
    font-size: 14px;
}
</style>
