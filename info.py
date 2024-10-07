import re
from os import environ

id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = environ.get('SESSION', 'TechVJBot')
API_ID = int(environ.get('API_ID', '24579269'))
API_HASH = environ.get('API_HASH', '99dff6c471774c2be6ff3d4623a6c0c0')
BOT_TOKEN = environ.get('BOT_TOKEN', "")

# Bot settings
PORT = environ.get("PORT", "8080")

# Online Stream and Download
MULTI_CLIENT = False
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
else:
    ON_HEROKU = False
URL = environ.get("URL", "")

# Admins, Channels & Users
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002261561351'))
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '').split()]

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://jhnbsomers0uh14:rVz5pWHzELN6aJWU@cluster0.sloz4.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = environ.get('DATABASE_NAME', "techvjautobot")

# Shortlink Info
SHORTLINK = bool(environ.get('SHORTLINK', False)) # Set True Or False
SHORTLINK_URL = environ.get('SHORTLINK_URL', 'modijiurl.com')
SHORTLINK_API = environ.get('SHORTLINK_API', '29b557074aa857e56ca7fd6ad2e42ef2788e8443')
