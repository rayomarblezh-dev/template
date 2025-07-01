# Bot de Telegram con PyTelegramBotAPI

Plantilla sencilla de Ray O. Blez para crear tu propio bot de Telegram usando la librería [PyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI).

---

## Requisitos

- Python 3.7 o superior
- pyTelegramBotAPI
- python-dotenv (opcional, recomendado para gestionar el token de forma segura)

---

## Instalación

Instala las dependencias necesarias:

```bash
pip install -r requirements.txt
```

---

## Configuración

1. Crea tu bot en Telegram y obtén el token con [@BotFather](https://t.me/BotFather).
2. Clona este repositorio y crea un archivo `.env` en la raíz del proyecto con el siguiente contenido:

    ```
    TOKEN=tu_token_aqui
    ```

3. Personaliza `main.py` según la lógica que desees para tu bot.

---

## Ejemplo de uso

```python
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
```

Agrega nuevos archivos en la carpeta `handlers/` con una función `register_handlers(bot)` para añadir comandos o funcionalidades.

---

## Ejecución

Inicia el bot con:

```bash
python main.py
```

---

## Recursos útiles

- [Documentación oficial de PyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI)
- [API de Telegram Bots](https://core.telegram.org/bots/api)

---

Personaliza este proyecto y crea tu propio bot de Telegram.