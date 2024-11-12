from email.policy import default

from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")  # Bot token
ADMINS = env.list("ADMINS")  # adminlar ro'yxati
BACKEND_URL = env.str("BACKEND_URL")  # BACKEND_URL manzili
ADMIN_TOKEN = env.str("ADMIN_TOKEN")  # Admin tokeni

CHANNELS = env.list("CHANNELS", default=[])  # channels
