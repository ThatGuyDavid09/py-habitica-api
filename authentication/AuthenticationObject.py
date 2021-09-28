from authentication.AuthenticationType import AuthenticationType


class AuthenticationObject:
    def __init__(self, auth_type, auth_obj, user_id):
        self.raw = auth_obj
        self.auth_type = auth_type
        self.user_id = user_id

        self.generate_object()
    
    def generate_object(self):
        if self.auth_type == AuthenticationType.APPLE:
            pass