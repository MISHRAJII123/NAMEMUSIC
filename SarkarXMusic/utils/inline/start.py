from pyrogram.types import InlineKeyboardButton

import config
from SarkarXMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
        ],
        [
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_5"], url=f"https://t.me/ll_STYLISH_NAME_BOT"
            ),
        ],
        [
            InlineKeyboardButton(text="❍ 𝐎꯭ᴡ꯭ɴᴇ꯭ʀ ❍", url=f"https://t.me/ll_SARKAR_OWNER_ll"),
        ],
        [
            InlineKeyboardButton(text="❍ 𝐌𝐔𝐒𝐈𝐂 𝐁𝐎𝐓 ❍", url=f"https://t.me/SARKAR_UPDATE/74"),
        ],
    ]
    return buttons
