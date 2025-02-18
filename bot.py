# ©️ LISA-KOREA | @LISA_FAN_LK | NT_BOT_CHANNEL | LISA-KOREA/YouTube-Video-Download-Bot

# [⚠️ Do not change this repo link ⚠️] :- https://github.com/LISA-KOREA/YouTube-Video-Download-Bot



from pyrogram import Client, filters
from Youtube.config import Config

# Create a Pyrogram client
app = Client(
    "my_bot",
    api_id=Config.26804861, 
    api_hash=Config.ce5aa9682dc27f62d872f1fd7883990b, 
    bot_token=Config.7938000654:AAGi0lvPQJxvH29YelPEawOaj-WFrKG9qtU,
    plugins=dict(root="Youtube")
)



# Start the bot
print("🎊 I AM ALIVE 🎊")
app.run()
