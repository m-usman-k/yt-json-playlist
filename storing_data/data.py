from datetime import datetime

user_data = {
    "user_id": 1001,
    "username": "jane_smith",
    "email": "jane@example.com",
    "age": 25,
    "is_premium": True,
    "interests": ["photography", "hiking", "cooking"]
}

tasks = [
    {
        "id": 1,
        "title": "Complete Python tutorial",
        "completed": False,
        "priority": "high"
    },
    {
        "id": 2,
        "title": "Review pull requests",
        "completed": True,
        "priority": "medium"
    },
    {
        "id": 3,
        "title": "Update documentation",
        "completed": False,
        "priority": "low"
    }
]


api_payload = {
    "action": "create_user",
    "data": {
        "username": "newuser123",
        "email": "newuser@example.com",
        "role": "member"
    },
    "timestamp": datetime.now().isoformat()
}


data = {
    "name": "Alice",
    "address": {
        "street": "123 Main St",
        "city": "Boston",
        "zip": "02101"
    },
    "hobbies": ["reading", "gaming"]
}


settings = {
    "app_name": "MyApp",
    "version": "1.0.0",
    "features": {
        "dark_mode": True,
        "notifications": True,
        "auto_save": True
    },
    "limits": {
        "max_file_size": 100,
        "max_users": 1000
    }
}


messy_data = {
    "zebra": 1,
    "apple": 2,
    "mango": 3,
    "banana": 4,
    "cherry": 5
}


config = {
    "database": {
        "password": "secret",
        "host": "localhost",
        "username": "admin",
        "port": 5432
    },
    "cache": {
        "ttl": 3600,
        "enabled": True,
        "max_size": 1000
    },
    "api": {
        "version": "v1",
        "timeout": 30,
        "base_url": "https://api.example.com"
    }
}

international_data = {
    "name": "José García",
    "city": "São Paulo",
    "greeting": "你好",
    "emoji": "🎉"
}