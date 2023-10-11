# Don't Remove Credit @ALAS
# Subscribe YouTube Channel For Amazing Bot @ALAS
# Ask Doubt on telegram @ALAS


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "23684657"))
    API_HASH = getenv("API_HASH", "471fbeeb71b5fbf9246fc7342bb6754a")
    BOT_TOKEN = getenv("BOT_TOKEN", "6610750400:AAH2zIr8WZp52v-WutBriMAyLG1P9oVsCuc")
    FSUB = getenv("FSUB", "ALASUpdate")
    CHID = int(getenv("CHID", "-1001944794673"))
    SUDO = list(map(int, getenv("SUDO", "1410065122").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://sushankm16:4i1WAfPYKWyqPIDD@cluster0.sngp9pz.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()

# Don't Remove Credit @ALAS
# Subscribe YouTube Channel For Amazing Bot @ALAS
# Ask Doubt on telegram @ALAS
