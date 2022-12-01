import telebot
from telebot import types
from tkinter import *

bot = telebot.TeleBot("ТОКЕН", parse_mode=None)

markup = types.ReplyKeyboardMarkup()
leave_message = types.KeyboardButton('Обращение')
ok = types.KeyboardButton('Подтвердить')
markup.add(leave_message, ok)


# ЗАДАЧА№1_____________________________________________________________________________________
@bot.message_handler(commands=['start'])
def hello(message):
    bot.send_message(message.from_user.id, f"Здравствуйте, {message.from_user.first_name}! Чем могу помочь?", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def leave_message(message):
    
    

    if message.text.lower() == 'обращение':
        bot.send_message(message.from_user.id, "Опишите ситуацию.")
        global message_1
        message_1 = True
    elif message_1:
        data = open("all_appeals.txt", 'a', encoding='utf-8')
        data.writelines(f"{message.from_user.id}: {message.text}\n")
        data.close
        bot.send_message(message.from_user.id, 'Ваше обращение записано. Для поддтверждения нажмите кнопку "Подтвердить".')
        message_1 = False
        # ЗАДАЧА№2_________________________________________________________________________________________________________
    elif message.text.lower() == 'подтвердить':
        global all_message
        global print_message
        global send_message
        def print_message():
            data = open("all_appeals.txt", 'r', encoding='utf-8')
            for message in data.readlines():
                all_message.insert(END, message)
            data.close()

        def send_message():
            m_cop = all_message.curselection()
            all_message.get(m_cop[0])
            all_message.clipboard_clear()
            all_message.clipboard_append(all_message.get(m_cop[0]))
            list = all_message.get(m_cop[0]).split(":")
            text_mes=list[1].removesuffix("\n")
            text = text_reply.get("1.0", END)
            id =str(list[0])
            bot.send_message(id, f'Здравствуйте.\nВы оставили нам следующее обращение: "{text_mes}".\nВот наш ответ:\n{text}')

        root = Tk()
        root.geometry('1280x720')

        all_message = Listbox(root, width=212, height=30, selectmode=EXTENDED)
        all_message.grid(row=0, column=0)
        print_message()

        lable_reply = Label(root, text='Введите ответ:')
        lable_reply.grid(row=2, column=0)
        text_reply = Text(root, width=150, height=10)
        text_reply.grid(row=3, column=0)
        but_send_reply = Button(root, text="Отправить ответ", command=send_message)
        but_send_reply.grid(row=4, column=0)
    
        root.mainloop()





bot.infinity_polling()
