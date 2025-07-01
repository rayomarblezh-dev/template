import os
from dotenv import load_dotenv

load_dotenv()

def get_token():
    """Obtiene el token del bot desde las variables de entorno."""
    return os.getenv("TOKEN")
