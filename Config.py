import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "25698939"))
    API_HASH = os.environ.get("API_HASH", "7430f53836560b21010e8cfd92e0239b")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6008570960:AAHiRxv5rd3t7grZw0drjcUaF5syndSrQls")
    STRING_SESSION = os.environ.get("STRING_SESSION", "AQGIInsABuNr2vi-VJCr6EVlhmFxwWzk5_DtbEB5tM_CBrGEYrmcx-saCl1CZqhMvjUXMMFdiRctNr8bJJv49PbP48B8cBGU5Uks6E4SKBJgSKAKWL0aqZiNXaLWf-6Z-U-MNpvItlPJb7x9tAtIpZv_C-cxuIPdmsgGAZ37BiXePbwAIBFac1Ct28gsrYExbiEMYime3_tGthXS1_h_IPHNph9BOmDJqZ3Tr5XeLEI5HlNiXr4AiEP3yKDvTc10P1eqtJJMRn53kvoTGM5p9JHSRATUwn_-HFdgXu3fQWftFxfYO--jFidzKW1hOF47Q_HOeeHVxHcolLP_KegE57VW4MZTKQAAAAFyb8lPAA")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", True)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "II_QUEEN_X_Y_MUSIC_BOT")
    SUPPORT = os.environ.get("SUPPORT", "indian_chatting_club_offical") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "shayari_ka_tadka") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://te.legra.ph/file/38f105acc8beea6779e10.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://te.legra.ph/file/30b4c615d3258d3a8201f.jpg")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "6214895951")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', True) # Change it to "True"
