from RequesterTemplate import RequesterTemplate
from uuid import UUID

from types.StatType import StatType


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

    def toggle_block_user(self, user: UUID):
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

    def change_class(self, class_type: ClassType):
        data = {
            "class": class_type.value
        }
        return self._post_request("user/change-class", data=data)

    def delete_message(self, message_id: UUID):
        return self._delete_request(f"user/messages/{str(message_id)}")
    
    def delete_all_messages(self):
        return self._delete_request(f"user/messages")
    
    def delete_account(self):
        return self._delete_request("user")
    
    def delete_authentication_method(self, network):
        return self._delete_request(f"user/auth/social/{network}")
    
    def disable_classes(self):
        return self._post_request("user/disable-classes")
    
    def toggle_equip_item(self, item_type: ItemType, item_key):
        return self._post_request(f"user/equip/{item_type.value}/{item_key}")
    
    def feed_pet(self, pet_key, food_key):
        return self._post_request(f"user/feed/{pet_key}/{food_key}")
    
    def get_anonymized_profile(self):
        return self._get_request("user/anonymized")
    
    def get_purchasable_items(self):
        return self._get_request("user/inventory/buy")
    
    def get_rewards(self):
        return self._get_request("user/in-app-rewards")
    
    def hatch_pet(self, egg_key, hatching_potion_key):
        return self._post_request(f"user/hatch/{egg_key}/{hatching_potion_key}")
    
    def login(self, username, password):
        data = {
            "username": username,
            "password": password
        }
        return self._post_request("user/auth/local/login", data=data)
    
    def toggle_inn_status(self):
        return self._post_request("user/sleep")
    
    def mark_pms_read(self):
        return self._post_request("user/mark-pms-read")

    def move_pinned_item(self, item_type: ItemType, path, position):
        return self._post_request(f"user/move-pinned-item/{item_type.value}/{path}/move/to/{position}")

    def open_mystery_item(self):
        return self._post_request("user/open-mystery-item")
    
    def purchase_gem_item(self, item_type: GemPurchasableType, item_key):
        return self._post_request(f"user/purchase/{item_type.value}/{item_key}")
    
    def purchase_hourglass_item(self, item_type: HourglassPurchasableType, item_key):
        return self._post_request(f"user/purchase-hourglass/{item_type.value}/{item_key}")
    
    def read_card(self, card_type):
        return self._post_request(f"user/read-card/{card_type}")
    
    def register(self, username, email, password):
        data = {
            "username": username,
            "email": email,
            "password": password,
            "confirmPassword": password
        }
        return self._post_request(f"user/auth/local/register", data=data)
    
    def release_mounts(self):
        return self._post_request("user/release-mounts")
    
    def release_pets_and_mounts(self):
        return self._post_request("user/release-both")
    
    def reroll(self):
        return self._post_request("user/reroll")
    
    def send_password_reset_email(self, email):
        data = {
            "email": email
        }
        return self._post_request("user/reset-password", data=data)
    
    def reset_password(self, new_password):
        data = {
            "newPassword": new_password,
            "confirmPassword": new_password
        }
        return self._post_request("user/auth/reset-password-set-new-one", data=data)
    
    def reset_user(self):
        return self._post_request("user/reset")
    
    def revive(self):
        return self._post_request("user/revive")
    
    def sell_gold_item(self, item_type: GoldSellableType, item_key, amount=1):
        data = {
            "amount": amount
        } 
        return self._post_request(f"user/sell/{item_type.value}/{item_key}", data=data)

    def set_custom_day_start(self, day_start):
        data = {
            "dayStart": day_start
        }
        return self._post_request("user/custom-day-start", data=data)

    def toggle_item_pin(self, item_key):
        return self._get_request(f"user/toggle-pinned-item/{item_key}")

    def unequip_all_by_type(self, unequip_type: UnequipAllType):
        return self._post_request(f"user/unequip/{unequip_type.value}")

    def unlock_item(self, item_path):
        data = {
            "path": item_path
        }
        return self._post_request("user/unlock", data=data)

    def update_email(self, new_email, password):
        data = {
            "newEmail": new_email,
            "password": password
        }
        self._put_request("user/auth/update-email", data=data)

    def update_password(self, old_password, new_password):
        data = {
            "password": old_password,
            "newPassword": new_password,
            "confirmPassword": new_password
        }
        self._put_request("user/auth/update-password", data=data)

    def update_user(self, new_settings_dict):
        return self._put_request("user", data=new_settings_dict)

    def update_username(self, new_username, password):
        data = {
            "username": new_username,
            "password": password
        }
        return self._put_request("user/auth/update-username", data=data)

    def use_orb_of_rebirth(self):
        return self._post_request("user/rebirth")

    def __repr__(self):
        return f"<UserProfile [{str(self.user_id)}]>"
