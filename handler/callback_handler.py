from bot import *
from Users import *
from handler.pengantar import *
from handler.kematian import *
from db import *

def nothing(message):
    if message.content_type == 'text':
        if message.text != '':
            bot.clear_step_handler(message)
            bot.register_next_step_handler(message, nothing)
    else:
        bot.clear_step_handler(message)
        bot.register_next_step_handler(message, nothing)

def sekretaris_panel():
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    tambah = types.InlineKeyboardButton('✏️ Tambah Register', callback_data='tambah_register')
    lihat = types.InlineKeyboardButton('📝 Lihat Register', callback_data='lihat_register')
    refresh = types.InlineKeyboardButton('🔃 Refresh', callback_data='refresh')
    keyboard.add(tambah, lihat, refresh)
    return keyboard   

def verifikasi_nomorsurat(message):
    if message.content_type == 'text':
        if message.text != '':
            surat_info_pengantar = get_infopengantar(nomorsuratpengantar=message.text)
            surat_info_kematian = get_infokematian(nomorsuratkematian=message.text)
            bot.send_message(message.from_user.id, 'Memeriksa nomor surat dalam data register . . .', parse_mode='Markdown')
            if (check_nomorsuratpengantar(nomorsuratpengantar=message.text)[0]) or (check_nomorsuratkematian(nomorsuratkematian=message.text)[0]):
                if check_nomorsuratpengantar(nomorsuratpengantar=message.text)[0]:
                    bot.send_message(message.from_user.id, '✅ Data ditemukan.', parse_mode='Markdown')
                    bot.send_message(message.from_user.id, '*Data Surat Pengantar* :' + '\n*Nomor Surat* : ' 
                                + '`' + str(surat_info_pengantar[2]) + '`' + '\n*Tanggal Surat* : '
                                + '`' + str(surat_info_pengantar[4]) + '`' + '\n*Perihal* : '
                                + '`' + 'Surat Pengantar' + '`' + '\n\nNama : '
                                + '`' + str(surat_info_pengantar[6]) + '`' + '\nTTL : '
                                + '`' + str(surat_info_pengantar[12]) + '`' + '\nJenis Kelamin : '
                                + '`' + str(surat_info_pengantar[9]) + '`' + '\nStatus : '
                                + '`' + str(surat_info_pengantar[15]) + '`' + '\nAgama : '
                                + '`' + str(surat_info_pengantar[16]) + '`' + '\nPekerjaan : '
                                + '`' + str(surat_info_pengantar[17]) + '`' + '\nNo.NIK/KTP : '
                                + '`' + str(surat_info_pengantar[18]) + '`' + '\nPBB : '
                                + '`' + str(surat_info_pengantar[22]) + '`' + '\nAlamat : '
                                + '`' + str(surat_info_pengantar[23]) + '`' + '\nKeperluan : '
                                + '`' + str(surat_info_pengantar[26]) + '`', parse_mode='Markdown')
                    bot.send_message(message.from_user.id, '⚙️ *Sekretaris Kontrol Panel*', reply_markup=sekretaris_panel(), parse_mode='Markdown')
                    bot.register_next_step_handler(message, nothing)
                else:
                    bot.send_message(message.from_user.id, '✅ Data ditemukan.', parse_mode='Markdown')
                    bot.send_message(message.from_user.id, '*Data Surat Kematian* :' + '\n*Nomor Surat* : '
                            + '`' + str(surat_info_kematian[3]) + '`' + '\n*Tanggal Surat*: '
                            + '`' + str(surat_info_kematian[5]) + '`' + '\n*Perihal* : '
                            + '`' + 'Surat Kematian' + '`' + '\n\n*Telah meninggal* :' + '\nNama : '
                            + '`' + str(surat_info_kematian[7]) + '`' + '\nJenis Kelamin : '
                            + '`' + str(surat_info_kematian[10]) + '`' + '\nTTL : '
                            + '`' + str(surat_info_kematian[13]) + '`' + '\nNo.NIK/KTP : '
                            + '`' + str(surat_info_kematian[19]) + '`' + '\nNo.Kartu Keluarga : '
                            + '`' + str(surat_info_kematian[21]) + '`' + '\nAlamat : '
                            + '`' + str(surat_info_kematian[24]) + '`' + '\nWaktu : '
                            + '`' + str(surat_info_kematian[27]) + '`' + '\n\n*Pelapor* : ' + '\n*Nama* : '
                            + '`' + str(surat_info_kematian[8]) + '`' + '\nJenis Kelamin : '
                            + '`' + str(surat_info_kematian[11]) + '`' + '\n*Tempat, Tanggal Lahir* : '
                            + '`' + str(surat_info_kematian[14]) + '`' + '\nNo.NIK/KTP : '
                            + '`' + str(surat_info_kematian[20]) + '`' + '\nAlamat : '
                            + '`' + str(surat_info_kematian[25]) + '`' +  '\nHubungan pelapor : '
                            + '`' + str(surat_info_kematian[28]) + '`', parse_mode='Markdown')
                    bot.send_message(message.from_user.id, '⚙️ *Sekretaris Kontrol Panel*', reply_markup=sekretaris_panel(), parse_mode='Markdown')
                    bot.register_next_step_handler(message, nothing)
            else:
                bot.send_message(message.from_user.id, '❌ Nomor surat yang dimasukkan tidak ada dalam data!', parse_mode='Markdown')
                bot.send_message(message.from_user.id, '⚙️ *Sekretaris Kontrol Panel*', reply_markup=sekretaris_panel(), parse_mode='Markdown')
                bot.register_next_step_handler(message, nothing)
    else:
        bot.send_message(message.from_user.id, 'Masukkan nomor surat yang terdaftar!', parse_mode='Markdown')
        bot.register_next_step_handler(message, verifikasi_nomorsurat)
