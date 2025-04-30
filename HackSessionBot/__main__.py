import threading
from flask import Flask
import os

# Run Flask dummy server in a thread
app = Flask(__name__)

@app.route('/')
def home():
    return "Telegram bot running on Render."

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

if __name__ == "__main__":
    # Start dummy web server in background
    threading.Thread(target=run_flask).start()

    # Then start your actual bot logic (make sure it's not blocking)
    from HackSessionBot.main import run_bot  # adjust to your entrypoint
    run_bot()
    
    import asyncio
import importlib

from pyrogram import idle
from HackSessionBot import LOG
from HackSessionBot.modules import ALL_MODULES


async def start_bot():
    for all_module in ALL_MODULES:
        importlib.import_module("HackSessionBot.modules." + all_module)
    LOG.print("[bold yellow]✨ ʙᴏᴛ sᴛᴀʀᴛᴇᴅ")
    await idle() 
    LOG.print("[bold red]ᴄᴀɴᴄᴇʟɪɴɢ ᴀʟʟ ᴛᴀsᴋs.")



if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(start_bot())
