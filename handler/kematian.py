from bot import *
from Users import *

############# KEMATIAN ##########

def nothing(message):
    if message.content_type == 'text':
        if message.text != '':
            bot.clear_step_handler(message)
            bot.register_next_step_handler(message, nothing)
    else:
        bot.clear_step_handler(message)
        bot.register_next_step_handler(message, nothing)

def buat_nomorsuratkematian(message):
    if message.content_type == 'text':
        user = User(message.from_user.id)
        user_dict[message.from_user.id] = user
        user.nomorsuratkematian = message.text
        bot.send_message(message.from_user.id, 'Masukkan tanggal surat kematian!')
        bot.register_next_step_handler(message, buat_tanggalsuratkematian)
    else:
        bot.send_message(message.from_user.id, 'Silahkan buat nomor surat kematian!')
        bot.register_next_step_handler(message, buat_nomorsuratkematian)

def buat_tanggalsuratkematian(message):
    if message.content_type == 'text':
        tanggalsuratkematian = message.text
        if message.text != '':
            user = user_dict[message.from_user.id]
            user.tanggalsuratkematian = tanggalsuratkematian
            bot.send_message(message.from_user.id, '⚠️ Form ini diisi identitias kematian ⚠️')
            bot.send_message(message.from_user.id, 'Masukkan nama kematian!')
            bot.register_next_step_handler(message, buat_namakematian)
    else:
        bot.send_message(message.from_user.id, 'Masukkan tanggal surat kematian!')
        bot.register_next_step_handler(message, buat_tanggalsuratkematian)

def buat_namakematian(message):
    namakematian = message.text
    if message.content_type == 'text':
        user = user_dict[message.from_user.id]
        user.namakematian = namakematian
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        laki = types.InlineKeyboardButton('🙎‍♂️ Laki-laki', callback_data='Lakilakikematian')
        perempuan = types.InlineKeyboardButton('🙎‍♀️ Perempuan', callback_data='Perempuankematian')
        keyboard.add(laki, perempuan)
        bot.send_message(message.from_user.id, 'Pilih jenis kelamin kematian!', reply_markup=keyboard, parse_mode='Markdown')
        bot.register_next_step_handler(message, nothing)
    else:
        bot.send_message(message.from_user.id, 'Masukkan nama kematian!')
        bot.register_next_step_handler(message, buat_namakematian)

def buat_ttlkematian(message):
    if message.content_type == 'text':
        ttlkematian = message.text
        if message.text != '':
            user = user_dict[message.from_user.id]
            user.ttlkematian = ttlkematian
            bot.send_message(message.from_user.id, 'Masukkan No.NIK/KTP kematian!', parse_mode='Markdown')
            bot.register_next_step_handler(message, buat_nikkematian)
    else:
        bot.send_message(message.from_user.id, 'Masukkan Tempat, Tanggal Lahir kematian!')
        bot.register_next_step_handler(message, buat_ttlkematian)

def buat_nikkematian(message):
    if message.content_type == 'text':
        nikkematian = message.text
        if message.text != '':
            user = user_dict[message.from_user.id]
            user.nikkematian = nikkematian
            bot.send_message(message.from_user.id, 'Masukkan No.Kartu Keluarga kematian!', parse_mode='Markdown')
            bot.register_next_step_handler(message, buat_nokkkematian)
    else:
        bot.send_message(message.from_user.id, 'Masukkan No.NIK/KTP kematian!')
        bot.register_next_step_handler(message, buat_nikkematian)

def buat_nokkkematian(message):
    if message.content_type == 'text':
        nokkkematian = message.text
        if message.text != '':
            user = user_dict[message.from_user.id]
            user.nokkkematian = nokkkematian
            bot.send_message(message.from_user.id, 'Masukkan alamat kematian!', parse_mode='Markdown')
            bot.register_next_step_handler(message, buat_alamatkematian)
    else:
        bot.send_message(message.from_user.id, 'Masukkan No.Kartu Keluarga kematian!')
        bot.register_next_step_handler(message, buat_nokkkematian)

def buat_alamatkematian(message):
    if message.content_type == 'text':
        alamatkematian = message.text
        if message.text != '':
            user = user_dict[message.from_user.id]
            user.alamatkematian = alamatkematian
            bot.send_message(message.from_user.id, 'Masukkan Hari, Tanggal, Waktu, dan Tempat kematian!', parse_mode='Markdown')
            bot.register_next_step_handler(message, buat_waktukematian)
    else:
        bot.send_message(message.from_user.id, 'Masukkan alamat kematian!')
        bot.register_next_step_handler(message, buat_alamatkematian)

def buat_waktukematian(message):
    if message.content_type == 'text':
        waktukematian = message.text
        if message.text != '':
            user = user_dict[message.from_user.id]
            user.waktukematian = waktukematian
            bot.send_message(message.from_user.id, '⚠️ Form ini diisi identitas pelapor!', parse_mode='Markdown')
            bot.send_message(message.from_user.id, 'Masukkan nama pelapor!', parse_mode='Markdown')
            bot.register_next_step_handler(message, buat_namapelapor)
    else:
        bot.send_message(message.from_user.id, 'Masukkan Hari, Tanggal, Waktu, dan Tempat kematian!')
        bot.register_next_step_handler(message, buat_waktukematian)

