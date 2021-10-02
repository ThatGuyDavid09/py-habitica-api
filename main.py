import json
import os
import re

import requests

from PyHabitica import PyHabitica

"""
API RETURNS EITHER:
{
    "success": false,
    "error": "ErrorType",
    "message": "message"
}

or

{
    "success": true,
    "data": {data}
}
"""
#
client = PyHabitica("d009e682-8b82-4e5e-86ef-1cfb16c09f8a", os.environ["API_KEY"])
user = client.user

# print(type(json_content["data"]["achievements"]))
# input()

# pprint(r.headers)
# print(user.id)
# pprint(json.loads(r.text))
# pyperclip.copy(json.dumps(user.profile))
# print(user.buy_mystery_set(UUID("d009e682-8b82-4e5e-86ef-1cfb16c09f8a")))
