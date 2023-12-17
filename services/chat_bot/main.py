from gigachat import GigaChat
from aiogram import Bot, Dispatcher, types, executor


bot = Bot(token='6784263805:AAHnRP-J0foSYgrOg63PUG3pLjRqGRcFYUY')

dp = Dispatcher(bot)

giga_token = 'Njg0ZDZhYmQtYzMzNi00N2I4LTg3MWQtZDc0NzU4ZjA2NjYxOmY2MmRjMzQ3LWU2MGEtNDQxMi04NGZjLWZhZTUwM2JhZGZhMA=='

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет, я твой личный помощник выборе профессии и карьеры в ней, задавай любой вопрос по твоей будущей профессии и я помогу тебе.")

@dp.message_handler()
async def send_welcome(message: types.Message):
    text = message.text

    with GigaChat(credentials=giga_token, verify_ssl_certs=False) as giga:
        response = giga.chat(text)
        await message.reply(response.choices[0].message.content)


if __name__ == '__main__':
    print('runned')
    executor.start_polling(dp)
