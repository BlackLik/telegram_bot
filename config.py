from dotenv import load_dotenv
import os

load_dotenv()

# BOT_API
BOT_API = os.environ.get('BOT_API')

# help message
help_message = "\n".join([
    '/start - Начало программы',
    '/help - Показывает все доступные собщения'
])