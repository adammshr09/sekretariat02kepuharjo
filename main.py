from bot import *
from handler.callback_handler import *

############ WELCOME AREA ############# 

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.from_user.id, 'Silahkan masukkan password login untuk akses sekretariat!', parse_mode='Markdown')
    bot.register_next_step_handler(message, sekretariat_auth)

def sekretariat_auth(message):
    if message.content_type == 'text':
        if message.text == '895423':
            bot.send_message(message.from_user.id, '✅ Login berhasil.')
            bot.send_message(message.from_user.id, '⚙️ *Sekretaris Kontrol Panel*', reply_markup=sekretaris_panel(), parse_mode='Markdown')
            bot.register_next_step_handler(message, nothing)
        else: 
            bot.send_message(message.from_user.id, '📵 Login gagal')
            bot.register_next_step_handler(message, sekretariat_auth)
    else:
        bot.send_message(message.from_user.id, '📵 Login gagal')
        bot.register_next_step_handler(message, sekretariat_auth)

bot.polling()