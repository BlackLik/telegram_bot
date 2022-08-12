from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData
from aiogram import types
import config

#keyboard interface
class KeyboardInterface():
    _text_btn_get_command = 'Доступные команды 🖥️'
    _text_btn_get_contact = 'Отправить свой контакт ☎️'

class Keyboards(KeyboardInterface):
    # init keyboards
    keyboard_contact = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard_command = ReplyKeyboardMarkup(resize_keyboard=True)
    
    def __init__(self):
        """Construct keyboard and buttons"""
        # create buttons to keyboards
        btn_contact = KeyboardButton(text=self._text_btn_get_contact, request_contact=True)
        btn_command = KeyboardButton(text=self._text_btn_get_command)
        
        # add buttons to keyboards
        # keyboard contact
        self.keyboard_contact.add(btn_contact)
        self.keyboard_contact.add(btn_command)
        
        #keyboard command
        self.keyboard_command.add(btn_command)
    
    def get_contact(self):
        """Returns contact keyboard"""
        return self.keyboard_contact
    
    def get_command(self):
        """Returns keyboard command"""
        return self.keyboard_command


class KeyboardCallbacks(KeyboardInterface):
    
    def __init__(self):
        super().__init__()
    
    async def check_word_callback(self, message: types.Message, kb: Keyboards = None):
        match message.text:
            case self._text_btn_get_command:
                await message.answer(config.help_message, reply_markup=kb.get_command())
            case _:
                await message.answer('Я очень люблю поболтать', reply_markup=kb.get_command())
