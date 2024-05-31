from logging import getLogger

import os
import telebot

from car_brands import CarBrands

logger = getLogger(__name__)

telegram_token = os.environ.get("TELEGRAM_TOKEN")

if telegram_token is None:
    raise ValueError("Telegram token not found in env TELEGRAM_TOKEN")

bot = telebot.TeleBot(telegram_token)

car_brands_instance = CarBrands()


@bot.message_handler(commands=["start"])
def welcome(message):
    bot.send_message(message.chat.id, "Дарова синки")


@bot.message_handler(content_types=["text"])
def handle_message(message):
    for brand in car_brands_instance.get_car_brands():
        if brand.lower() in message.text.lower():
            bot.send_message(
                message.chat.id, "Знаєш шо хочеться спитать? Чого не шкода?"
            )
            return
        if (
            "volkswagen" in message.text.lower()
            or "фольц" in message.text.lower()
            or "фольксваген" in message.text.lower()
        ):
            bot.send_message(message.chat.id, "не шкода, але норм")
            return
        if "шкода" in message.text.lower() or "skoda" in message.text.lower():
            bot.send_message(message.chat.id, "шкода топ")
            return
        if "яка сама піздата тачка" in message.text.lower():
            bot.send_message(message.chat.id, "канєшно шкода")
            return


if __name__ == "__main__":
    print("Bot started")
    bot.polling(none_stop=True)
