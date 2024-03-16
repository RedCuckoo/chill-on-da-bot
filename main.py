import telebot
from logging import getLogger

logger = getLogger(__name__)

bot = telebot.TeleBot("")


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, "Дарова синки")


def get_car_brands():
    return [
        "Abarth",
        "Alfa Romeo",
        "Aston Martin",
        "Audi",
        "Bentley",
        "BMW",
        "Bugatti",
        "Cadillac",
        "Chevrolet",
        "Chrysler",
        "Citroën",
        "Dacia",
        "Daewoo",
        "Daihatsu",
        "Dodge",
        "Donkervoort",
        "DS",
        "Ferrari",
        "Fiat",
        "Fisker",
        "Ford",
        "Honda",
        "Hummer",
        "Hyundai",
        "Infiniti",
        "Iveco",
        "Jaguar",
        "Jeep",
        "Kia",
        "KTM",
        "Lada",
        "Lamborghini",
        "Lancia",
        "Land Rover",
        "Landwind",
        "Lexus",
        "Lotus",
        "Maserati",
        "Maybach",
        "Mazda",
        "McLaren",
        "Mercedes-Benz",
        "MG",
        "Mini",
        "Mitsubishi",
        "Morgan",
        "Nissan",
        "Opel",
        "Peugeot",
        "Porsche",
        "Renault",
        "Rolls-Royce",
        "Rover",
        "Saab",
        "Seat",
        "Smart",
        "SsangYong",
        "Subaru",
        "Suzuki",
        "Tesla",
        "Toyota",
        "Volvo",
        "жигулі",
        "жига",
        "копійка",
        "копейка",
        "бмв",
        "тойота",
        "рено",
        "мено",
        "реган",
        "мерс",
        "беха",
        "порш",
        "мазда",
        "ауді",
        "бумер",
    ]


@bot.message_handler(content_types=['text'])
def handle_message(message):
    for brand in get_car_brands():
        if brand.lower() in message.text.lower():
            bot.send_message(message.chat.id, "Знаєш шо хочеться спитать? Чого не шкода?")
            return
        if "volkswagen" in message.text.lower() or "фольц" in message.text.lower() or "фольксваген" in message.text.lower():
            bot.send_message(message.chat.id, "не шкода, але норм")
            return
        if "шкода" in message.text.lower() or "skoda" in message.text.lower():
            bot.send_message(message.chat.id, "шкода топ")
            return
        if "яка сама піздата тачка" in message.text.lower():
            bot.send_message(message.chat.id, "канєшно шкода")
            return


if __name__ == "__main__":
    bot.polling(none_stop=True)
