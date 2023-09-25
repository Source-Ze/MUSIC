from pyrogram.types import InlineKeyboardButton
import config

def song_markup(_, vidid):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["SG_B_2"],
                callback_data=f"song_helper audio|{vidid}",
            ),
            InlineKeyboardButton(
                text=_["SG_B_3"],
                callback_data=f"song_helper video|{vidid}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="⌞ ѕᴏụʀᴄᴇ ze ⌝", url=f"https://t.me/UI_XB",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"], callback_data="close"
            ),
        ],
    ]
    return buttons
