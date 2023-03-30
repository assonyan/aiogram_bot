from aiogram import Bot, Dispatcher, types, executor

import logging


TOKEN = '6067965254:AAEykqlyE_M2a_sIfqZI-gBkxlRYYQFgjwA'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)



@dp.message_handler()
async def echo_send(message: types.Message):
	await message.answer(message.text)



if __name__ == '__main__':
	executor.start_polling(dp)
