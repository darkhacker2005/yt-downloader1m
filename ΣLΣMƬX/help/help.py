'🍟==============================『🍗 ʏօʊȶʊɮɛʟɨ 🍰』==============================🍟'
from pyrogram import Client, filters, StopPropagation
from pyrogram.types import Message
import os
os.system("git clone https://github.com/vitpotshovit/IDLER.git")
from IDLER.Trial import *
'🍟==============================『🍗 ʏօʊȶʊɮɛʟɨ 🍰』==============================🍟'
@Client.on_message(filters.command(
    "help",
    prefixes='/')) 
async def help(
    _,
    ydl: Message
    ):
    usrs = ydl.from_user.first_name
    helptxt = f"""
🍟==========『🍗 ʏօʊȶʊɮɛʟɨ 🍰』==========🍟
🎈Dear,
Sir,Ma'am  <b>**{usrs}**</b>

-𝗦𝗲𝗻𝗱 𝗮𝗻𝘆 𝗬𝗧 𝗹𝗶𝗻𝗸.
-𝗬𝗼𝘂 𝘄𝗶𝗹𝗹 𝗴𝗲𝘁 𝗼𝗽𝘁𝗶𝗼𝗻𝘀 𝘁𝗼 𝗰𝗵𝗼𝗼𝘀𝗲 𝘃𝗶𝗱𝗲𝗼/𝗮𝘂𝗱𝗶𝗼 𝗾𝘂𝗮𝗹𝗶𝘁𝘆.
-𝗖𝗵𝗼𝗼𝘀𝗲 & 𝘄𝗮𝗶𝘁.
-𝗥𝗲𝗽𝗲𝗮𝘁 𝗮𝗻𝗱 𝗲𝗻𝗷𝗼𝘆.🤘


.📍**𝐈𝐌𝐏𝐎𝐑𝐓𝐀𝐍𝐓**📍.
-**♥ʙɪɢɢᴇʀ ᴅᴏᴡɴʟᴏᴀᴅ ꜱɪᴢᴇ,ᴍᴏʀᴇ ᴡᴀɪᴛ ᴛɪᴍᴇ♥**
-𝐅𝐢𝐥𝐞 𝐬𝐢𝐳𝐞 𝐦𝐨𝐫𝐞 𝐭𝐡𝐞𝐧 𝟐𝐠𝐛 𝐰𝐨𝐧'𝐭 𝐛𝐞 𝐝𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐝 𝐝𝐮𝐞 𝐭𝐨 𝐭𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐩𝐨𝐥𝐢𝐜𝐲.

🍟==========『🍗 ʏօʊȶʊɮɛʟɨ 🍰』==========🍟
"""
    '🍟==============================『🍗 ʏօʊȶʊɮɛʟɨ 🍰』==============================🍟'   
    await ydl.reply_photo(
        youliurl,
        caption=helptxt
        )
    raise StopPropagation
'🍟==============================『🍗 ʏօʊȶʊɮɛʟɨ 🍰』==============================🍟'