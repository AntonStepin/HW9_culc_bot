
from tkinter.tix import Tree
from check import *
from culc import*

def start(update, context):
    arg = context.args
    if not arg:
        context.bot.send_message(update.effective_chat.id, "Привет, пока я могу быть только калькулятором...ну и не особо заморачиваюсь - /info")
    else:
        context.bot.send_message(update.effective_chat.id, f"{' '.join(arg)}")


def info(update, context):
    context.bot.send_message(update.effective_chat.id, "Два компота, пожалуйста...можешь ввести свое что хочешь посчитать в строку...5+5-2*1 что то такое")


def culc(update, context):
    text = update.message.text
    user_input = str(text).lower()
    try:
        if check_for_logic(user_input) == True and checks_for_user_input(user_input) == True:
            result = start_modul(user_input)
            if result == False:
                context.bot.send_message(update.effective_chat.id, "Компот со скобками")
            else:
                context.bot.send_message(update.effective_chat.id, result)
        elif check_for_logic(user_input) == False or checks_for_user_input(user_input) == False:
            context.bot.send_message(update.effective_chat.id, 'Это компот а не уровнение')
    except:
        context.bot.send_message(update.effective_chat.id, 'Этот компот выше моих сил')



def unknown(update, context):
    context.bot.send_message(update.effective_chat.id, f'Такой фрукты в моем компоте нет')
