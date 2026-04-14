from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Course, UserProfile, Enrollment, Wishlist, Video, Progress

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = UserProfile
        fields = ['user', 'bio', 'avatar']

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'title', 'video_url', 'duration_seconds', 'order']

class CourseSerializer(serializers.ModelSerializer):
    videos = VideoSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = '__all__'

class EnrollmentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    course = CourseSerializer(read_only=True)
    user_id = serializers.IntegerField(write_only=True)
    course_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Enrollment
        fields = ['id', 'user', 'course', 'enrolled_at', 'completed', 'user_id', 'course_id']

class WishlistSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    course = CourseSerializer(read_only=True)
    user_id = serializers.IntegerField(write_only=True)
    course_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Wishlist
        fields = ['id', 'user', 'course', 'added_at', 'user_id', 'course_id']

class ProgressSerializer(serializers.ModelSerializer):
    video_title = serializers.CharField(source='video.title', read_only=True)
    
    class Meta:
        model = Progress
        fields = ['id', 'user', 'video', 'video_title', 'enrollment', 'watched', 'watched_at', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']

class EnrollmentDetailSerializer(serializers.ModelSerializer):
    """Serializer for enrollment with detailed progress information"""
    user = UserSerializer(read_only=True)
    course = CourseSerializer(read_only=True)
    user_id = serializers.IntegerField(write_only=True)
    course_id = serializers.IntegerField(write_only=True)
    progress_list = serializers.SerializerMethodField()
    completion_percentage = serializers.SerializerMethodField()
    
    class Meta:
        model = Enrollment
        fields = ['id', 'user', 'course', 'enrolled_at', 'completed', 'user_id', 'course_id', 'progress_list', 'completion_percentage']
    
    def get_progress_list(self, obj):
        """Get all progress records for this enrollment"""
        progress = Progress.objects.filter(enrollment=obj)
        return ProgressSerializer(progress, many=True).data
    
    def get_completion_percentage(self, obj):
        """Calculate the percentage of videos watched for this course"""
        total_videos = obj.course.videos.count()
        if total_videos == 0:
            return 0
        watched_videos = Progress.objects.filter(
            enrollment=obj,
            watched=True
        ).count()
        return round((watched_videos / total_videos) * 100, 2)