############# PANGGILAN DATA USER ##########

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == ('tambah_register') or (call.data == 'lihat_register'):
        if call.data == 'tambah_register':
            keyboard = types.InlineKeyboardMarkup(row_width=2)
            pengantar = types.InlineKeyboardButton('📝 Pengantar', callback_data='pengantar')
            kematian = types.InlineKeyboardButton('📝 Kematian', callback_data='kematian')
            batal = types.InlineKeyboardButton('❌ Batal', callback_data='batal')
            keyboard.add(pengantar, kematian, batal)
            bot.clear_step_handler(call.message)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Pilih jenis register!', reply_markup=keyboard, parse_mode='Markdown')
            bot.register_next_step_handler(call.message, nothing)
        else:
            bot.clear_step_handler(call.message)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Masukkan nomor surat yang terdaftar!', parse_mode='Markdown')
            bot.register_next_step_handler(call.message, verifikasi_nomorsurat)
    elif call.data == 'refresh':
        bot.clear_step_handler(call.message)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='🔃 Refresh', parse_mode='Markdown')
        bot.send_message(chat_id=call.message.chat.id, text='⚙️ *Sekretaris Kontrol Panel*', reply_markup=sekretaris_panel(), parse_mode='Markdown')
        bot.register_next_step_handler(call.message, nothing)
      
    elif call.data == 'batal':
        bot.clear_step_handler(call.message)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='❌ Dibatalkan.', parse_mode='Markdown')
        bot.send_message(chat_id=call.message.chat.id, text='⚙️ *Sekretaris Kontrol Panel*', reply_markup=sekretaris_panel(), parse_mode='Markdown')
        bot.register_next_step_handler(call.message, nothing)
    
    elif call.data == 'pengantar':
        bot.clear_step_handler(call.message)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Silahkan buat nomor surat pengantar!', parse_mode='Markdown')
        bot.register_next_step_handler(call.message, buat_nomorsuratpengantar)

    elif call.data == 'kematian':
        bot.clear_step_handler(call.message)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Silahkan buat nomor surat kematian!', parse_mode='Markdown')
        bot.register_next_step_handler(call.message, buat_nomorsuratkematian)

    elif call.data == ('Lakilakipemohon') or (call.data == 'Perempuanpemohon'):
        kelaminlaki = 'LAKI-LAKI'
        kelaminperempuan = 'PEREMPUAN'
        if call.data == 'Lakilakipemohon':
            if call.message.chat.id in user_dict.keys():
                user = user_dict[call.message.chat.id]
                user.jeniskelaminpemohon = kelaminlaki
                bot.clear_step_handler(call.message)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Jenis kelamin pemohon : 🙎‍♂️ Laki-laki', parse_mode='Markdown')
                bot.send_message(chat_id=call.message.chat.id, text='Masukkan status pemohon!', parse_mode='Markdown')
                bot.register_next_step_handler(call.message, buat_statuspemohon)
            else:
                bot.clear_step_handler(call.message)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='⚙️ *Sekretaris Kontrol Panel*', reply_markup=sekretaris_panel(), parse_mode='Markdown')
                bot.register_next_step_handler(call.message, nothing)
        else:
            if call.message.chat.id in user_dict.keys():
                user = user_dict[call.message.chat.id]
                user.jeniskelaminpemohon = kelaminperempuan
                bot.clear_step_handler(call.message)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Jenis kelamin pemohon : 🙎‍♀️ Perempuan', parse_mode='Markdown')
                bot.send_message(chat_id=call.message.chat.id, text='Masukkan status pemohon!', parse_mode='Markdown')
                bot.register_next_step_handler(call.message, buat_statuspemohon)
            else:
                bot.clear_step_handler(call.message)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='⚙️ *Sekretaris Kontrol Panel*', reply_markup=sekretaris_panel(), parse_mode='Markdown')
                bot.register_next_step_handler(call.message, nothing)
    
    elif call.data == ('Lakilakikematian') or (call.data == 'Perempuankematian'):
        kelaminlaki = 'LAKI-LAKI'
        kelaminperempuan = 'PEREMPUAN'
        if call.data == 'Lakilakikematian':
            if call.message.chat.id in user_dict.keys():
                user = user_dict[call.message.chat.id]
                user.jeniskelaminkematian = kelaminlaki
                bot.clear_step_handler(call.message)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Jenis kelamin kematian : 🙎‍♂️ Laki-laki', parse_mode='Markdown')
                bot.send_message(chat_id=call.message.chat.id, text='Masukkan Tempat, Tanggal Lahir kematian!', parse_mode='Markdown')
                bot.register_next_step_handler(call.message, buat_ttlkematian)
            else:
                bot.clear_step_handler(call.message)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='⚙️ *Sekretaris Kontrol Panel*', reply_markup=sekretaris_panel(), parse_mode='Markdown')
                bot.register_next_step_handler(call.message, nothing)
        else:
            if call.message.chat.id in user_dict.keys():
                user = user_dict[call.message.chat.id]
                user.jeniskelaminkematian = kelaminperempuan
                bot.clear_step_handler(call.message)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Jenis kelamin kematian : 🙎‍♀️ Perempuan', parse_mode='Markdown')
                bot.send_message(chat_id=call.message.chat.id, text='Masukkan Tempat, Tanggal Lahir kematian!', parse_mode='Markdown')
                bot.register_next_step_handler(call.message, buat_ttlkematian)
            else:
                bot.clear_step_handler(call.message)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='⚙️ *Sekretaris Kontrol Panel*', reply_markup=sekretaris_panel(), parse_mode='Markdown')
                bot.register_next_step_handler(call.message, nothing)

    elif call.data == ('Lakilakipelapor') or (call.data == 'Perempuanpelapor'):
        kelaminlaki = 'LAKI-LAKI'
        kelaminperempuan = 'PEREMPUAN'
        if call.data == 'Lakilakipelapor':
            if call.message.chat.id in user_dict.keys():
                user = user_dict[call.message.chat.id]
                user.jeniskelaminpelapor = kelaminlaki
                bot.clear_step_handler(call.message)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Jenis kelamin pelapor : 🙎‍♂️ Laki-laki', parse_mode='Markdown')
                bot.send_message(chat_id=call.message.chat.id, text='Masukkan Tempat, Tanggal Lahir pelapor!', parse_mode='Markdown')
                bot.register_next_step_handler(call.message, buat_ttlpelapor)
            else:
                bot.clear_step_handler(call.message)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='⚙️ *Sekretaris Kontrol Panel*', reply_markup=sekretaris_panel(), parse_mode='Markdown')
                bot.register_next_step_handler(call.message, nothing)
        else:
            if call.message.chat.id in user_dict.keys():
                user = user_dict[call.message.chat.id]
                user.jeniskelaminpelapor = kelaminperempuan
                bot.clear_step_handler(call.message)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Jenis kelamin pelapor : 🙎‍♀️ Perempuan', parse_mode='Markdown')
                bot.send_message(chat_id=call.message.chat.id, text='Masukkan Tempat, Tanggal Lahir pelapor!', parse_mode='Markdown')
                bot.register_next_step_handler(call.message, buat_ttlpelapor)
            else:
                bot.clear_step_handler(call.message)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='⚙️ *Sekretaris Kontrol Panel*', reply_markup=sekretaris_panel(), parse_mode='Markdown')
                bot.register_next_step_handler(call.message, nothing)

    elif call.data == ('LUNAS') or (call.data == 'BELUM LUNAS'):
        if call.data == 'LUNAS':
            if call.message.chat.id in user_dict.keys():
                user = user_dict[call.message.chat.id]
                user.pbbpemohon = call.data
                bot.clear_step_handler(call.message)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Status PBB : ✅ Lunas', parse_mode='Markdown')
                bot.send_message(chat_id=call.message.chat.id, text='Masukkan alamat pemohon!', parse_mode='Markdown')
                bot.register_next_step_handler(call.message, buat_alamatpemohon)
            else:
                bot.clear_step_handler(call.message)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='⚙️ *Sekretaris Kontrol Panel*', reply_markup=sekretaris_panel(), parse_mode='Markdown')
                bot.register_next_step_handler(call.message, nothing)
        else:
            if call.message.chat.id in user_dict.keys():
                user = user_dict[call.message.chat.id]
                user.pbbpemohon = call.data
                bot.clear_step_handler(call.message)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Status PBB : ❌ Belum Lunas', parse_mode='Markdown')
                bot.send_message(chat_id=call.message.chat.id, text='Masukkan alamat pemohon!', parse_mode='Markdown')
                bot.register_next_step_handler(call.message, buat_alamatpemohon)
            else:
                bot.clear_step_handler(call.message)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='⚙️ *Sekretaris Kontrol Panel*', reply_markup=sekretaris_panel(), parse_mode='Markdown')
                bot.register_next_step_handler(call.message, nothing)

    elif (call.data == 'ya_tambahkan_pengantar') or (call.data == 'tidak_jangan_pengantar') or (call.data == 'ya_tambahkan_kematian') or (call.data == 'tidak_jangan_kematian'):
        if call.data == 'ya_tambahkan_pengantar':
            if call.message.chat.id in user_dict.keys():
                user = user_dict[call.message.chat.id]
                bot.clear_step_handler(call.message)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Menambahkan data ' + '*' + str(user.namapemohon) + '*' + ' ke register . . .', parse_mode='Markdown')
                reg_db_pengantar(nomorsuratpengantar=user.nomorsuratpengantar, tanggalsuratpengantar=user.tanggalsuratpengantar, namapemohon=user.namapemohon, ttlpemohon=user.ttlpemohon, 
                                    jeniskelaminpemohon=user.jeniskelaminpemohon, statuspemohon=user.statuspemohon, agamapemohon=user.agamapemohon, pekerjaanpemohon=user.pekerjaanpemohon, nikpemohon=user.nikpemohon, 
                                    pbbpemohon=user.pbbpemohon, alamatpemohon=user.alamatpemohon, keperluanpemohon=user.keperluanpemohon) 
                bot.send_message(chat_id=call.message.chat.id, text='✅ Data ' + '*' + str(user.namapemohon) + '*' + ' berhasil ditambahkan.', parse_mode='Markdown')
                bot.send_message(chat_id=call.message.chat.id, text='⚙️ *Sekretaris Kontrol Panel*', reply_markup=sekretaris_panel(), parse_mode='Markdown')
                bot.register_next_step_handler(call.message, nothing)
            else:
                bot.clear_step_handler(call.message)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='⚙️ *Sekretaris Kontrol Panel*', reply_markup=sekretaris_panel(), parse_mode='Markdown')
                bot.register_next_step_handler(call.message, nothing)

        elif call.data =='tidak_jangan_pengantar':
            bot.clear_step_handler(call.message)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='❌ Dibatalkan.', parse_mode='Markdown')
            bot.send_message(chat_id=call.message.chat.id, text='⚙️ *Sekretaris Kontrol Panel*', reply_markup=sekretaris_panel(), parse_mode='Markdown')
            bot.register_next_step_handler(call.message, nothing)

        elif call.data == 'ya_tambahkan_kematian':
            if call.message.chat.id in user_dict.keys():
                user = user_dict[call.message.chat.id]
                bot.clear_step_handler(call.message)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Menambahkan data ' + '*' + str(user.namakematian) + '*' + ' ke register . . .', parse_mode='Markdown')
                reg_db_kematian(nomorsuratkematian=user.nomorsuratkematian, tanggalsuratkematian=user.tanggalsuratkematian, namakematian=user.namakematian, namapelapor=user.namapelapor, hubungankematian=user.namapelapor, 
                            ttlkematian=user.ttlkematian, ttlpelapor=user.ttlpelapor, jeniskelaminkematian=user.jeniskelaminkematian, jeniskelaminpelapor=user.jeniskelaminpelapor, nikpelapor=user.nikpelapor, 
                            nokkkematian=user.nokkkematian, nikkematian=user.nikkematian, alamatpelapor=user.alamatpelapor, alamatkematian=user.alamatkematian, 
                            waktukematian=user.waktukematian) 
                bot.send_message(chat_id=call.message.chat.id, text='✅ Data ' + '*' + str(user.namakematian) + '*' + ' berhasil ditambahkan.', parse_mode='Markdown')
                bot.send_message(chat_id=call.message.chat.id, text='⚙️ *Sekretaris Kontrol Panel*', reply_markup=sekretaris_panel(), parse_mode='Markdown')
                bot.register_next_step_handler(call.message, nothing)
            else:
                bot.clear_step_handler(call.message)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='⚙️ *Sekretaris Kontrol Panel*', reply_markup=sekretaris_panel(), parse_mode='Markdown')
                bot.register_next_step_handler(call.message, nothing)

        elif call.data =='tidak_jangan_kematian':
            bot.clear_step_handler(call.message)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='❌ Dibatalkan.', parse_mode='Markdown')
            bot.send_message(chat_id=call.message.chat.id, text='⚙️ *Sekretaris Kontrol Panel*', reply_markup=sekretaris_panel(), parse_mode='Markdown')
            bot.register_next_step_handler(call.message, nothing)
