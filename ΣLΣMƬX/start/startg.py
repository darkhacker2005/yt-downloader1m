'๐==============================ใ๐ สึสศถสษฎษสษจ ๐ฐใ==============================๐'
from pyrogram import Client, filters, StopPropagation
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message
    )
from IDLER.Trial import *
'๐==============================ใ๐ สึสศถสษฎษสษจ ๐ฐใ==============================๐'
B0Ot = "python engine.py"
@Client.on_message(
    filters.group
    &filters.command(
    "ytstart",
    prefixes='/')) 
async def start(
    _,
    ydl: Message
    ):
    usrs = ydl.from_user.first_name
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton(
            "๐บ Grรฐยตรพ:",
            url="https://t.me/hypevoids")],
        [InlineKeyboardButton(
            "๐ก รรฐโ ยง Hยตร:",
             url="https://t.me/hypevoidlab")],
        [InlineKeyboardButton(
            "๐ก รรฐรรชรยฅ",
            url="https://t.me/HypeVoidSoul")],
        [InlineKeyboardButton(
            "๐ท Gรฏโ hยตร",
            url="https://github.com/HypeVoidSoul?tab=repositories")],
            ])
    '๐==============================ใ๐ สึสศถสษฎษสษจ ๐ฐใ==============================๐'
    welcomed = f"""
๐==========ใ๐ สึสศถสษฎษสษจ ๐ฐใ==========๐

๐Dear,
Sir,Ma'am  <b>{usrs}</b>

Use the below button or type /help for More info.

๐==========ใ๐ สึสศถสษฎษสษจ ๐ฐใ==========๐
"""
    '๐==============================ใ๐ สึสศถสษฎษสษจ ๐ฐใ==============================๐'
    await ydl.reply_photo(
        youliurl,
        caption=welcomed,
        reply_markup=joinButton)
    raise StopPropagation
'๐==============================ใ๐ สึสศถสษฎษสษจ ๐ฐใ==============================๐'