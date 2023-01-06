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
👋 Hi ! {} Selamat Datang di @foto_ebot

**Dengan Bot Ini Anda Dapat mengunggah Gambar Anda Di web **

Anda Dapat Mengirim Gambar Sebagai Pesan Terusan Dari Obrolan/Saluran Apa Pun Atau Mengunggahnya Sebagai Foto Atau File.

"""

    ABOUT_TEXT = """🤖 **My Name:** [FotoEbot](t.me/foto_ebot)

📝 **Language:** [Python 3](https://www.python.org)

📚 **Framework:** [Pyrogram](https://github.com/pyrogram/pyrogram)

📡 **Hosted On:** [Yon](t.me/idnrobot)

👨‍💻 **Developer:** [raiyen](t.me/eueon)

📢 **Updates Channel:** [LeeYeon](https://t.me/sewuon)


❤ [Donate](https://t.me/rwyan) (Yon)
"""

    HELP_TEXT = """💡 Cukup Kirimkan Saya Foto Anda Dan Saya Akan Mengunggahnya untuk Anda.

"""

    ERR_TEXT = "⚠️ API Tidak Ditemukan"

    ERRTOKEN_TEXT = "😶 Token Akses yang Diberikan Kedaluwarsa, Dicabut, Cacat, atau Tidak Valid Karena Alasan Lain. DM @eueon",

    WAIT = "💬 Harap tunggu !!"
