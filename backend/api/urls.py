from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'courses', views.CourseViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/login/', views.login_view, name='login'),
    path('auth/signup/', views.signup_view, name='signup'),
    path('auth/logout/', views.logout_view, name='logout'),
    path('auth/profile/', views.user_profile, name='profile'),
    path('enroll/', views.enroll_course, name='enroll'),
    path('my-enrollments/', views.my_enrollments, name='my-enrollments'),
    path('enrollment/<int:enrollment_id>/', views.enrollment_detail, name='enrollment-detail'),
    path('wishlist/add/', views.add_to_wishlist, name='add-to-wishlist'),
    path('wishlist/', views.my_wishlist, name='my-wishlist'),
    path('wishlist/remove/<int:course_id>/', views.remove_from_wishlist, name='remove-from-wishlist'),
    path('progress/mark-watched/', views.mark_video_watched, name='mark-video-watched'),
    path('progress/mark-unwatched/', views.mark_video_unwatched, name='mark-video-unwatched'),
    path('progress/<int:enrollment_id>/', views.course_progress, name='course-progress'),
]