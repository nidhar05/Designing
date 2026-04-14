from django.core.management.base import BaseCommand
from api.models import Course, Video

class Command(BaseCommand):
    help = 'Populate database with sample courses and videos'

    def handle(self, *args, **options):
        courses_data = [
            # AI Courses
            {
                'title': 'AI Strategy & Governance',
                'instructor': 'School of AI',
                'category': 'ai',
                'description': 'Learn how to lead AI initiatives and build governance frameworks for safe deployment.',
                'price': 539.00,
                'rating': 4.5,
                'image_url': 'https://picsum.photos/300/180',
                'videos': [
                    {
                        'title': 'Introduction to AI Strategy',
                        'video_url': 'https://www.example.com/video/ai-strategy-1',
                        'duration_seconds': 420,
                        'order': 1,
                    },
                    {
                        'title': 'Governance Frameworks',
                        'video_url': 'https://www.example.com/video/ai-strategy-2',
                        'duration_seconds': 510,
                        'order': 2,
                    },
                ],
            },
            {
                'title': 'Test AI & LLM Apps',
                'instructor': 'Karthik KK',
                'category': 'ai',
                'description': 'Build and test intelligent applications using LLMs, prompt engineering, and evaluation methods.',
                'price': 519.00,
                'rating': 4.3,
                'image_url': 'https://picsum.photos/301/180',
                'videos': [
                    {
                        'title': 'LLM Testing Fundamentals',
                        'video_url': 'https://www.example.com/video/llm-testing-1',
                        'duration_seconds': 390,
                        'order': 1,
                    },
                    {
                        'title': 'Prompt Evaluation',
                        'video_url': 'https://www.example.com/video/llm-testing-2',
                        'duration_seconds': 470,
                        'order': 2,
                    },
                ],
            },
            {
                'title': 'Full Stack AI Engineer',
                'instructor': 'School of AI',
                'category': 'ai',
                'description': 'End-to-end AI product development including data pipelines, model deployment, and monitoring.',
                'price': 519.00,
                'rating': 4.3,
                'image_url': 'https://picsum.photos/302/180',
                'videos': [
                    {
                        'title': 'AI Architecture Overview',
                        'video_url': 'https://www.example.com/video/ai-stack-1',
                        'duration_seconds': 440,
                        'order': 1,
                    },
                    {
                        'title': 'Deploying AI Services',
                        'video_url': 'https://www.example.com/video/ai-stack-2',
                        'duration_seconds': 530,
                        'order': 2,
                    },
                ],
            },
            {
                'title': 'AI Engineering Masterclass',
                'instructor': 'School of AI',
                'category': 'ai',
                'description': 'Advance your AI engineering skills with scalable systems, MLOps, and model reliability.',
                'price': 569.00,
                'rating': 4.4,
                'image_url': 'https://picsum.photos/303/180',
                'videos': [
                    {
                        'title': 'MLOps Best Practices',
                        'video_url': 'https://www.example.com/video/ai-melops-1',
                        'duration_seconds': 500,
                        'order': 1,
                    },
                    {
                        'title': 'Model Reliability',
                        'video_url': 'https://www.example.com/video/ai-melops-2',
                        'duration_seconds': 480,
                        'order': 2,
                    },
                ],
            },
            # Python Courses
            {
                'title': 'Python for Beginners',
                'instructor': 'John Smith',
                'category': 'python',
                'description': 'Start your Python journey with basics, data types, and fundamental programming concepts.',
                'price': 499.00,
                'rating': 4.6,
                'image_url': 'https://picsum.photos/304/180',
                'videos': [
                    {
                        'title': 'Python Basics',
                        'video_url': 'https://www.example.com/video/python-basics-1',
                        'duration_seconds': 360,
                        'order': 1,
                    },
                    {
                        'title': 'Variables and Data Types',
                        'video_url': 'https://www.example.com/video/python-basics-2',
                        'duration_seconds': 450,
                        'order': 2,
                    },
                    {
                        'title': 'Control Flows',
                        'video_url': 'https://www.example.com/video/python-basics-3',
                        'duration_seconds': 420,
                        'order': 3,
                    },
                ],
            },
            {
                'title': 'Python Django Masterclass',
                'instructor': 'David Lee',
                'category': 'python',
                'description': 'Build production-grade Django applications with authentication, APIs, and deployment.',
                'price': 599.00,
                'rating': 4.5,
                'image_url': 'https://picsum.photos/305/180',
                'videos': [
                    {
                        'title': 'Getting Started with Django',
                        'video_url': 'https://www.example.com/video/django-1',
                        'duration_seconds': 410,
                        'order': 1,
                    },
                    {
                        'title': 'REST APIs in Django',
                        'video_url': 'https://www.example.com/video/django-2',
                        'duration_seconds': 520,
                        'order': 2,
                    },
                ],
            },
            {
                'title': 'Data Science with Python',
                'instructor': 'Andrew AI',
                'category': 'python',
                'description': 'Master data analysis, visualization, and machinLearn-app techniques with Python libraries.',
                'price': 699.00,
                'rating': 4.4,
                'image_url': 'https://picsum.photos/306/180',
                'videos': [
                    {
                        'title': 'NumPy and Pandas Basics',
                        'video_url': 'https://www.example.com/video/ds-python-1',
                        'duration_seconds': 480,
                        'order': 1,
                    },
                    {
                        'title': 'Data Visualization with Matplotlib',
                        'video_url': 'https://www.example.com/video/ds-python-2',
                        'duration_seconds': 420,
                        'order': 2,
                    },
                    {
                        'title': 'Introduction to MachinLearn-app',
                        'video_url': 'https://www.example.com/video/ds-python-3',
                        'duration_seconds': 550,
                        'order': 3,
                    },
                ],
            },
            {
                'title': 'Flask Web Development',
                'instructor': 'Code Academy',
                'category': 'python',
                'description': 'Build lightweight web applications with Flask, including templates, forms, and deployment.',
                'price': 529.00,
                'rating': 4.3,
                'image_url': 'https://picsum.photos/307/180',
                'videos': [
                    {
                        'title': 'Flask Fundamentals',
                        'video_url': 'https://www.example.com/video/flask-1',
                        'duration_seconds': 400,
                        'order': 1,
                    },
                    {
                        'title': 'Templates and Forms',
                        'video_url': 'https://www.example.com/video/flask-2',
                        'duration_seconds': 430,
                        'order': 2,
                    },
                    {
                        'title': 'Database Integration',
                        'video_url': 'https://www.example.com/video/flask-3',
                        'duration_seconds': 500,
                        'order': 3,
                    },
                ],
            },
            # Marketing Courses
            {
                'title': 'Digital Marketing Fundamentals',
                'instructor': 'Maya Patel',
                'category': 'marketing',
                'description': 'Learn the core channels of digital marketing, including SEO, social ads, and email strategy.',
                'price': 459.00,
                'rating': 4.5,
                'image_url': 'https://picsum.photos/312/180',
                'videos': [
                    {
                        'title': 'SEO Basics',
                        'video_url': 'https://www.example.com/video/marketing-seo-1',
                        'duration_seconds': 340,
                        'order': 1,
                    },
                    {
                        'title': 'Social Media Strategy',
                        'video_url': 'https://www.example.com/video/marketing-social-1',
                        'duration_seconds': 410,
                        'order': 2,
                    },
                ],
            },
            {
                'title': 'Content Marketing Mastery',
                'instructor': 'Aditi Rao',
                'category': 'marketing',
                'description': 'Create compelling content campaigns that generate leads, engagement, and brand trust.',
                'price': 529.00,
                'rating': 4.6,
                'image_url': 'https://picsum.photos/313/180',
                'videos': [
                    {
                        'title': 'Content Planning',
                        'video_url': 'https://www.example.com/video/marketing-content-1',
                        'duration_seconds': 385,
                        'order': 1,
                    },
                    {
                        'title': 'Measuring Campaign Performance',
                        'video_url': 'https://www.example.com/video/marketing-content-2',
                        'duration_seconds': 460,
                        'order': 2,
                    },
                ],
            },
            # Excel Courses
            {
                'title': 'Excel for Beginners',
                'instructor': 'Microsoft School',
                'category': 'excel',
                'description': 'Learn the fundamentals of Excel including formulas, formatting, and basic data management.',
                'price': 399.00,
                'rating': 4.6,
                'image_url': 'https://picsum.photos/308/180',
                'videos': [
                    {
                        'title': 'Excel Interface and Basics',
                        'video_url': 'https://www.example.com/video/excel-basics-1',
                        'duration_seconds': 300,
                        'order': 1,
                    },
                    {
                        'title': 'Formulas and Functions',
                        'video_url': 'https://www.example.com/video/excel-basics-2',
                        'duration_seconds': 380,
                        'order': 2,
                    },
                    {
                        'title': 'Formatting and Styling',
                        'video_url': 'https://www.example.com/video/excel-basics-3',
                        'duration_seconds': 320,
                        'order': 3,
                    },
                ],
            },
            {
                'title': 'Advanced Excel',
                'instructor': 'Office Pro',
                'category': 'excel',
                'description': 'Take your Excel skills further with advanced formulas, macros, and data analysis techniques.',
                'price': 499.00,
                'rating': 4.5,
                'image_url': 'https://picsum.photos/309/180',
                'videos': [
                    {
                        'title': 'Advanced Formulas',
                        'video_url': 'https://www.example.com/video/excel-advanced-1',
                        'duration_seconds': 420,
                        'order': 1,
                    },
                    {
                        'title': 'Pivot Tables',
                        'video_url': 'https://www.example.com/video/excel-advanced-2',
                        'duration_seconds': 460,
                        'order': 2,
                    },
                    {
                        'title': 'Macros and VBA Basics',
                        'video_url': 'https://www.example.com/video/excel-advanced-3',
                        'duration_seconds': 510,
                        'order': 3,
                    },
                ],
            },
            {
                'title': 'Excel Data Analysis',
                'instructor': 'Analytics Hub',
                'category': 'excel',
                'description': 'Analyze large datasets in Excel using advanced functions, statistical analysis, and forecasting.',
                'price': 549.00,
                'rating': 4.3,
                'image_url': 'https://picsum.photos/310/180',
                'videos': [
                    {
                        'title': 'Data Cleaning and Preparation',
                        'video_url': 'https://www.example.com/video/excel-analysis-1',
                        'duration_seconds': 440,
                        'order': 1,
                    },
                    {
                        'title': 'Statistical Analysis',
                        'video_url': 'https://www.example.com/video/excel-analysis-2',
                        'duration_seconds': 480,
                        'order': 2,
                    },
                    {
                        'title': 'Forecasting and Trends',
                        'video_url': 'https://www.example.com/video/excel-analysis-3',
                        'duration_seconds': 500,
                        'order': 3,
                    },
                ],
            },
            {
                'title': 'Excel Dashboard',
                'instructor': 'Excel Academy',
                'category': 'excel',
                'description': 'Build interactive Excel dashboards with charts, pivot tables, and dashboard design best practices.',
                'price': 459.00,
                'rating': 4.4,
                'image_url': 'https://picsum.photos/311/180',
                'videos': [
                    {
                        'title': 'Dashboard Planning',
                        'video_url': 'https://www.example.com/video/excel-dashboard-1',
                        'duration_seconds': 380,
                        'order': 1,
                    },
                    {
                        'title': 'Charts & Visualization',
                        'video_url': 'https://www.example.com/video/excel-dashboard-2',
                        'duration_seconds': 450,
                        'order': 2,
                    },
                ],
            },
        ]

        for course_data in courses_data:
            videos = course_data.pop('videos', [])
            course, created = Course.objects.get_or_create(
                title=course_data['title'],
                defaults=course_data
            )
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Created course: {course.title}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'Course already exists: {course.title}')
                )

            for video_data in videos:
                video, video_created = Video.objects.get_or_create(
                    course=course,
                    title=video_data['title'],
                    defaults=video_data,
                )
                if video_created:
                    self.stdout.write(
                        self.style.SUCCESS(f'  Added video: {video.title}')
                    )
                else:
                    self.stdout.write(
                        self.style.WARNING(f'  Video already exists: {video.title}')
                    )

        self.stdout.write(
            self.style.SUCCESS('Successfully populated courses and videos')
        )