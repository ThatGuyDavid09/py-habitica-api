class User:
    def __init__(self, user_obj):
        self.sticky_notifications = user_obj["notifications"]
        self.auth = user_obj["data"]["auth"]
        self.achievements = user_obj["data"]["achievements"]
        self.backer = user_obj["data"]["backer"]
        self.contributor = user_obj["data"]["contributor"]
        self.purchased = user_obj["data"]["purchased"]
        self.flags = user_obj["data"]["flags"]
        self.history = user_obj["data"]["history"]
        self.items = user_obj["data"]["items"]
        self.invitations = user_obj["data"]["invitations"]
        self.party = user_obj["data"]["party"]
        self.preferences = user_obj["data"]["preferences"]
        self.profile = user_obj["data"]["profile"]
        self.stats = user_obj["data"]["stats"]
        self.inbox = user_obj["data"]["inbox"]
        self.tasks_order = user_obj["data"]["tasksOrder"]
        self.challenges = user_obj["data"]["challenges"]
        self.guilds = user_obj["data"]["guilds"]
        self.pinned_items_order = user_obj["data"]["pinnedItemsOrder"]
        self.new_messages = user_obj["data"]["newMessages"]
        self.unread_notifications = user_obj["data"]["notifications"]
        self.tags = user_obj["data"]["tags"]
        self.extra = user_obj["data"]["extra"]
        self.push_devices = user_obj["data"]["pushDevices"]
        self.webhooks = user_obj["data"]["webhooks"]
        self.pinned_items = user_obj["data"]["pinnedItems"]
        self.unpinned_items = user_obj["data"]["unpinnedItems"]

        self.id = user_obj["data"]["id"]
        self.needs_cron = user_obj["data"]["needsCron"]

        self.raw = user_obj

    def get_raw(self):
        return self.raw

    def get_user_id(self):
        return self.id
