'use client';

import { useState, useEffect } from 'react';
import Link from 'next/link';
import { useRouter } from 'next/navigation';

export default function Notifications() {
    const [user, setUser] = useState(null);
    const router = useRouter();

    useEffect(() => {
        const userData = localStorage.getItem('user');
        if (!userData) {
            router.push('/login');
            return;
        }
        setUser(JSON.parse(userData));
    }, []);

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

    // Mock notifications data
    const notifications = [
        {
            id: 1,
            title: 'New course available!',
            message: 'Check out our new AI Engineering Masterclass',
            date: '2024-04-14',
            read: false,
        },
        {
            id: 2,
            title: 'Course completion reminder',
            message: 'You have unfinished lessons in Python for Beginners',
            date: '2024-04-13',
            read: true,
        },
        {
            id: 3,
            title: 'Special offer',
            message: '50% off on all Excel courses this weekend!',
            date: '2024-04-12',
            read: true,
        },
    ];

    return (
        <>
            <header className="navbar">
                <h2 className="logo">Learn-app</h2>

                <input type="text" placeholder="Search for anything" className="search" />

                <div className="nav-buttons">
                    <Link href="/dashboard" className="login">Dashboard</Link>
                    <Link href="/mylearning" className="login">My Learning</Link>
                    <Link href="/wishlist" className="login">Wishlist</Link>
                    <button onClick={handleLogout} className="signup">Logout</button>
                </div>
            </header>

            <section className="title">
                <h1>Notifications</h1>
                <p>Stay updated with your learning progress</p>
            </section>

            <div style={{ padding: '40px 60px' }}>
                {notifications.length === 0 ? (
                    <p style={{ color: '#cbd5e1' }}>No notifications yet.</p>
                ) : (
                    <div style={{ maxWidth: '800px' }}>
                        {notifications.map((notification) => (
                            <div
                                key={notification.id}
                                style={{
                                    background: '#1e1f26',
                                    padding: '20px',
                                    borderRadius: '12px',
                                    marginBottom: '15px',
                                    boxShadow: '0 15px 35px rgba(0, 0, 0, 0.4)',
                                    borderLeft: notification.read ? '4px solid #2563eb' : '4px solid #facc15',
                                }}
                            >
                                <h3 style={{ color: '#f8fafc', margin: '0 0 10px 0' }}>
                                    {notification.title}
                                    {!notification.read && (
                                        <span style={{
                                            background: '#facc15',
                                            color: '#1e1f26',
                                            padding: '2px 6px',
                                            borderRadius: '4px',
                                            fontSize: '12px',
                                            marginLeft: '10px'
                                        }}>
                                            New
                                        </span>
                                    )}
                                </h3>
                                <p style={{ color: '#cbd5e1', margin: '0 0 10px 0' }}>
                                    {notification.message}
                                </p>
                                <small style={{ color: '#9ca3af' }}>{notification.date}</small>
                            </div>
                        ))}
                    </div>
                )}
            </div>
        </>
    );
}