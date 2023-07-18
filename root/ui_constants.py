import html
import time

import aiogram.utils.markdown as md
from aiogram.types.reply_keyboard import ReplyKeyboardMarkup, KeyboardButton as RKB


def unescape(s: str):
    return html.unescape(s.replace("$#", "&#"))


class Signer:
    signature_base: str

    def set_signature(self, bot_name: str):
        self.signature_base = f'via {bot_name}'

    def get_signature(self, performer: str):
        return md.hitalic(
            f'#{performer.replace(" ", "_")}, {self.signature_base}')


YES = "🟢"
NO = "🔴"
BACK = "⬆️ Back"
HIDE = "⤴️ Hide"
SHOW = "⤵️ Show"
PREV = "◀️"
NEXT = "▶️"
STOP = "⛔️"
REFRESH = "🔄"
ROCKET = "🚀"
EARTH = "🌍"
JUPITER = "🪐"
CLOCK = "⏳"
LIGHTNING = "⚡"

NO_CONFIG_MESSAGE = "Please take config.ini from developers"
SETTINGS = "Settings.."
MODE_ON = "Mode was changed (ON)"
MODE_OFF = "Mode was changed (OFF)"

ADDED = "Succsesfully added!"
SETTED = "Succsesfully setted!"
DELETED = "Succsesfully deleted!"
SENDED = "Succsesfully sent!"
FINDED = "По вашему запросу нашлось"

WAIT = "Please wait..."
WRONG = "Wrong command("
ERROR = "Что-то сломалось :c"
NOT_FOUND = "По вашему запросу ничего не нашлось :с"
NOTHING_NEW = "Nothing is new."
FIND_NO_ARGS = "Please write '/find some text' to seek streams.\nMinimal length of text 3!\nMaximal length of text 30!"
TOO_SMALL = "Message is to small"
TOO_BIG = "Слишком большой запрос :с"
EMPTY = "Ваш запрос пуст. Поcмотрите примеры в /help"
UNKNOW_CMD = "Unknow command =/\nEnter /help to get list of commands"
NO_ACCESS = "Недостаточно прав!"
OLD_MESSAGE = "Sorry. It's message is out of date :("


MAIN_KEYBOARD = ReplyKeyboardMarkup(keyboard=[
    [RKB(text='👑 Popular'), RKB(text='🆕 New songs')],
    [RKB(text='❓ Help')],
    [RKB(text='🔨 Settings'),    RKB(text='📔 About')]
], resize_keyboard=True, one_time_keyboard=True, selective=True)

SETTINGS_KEYBOARD = [
    [RKB(text='↩️ Back')]
]

KEYBOARD_COMMANDS = {
    'popular': '👑 Popular',
    'new_songs': '🆕 New songs',
    'help': '❓ Help',
    'settings': '🔨 Settings',
    'about': '📔 About',
    'get_state': '📈 Bot State',
    'all_mode_on': '🐵 Listen to all message',
    'all_mode_off': '🙈 Listen only to commands',
    'start': '↩️ Back'
}


HELP_TEXT = """❓ Help
/start - получить основную клавиатуру.

/help - рекурсия...
/about - информация о разработчике.

/find - искать музыку🔍. Чтобы воспользоватся после команды надо написать название или автора произведения.
Синоним: /f
Пример: "/find zoom - last dinosaurs"
Пример: "/f zoom - last dinosaurs"

/popular - получить список самых популярных треков.
Синоним: /chart

/new_songs - получить список новинок.
Синоним: /novelties

/review - написать разработчику
Синоним: /r
Пример: "/review Привет!"
Пример: "/r Привет!"


Для админов чатов:
/settings - открыть настройки.
/all_mode_on - включить публичный мод.
/all_mode_off - отключить публичный мод.

Публичный мод - мод в котором бот читает все сообщения и воспринимает их как запрос к поиску /find.
Если мод отключен, бот реагирует только на команды.
Чтобы бот игнорировал любые сообщения добавте '\\' в началоо сообщения
"""

VIPHELP_TEXT = """
/vipinfo - get raw info about msg
/viphelp - get help for admin commands

/rep chat_id - answer to review

/err - raise err in bot
"""

ABOUT_TEXT = """📔 About!
📫 For any questions: @dashed_man
py3.11"""


def queue_is_full():
    return f'{STOP} Service is busy! Try later again.'


def add_to_download_queue(title: str, artist: str, average_load_time: float):
    return f'{CLOCK} {artist} - {title} added to queue! (average waiting time: {int(average_load_time):d} sec)'


def starting_download(title: str, artist: str):
    return f'{ROCKET} {artist} - {title}'


def build_review_info(message):
    return f"Review from {md.quote_html(message.from_user.mention)}" \
           f"(user: {md.hcode(message.from_user.id)}, " \
           f"chat: {md.hcode(message.chat.id)})" \
           f"{'[is a bot]' if message.from_user.is_bot else ''}"


def build_track_button_name(
        performer: str,
        title: str,
        duration: time.struct_time,
        is_in_cache: bool,
):
    return f'{performer} - {title} ({duration.tm_min}:{duration.tm_sec:02})' + (
         ' ' + LIGHTNING if is_in_cache else ''
    )
