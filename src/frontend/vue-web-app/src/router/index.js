import { createWebHistory, createRouter } from "vue-router";
import Upload from "@/views/Upload.vue";
import Analysis from "@/views/Analysis.vue";

const routes = [
  {
    path: "/",
    name: "Upload",
    component: Upload
  },

  {
    path: "/analysis",
    name: "Analysis",
    component: Analysis
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
