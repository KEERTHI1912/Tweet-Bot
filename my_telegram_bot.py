from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import prediction_model as model
from private_data import TOKEN
import logging

logging.basicConfig(level=logging.INFO)

my_bot = Bot(TOKEN)
mydispatcher= Dispatcher(my_bot)

news_info = 'news hope gop nude paul ryan emerg ayahuasca tent vision new republican parti'



mydispatcher.message_handler(commands=["news"])
async def get_news(message: types.Message):
    news_info["content"] = message.text
    await message.answer(f'News {message.text} saved')


mydispatcher.message_handler(commands="start")
async def start(message: types.Message):
    await message.answer(f"Hi,"
                         "\nThis bot will help you detect fakeness and genuineness of a news or a message ."
                         "\nWe use advanced machine learning, NLP and Open LLM methods to classify the input"
                         "\nPlease provide the news article or message or tweet."
                         "\n\n/news"
                         "\n\n/classify"
                         )





mydispatcher.message_handler(commands=["classify"])
async def send_result(message: types.Message):
    my_result = model.predict_me(news_info)
    logging.info(f"Predicting for user with data:{news_info}")
    await message.answer(f'This is {my_result} !!!')




def main():
    executor.start_polling(mydispatcher)


if __name__ == '__main__':
    main()
