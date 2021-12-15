from bot import *
from Users import *

############# PENGANTAR ##########

def nothing(message):
    if message.content_type == 'text':
        if message.text != '':
            bot.clear_step_handler(message)
            bot.register_next_step_handler(message, nothing)
    else:
        bot.clear_step_handler(message)
        bot.register_next_step_handler(message, nothing)

def buat_nomorsuratpengantar(message):
    if message.content_type == 'text':
        user = User(message.from_user.id)
        user_dict[message.from_user.id] = user
        user.nomorsuratpengantar = message.text
        bot.send_message(message.from_user.id, 'Masukkan tanggal surat pengantar!')
        bot.register_next_step_handler(message, buat_tanggalsuratpengantar)
    else:
        bot.send_message(message.from_user.id, 'Silahkan buat nomor surat pengantar!')
        bot.register_next_step_handler(message, buat_nomorsuratpengantar)

def buat_tanggalsuratpengantar(message):
    if message.content_type == 'text':
        tanggalsuratpengantar = message.text
        if message.text != '':
            user = user_dict[message.from_user.id]
            user.tanggalsuratpengantar = tanggalsuratpengantar
            bot.send_message(message.from_user.id, 'Masukkan nama pemohon!')
            bot.register_next_step_handler(message, buat_namapemohon)
    else:
        bot.send_message(message.from_user.id, 'Masukkan tanggal surat pengantar!')
        bot.register_next_step_handler(message, buat_tanggalsuratpengantar)

def buat_namapemohon(message):
    if message.content_type == 'text':
        namapemohon = message.text
        if message.text != '':
            user = user_dict[message.from_user.id]
            user.namapemohon = namapemohon
            bot.send_message(message.from_user.id, 'Masukkan Tempat, Tanggal lahir!')
            bot.register_next_step_handler(message, buat_ttlpemohon)
    else:
        bot.send_message(message.from_user.id, 'Masukkan nama pemohon!')
        bot.register_next_step_handler(message, buat_namapemohon)

def buat_ttlpemohon(message):
    if message.content_type == 'text':
        ttlpemohon = message.text
        if message.text != '':
            user = user_dict[message.from_user.id]
            user.ttlpemohon = ttlpemohon
            keyboard = types.InlineKeyboardMarkup(row_width=2)
            laki = types.InlineKeyboardButton('🙎‍♂️ Laki-laki', callback_data='Lakilakipemohon')
            perempuan = types.InlineKeyboardButton('🙎‍♀️ Perempuan', callback_data='Perempuanpemohon')
            keyboard.add(laki, perempuan)
            bot.send_message(message.from_user.id, 'Pilih jenis kelamin pemohon!', reply_markup=keyboard, parse_mode='Markdown')
            bot.register_next_step_handler(message, nothing)
    else:
        bot.send_message(message.from_user.id, 'Masukkan Tempat, Tanggal lahir!')
        bot.register_next_step_handler(message, buat_ttlpemohon)

def buat_statuspemohon(message):
    if message.content_type == 'text':
        statuspemohon = message.text
        if message.text != '':
            user = user_dict[message.from_user.id]
            user.statuspemohon = statuspemohon
            bot.send_message(message.from_user.id, 'Masukkan agama pemohon!', parse_mode='Markdown')
            bot.register_next_step_handler(message, buat_agamapemohon)
    else:
        bot.send_message(message.from_user.id, 'Masukkan status pemohon!')
        bot.register_next_step_handler(message, buat_statuspemohon)

def buat_agamapemohon(message):
    if message.content_type == 'text':
        agamapemohon = message.text
        if message.text != '':
            user = user_dict[message.from_user.id]
            user.agamapemohon = agamapemohon
            bot.send_message(message.from_user.id, 'Masukkan pekerjaan pemohon!', parse_mode='Markdown')
            bot.register_next_step_handler(message, buat_pekerjaanpemohon)
    else:
        bot.send_message(message.from_user.id, 'Masukkan agama pemohon!')
        bot.register_next_step_handler(message, buat_agamapemohon)

