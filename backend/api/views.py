from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Course, Enrollment, Wishlist, UserProfile, Progress, Video
from .serializers import CourseSerializer, EnrollmentSerializer, WishlistSerializer, UserSerializer, ProgressSerializer, EnrollmentDetailSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = Course.objects.all()
        category = self.request.query_params.get('category', None)
        if category is not None:
            queryset = queryset.filter(category=category)
        return queryset

@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)
    if user:
        login(request, user)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
@permission_classes([AllowAny])
def signup_view(request):
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')
    first_name = request.data.get('first_name', '')
    last_name = request.data.get('last_name', '')

    if User.objects.filter(username=username).exists():
        return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create_user(
        username=username,
        email=email,
        password=password,
        first_name=first_name,
        last_name=last_name
    )
    UserProfile.objects.create(user=user)
    serializer = UserSerializer(user)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
@permission_classes([AllowAny])
def logout_view(request):
    logout(request)
    return Response({'message': 'Logged out successfully'})

@api_view(['GET'])
@permission_classes([AllowAny])
def user_profile(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([AllowAny])
def enroll_course(request):
    course_id = request.data.get('course_id')
    try:
        course = Course.objects.get(id=course_id)
        enrollment, created = Enrollment.objects.get_or_create(
            user=request.user,
            course=course
        )
        if created:
            serializer = EnrollmentSerializer(enrollment)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'Already enrolled'}, status=status.HTTP_200_OK)
    except Course.DoesNotExist:
        return Response({'error': 'Course not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes([AllowAny])
def my_enrollments(request):
    # For now, return empty list since we don't have proper auth
    return Response([])

@api_view(['POST'])
@permission_classes([AllowAny])
def add_to_wishlist(request):
    course_id = request.data.get('course_id')
    try:
        course = Course.objects.get(id=course_id)
        wishlist_item, created = Wishlist.objects.get_or_create(
            user=request.user,
            course=course
        )
        if created:
            serializer = WishlistSerializer(wishlist_item)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'Already in wishlist'}, status=status.HTTP_200_OK)
    except Course.DoesNotExist:
        return Response({'error': 'Course not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes([AllowAny])
def my_wishlist(request):
    wishlist_items = Wishlist.objects.filter(user=request.user)
    serializer = WishlistSerializer(wishlist_items, many=True)
    return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes([AllowAny])
def remove_from_wishlist(request, course_id):
    try:
        wishlist_item = Wishlist.objects.get(user=request.user, course_id=course_id)
        wishlist_item.delete()
        return Response({'message': 'Removed from wishlist'}, status=status.HTTP_204_NO_CONTENT)
    except Wishlist.DoesNotExist:
        return Response({'error': 'Not in wishlist'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes([AllowAny])
def enrollment_detail(request, enrollment_id):
    """Get detailed enrollment information including progress"""
    try:
        enrollment = Enrollment.objects.get(id=enrollment_id, user=request.user)
        serializer = EnrollmentDetailSerializer(enrollment)
        return Response(serializer.data)
    except Enrollment.DoesNotExist:
        return Response({'error': 'Enrollment not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@permission_classes([AllowAny])
def mark_video_watched(request):
    """Mark a video as watched for progress tracking"""
    video_id = request.data.get('video_id')
    enrollment_id = request.data.get('enrollment_id')
    
    try:
        video = Video.objects.get(id=video_id)
        enrollment = Enrollment.objects.get(id=enrollment_id, user=request.user)
        
        progress, created = Progress.objects.get_or_create(
            user=request.user,
            video=video,
            enrollment=enrollment,
            defaults={'watched': True}
        )
        
        if not created:
            progress.watched = True
            from django.utils import timezone
            progress.watched_at = timezone.now()
            progress.save()
        
        serializer = ProgressSerializer(progress)
        return Response(serializer.data, status=status.HTTP_201_CREATED if created else status.HTTP_200_OK)
    except (Video.DoesNotExist, Enrollment.DoesNotExist):
        return Response({'error': 'Video or enrollment not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@permission_classes([AllowAny])
def mark_video_unwatched(request):
    """Mark a video as unwatched"""
    video_id = request.data.get('video_id')
    enrollment_id = request.data.get('enrollment_id')
    
    try:
        video = Video.objects.get(id=video_id)
        enrollment = Enrollment.objects.get(id=enrollment_id, user=request.user)
        
        progress = Progress.objects.get(
            user=request.user,
            video=video,
            enrollment=enrollment
        )
        progress.watched = False
        progress.watched_at = None
        progress.save()
        
        serializer = ProgressSerializer(progress)
        return Response(serializer.data)
    except Progress.DoesNotExist:
        return Response({'error': 'Progress not found'}, status=status.HTTP_404_NOT_FOUND)
    except (Video.DoesNotExist, Enrollment.DoesNotExist):
        return Response({'error': 'Video or enrollment not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes([AllowAny])
def course_progress(request, enrollment_id):
    """Get detailed progress for a specific course enrollment"""
    try:
        enrollment = Enrollment.objects.get(id=enrollment_id, user=request.user)
        videos = enrollment.course.videos.all()
        progress_records = Progress.objects.filter(enrollment=enrollment)
        
        # Create a list of videos with their progress status
        progress_list = []
        total_videos = videos.count()
        watched_count = 0
        
        for video in videos:
            progress = progress_records.filter(video=video).first()
            is_watched = progress.watched if progress else False
            if is_watched:
                watched_count += 1
            progress_list.append({
                'video_id': video.id,
                'video_title': video.title,
                'video_url': video.video_url,
                'duration_seconds': video.duration_seconds,
                'order': video.order,
                'watched': is_watched,
                'watched_at': progress.watched_at if progress else None,
            })
        
        completion_percentage = (watched_count / total_videos * 100) if total_videos > 0 else 0
        
        return Response({
            'enrollment_id': enrollment_id,
            'course_title': enrollment.course.title,
            'total_videos': total_videos,
            'watched_videos': watched_count,
            'completion_percentage': round(completion_percentage, 2),
            'videos': progress_list,
        })
    except Enrollment.DoesNotExist:
        return Response({'error': 'Enrollment not found'}, status=status.HTTP_404_NOT_FOUND)
