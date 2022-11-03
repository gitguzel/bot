import os

from aiogram import*
from telegrambot import Youtube

bot = Bot("5773280727:AAHpBWXiM4CrD26E_5vBNykde9nlju6w1qU")
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_message(message:types.Message):
    chat_id = message.chat.id
    await bot.send_message(chat_id, "Привет, я могу скачивать видео с Youtube\n"
                                    "Отправь мне ссылку")

@dp.message_handler()
async def text_message(message:types.Message):
    chat_id = message.chat.id
    url = message.text
    yt = Youtube(url)
    if message.text.startswith == "https://youtu.be/" or "https://www.youtube.com/":
        await bot.send_message(chat_id, f"*Начинаю загрузку видео* : {yt.title}*\n"
                                        f"*С канала*:[{yt.author}]({yt.channel_url})", parse_mode="Markdown")
        await download_youtube_video(url, message, bot)

    
async def download_youtube_video(url, message, bot):
    yt = Youtube(url)
    stream = yt.streams.filter(progressive=True, file_extension="mp4")
    stream.get_highest_resolution().download(f"{message.chat.id}","{message.chat.id}_{yt.title}")
    with open ("{message.chat.id}/{message.chat.id}_{yt.title}", "rb") as video:
       await bot.send_video(message.chat.id, video, caption = "*Ваше видео*", parse_mode = "Markdown")
    os.remove(f"{message.chat.id}/{message.chat.id}_{yt.title}")


if __name__ == "__main__":
    executor.start_polling(dp)
