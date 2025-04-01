# bot developer @mr_jisshu
from os import environ 

class Config:
    
    API_ID = environ.get("API_ID", "23701314")
    API_HASH = environ.get("API_HASH", "ec3978bf717a5ae1c55dbe0a8f9408aa")
    BOT_TOKEN = environ.get("7905420827:AAECUlCvN2qxaftKmn4qJ5jN5tEEeJNiaPY") 
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '8036877196').split()]
    BOT_SESSION = environ.get("BOT_SESSION", "slow1") 

    PICS = (environ.get('PICS', 'https://graph.org/file/e223aea8aca83e99162bb.jpg'))
    
    DATABASE_URI = environ.get("DATABASE_URI", "mongodb+srv://justsagara:HO51oF0IOvrZV8NB@cluster0.iy1cv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "slow1")
    
    LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '1002539828525'))
    FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "") # FORCE SUB channel link 
    FORCE_SUB_ON = environ.get("FORCE_SUB_ON", "False")  # FORCE SUB ON - OFF


class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
