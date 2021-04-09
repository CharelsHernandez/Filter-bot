#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @trojanzhex

import asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from script import script
from pyrogram.errors import FloodWait



@Client.on_message(filters.command(["start"]) & filters.private)
async def start(client, message):
    text = message.text
    if ("get" in text):
        args = text.split(" ", 1)[1]
        argument = args.split("_")
        if len(argument) == 3:
            try:
                msg_id = int(argument[1])
                chat_id = int(argument[2])
            except:
                return
        try:
            msg = await client.get_messages(
                chat_id=chat_id,
                message_ids=msg_id
            )
        except:
            await message.reply_text("Something went wrong..!")
            return
        try:
            await msg.copy(chat_id=message.from_user.id)
        except FloodWait as e:
            await asyncio.sleep(e.x)
            await msg.copy(chat_id=message.from_user.id)
        except:
            pass
        return
    try:
        await message.reply_text(
            text=script.START_MSG.format(message.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("HELP", callback_data="help_data"),
                        InlineKeyboardButton("ABOUT", callback_data="about_data"),
                    ],
                    [
                        InlineKeyboardButton(
                            "⭕️ JOIN OUR CHANNEL ⭕️", url="https://t.me/TroJanzHEX")
                    ]
                ]
            ),
            reply_to_message_id=message.message_id
        )
    except:
        pass

@Client.on_message(filters.command(["help"]) & filters.private)
async def help(client, message):
    try:
        await message.reply_text(
            text=script.HELP_MSG,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("BACK", callback_data="start_data"),
                        InlineKeyboardButton("ABOUT", callback_data="about_data"),
                    ],
                    [
                        InlineKeyboardButton(
                            "⭕️ SUPPORT ⭕️", url="https://t.me/TroJanzSupport")
                    ]
                ]
            ),
            reply_to_message_id=message.message_id
        )
    except:
        pass

@Client.on_message(filters.command(["about"]) & filters.private)
async def about(client, message):
    try:
        await message.reply_text(
            text=script.ABOUT_MSG,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("BACK", callback_data="help_data"),
                        InlineKeyboardButton("START", callback_data="start_data"),
                    ],
                    [
                        InlineKeyboardButton(
                            "SOURCE CODE", url="https://github.com/TroJanzHEX/Auto-Filter-Bot-V2")
                    ]
                ]
            ),
            reply_to_message_id=message.message_id
        )
    except:
        pass
