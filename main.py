import requests
import os
from pprint import pprint
import json
import pyperclip

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

headers = {
    "x-client": "d009e682-8b82-4e5e-86ef-1cfb16c09f8a-PyHabitica",
    "x-api-user": "d009e682-8b82-4e5e-86ef-1cfb16c09f8a",
    "x-api-key": os.environ["API_KEY"]
}

url = "https://habitica.com/api/v3/"
r = requests.get(url + "user", headers=headers)

# pprint(r.headers)
print(r)
# pprint(json.loads(r.text))
pyperclip.copy((r.text))



