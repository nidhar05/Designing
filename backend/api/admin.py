from django.contrib import admin
from .models import Course, Video, UserProfile, Enrollment, Wishlist, Progress

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'instructor', 'category', 'price', 'rating', 'created_at']
    list_filter = ['category', 'created_at']
    search_fields = ['title', 'instructor']

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['title', 'course', 'duration_seconds', 'order', 'created_at']
    list_filter = ['course', 'created_at']
    search_fields = ['title', 'course__title']

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'bio']
    search_fields = ['user__username']

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ['user', 'course', 'enrolled_at', 'completed']
    list_filter = ['completed', 'enrolled_at']
    search_fields = ['user__username', 'course__title']

@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ['user', 'course', 'added_at']
    list_filter = ['added_at']
    search_fields = ['user__username', 'course__title']

@admin.register(Progress)
class ProgressAdmin(admin.ModelAdmin):
    list_display = ['user', 'video', 'enrollment', 'watched', 'watched_at', 'updated_at']
    list_filter = ['watched', 'created_at', 'updated_at']
    search_fields = ['user__username', 'video__title', 'enrollment__course__title']
