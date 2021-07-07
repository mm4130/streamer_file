import os 

class Config:

    class config:
        APP_ID = 2544613

        API_HASH = "0f412888935b3f1eaad6de9d3f4e425c"
        
        BOT_TOKEN = "1871931544:AAHzxYmGPF3_ZPxuG7bzfc-B-Kuzl5ao4IU"
        
        HOST = "127.0.0.1"

        PORT = os.getenv('PORT')

        ROOT_URI = f"https://mydlr.herokuapp.com/"


        ENCODING = "utf8"


        # ALLOWED_EXT = ["mkv", "mp4", "flv"]
