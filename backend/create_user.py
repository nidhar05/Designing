import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'elearning.settings')
django.setup()

from django.contrib.auth.models import User
from api.models import UserProfile

# Create test user
if not User.objects.filter(username='testuser').exists():
    user = User.objects.create_user(username='testuser', email='test@example.com', password='testpass123')
    UserProfile.objects.create(user=user)
    print(f'Created user: {user.username}')
else:
    print('User already exists')
