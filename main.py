import requests
import os
from pprint import pprint
import json
import pyperclip

from PyHabitica import PyHabitica
from user.StatType import StatType

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

client = PyHabitica("d009e682-8b82-4e5e-86ef-1cfb16c09f8a", os.environ["API_KEY"])
user = client.user_id

# pprint(r.headers)
print(user.id)
# pprint(json.loads(r.text))
# pyperclip.copy(json.dumps(user.profile))
print(user.allocate_bulk_stat(str=0, per=1))
