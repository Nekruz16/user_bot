from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from PIL import Image, ImageDraw, ImageFont
from pydub import AudioSegment
import tempfile
import os
from time import sleep
import random
import textwrap
import pymorphy2


api_id = 20560830
api_hash = 'f74af123d33751da3adbd462199f1290'

app = Client("my_account", api_id=api_id, api_hash=api_hash)

# Путь к шрифту и фоновому изображению
font_path = 'шрифт.ttf'

morph = pymorphy2.MorphAnalyzer()

@app.on_message(filters.command("type", prefixes=".") & filters.me)
def type(_, msg):
    orig_text = msg.text.split(".type ", maxsplit=1)[1]
    text = orig_text
    tbp = ""
    typing_symbol = "❋"

    while(tbp != orig_text):
        try:
            msg.edit(tbp + typing_symbol)
            sleep(0.01)

            tbp = tbp + text[0]
            text = text[1:]

            msg.edit(tbp)
            sleep(0.01)

        except FloodWait as e:
            sleep(e.x)

app.run()
