import math

from pyrogram.types import InlineKeyboardButton

from JioSavaan.utils.formatters import time_to_seconds


def track_markup(_, videoid, user_id, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
    ]
    return buttons


def stream_markup_timer(_, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    anon = math.floor(percentage)
    if 0 < anon <= 10:
        ba = "𓆰⚡͚̍𝆹𝅥𝐁𝔢𝖆𝛅𝐓 𝐅🐺𝐗 𝐍𝔢𝖙𝔴𝖔𝔯𝐊🕸️"
    elif 10 < anon < 20:
        ba = "𓆰⚡͚̍𝆹𝅥𝐁𝔢𝖆𝛅𝐓 𝐅🐺𝐗 𝐍𝔢𝖙𝔴𝖔𝔯𝐊🕸️"
    elif 20 <= anon < 30:
        ba = "𓆰⚡͚̍𝆹𝅥𝐁𝔢𝖆𝛅𝐓 𝐅🐺𝐗 𝐍𝔢𝖙𝔴𝖔𝔯𝐊🕸️"
    elif 30 <= anon < 40:
        ba = "𓆰⚡͚̍𝆹𝅥𝐁𝔢𝖆𝛅𝐓 𝐅🐺𝐗 𝐍𝔢𝖙𝔴𝖔𝔯𝐊🕸️"
    elif 40 <= anon < 50:
        ba = "𓆰⚡͚̍𝆹𝅥𝐁𝔢𝖆𝛅𝐓 𝐅🐺𝐗 𝐍𝔢𝖙𝔴𝖔𝔯𝐊🕸️"
    elif 50 <= anon < 60:
        ba = "𓆰⚡͚̍𝆹𝅥𝐁𝔢𝖆𝛅𝐓 𝐅🐺𝐗 𝐍𝔢𝖙𝔴𝖔𝔯𝐊🕸️"
    elif 60 <= anon < 70:
        ba = "𓆰⚡͚̍𝆹𝅥𝐁𝔢𝖆𝛅𝐓 𝐅🐺𝐗 𝐍𝔢𝖙𝔴𝖔𝔯𝐊🕸️"
    elif 70 <= anon < 80:
        ba = "𓆰⚡͚̍𝆹𝅥𝐁𝔢𝖆𝛅𝐓 𝐅🐺𝐗 𝐍𝔢𝖙𝔴𝖔𝔯𝐊🕸️"
    elif 80 <= anon < 95:
        ba = "𓆰⚡͚̍𝆹𝅥𝐁𝔢𝖆𝛅𝐓 𝐅🐺𝐗 𝐍𝔢𝖙𝔴𝖔𝔯𝐊🕸️"
    else:
        ba = "𓆰⚡͚̍𝆹𝅥𝐁𝔢𝖆𝛅𝐓 𝐅🐺𝐗 𝐍𝔢𝖙𝔴𝖔𝔯𝐊🕸️"

##bar of wynk---------------------------------------
    
    if 0 < anon <= 5:
        bar = "Mᴏᴏɴ Vɪʙᴇ 🌛"
    elif 5 <= anon < 10:
        bar = "Mᴏᴏɴ Vɪʙᴇ 🌛"
    elif 10 <= anon < 15:
        bar = "Mᴏᴏɴ Vɪʙᴇ 🌛"
    elif 15 <= anon < 20:
        bar = "Mᴏᴏɴ Vɪʙᴇ 🌛"
    elif 20 <= anon < 25:
        bar = "Mᴏᴏɴ Vɪʙᴇ 🌛"
    elif 25 <= anon < 30:
        bar = "Mᴏᴏɴ Vɪʙᴇ 🌛"
    elif 30 <= anon < 35:
        bar = "Mᴏᴏɴ Vɪʙᴇ 🌛"
    elif 35 <= anon < 40:
        bar = "Mᴏᴏɴ Vɪʙᴇ 🌛"
    elif 40 <= anon < 45:
        bar = "Mᴏᴏɴ Vɪʙᴇ 🌛"
    elif 45 <= anon < 50:
        bar = "Mᴏᴏɴ Vɪʙᴇ 🌛"
    elif 50 <= anon < 55:
        bar = "Mᴏᴏɴ Vɪʙᴇ 🌛"
    elif 55 <= anon < 60:
        bar = "Mᴏᴏɴ Vɪʙᴇ 🌛"
    elif 60 <= anon < 65:
        bar = "Mᴏᴏɴ Vɪʙᴇ 🌛"
    elif 65 <= anon < 70:
        bar = "Mᴏᴏɴ Vɪʙᴇ 🌛"
    elif 70 <= anon < 75:
        bar = "Mᴏᴏɴ Vɪʙᴇ 🌛"
    elif 80 <= anon < 80:
        bar = "Mᴏᴏɴ Vɪʙᴇ 🌛"
    elif 80 <= anon < 85:
        bar = "Mᴏᴏɴ Vɪʙᴇ 🌛"
    elif 85 <= anon < 90:
        bar = "Mᴏᴏɴ Vɪʙᴇ 🌛"
    elif 90 <= anon < 95:
        bar = "Mᴏᴏɴ Vɪʙᴇ 🌛"
    else:
        bar = "Mᴏᴏɴ Vɪʙᴇ 🌛"
    
    buttons = [
        [
            InlineKeyboardButton(text="▷", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="II", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="↻", callback_data=f"ADMIN Replay|{chat_id}"),
            InlineKeyboardButton(text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"),
            InlineKeyboardButton(text="▢", callback_data=f"ADMIN Stop|{chat_id}"),
        ],
        [
            InlineKeyboardButton(
                text=f"{bar}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(
                text=f"{played} {ba} {dur}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(text="𝀤ٜ𖦹 𝘄 𝐍 𞥄𝝴 𝗥", url=f"ttps://t.me/Itz_alpha_dude"),
            InlineKeyboardButton(text="𝀤ٜ 𝗖 ʜ 𞥄𝝰 𝝩 𞥇", url=f"https://t.me/avalum_naanum"),           
        ],
        [
        InlineKeyboardButton(text="𝐔𝞀𝗱𝛂𝖙𝝴", url=f"https://t.me/beast_fox_network"),
        InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data=" close "),
        ]
    ]
    return buttons


def stream_markup(_, chat_id):
    buttons = [
        [
            InlineKeyboardButton(text="▷", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="II", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="↻", callback_data=f"ADMIN Replay|{chat_id}"),
            InlineKeyboardButton(text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"),
            InlineKeyboardButton(text="▢", callback_data=f"ADMIN Stop|{chat_id}"),
        ],
         [
            InlineKeyboardButton(text="𝀤ٜ𖦹 𝘄 𝐍 𞥄𝝴 𝗥", url=f"ttps://t.me/Itz_alpha_dude"),
            InlineKeyboardButton(text="𝀤ٜ 𝗖 ʜ 𞥄𝝰 𝝩 𞥇", url=f"https://t.me/avalum_naanum"),           
        ],
        [
        InlineKeyboardButton(text="𝐔𝞀𝗱𝛂𝖙𝝴", url=f"https://t.me/beast_fox_network"),
        InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data=" close "),
        ]
    ]
    return buttons


def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"AviaxPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"AviaxPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_3"],
                callback_data=f"LiveStream {videoid}|{user_id}|{mode}|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


def slider_markup(_, videoid, user_id, query, query_type, channel, fplay):
    query = f"{query[:20]}"
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="◁",
                callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {query}|{user_id}",
            ),
            InlineKeyboardButton(
                text="▷",
                callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
        ],
    ]
    return buttons
