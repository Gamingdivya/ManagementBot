from telegraph import upload_file
from pyrogram import filters
from MahakXMusic import app
from pyrogram.types import InputMediaPhoto
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

EVAA = [
    [
        InlineKeyboardButton(text="ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ", url=f"https://t.me/mahakxbot?startgroup=true"),
    ],
]

@app.on_message(filters.command(["tm"]))
def ul(_, message):
    reply = message.reply_to_message
    if reply.media:
        i = message.reply("❖ ᴍᴀᴋᴇ ᴀ ʟɪɴᴋ...")
        path = reply.download()
        fk = upload_file(path)
        for x in fk:
            url = "https://telegra.ph" + x

        i.edit(f'❖ ʏᴏᴜʀ ᴛᴇʟᴇɢʀᴀᴘʜ ᴜʀʟ ɪs ʀᴇᴀᴅʏ ʙᴀʙʏ ➥ {url}\n\n❖ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ➥ ๛ᴍ ᴀ ʜ ᴀ ᴋ ♡゙' , reply_markup=InlineKeyboardMarkup(EVAA),)

########____________________________________________________________######

@app.on_message(filters.command(["graph" , "grf"]))
def ul(_, message):
    reply = message.reply_to_message
    if reply.media:
        i = message.reply("❖ ᴍᴀᴋᴇ ᴀ ʟɪɴᴋ...")
        path = reply.download()
        fk = upload_file(path)
        for x in fk:
            url = "https://graph.org" + x

        i.edit(f'❖ ʏᴏᴜʀ ɢʀᴀᴘʜ ᴜʀʟ ɪs ʀᴇᴀᴅʏ ʙᴀʙʏ ➥ `{url}`\n\n❖ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ➥ ๛ᴍ ᴀ ʜ ᴀ ᴋ ♡゙' , reply_markup=InlineKeyboardMarkup(EVAA),)

__help__ = """
 ❍ ɪ ᴄᴀɴ ᴜᴘʟᴏᴀᴅ ғɪʟᴇs ᴛᴏ ᴛᴇʟᴇɢʀᴀᴘʜ


 ❍ /tm ➛ ɢᴇᴛ ᴛᴇʟᴇɢʀᴀᴘʜ ʟɪɴᴋ ᴏғ ʀᴇᴘʟɪᴇᴅ ᴍᴇᴅɪᴀ
 ❍ /grf ➛ ɢᴇᴛ ɢʀᴀᴘʜ ʟɪɴᴋ ᴏғ ʀᴇᴘʟɪᴇᴅ ᴛᴇxᴛ

"""

__mod_name__ = "ɢʀᴀᴘʜ"