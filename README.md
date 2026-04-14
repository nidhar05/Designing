# E-Learning Platform

A full-stack e-learning platform built with Next.js (frontend) and Django (backend).

## Project Structure

```
/
├── frontend/          # Next.js application
├── backend/           # Django application
└── README.md         # This file
```

## Features

- **Frontend (Next.js):**
  - Course browsing with category filtering
  - User authentication (login/signup)
  - Dashboard for enrolled users
  - My Learning page
  - Wishlist functionality
  - Notifications page
  - Responsive dark theme design

- **Backend (Django):**
  - REST API with Django REST Framework
  - User authentication and profiles
  - Course management
  - Enrollment system
  - Wishlist functionality
  - SQLite database

## Setup Instructions

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Activate the virtual environment:
   ```bash
   .\venv\Scripts\activate  # Windows
   ```

3. Run the Django development server:
   ```bash
   python manage.py runserver
   ```

The backend will be available at `http://localhost:8000`

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Run the Next.js development server:
   ```bash
   npm run dev
   ```

The frontend will be available at `http://localhost:3000`

## API Endpoints

### Authentication
- `POST /api/auth/login/` - User login
- `POST /api/auth/signup/` - User registration
- `POST /api/auth/logout/` - User logout
- `GET /api/auth/profile/` - Get user profile

### Courses
- `GET /api/courses/` - List all courses (with optional category filter)
- `GET /api/courses/{id}/` - Get specific course

### User Actions
- `POST /api/enroll/` - Enroll in a course
- `GET /api/my-enrollments/` - Get user's enrolled courses
- `POST /api/wishlist/add/` - Add course to wishlist
- `GET /api/wishlist/` - Get user's wishlist
- `DELETE /api/wishlist/remove/{course_id}/` - Remove from wishlist

## Sample Data

The backend includes a management command to populate the database with sample courses:

```bash
cd backend
.\venv\Scripts\activate
python manage.py populate_courses
```

## Technologies Used

- **Frontend:**
  - Next.js 14 with App Router
  - TypeScript
  - Tailwind CSS
  - React Hooks

- **Backend:**
  - Django 6.0
  - Django REST Framework
  - Django CORS Headers
  - SQLite database

## Development Notes

- The frontend makes API calls to `http://localhost:8000` (Django backend)
- User authentication uses session-based auth with CSRF protection
- The design maintains the original dark theme aesthetic
- All course data is served from the Django API
- User state is managed via localStorage for simplicity

## Future Enhancements

- Add course content and video streaming
- Implement payment processing
- Add course progress tracking
- Include user reviews and ratings
- Add admin panel for course management
- Implement real-time notifications