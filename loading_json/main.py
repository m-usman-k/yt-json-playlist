import json


# with open("./user_profile.json", "r") as file:
#     json_data = json.load(file)
    
#     print(json_data.keys())
#     print(json_data.values())

#     print(json_data["user_id"])
#     print(json_data["interests"])
#     print(json_data["address"])
#     print(json_data["preferences"])


# with open("./products.json", "r") as file:
#     json_data = json.load(file)
    
#     print(json_data[0]["id"])
#     print(json_data[0]["name"])

# api_response = '''
# {
#     "status": "success",
#     "data": {
#         "temperature": 72,
#         "humidity": 65,
#         "conditions": "Partly Cloudy",
#         "wind_speed": 8
#     },
#     "timestamp": "2024-12-22T14:30:00Z",
#     "location": "New York"
# }
# '''


# json_data = json.loads(api_response)


# print(json_data["status"])
# print(json_data["data"]["conditions"])



try:
    with open("./new_data.json", "r") as file:
        json_data = json.load(file)
except FileNotFoundError as e:
    print("File not found, your file does not exist.")
    
    
try:
    with open("./invalid.json", "r") as file:
        json_data = json.load(file)
except json.JSONDecodeError as e:
    print("Error while decoding json data.")