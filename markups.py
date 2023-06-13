from aiogram.types import (
    InlineKeyboardButton , 
    InlineKeyboardMarkup , 
    ReplyKeyboardMarkup , 
    KeyboardButton
)
from database.models import StatusChoices

def help_markup():
    marcup = InlineKeyboardMarkup()
    btns = [
        InlineKeyboardButton("Админ панель" , callback_data="admin") , 
        InlineKeyboardButton("Меню" , callback_data= "menu") ,
        InlineKeyboardButton("Туториал" , url = "https://www.youtube.com/watch?v=YxB-otfIEfI")
    ]
    marcup.add(*btns)
    return marcup


def orders_markup(order):
    markup = InlineKeyboardMarkup()
    btns = [
        InlineKeyboardButton("Редактировать", callback_data=f"edit_{order.id}"),
    ]
    if order.status == StatusChoices.ordering:
        btns.append(InlineKeyboardButton("Завершить", callback_data=f"status_complete_{order.id}"))
    elif order.status == StatusChoices.active:
        btns.append(InlineKeyboardButton("Отменить", callback_data=f"status_reject_{order.id}"))
        btns.append(InlineKeyboardButton("Закрыть прием заказов", callback_data=f"status_close_{order.id}"))
    markup.row_width = 2
    markup.add(*btns)
    return markup