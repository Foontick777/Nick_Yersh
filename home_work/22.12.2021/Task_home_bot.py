import telebot
from telebot import types

bot = telebot.TeleBot('5056339400:AAE89rtqMIIECz3_YNyBNZBE1A3iQHPongc')

@bot.message_handler(content_types=['text'])
def inline(message):
    if message.text == "Привет":
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Справочник", callback_data="Справочник")
        but_2 = types.InlineKeyboardButton(text="Поиск", callback_data="Поиск")
        but_3 = types.InlineKeyboardButton(text="Статистика", callback_data="Статистика")
        but_4 = types.InlineKeyboardButton(text="Мои соседи", callback_data="Мои соседи")
        but_5 = types.InlineKeyboardButton(text="Контроль", callback_data="Контроль")
        but_6 = types.InlineKeyboardButton(text="Мой профиль", callback_data="Мой профиль")
        key.add(but_1, but_2, but_3, but_4, but_5, but_6)
        bot.send_message(message.chat.id, "Меню", reply_markup=key)
    else:
        bot.send_message(message.chat.id, "Не понимаю. Напиши 'Привет' ")

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == "Справочник":
        keyboard = types.InlineKeyboardMarkup()
        key_1 = types.InlineKeyboardButton(text='Администрация', callback_data='key_1')
        key_2 = types.InlineKeyboardButton(text='Телефоны строителей', callback_data='key_2')
        key_3 = types.InlineKeyboardButton(text='Адрес дома', callback_data='key_3')
        key_4 = types.InlineKeyboardButton(text='Инфраструктура', callback_data='key_4')
        keyboard.add(key_1)
        keyboard.add(key_2)
        keyboard.add(key_3)
        keyboard.add(key_4)
        bot.send_message(call.message.chat.id, text='Выберите раздел для просмотра: ', reply_markup=keyboard)
    elif call.data == "Поиск":
        keyboard_2 = types.InlineKeyboardMarkup()
        key_5 = types.InlineKeyboardButton(text='По номеру квартиры', callback_data='key_5')
        key_6 = types.InlineKeyboardButton(text='По номеру телефона', callback_data='key_6')
        key_7 = types.InlineKeyboardButton(text='По номеру автомобиля', callback_data='key_7')
        key_8 = types.InlineKeyboardButton(text='Отмена', callback_data='key_8')
        keyboard_2.add(key_5)
        keyboard_2.add(key_6)
        keyboard_2.add(key_7)
        keyboard_2.add(key_8)
        bot.send_message(call.message.chat.id, text='Как будем искать жильцов?', reply_markup=keyboard_2)
    elif call.data == "Статистика":
        keyboard_3 = types.InlineKeyboardMarkup()
        key_9 = types.InlineKeyboardButton(text='Шахматка квартир', callback_data='key_9')
        keyboard_3.add(key_9)
        bot.edit_message_text( call.message.chat.id, call.message.message_id, reply_markup=keyboard_3)

bot.polling()