import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("6998378624:AAEDNYDAyA-MZbkli45-8t8A-hovaJqd5DM", "")

    APP_ID = int(os.environ.get("APP_ID", 25535561))

    API_HASH = os.environ.get("API_HASH", "f40dbe709ac3d5b8a18aed1edb9b0d04")
