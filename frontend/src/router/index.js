import { createRouter, createWebHistory } from "vue-router";
import { useAuthStore } from "../stores/authStore";
import SignIn from "../auth/SigninPage.vue";
import IndexPage from "../main/IndexPage.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      redirect: "/signin",
    },
    {
      path: "/signin",
      name: "SignIn",
      component: SignIn,
    },
    {
      path: "/index",
      name: "Index",
      component: IndexPage,
      children: [
        {
          path: "dashboard",
          name: "Dashboard",
          component: () => import('../main/DashboardPage.vue'),
        },
        {
          path: "dashboard-1",
          name: "Teacher Dashboard",
          component: () => import('../main/TeacherDashboard.vue'),
        },
        {
          path: "dashboard-2",
          name: "Student Dashboard",
          component: () => import('../main/StudentDashboard.vue'),
        },
        {
          path: "add-student",
          name: "Add Student",
          component: () => import('../main/AddStudent.vue'),
        },
        {
          path: "list-student",
          name: "All Students",
          component: () => import('../main/ListStudent.vue'),
        },
        {
          path: "add-program",
          name: "Add Program",
          component: () => import('../main/AddProgram.vue'),
        },
        {
          path: "add-curriculum",
          name: "Add Curriculum",
          component: () => import('../main/AddCurriculum.vue'),
        },
        {
          path: "add-subject",
          name: "Add Subject",
          component: () => import('../main/AddSubject.vue'),
        },
      ],
      meta: {
        requiresAuth: true,
      },
    },
  ],
});

router.beforeEach((to, from, next) => {
  const authStore = useAuthStore();

  if (to.path === "/signin" && authStore.isAuthenticated) {
    next({ path: localStorage.getItem("savedPath") });
  } else if (to.matched.some((record) => record.meta.requiresAuth)) {
    if (!authStore.isAuthenticated) {
      next({ name: "SignIn" });
    } else {
      next();
    }
  } else {
    next();
  }
});

export default router;
