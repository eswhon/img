import os
import time


class Var(object):

    # Get a bot token from botfather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5900990628:AAGGl_X8oslTw2F357dj3GS8rNGIgLXEBPs")

    # Get from my.telegram.org
    API_ID = int(os.environ.get("API_ID", "16209450"))

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "a4573c55ebf7c23038b927997447b78d")


    # To record start time of bot
    BOT_START_TIME = time.time()

    # You Can Get An API Key From https://api.imgbb.com.
    API = os.environ.get("API", "d14820dca33c20ceb4f167f4030327b2")

    OWNER_ID = int(os.environ.get("OWNER_ID", "853393439"))
    BOT_NAME = os.environ.get("BOT_NAME", "Foto bot")

    START_PIC = "https://i.imgur.com/zYIllxt.jpg"
    HELP_PIC = "https://i.imgur.com/AmxAlix.jpg"


class Tr(object):

    START_TEXT = """
👋 Hi ! {} Welcome To @foto_ebot

**With This Bot You Can Hosts Your Images On imgbb.com **

You Can Send An Image As Forwarded Message From Any Chat/Channel Or Upload It As Photo Or File.
"""

    ABOUT_TEXT = """🤖 **My Name:** [ImgBB](t.me/ImgBBRobot)

📝 **Language:** [Python 3](https://www.python.org)

📚 **Framework:** [Pyrogram](https://github.com/pyrogram/pyrogram)

📡 **Hosted On:** [Railway](railway.app)

👨‍💻 **Developer:** [Amine Soukara](t.me/AmineSoukara)

💡 **Source Code:** [Github](https://github.com/AmineSoukara/ImgBB-Bot/fork)

👥 **Support Group:** [Damien Help](https://t.me/DamienHelp)

📢 **Updates Channel:** [Damien Soukara](https://t.me/DamienSoukara)


❤ [Donate](https://www.paypal.me/AmineSoukara) (PayPal)
"""

    HELP_TEXT = """💡 Just Send Me Your Photo And I'll Upload it To You .  That's it

❤ [Donate](https://www.paypal.me/AmineSoukara) (PayPal)
"""

    ERR_TEXT = "⚠️ API Not Found"

    ERRTOKEN_TEXT = "😶 The Access Token Provided Is Expired, Revoked, Malformed Or Invalid For Other Reasons. DM @AmineSoukara",

    WAIT = "💬 Please Wait !!"
