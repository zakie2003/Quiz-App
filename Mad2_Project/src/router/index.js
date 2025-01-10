import { createRouter, createWebHistory } from 'vue-router'
import index from '@/views/Index.vue';
import NavSignIn from '@/views/SignIn.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Index',
      component: index,
      meta: { requiresAuth: false }
    },
    {
      path:'/signin',
      name:'Signin',
      component:NavSignIn,
      meta: { requiresAuth: false }
    },
    {
      path: '/admin/home',
      name: 'AdminHome',
      component: () => import('../views/Home.vue'),
      meta: { requiresAuth: true } 
    },
    {
      path: '/admin/create_subject',
      name: 'CreateSubject',
      component: () => import('../views/CreateSubject.vue'),
      meta: { requiresAuth: true } 
    },
    {
      path: '/admin/create_chapter',
      name: 'CreateChapter',
      component: () => import('../views/CreateChapter.vue'),
      meta: { requiresAuth: true }
    },
    {
      path: '/admin/edit_chapter',
      name: 'EditChapter',
      component: () => import('../views/EditChapter.vue'),
      meta: { requiresAuth: true }
    },
    {
      path: '/admin/quiz_dashboard',
      name: 'QuizDashboard',
      component: () => import('../views/QuizBoard.vue'),
      meta: { requiresAuth: true }
    },
    {
      path: '/admin/create_quiz',
      name: 'CreateQuiz',
      component: ()=> import('../views/CreateQuiz.vue'),
      meta: { requiresAuth: true }
    },
    {
      path: '/admin/add_question',
      name: "AddQuestion",
      component: () => import('../views/AddQuestion.vue'),
      meta: { requiresAuth: true }
    }

    
  ],
})

// Add a global navigation guard
router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    // Check if the user is authenticated
    const token = sessionStorage.getItem('token');
    if (!token) {
      next({ name: 'Signin' }); // Redirect to the Signin page if not authenticated
    } else {
      next(); // Proceed to the route if authenticated
    }
  } else {
    next(); // Proceed to the route if it does not require authentication
  }
});

export default router
