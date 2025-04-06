# Apache License 2.0
# Copyright (c) 2022 @AniHorizon 
# Telegram Link : https://t.me/AniHorizon 
# Repo Link : https://github.com/MythicMosaic/4GB-Renamer-bot-With-metadata-
# License Link : https://github.com/MythicMosaic/4GB-Renamer-bot-With-metadata-/tree/main/LICENSE

import re
import os
import time

id_pattern = re.compile(r'^.\d+$') 

class Config(object):
    # AniHorizon client config
    API_ID = os.environ.get("API_ID", "")
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 

    # Premium account string session required
    STRING_SESSION = os.environ.get("STRING_SESSION", "")
    
    # Database config
    DB_NAME = os.environ.get("DB_NAME", "cluster0")     
    DB_URL = os.environ.get("DB_URL", "")
 
    # Other configs
    RKN_PIC = os.environ.get("RKN_PIC", "https://files.catbox.moe/6afj23.jpg")
    ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '6705898491').split()]
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002283909105"))

    # Free upload limit 
    FREE_UPLOAD_LIMIT = 6442450944  # 6 * 1024 * 1024 * 1024

    # Premium mode features
    UPLOAD_LIMIT_MODE = True 
    PREMIUM_MODE = True 
    
    # Force subscribe
    try:
        FORCE_SUB = int(os.environ.get("FORCE_SUB", ""))
    except:
        FORCE_SUB = os.environ.get("FORCE_SUB", "Digital_Botz")
        
    # Web response configuration     
    PORT = int(os.environ.get("PORT", "8080"))
    BOT_UPTIME = time.time()

