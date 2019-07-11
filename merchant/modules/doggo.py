import requests
from random import randint
import re

from pyrogram import Filters, Message

from merchant import BOT
from merchant.helpers import ReplyCheck


def get_dog(filter_types):
    r = requests.get("https://random.dog/woof.json?filter={}".format(filter_types))
    if r.status_code == 200:
        data = r.json()
        url = data["url"]
        return url


def get_doggo():
    r = requests.get("http://shibe.online/api/shibes")
    if r.status_code == 200:
        data = r.json()
        url = data[0]
        return url


@BOT.on_message(Filters.regex("(?i)(post|get|send) (shibe|dog|doggo|woof|🐶|🐕) (gif|gifs)") & ~Filters.edited)
async def send_dog(bot: BOT, message: Message):
    if re.match("(?i)(post|get|send) (dog|doggo|woof|🐶|🐕) (gif|gifs)", message.text):
        link_to_image = get_dog("webm,png,jpg,jpeg")
        await BOT.send_animation(
            chat_id=message.chat.id,
            animation=link_to_image,
            disable_notification=True,
            reply_to_message_id=ReplyCheck(message)
        )


@BOT.on_message(Filters.regex("(?i)(post|get|send) (shibe|dog|doggo|woof|🐶|🐕)") & ~Filters.edited)
async def send_dog_gif(bot: BOT, message: Message):
    if re.match("(?i)(post|get|send) (dog|doggo|woof|🐶|🐕)", message.text):
        if randint(0, 1) == 1:
            link_to_image = get_dog("webm,mp4")
        else:
            link_to_image = get_doggo()

        await BOT.send_photo(
            chat_id=message.chat.id,
            photo=link_to_image,
            disable_notification=True,
            reply_to_message_id=ReplyCheck(message)
        )