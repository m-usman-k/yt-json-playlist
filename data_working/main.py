import json
from data import *


# print(json.dumps(simple_nested, indent=4))

# print(simple_nested["user"]["name"])
# print(simple_nested["user"]["contact"]["phone"]["mobile"])
# print(simple_nested["user"])


# print(json.dumps(mixed_structure["employees"][0]["name"], indent=4))

print(api_response["data"]["user"]["posts"])