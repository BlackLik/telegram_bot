from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

class Keyboards():
    # init keyboards
    keyboard_contact = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard_command = ReplyKeyboardMarkup(resize_keyboard=True)
    
    def __init__(self):
        """Construct"""
        # create buttons to keyboards
        btn_contact = KeyboardButton(text='Отправить свой контакт ☎️', request_contact=True)
        btn_command = KeyboardButton(text='Доступные команды 🖥️')
        
        # add buttons to keyboards
        self.keyboard_contact.add(btn_contact)
        self.keyboard_contact.add(btn_command)
        self.keyboard_command.add(btn_command)
    
    def get_contact(self):
        """Returns contact keyboard"""
        return self.keyboard_contact
    
    def get_command(self):
        """Returns keyboard command"""
        return self.keyboard_command

