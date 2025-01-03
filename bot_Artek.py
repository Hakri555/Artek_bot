import telebot
import Token

bot = telebot.TeleBot(Token.TOKEN)


@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(message.from_user.id, "Привет👋! Добро пожаловать в предложку. Прежде, чем скидывать какие-либо "
                                           "материалы, помните, что все они сразу же отправляются Классному "
                                           "руководителю❗")
    bot.send_message(message.from_user.id, "Разработчик: https://t.me/DetroitArtek")


# Обработчик для получения фото
@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    # Получаем фото и отправляем его администратору
    bot.forward_message(Token.ADMIN_USER_ID, message.chat.id, message.message_id)
    bot.send_message(message.chat.id, "Спасибо за фото и участие в жизни класса!")


# Обработчик для получения видео
@bot.message_handler(content_types=['video'])
def handle_video(message):
    # Получаем видео и отправляем его администратору
    bot.forward_message(Token.ADMIN_USER_ID, message.chat.id, message.message_id)
    bot.send_message(message.chat.id, "Спасибо за видео и участие в жизни класса!")


# Обработчик для получения файлов (документов)
@bot.message_handler(content_types=['document'])
def handle_document(message):
    # Получаем файл и отправляем его администратору
    bot.forward_message(Token.ADMIN_USER_ID, message.chat.id, message.message_id)
    bot.send_message(message.chat.id, "Спасибо за файл и участие в жизни класса!")


# Обработчик для получения любых других типов сообщений
@bot.message_handler(content_types=['text'])
def handle_text(message):
    bot.send_message(message.chat.id, "Пожалуйста, отправьте фото, видео или файл для предложки.")


# Запуск бота
if __name__ == '__main__':
    print('Бот запущен...')
    bot.infinity_polling()
