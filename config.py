import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6949246022:AAHCF2JY6ZLCDPItDC8Qx6O-hWAYt26hcYY")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "19169648"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "6e4a72fc13ac3486344ea662b002eaed")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "1334273918"))

# Your Mongodb Database Url
DB_URI = os.environ.get("DB_URI", "mongodb+srv://khaanbarwaani:qL47JyUNrzSRp2Aj@cluster0.qgucx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "khaanbarwaani")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
