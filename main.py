import asyncio
import config as conf
from telebot.async_telebot import AsyncTeleBot
from telebot import types
import inst

bot = AsyncTeleBot(conf.TOKEN)

Bot = asyncio.run(bot.get_me())

@bot.message_handler(commands=['start'])
async def greet(message: types.Message):
    await bot.send_message(message.from_user.id, "<b>👋Привет!</b>\nКидай ссылку на Reels, а я его тебе отправлю!", parse_mode='Html')

@bot.message_handler(content_types=['text'])
async def dl(message: types.Message):
    mess = await bot.send_message(message.from_user.id, "<b>Принял ссылку😊</b>\n\n<i>Подожди немного...</i>", parse_mode='Html')
    result, fstrm = await inst.download_reel(message.text)
    if result == "OK":
        await bot.edit_message_text("<b>✅Готово!</b>", message.from_user.id, mess.id, parse_mode='Html')
        await bot.send_video(message.from_user.id, fstrm)
    else:
        await bot.edit_message_text("<b>❌Ссылка не является Reels!</b>", message.from_user.id, mess.id, parse_mode='Html')

asyncio.run(bot.infinity_polling(skip_pending=True))