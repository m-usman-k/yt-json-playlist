import json
from data import *


# with open("./user_data.json", "w") as file:
#     json.dump(user_data, file)
    
# with open("./user_data.json", "r") as file:
#     json_data = json.load(file)
#     print(json_data)


# with open("./tasks.json", "w") as file:
#     json.dump(tasks, file, indent=4)
    
# with open("./tasks.json", "r") as file:
#     json_data = json.load(file)
#     print(json_data)


string_encoded = json.dumps(international_data, indent=4, ensure_ascii=False)
print(string_encoded)