import os
from uuid import UUID

from user.UserProfile import UserProfile


class PyHabitica:
    def __init__(self, user_id, user_api_key):
        self.id = UUID(user_id)
        self.headers = {
            "x-client": "d009e682-8b82-4e5e-86ef-1cfb16c09f8a-PyHabitica",
            "x-api-user": user_id,
            "x-api-key": user_api_key
        }
        self.url = "https://habitica.com/api/v3/"

    @property
    def user_id(self):
        return UserProfile(self.id, self.headers, self.url)
