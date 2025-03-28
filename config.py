# bot developer @mr_jisshu
from os import environ 

class Config:
    
    API_ID = environ.get("API_ID", "27866551")
    API_HASH = environ.get("API_HASH", "76057a79a74262e29d6de1e9f41aab0d")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7836766549:AAFhJa5KoLppp_lXdChYFKzMEMtD7L5KDMc") 
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '5437233066').split()]
    BOT_SESSION = environ.get("BOT_SESSION", "forward2") 

    PICS = (environ.get('PICS', 'https://graph.org/file/e223aea8aca83e99162bb.jpg'))
    
    DATABASE_URI = environ.get("DATABASE_URI", "mongodb+srv://justsagara:HO51oF0IOvrZV8NB@cluster0.iy1cv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward2")
    
    LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '1002419367395'))
    FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "") # FORCE SUB channel link 
    FORCE_SUB_ON = environ.get("FORCE_SUB_ON", "False")  # FORCE SUB ON - OFF


class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
