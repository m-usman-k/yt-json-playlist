import json
from datetime import datetime

class Person:
    name = "usman"
    age = 21
    created_at = datetime.now()
    
    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "created_at": self.created_at.isoformat()
        }
        
print(Person.__dict__.copy())
        
# print(json.dumps(Person().to_dict()))