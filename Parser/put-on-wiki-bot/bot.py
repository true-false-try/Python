import logging
import config
import wikipediaapi as wkapi

from aiogram import Bot, Dispatcher, executor, types

# Look at lvl the Logs
logging.basicConfig(level=logging.INFO)

# Initialization  my bot
bot = Bot(token=config.API_TOKEN)
dp = Dispatcher(bot)

# Parse wiki
wiki = wkapi.Wikipedia('ru')


@dp.message_handler(commands=['start'])
async def bagin(message: types.Message):
    await message.reply('Погнали, что найти: ')


@dp.message_handler()
async def echo(message: types.Message):
    search = message.text
    wiki_page = wiki.page(search)
    if wiki_page.exists():
        await message.answer(wiki_page.summary[:])
        await message.answer('Что найти: ')
    else:
        await message.answer("Страница не найдена, проверьте запрос на корректность ")


# Start my code
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)



