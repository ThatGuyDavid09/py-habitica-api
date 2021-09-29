from uuid import UUID

import requests
import json

from errors.NotAuthorized import NotAuthorized
from user.StatType import StatType


class UserProfile:
    def __init__(self, user_id: UUID, headers, url):
        self.user_id = user_id
        self.raw_profile = None
        self.headers = headers
        self.url = url

    def _request_profile(self):
        r = requests.get(self.url + "user", headers=self.headers)
        json_text = json.loads(r.text)
        if r.status_code == 200 and json_text["success"]:
            self.raw_profile = json_text
        elif r.status_code == 401:
            raise NotAuthorized(json_text["message"])
        else:
            raise ValueError(json_text["message"])

    @property
    def profile(self):
        if not self.raw_profile:
            self._request_profile()

        return self.raw_profile

    @property
    def id(self):
        return self.user_id

    def allocate_single_stat(self, stat_type: StatType):
        data = {
            "stat": stat_type.value
        }
        r = requests.post(self.url + "user/allocate", headers=self.headers, data=data)
        json_text = json.loads(r.text)
        if r.status_code == 401:
            raise NotAuthorized(json_text["message"])
        return json_text

    def allocate_all_stat(self):
        r = requests.post(self.url + "user/allocate", headers=self.headers)
        json_text = json.loads(r.text)
        if r.status_code == 401:
            raise NotAuthorized(json_text["message"])
        return json_text

    """
    
    """
    def allocate_bulk_stat(self, int=0, str=0, con=0, per=0):
        # TODO figure out how on earth this works
        data = {
            "stats": {
                "int": int,
                "str": str,
                "con": con,
                "per": per
            }
        }
        print(data)
        r = requests.post(self.url + "user/allocate-bulk", headers=self.headers, data=data)
        json_text = json.loads(r.text)
        if r.status_code == 401:
            raise NotAuthorized(json_text["message"])
        return json_text

    def __repr__(self):
        return f"<UserProfile [{str(self.user_id)}]>"
