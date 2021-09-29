import os
from uuid import UUID

from user.User import User


class PyHabitica:
    def __init__(self, user_id: str, user_api_key: str):
        self.id = UUID(user_id)
        self.headers = {
            "x-client": "d009e682-8b82-4e5e-86ef-1cfb16c09f8a-PyHabitica",
            "x-api-user": user_id,
            "x-api-key": user_api_key
        }
        self.url = "https://habitica.com/api/v3/"

    @property
    def user(self):
        return User(self.id, self.headers, self.url)

    def __repr__(self):
        return f"<PyHabitica [{str(self.id)}]>"
