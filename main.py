import config
import logging
from aiogram import Bot, Dispatcher, executor, types
from client.keyboard import Keyboards
from server.database import session, User, create_database
from sqlalchemy import select

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=config.BOT_API)
dp = Dispatcher(bot)
kb = Keyboards()

help_message = "\n".join([
    '/start - Начало программы',
    '/help - Показывает все доступные собщения'
])

def check_have_phone(id_telegram: int) -> bool:
    smtp  = select(User).where(User.id_telegram == id_telegram)
    try:
        print(session.scalars(smtp).one())
        return True
    except Exception:
        print('Could not find user')
        return False
# query callback_data

    
# create dispatcher message handlers starting
@dp.message_handler(commands=['start'])
async def start(message: types.Message) -> None:
    """Starting the dispatcher"""
    if check_have_phone(message.from_user.id) == False:
        await message.reply("Привет", reply_markup=kb.get_contact())
    else:
        await message.reply("Рад снова видеть", reply_markup=kb.get_command())
    
@dp.message_handler(content_types=['contact'])
async def contacts(message: types.Message):
    if check_have_phone(message.from_user.id) == False:
        user = User(
            id_telegram=message.contact.user_id,
            first_name=message.contact.first_name,
            last_name=message.contact.last_name,
            phone_number=message.contact.phone_number,
            vcard=message.contact.vcard
        )
        try:
            session.add(user)
            session.commit()
        except:
            session.rollback()
            
        await message.answer(f"Твой номер успешно получен: {message.contact.phone_number}", reply_markup=types.ReplyKeyboardRemove())
        await message.answer('Приступен к работе', reply_markup=kb.get_command())
    else:
        await message.answer('Я и так уже знаю твой номер', reply_markup=kb.get_command())

@dp.message_handler(commands=['help'])
async def start(message: types.Message) -> None:
    """Starting the dispatcher"""
    await message.answer(help_message, reply_markup=kb.get_command())

@dp.message_handler()
async def cmd_dialog(message: types.Message):
    await message.answer("/help - чтобы увидеть доступные команды")

def main() -> None:
    """Start"""
    create_database()
    executor.start_polling(dp, skip_updates=False)
    
if __name__ == '__main__':
    main()