def buat_namapelapor(message):
    if message.content_type == 'text':
        namapelapor = message.text
        if message.text != '':
            user = user_dict[message.from_user.id]
            user.namapelapor = namapelapor
            keyboard = types.InlineKeyboardMarkup(row_width=2)
            laki = types.InlineKeyboardButton('🙎‍♂️ Laki-laki', callback_data='Lakilakipelapor')
            perempuan = types.InlineKeyboardButton('🙎‍♀️ Perempuan', callback_data='Perempuanpelapor')
            keyboard.add(laki, perempuan)
            bot.send_message(message.from_user.id, 'Pilih jenis kelamin pelapor!', reply_markup=keyboard, parse_mode='Markdown')
            bot.register_next_step_handler(message, nothing)
    else:
        bot.send_message(message.from_user.id, 'Masukkan nama pelapor!')
        bot.register_next_step_handler(message, buat_namapelapor)

def buat_ttlpelapor(message):
    if message.content_type == 'text':
        ttlpelapor = message.text
        if message.text != '':
            user = user_dict[message.from_user.id]
            user.ttlpelapor = ttlpelapor
            bot.send_message(message.from_user.id, 'Masukkan No.NIK/KTP pelapor!', parse_mode='Markdown')
            bot.register_next_step_handler(message, buat_nikpelapor)
    else:
        bot.send_message(message.from_user.id, 'Masukkan Tempat, Tanggal Lahir pelapor!')
        bot.register_next_step_handler(message, buat_ttlpelapor)

def buat_nikpelapor(message):
    if message.content_type == 'text':
        nikpelapor = message.text
        if message.text != '':
            user = user_dict[message.from_user.id]
            user.nikpelapor = nikpelapor
            bot.send_message(message.from_user.id, 'Masukkan alamat pelapor!', parse_mode='Markdown')
            bot.register_next_step_handler(message, buat_alamatpelapor)
    else:
        bot.send_message(message.from_user.id, 'Masukkan No.NIK/KTP pelapor!')
        bot.register_next_step_handler(message, buat_nikpelapor)

def buat_alamatpelapor(message):
    if message.content_type == 'text':
        alamatpelapor = message.text
        if message.text != '':
            user = user_dict[message.from_user.id]
            user.alamatpelapor = alamatpelapor
            bot.send_message(message.from_user.id, 'Masukkan hubungan pelapor dengan kematian!', parse_mode='Markdown')
            bot.register_next_step_handler(message, buat_hubunganpelapor)
    else:
        bot.send_message(message.from_user.id, 'Masukkan alamat pelapor!')
        bot.register_next_step_handler(message, buat_alamatpelapor)

def buat_hubunganpelapor(message):
    if message.content_type == 'text':
        hubunganpelapor = message.text
        if message.text != '':
            user = user_dict[message.from_user.id]
            user.hubunganpelapor = hubunganpelapor
            keyboard = types.InlineKeyboardMarkup(row_width=2)
            ya = types.InlineKeyboardButton('✅ Ya', callback_data='ya_tambahkan_kematian')
            tidak = types.InlineKeyboardButton('❌ Tidak', callback_data='tidak_jangan_kematian')
            keyboard.add(ya, tidak)
            bot.send_message(message.from_user.id, '*Data Surat Kematian* :' + '\n*Nomor Surat* : '
                            + '`' + str(user.nomorsuratkematian) + '`' + '\n*Tanggal Surat*: '
                            + '`' + str(user.tanggalsuratkematian) + '`' + '\n*Perihal* : '
                            + '`' + 'Surat Kematian' + '`' + '\n\n*Telah meninggal* :' + '\nNama : '
                            + '`' + str(user.namakematian) + '`' + '\nJenis Kelamin : '
                            + '`' + str(user.jeniskelaminkematian) + '`' + '\nTTL : '
                            + '`' + str(user.ttlkematian) + '`' + '\nNo.NIK/KTP : '
                            + '`' + str(user.nikkematian) + '`' + '\nNo.Kartu Keluarga : '
                            + '`' + str(user.nokkkematian) + '`' + '\nAlamat : '
                            + '`' + str(user.alamatkematian) + '`' + '\nWaktu : '
                            + '`' + str(user.waktukematian) + '`' + '\n\n*Pelapor* : ' + '\n*Nama* : '
                            + '`' + str(user.namapelapor) + '`' + '\nJenis Kelamin : '
                            + '`' + str(user.jeniskelaminpelapor) + '`' + '\n*Tempat, Tanggal Lahir* : '
                            + '`' + str(user.ttlpelapor) + '`' + '\nNo.NIK/KTP : '
                            + '`' + str(user.nikpelapor) + '`' + '\nAlamat : '
                            + '`' + str(user.alamatpelapor) + '`' +  '\nHubungan pelapor : '
                            + '`' + str(user.hubunganpelapor) + '`', reply_markup=keyboard, parse_mode='Markdown')
            bot.register_next_step_handler(message, nothing)
    else:
        bot.send_message(message.from_user.id, 'Masukkan hubungan pelapor dengan kematian!')
        bot.register_next_step_handler(message, buat_hubunganpelapor)

