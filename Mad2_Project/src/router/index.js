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
      component: () => import('../views/admin/Home.vue'),
      meta: { requiresAuth: true } 
    },
    {
      path: '/admin/create_subject',
      name: 'CreateSubject',
      component: () => import('../views/admin/CreateSubject.vue'),
      meta: { requiresAuth: true } 
    },
    {
      path: '/admin/create_chapter',
      name: 'CreateChapter',
      component: () => import('../views/admin/CreateChapter.vue'),
      meta: { requiresAuth: true }
    },
    {
      path: '/admin/edit_chapter',
      name: 'EditChapter',
      component: () => import('../views/admin/EditChapter.vue'),
      meta: { requiresAuth: true }
    },
    {
      path: '/admin/quiz_dashboard',
      name: 'QuizDashboard',
      component: () => import('../views/admin/QuizBoard.vue'),
      meta: { requiresAuth: true }
    },
    {
      path: '/admin/create_quiz',
      name: 'CreateQuiz',
      component: ()=> import('../views/admin/CreateQuiz.vue'),
      meta: { requiresAuth: true }
    },
    {
      path: '/admin/add_question',
      name: "AddQuestion",
      component: () => import('../views/admin/AddQuestion.vue'),
      meta: { requiresAuth: true }
    },
    {
      path: '/admin/edit_question/:id',
      name: "EditQuestion",
      component: () => import('../views/admin/EditQuestion.vue'),
      meta: { requiresAuth: true }
    },
    {
      path: '/admin/quiz_preview/:chapter_name/:quiz_id',
      name: "QuizPreview",
      component: () => import('../views/admin/QuizPreview.vue'),
      meta: { requiresAuth: true }
    },
    {
      path: '/:pathMatch(.*)*',
      name: 'NotFound',
      component: () => import('../views/NotFound.vue'),
      meta: { requiresAuth: false }
    },


    {
      path: '/user/home',
      name: 'UserHome',
      component: () => import('../views/user/Home.vue'),
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
