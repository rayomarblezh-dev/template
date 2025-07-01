def register_handlers(bot):
    @bot.message_handler(commands=['about'])
    def about(message):
        bot.reply_to(message, "Este es un bot modular de ejemplo usando PyTelegramBotAPI.")
