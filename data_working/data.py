simple_nested = {
    "user": {
        "name": "John Doe",
        "contact": {
            "email": "john@example.com",
            "phone": {
                "home": "555-1234",
                "mobile": "555-5678"
            }
        }
    }
}


mixed_structure = {
    "company": "TechCorp",
    "employees": [
        {"name": "Alice", "role": "Developer"},
        {"name": "Bob", "role": "Designer"},
        {"name": "Charlie", "role": "Manager"}
    ]
}


courses = [
    {
        "id": 1,
        "name": "Python Basics",
        "instructor": {
            "name": "Dr. Smith",
            "rating": 4.8
        },
        "topics": ["variables", "functions", "loops"]
    },
    {
        "id": 2,
        "name": "Advanced Python",
        "instructor": {
            "name": "Prof. Johnson",
            "rating": 4.9
        },
        "topics": ["decorators", "generators", "async"]
    }
]


api_response = {
    "status": "success",
    "timestamp": "2024-12-22T10:30:00Z",
    "data": {
        "user": {
            "id": 12345,
            "username": "techguru",
            "profile": {
                "full_name": "Sarah Johnson",
                "bio": "Full-stack developer | Tech enthusiast",
                "avatar_url": "https://example.com/avatar.jpg",
                "location": {
                    "city": "San Francisco",
                    "state": "CA",
                    "country": "USA",
                    "coordinates": {
                        "lat": 37.7749,
                        "lng": -122.4194
                    }
                },
                "verified": True,
                "followers_count": 15420,
                "following_count": 892
            },
            "posts": [
                {
                    "id": 1001,
                    "content": "Just deployed my first Python app!",
                    "created_at": "2024-12-20T14:30:00Z",
                    "likes": 245,
                    "comments": [
                        {
                            "id": 5001,
                            "user": "john_dev",
                            "text": "Congratulations! 🎉",
                            "created_at": "2024-12-20T15:00:00Z"
                        },
                        {
                            "id": 5002,
                            "user": "code_master",
                            "text": "Great work! What framework did you use?",
                            "created_at": "2024-12-20T15:15:00Z"
                        }
                    ],
                    "media": [
                        {
                            "type": "image",
                            "url": "https://example.com/post1.jpg",
                            "dimensions": {"width": 1920, "height": 1080}
                        }
                    ],
                    "hashtags": ["python", "coding", "webdev"]
                },
                {
                    "id": 1002,
                    "content": "5 tips for better Python code...",
                    "created_at": "2024-12-21T10:00:00Z",
                    "likes": 567,
                    "comments": [
                        {
                            "id": 5003,
                            "user": "newbie_coder",
                            "text": "This is really helpful!",
                            "created_at": "2024-12-21T10:30:00Z"
                        }
                    ],
                    "media": [],
                    "hashtags": ["python", "tips", "programming"]
                }
            ],
            "statistics": {
                "total_posts": 234,
                "total_likes_received": 45678,
                "engagement_rate": 8.5,
                "active_days": 456
            }
        }
    },
    "metadata": {
        "api_version": "2.0",
        "rate_limit": {
            "remaining": 4950,
            "reset_at": "2024-12-22T11:00:00Z"
        }
    }
}