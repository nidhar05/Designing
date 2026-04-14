'use client';

import { useState, useEffect } from 'react';
import Link from 'next/link';
import { useRouter } from 'next/navigation';

export default function MyLearning() {
    const [user, setUser] = useState(null);
    const [enrollments, setEnrollments] = useState([]);
    const router = useRouter();

    useEffect(() => {
        const userData = localStorage.getItem('user');
        if (!userData) {
            router.push('/login');
            return;
        }
        setUser(JSON.parse(userData));
        fetchEnrollments();
    }, []);

    const fetchEnrollments = async () => {
        try {
            const response = await fetch('http://localhost:8000/api/my-enrollments/', {
                credentials: 'include',
            });
            if (response.ok) {
                const data = await response.json();
                setEnrollments(data.map((enrollment) => enrollment.course));
            }
        } catch (error) {
            console.error('Error fetching enrollments:', error);
        }
    };

    const handleLogout = async () => {
        try {
            await fetch('http://localhost:8000/api/auth/logout/', {
                method: 'POST',
                credentials: 'include',
            });
        } catch (error) {
            console.error('Logout error:', error);
        }
        localStorage.removeItem('user');
        router.push('/');
    };

    if (!user) return <div>Loading...</div>;

    return (
        <>
            <header className="navbar">
                <h2 className="logo">Learn-app</h2>

                <input type="text" placeholder="Search for anything" className="search" />

                <div className="nav-buttons">
                    <Link href="/dashboard" className="login">Dashboard</Link>
                    <Link href="/wishlist" className="login">Wishlist</Link>
                    <Link href="/notifications" className="login">Notifications</Link>
                    <button onClick={handleLogout} className="signup">Logout</button>
                </div>
            </header>

            <section className="title">
                <h1>My Learning</h1>
                <p>Continue where you left off</p>
            </section>

            <div className="courses">
                {enrollments.length === 0 ? (
                    <p style={{ color: '#cbd5e1', width: '100%' }}>You haven't enrolled in any courses yet. <Link href="/" style={{ color: '#2563eb' }}>Browse courses</Link></p>
                ) : (
                    enrollments.map((course) => (
                        <div key={course.id} className="card">
                            <img src={course.image_url} alt={course.title} />
                            <h3>{course.title}</h3>
                            <p>{course.instructor}</p>
                            <span className="rating">⭐ {course.rating}</span>
                            <h4>₹{course.price}</h4>
                            <button style={{
                                width: '100%',
                                padding: '8px',
                                background: '#2563eb',
                                color: 'white',
                                border: 'none',
                                borderRadius: '6px',
                                marginTop: '10px',
                                cursor: 'pointer'
                            }}>
                                ContinuLearn-app
                            </button>
                        </div>
                    ))
                )}
            </div>
        </>
    );
}