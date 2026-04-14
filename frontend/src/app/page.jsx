'use client';

import { useState, useEffect } from 'react';
import Link from 'next/link';

export default function Home() {
  const [activeTab, setActiveTab] = useState('ai');
  const [courses, setCourses] = useState([]);
  const [loading, setLoading] = useState(true);
  const [user, setUser] = useState(null);

  useEffect(() => {
    fetchCourses();
    const userData = localStorage.getItem('user');
    if (userData) {
      setUser(JSON.parse(userData));
    }
  }, []);

  const fetchCourses = async (category) => {
    try {
      const url = category ? `http://localhost:8000/api/courses/?category=${category}` : 'http://localhost:8000/api/courses/';
      const response = await fetch(url);
      const data = await response.json();
      setCourses(data);
    } catch (error) {
      console.error('Error fetching courses:', error);
    } finally {
      setLoading(false);
    }
  };

  const showCourses = (category) => {
    setActiveTab(category);
    fetchCourses(category);
  };

  const enrollCourse = async (courseId) => {
    if (!user) {
      alert('Please login to enroll in courses');
      return;
    }

    try {
      const response = await fetch('http://localhost:8000/api/enroll/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ course_id: courseId }),
      });

      if (response.ok) {
        alert('Successfully enrolled in the course!');
      } else {
        const errorData = await response.json();
        alert(errorData.error || errorData.detail || 'Failed to enroll');
      }
    } catch (error) {
      console.error('Error enrolling:', error);
      alert('Network error. Please try again.');
    }
  };

  const addToWishlist = async (courseId) => {
    if (!user) {
      alert('Please login to add courses to wishlist');
      return;
    }

    try {
      const response = await fetch('http://localhost:8000/api/wishlist/add/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ course_id: courseId }),
      });

      if (response.ok) {
        alert('Added to wishlist!');
      } else {
        const errorData = await response.json();
        alert(errorData.error || 'Failed to add to wishlist');
      }
    } catch (error) {
      console.error('Error adding to wishlist:', error);
      alert('Network error. Please try again.');
    }
  };

  const filteredCourses = courses.filter((course) => course.category === activeTab);

  return (
    <>
      <header className="navbar">
        <h2 className="logo">Learn-app</h2>

        <input type="text" placeholder="Search for anything" className="search" />

        <div className="nav-buttons">
          {user ? (
            <>
              <Link href="/dashboard" className="login">Dashboard</Link>
              <Link href="/mylearning" className="login">My Learning</Link>
              <Link href="/wishlist" className="login">Wishlist</Link>
              <Link href="/notifications" className="login">Notifications</Link>
            </>
          ) : (
            <>
              <Link href="/login" className="login">Log in</Link>
              <Link href="/signup" className="signup">Sign up</Link>
            </>
          )}
        </div>
      </header>

      <section className="title">
        <h1>Grow your skills. Shape your future.</h1>
        <p>Learn from expert instructors and advance your career.</p>
      </section>

      <div className="tabs">
        <span className={`tab ${activeTab === 'ai' ? 'active' : ''}`} onClick={() => showCourses('ai')}>
          Artificial Intelligence (AI)
        </span>
        <span className={`tab ${activeTab === 'python' ? 'active' : ''}`} onClick={() => showCourses('python')}>
          Python
        </span>
        <span className={`tab ${activeTab === 'excel' ? 'active' : ''}`} onClick={() => showCourses('excel')}>
          Microsoft Excel
        </span>
        <span className={`tab ${activeTab === 'marketing' ? 'active' : ''}`} onClick={() => showCourses('marketing')}>
          Digital Marketing
        </span>
      </div>

      <div className="courses">
        {loading ? (
          <p>Loading courses...</p>
        ) : (
          filteredCourses.map((course) => (
            <div key={course.id} className="card">
              <div className="card-img-wrapper" style={{ position: 'relative' }}>
                <img src={course.image_url} alt={course.title} />
                {user && (
                  <button
                    onClick={() => addToWishlist(course.id)}
                    style={{
                      position: 'absolute',
                      top: '10px',
                      right: '10px',
                      background: 'rgba(0,0,0,0.7)',
                      border: 'none',
                      borderRadius: '50%',
                      width: '40px',
                      height: '40px',
                      cursor: 'pointer',
                      display: 'flex',
                      alignItems: 'center',
                      justifyContent: 'center',
                    }}
                  >
                    <svg viewBox="0 0 24 24" fill="none" stroke="white" strokeWidth="2" style={{ width: '20px', height: '20px' }}>
                      <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78L12 21.23l8.84-8.84a5.5 5.5 0 0 0 0-7.78z"></path>
                    </svg>
                  </button>
                )}
              </div>
              <h3>{course.title}</h3>
              <p>{course.instructor}</p>
              <p style={{ color: '#9ca3af', fontSize: '14px', margin: '4px 0 8px' }}>
                {course.videos ? course.videos.length : 0} videos • {course.description || 'No description yet.'}
              </p>
              <span className="rating">⭐ {course.rating}</span>
              <h4>₹{course.price}</h4>
              {user && (
                <button
                  onClick={() => enrollCourse(course.id)}
                  style={{
                    width: '100%',
                    padding: '8px',
                    background: '#2563eb',
                    color: 'white',
                    border: 'none',
                    borderRadius: '6px',
                    marginTop: '10px',
                    cursor: 'pointer',
                  }}
                >
                  Enroll Now
                </button>
              )}
            </div>
          ))
        )}
      </div>
    </>
  );
}
