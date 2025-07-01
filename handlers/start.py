from utils.utils import saludo_usuario

def register_handlers(bot):
    @bot.message_handler(commands=['start', 'help'])
    def send_welcome(message):
        nombre = message.from_user.first_name or "usuario"
        saludo = saludo_usuario(nombre)
        bot.reply_to(message, saludo)
