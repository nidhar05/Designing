'use client';

import { useState, useEffect } from 'react';
import Link from 'next/link';
import { useRouter } from 'next/navigation';

export default function Wishlist() {
    const [user, setUser] = useState(null);
    const [wishlist, setWishlist] = useState([]);
    const router = useRouter();

    useEffect(() => {
        const userData = localStorage.getItem('user');
        if (!userData) {
            router.push('/login');
            return;
        }
        setUser(JSON.parse(userData));
        fetchWishlist();
    }, []);

    const fetchWishlist = async () => {
        try {
            const response = await fetch('http://localhost:8000/api/wishlist/');
            if (response.ok) {
                const data = await response.json();
                setWishlist(data.map((item) => item.course));
            }
        } catch (error) {
            console.error('Error fetching wishlist:', error);
        }
    };

    const removeFromWishlist = async (courseId) => {
        try {
            const response = await fetch(`http://localhost:8000/api/wishlist/remove/${courseId}/`, {
                method: 'DELETE',
            });
            if (response.ok) {
                setWishlist(wishlist.filter(course => course.id !== courseId));
            }
        } catch (error) {
            console.error('Error removing from wishlist:', error);
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
                    <Link href="/mylearning" className="login">My Learning</Link>
                    <Link href="/notifications" className="login">Notifications</Link>
                    <button onClick={handleLogout} className="signup">Logout</button>
                </div>
            </header>

            <section className="title">
                <h1>My Wishlist</h1>
                <p>Courses you're interested in</p>
            </section>

            <div className="courses">
                {wishlist.length === 0 ? (
                    <p style={{ color: '#cbd5e1', width: '100%' }}>Your wishlist is empty. <Link href="/" style={{ color: '#2563eb' }}>Browse courses</Link></p>
                ) : (
                    wishlist.map((course) => (
                        <div key={course.id} className="card">
                            <img src={course.image_url} alt={course.title} />
                            <h3>{course.title}</h3>
                            <p>{course.instructor}</p>
                            <span className="rating">⭐ {course.rating}</span>
                            <h4>₹{course.price}</h4>
                            <button
                                onClick={() => removeFromWishlist(course.id)}
                                style={{
                                    width: '100%',
                                    padding: '8px',
                                    background: '#dc2626',
                                    color: 'white',
                                    border: 'none',
                                    borderRadius: '6px',
                                    marginTop: '10px',
                                    cursor: 'pointer'
                                }}
                            >
                                Remove from Wishlist
                            </button>
                        </div>
                    ))
                )}
            </div>
        </>
    );
}