class rkn(object):
    # Part of text configuration
    START_TXT = """<b><blockquote>ʜᴇʏ !! (user.mention)

ɪ ᴀᴍ ᴀ ᴘᴏᴡᴇʀғᴜʟ ғɪʟᴇ ʀᴇɴᴀᴍᴇʀ ʙᴏᴛ~  
ɪ ᴄᴀɴ ʀᴇɴᴀᴍᴇ ᴀɴʏ ᴠɪᴅᴇᴏs, ᴍᴏᴠɪᴇs, ᴀɴɪᴍᴇs, ᴏʀ ᴀɴʏ ғɪʟᴇs ʏᴏᴜ sᴇɴᴅ~

ᴊᴜsᴛ sᴇɴᴅ ᴀɴʏ ғɪʟᴇ ᴀɴᴅ ᴘɪᴄᴋ ᴀ ɴᴇᴡ ɴᴀᴍᴇ ғᴏʀ ɪᴛ!</blockquote></b>"""

    ABOUT_TXT = """<b><blockquote>
Owner     : <a href='https://t.me/Momo_Ayase_bot'>This Person</a>
Library   : <a href='https://github.com/pyrogram'>Pyrogram</a>
Language  : <a href='https://www.python.org'>Python 3</a>
Updates   : <a href='https://t.me/AniHorizon'>AniHorizon</a>
Paid Bot  : <a href='https://t.me/Tharun_stryker'>REON</a>
Developer : <a href='https://t.me/Momo_Ayase_bot'>STRYKER</a>
</blockquote></b>"""

    HELP_TXT = """
/start Tʜᴇ Bᴏᴛ.

<b><u>Hᴏᴡ Tᴏ Rᴇɴᴀᴍᴇ A Fɪʟᴇ</u></b>
Sᴇɴᴅ Aɴy Fɪʟᴇ Aɴᴅ Tyᴩᴇ Nᴇᴡ Fɪʟᴇ Nᴀᴍᴇ \nAɴᴅ Sᴇʟᴇᴄᴛ Tʜᴇ Fᴏʀᴍᴀᴛ [document, video, audio].           
ℹ️ 𝗔𝗻𝘆 𝗢𝘁𝗵𝗲𝗿 𝗛𝗲𝗹𝗽 𝗖𝗼𝗻𝘁𝗮𝗰𝘁 :- <a href=https://t.me/Momo_Ayase_bot>For Support</a>
"""

    UPGRADE_PREMIUM = """
•⪼ ★𝘗𝘭𝘢𝘯𝘴    -  ⏳𝘋𝘢𝘵𝘦 - 💸𝘗𝘳𝘪𝘤𝘦 
•⪼ 🥉𝘉𝘳𝘰𝘯𝘻𝘦  -   3𝘥𝘢𝘺𝘴 -   39
•⪼ 🥈𝘚𝘪𝘭𝘷𝘦𝘳   -   7𝘥𝘢𝘺𝘴 -   59
•⪼ 🥇𝘎𝘰𝘭𝘥    -  15𝘥𝘢𝘺𝘴 -  99
•⪼ 🏆𝘗𝘭𝘢𝘵𝘪𝘯𝘶𝘮 -  1𝘮𝘰𝘯𝘵𝘩 -  179
•⪼ 💎𝘋𝘪𝘢𝘮𝘰𝘯𝘥 -  2𝘮𝘰𝘯𝘵𝘩 -  339

- 𝘋𝘢𝘪𝘭𝘺 𝘜𝘱𝘭𝘰𝘢𝘥 𝘓𝘪𝘮𝘪𝘵 𝘜𝘯𝘭𝘪𝘮𝘪𝘵𝘦𝘥
- 𝘋𝘪𝘴𝘤𝘰𝘶𝘯𝘵 𝘈𝘭𝘭 𝘗𝘭𝘢𝘯 𝘙𝘴.9
"""

    UPGRADE_PLAN = """
𝘗𝘭𝘢𝘯: 𝘗𝘳𝘰
𝘋𝘢𝘵𝘦: 1 𝘮𝘰𝘯𝘵𝘩 
𝘗𝘳𝘪𝘤𝘦: 179
𝘓𝘪𝘮𝘪𝘵: 100 𝘎𝘉

𝘗𝘭𝘢𝘯: 𝘜𝘭𝘵𝘢 𝘗𝘳𝘰 
𝘋𝘢𝘵𝘦: 1 𝘮𝘰𝘯𝘵𝘩 
𝘗𝘳𝘪𝘤𝘦: 199
𝘓𝘪𝘮𝘪𝘵: 1000 𝘎𝘉

- 𝘋𝘪𝘴𝘤𝘰𝘶𝘯𝘵 𝘈𝘭𝘭 𝘗𝘭𝘢𝘯 𝘙𝘴.9
"""

    THUMBNAIL = """
🌌 <b><u>Hᴏᴡ Tᴏ Sᴇᴛ Tʜᴜᴍʙɴɪʟᴇ</u></b>

<b>•></b> Sᴇɴᴅ Aɴy Pʜᴏᴛᴏ Tᴏ Aᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟy Sᴇᴛ Tʜᴜᴍʙɴɪʟᴇ.
<b>•></b> /del_thumb - Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Dᴇʟᴇᴛᴇ Yᴏᴜʀ Oʟᴅ Tʜᴜᴍʙɴɪʟᴇ.
<b>•></b> /view_thumb - Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Vɪᴇᴡ Yᴏᴜʀ Cᴜʀʀᴇɴᴛ Tʜᴜᴍʙɴɪʟᴇ.
"""

    CAPTION = """
📑 <b><u>Hᴏᴡ Tᴏ Sᴇᴛ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ</u></b>

<b>•></b> /set_caption - Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Sᴇᴛ ᴀ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ
<b>•></b> /see_caption - Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Vɪᴇᴡ Yᴏᴜʀ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ
<b>•></b> /del_caption - Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Dᴇʟᴇᴛᴇ Yᴏᴜʀ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ

Exᴀᴍᴩʟᴇ:- `/set_caption 📕 Fɪʟᴇ Nᴀᴍᴇ: {filename}
💾 Sɪᴢᴇ: {filesize}
⏰ Dᴜʀᴀᴛɪᴏɴ: {duration}`
"""

    BOT_STATUS = """
⚡️ ʙᴏᴛ sᴛᴀᴛᴜs ⚡️

⌚️ ʙᴏᴛ ᴜᴩᴛɪᴍᴇ: `{}`
👭 ᴛᴏᴛᴀʟ ᴜsᴇʀꜱ: `{}`
💸 ᴛᴏᴛᴀʟ ᴘʀᴇᴍɪᴜᴍ ᴜsᴇʀs: `{}`
֍ ᴜᴘʟᴏᴀᴅ: `{}`
"""
