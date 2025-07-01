import telebot
from config.config import get_token
import importlib
import pkgutil

TOKEN = get_token()
bot = telebot.TeleBot(TOKEN)

# Cargar y registrar todos los handlers automáticamente
def cargar_handlers():
    import handlers
    for _, module_name, _ in pkgutil.iter_modules(handlers.__path__):
        if module_name == "__init__":
            continue
        module = importlib.import_module(f"handlers.{module_name}")
        if hasattr(module, "register_handlers"):
            module.register_handlers(bot)

if __name__ == "__main__":
    cargar_handlers()
    print("Bot iniciado...")
    bot.polling()
