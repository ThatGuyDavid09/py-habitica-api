from RequesterTemplate import RequesterTemplate
from errors.RequestError import RequestError
from uuid import UUID

import requests
import json

from user.SpellType import SpellType
from user.StatType import StatType


class User(RequesterTemplate):
    def __init__(self, user_id: UUID, headers, url):
        super().__init__(headers, url)
        self.user_id: UUID = user_id
        self.raw_profile = None

    def _request_profile(self):
        self.raw_profile = self._get_request("user")

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
        return self._post_request("user/allocate", data=data)

    def allocate_all_stat(self):
        return self._post_request("user/allocate-now")

    def allocate_bulk_stat(self, int=0, str=0, con=0, per=0):
        data = {
            "stats": {
                "int": int,
                "str": str,
                "con": con,
                "per": per
            }
        }
        # print(data)
        return self._post_request("user/allocate-bulk", json=data)

    def block_unblock_user(self, user: UUID):
        data = {
            "uuid": str(user)
        }
        return self._post_request("user/block", data=data)

    def buy_mystery_set(self, set_key):
        return self._post_request(f"user/buy-mystery-set/{set_key}")

    def buy_health_potion(self):
        return self._post_request("user/buy-health-potion")

    def buy_gear_item(self, item_key):
        return self._post_request(f"user/buy-gear/{item_key}")

    def buy_quest_with_gold(self, quest_key):
        return self._post_request(f"user/buy-quest/{quest_key}")

    def buy_armoire(self):
        return self._post_request("user/buy-armoire")

    def buy(self, key):
        return self._post_request(f"user/buy/{key}")

    def buy_special_item(self, special_key):
        return self._post_request(f"user/buy-special-spell/{special_key}")

    def cast(self, spell: SpellType, target_id: UUID = None):
        data = None
        if target_id:
            data = {
                "targetId": str(target_id)
            }

        return self._post_request(f"user/class/cast/{spell.value}", data=data)

    def __repr__(self):
        return f"<UserProfile [{str(self.user_id)}]>"
