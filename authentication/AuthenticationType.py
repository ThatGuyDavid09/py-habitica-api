from enum import Enum

class AuthenticationType(Enum):
    GOOGLE = "google"
    APPLE = "apple"
    FACEBOOK = "facebook"
    LOCAL = "local"
    TIMESTAMP = "timestamp"