def buat_pekerjaanpemohon(message):
    if message.content_type == 'text':
        pekerjaanpemohon = message.text
        if message.text != '':
            user = user_dict[message.from_user.id]
            user.pekerjaanpemohon = pekerjaanpemohon
            bot.send_message(message.from_user.id, 'Masukkan No.NIK/KTP pemohon!', parse_mode='Markdown')
            bot.register_next_step_handler(message, buat_nikpemohon)
    else:
        bot.send_message(message.from_user.id, 'Masukkan pekerjaan pemohon!')
        bot.register_next_step_handler(message, buat_pekerjaanpemohon)

def buat_nikpemohon(message):
    if message.content_type == 'text':
        nikpemohon = message.text
        if message.text != '':
            user = user_dict[message.from_user.id]
            user.nikpemohon = nikpemohon
            keyboard = types.InlineKeyboardMarkup(row_width=2)
            lunas = types.InlineKeyboardButton('✅ Lunas', callback_data='LUNAS')
            belumlunas = types.InlineKeyboardButton('❌ Belum Lunas', callback_data='BELUM LUNAS')
            keyboard.add(lunas, belumlunas)
            bot.send_message(message.from_user.id, 'Pilih status PBB pemohon!', reply_markup=keyboard, parse_mode='Markdown')
            bot.register_next_step_handler(message, nothing)
    else:
        bot.send_message(message.from_user.id, 'Masukkan No.NIK/KTP pemohon!')
        bot.register_next_step_handler(message, buat_nikpemohon)

def buat_alamatpemohon(message):
    if message.content_type == 'text':
        alamatpemohon = message.text
        if message.text != '':
            user = user_dict[message.from_user.id]
            user.alamatpemohon = alamatpemohon
            bot.send_message(message.from_user.id, 'Masukkan keperluan pemohon!', parse_mode='Markdown')
            bot.register_next_step_handler(message, buat_keperluanpemohon)
    else:
        bot.send_message(message.from_user.id, 'Masukkan alamat pemohon!')
        bot.register_next_step_handler(message, buat_alamatpemohon)

def buat_keperluanpemohon(message):
    if message.content_type == 'text':
        keperluanpemohon = message.text
        if message.text != '':
            user = user_dict[message.from_user.id]
            user.keperluanpemohon = keperluanpemohon
            keyboard = types.InlineKeyboardMarkup(row_width=2)
            ya = types.InlineKeyboardButton('✅ Ya', callback_data='ya_tambahkan_pengantar')
            tidak = types.InlineKeyboardButton('❌ Tidak', callback_data='tidak_jangan_pengantar')
            keyboard.add(ya, tidak)
            bot.send_message(message.from_user.id, '*Data Surat Pengantar Pemohon* :' + '\n*Nomor Surat* : '
                                + '`' + str(user.nomorsuratpengantar) + '`' + '\n*Tanggal Surat* : '
                                + '`' + str(user.tanggalsuratpengantar) + '`' + '\n*Perihal* : '
                                + '`' + 'Surat Pengantar' + '`' + '\n\nNama : '
                                + '`' + str(user.namapemohon) + '`' + '\nTTL : '
                                + '`' + str(user.ttlpemohon) + '`' + '\nJenis Kelamin : '
                                + '`' + str(user.jeniskelaminpemohon) + '`' + '\nStatus : '
                                + '`' + str(user.statuspemohon) + '`' + '\nAgama : '
                                + '`' + str(user.agamapemohon) + '`' + '\nPekerjaan : '
                                + '`' + str(user.pekerjaanpemohon) + '`' + '\nNo.NIK/KTP : '
                                + '`' + str(user.nikpemohon) + '`' + '\nPBB : '
                                + '`' + str(user.pbbpemohon) + '`' + '\nAlamat : '
                                + '`' + str(user.alamatpemohon) + '`' + '\nKeperluan : '
                                + '`' + str(user.keperluanpemohon) + '`', parse_mode='Markdown')
            bot.send_message(message.from_user.id, 'Tambahkan ke data register?', reply_markup=keyboard, parse_mode='Markdown')
            bot.register_next_step_handler(message, nothing)
    else:
        bot.send_message(message.from_user.id, 'Masukkan keperluan pemohon!')
        bot.register_next_step_handler(message, buat_keperluanpemohon)