import os

class Config(object):
    BOT_TOKEN = os.environ.get("7430017413:AAFG8r3su1vRkZceXfovtaMKRNBIjhf4k6E")
    API_ID = int(os.environ.get("25693368"))
    API_HASH = os.environ.get("2dcf91b0f99c0b9d4875e87020e6bd07")
    AUTH_USER = os.environ.get('6302749609', '5927517339').split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
    HOST = "https://drm-api-six.vercel.app"
    CREDIT = "[꧁ ASTRONAUT ꧂]"
