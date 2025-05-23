import os

class Config(object):
    BOT_TOKEN = os.environ.get("")
    API_ID = int(os.environ.get(""))
    API_HASH = os.environ.get("")
    AUTH_USER = os.environ.get('6302749609', '5927517339').split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
    HOST = "https://drm-api-six.vercel.app"
    CREDIT = "[꧁ ASTRONAUT ꧂]"
