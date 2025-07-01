<style>
.readme-container {
    font-family: 'Segoe UI', Arial, sans-serif;
    background: #f7f9fa;
    border-radius: 12px;
    padding: 32px 24px;
    max-width: 800px;
    margin: 32px auto;
    box-shadow: 0 4px 24px rgba(0,0,0,0.07);
    color: #222;
}
.readme-container h1 {
    color: #0088cc;
    font-size: 2.5em;
    margin-bottom: 0.2em;
}
.readme-container h2, .readme-container h3 {
    color: #005f8c;
    margin-top: 1.5em;
}
.readme-container ul {
    padding-left: 1.5em;
}
.readme-container code, .readme-container pre {
    background: #eaf6fb;
    color: #005f8c;
    border-radius: 5px;
    padding: 2px 6px;
    font-size: 1em;
}
.readme-container pre {
    padding: 12px;
    overflow-x: auto;
}
.readme-container a {
    color: #0088cc;
    text-decoration: none;
    border-bottom: 1px dotted #0088cc;
    transition: border 0.2s;
}
.readme-container a:hover {
    border-bottom: 1px solid #0088cc;
}
.readme-container hr {
    border: none;
    border-top: 1px solid #cce7f6;
    margin: 2em 0;
}
.readme-container .note {
    background: #fffbe6;
    border-left: 4px solid #ffe066;
    padding: 12px 18px;
    margin: 1em 0;
    border-radius: 6px;
    color: #7a6700;
}
</style>

<div class="readme-container">

# Bot de Telegram con PyTelegramBotAPI

Esta plantilla te permite crear fácilmente un bot de Telegram utilizando la librería <a href="https://github.com/eternnoir/pyTelegramBotAPI" target="_blank">PyTelegramBotAPI</a>.

## Requisitos

<ul>
    <li>Python 3.7 o superior</li>
    <li>pyTelegramBotAPI</li>
    <li>python-dotenv <span style="color:#888;">(opcional, recomendado para gestionar el token de forma segura)</span></li>
</ul>

## Instalación

Instala las dependencias necesarias con pip:

<pre><code>pip install -r requirements.txt</code></pre>

## Configuración

<ol>
    <li><b>Crea un bot en Telegram</b> y obtén tu token usando <a href="https://t.me/BotFather" target="_blank">@BotFather</a>.</li>
    <li><b>Clona este repositorio</b> y crea un archivo <code>.env</code> en la raíz del proyecto con el siguiente contenido:
        <pre><code>TOKEN=tu_token_aqui</code></pre>
    </li>
    <li><b>Edita <code>main.py</code></b> si es necesario para personalizar la lógica de tu bot.</li>
</ol>

## Ejemplo de uso

<pre><code>import telebot
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
</code></pre>

<div class="note">
Ahora puedes agregar nuevos archivos en la carpeta <code>handlers/</code> con una función <code>register_handlers(bot)</code> para añadir más comandos o funcionalidades.
</div>

## Ejecución

Inicia el bot ejecutando:

<pre><code>python main.py</code></pre>

## Recursos útiles

<ul>
    <li><a href="https://github.com/eternnoir/pyTelegramBotAPI" target="_blank">Documentación oficial de PyTelegramBotAPI</a></li>
    <li><a href="https://core.telegram.org/bots/api" target="_blank">API de Telegram Bots</a></li>
</ul>

<hr />

¡Personaliza este proyecto para crear tu propio bot de Telegram!

</div>