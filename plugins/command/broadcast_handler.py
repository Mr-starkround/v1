import asyncio
import config
import re

from pyrogram import Client
from pyrogram.types import (
    Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
)
from pyrogram.errors import (
    FloodWait, PeerIdInvalid, UserIsBlocked, InputUserDeactivated
)
from plugins import Database

async def broadcast_handler(client: Client, msg: Message):
    if msg.reply_to_message is None:
        await msg.reply('Harap reply sebuah pesan', True)

    else:
        anu = msg.reply_to_message
        anu = await anu.copy(msg.chat.id, reply_to_message_id=anu.id)
        markup = InlineKeyboardMarkup([
            [InlineKeyboardButton('Ya', 'ya_confirm'), InlineKeyboardButton('Tidak', 'ttp')]
        ])
        await anu.reply('apakah kamu akan mengirimkan pesan broadcast ?', True, reply_markup=markup)

async def broadcast_ya(client: Client, query: CallbackQuery):
    msg = query.message
    db = Database(msg.from_user.id)
    if not msg.reply_to_message:
        await query.answer('Pesan tidak ditemukan', True)
        await query.message.delete()
        return
    message = msg.reply_to_message
    user_ids = db.get_pelanggan().id_pelanggan

    berhasil = 0
    dihapus = 0
    blokir = 0
    gagal = 0
    await msg.edit('<code>Broadcast sedang berlangsung, tunggu sebentar</code>', reply_markup = None)
    for user_id in user_ids:
        try:
            await message.copy(user_id)
            berhasil += 1
        except FloodWait as e:
            await asyncio.sleep(e.x)
            await message.copy(user_id)
            berhasil += 1
        except UserIsBlocked:
            blokir += 1
        except PeerIdInvalid:
            gagal += 1
        except InputUserDeactivated:
            dihapus += 1
            await db.hapus_pelanggan(user_id)
    text = f"""<b>Broadcast selesai</b>
    
Jumlah pengguna: {len(user_ids)}
Berhasil terkirim: {str(berhasil)}
Pengguna diblokir: {str(blokir)}
Akun yang dihapus: {str(dihapus)} (<i>Telah dihapus dari database</i>)
Gagal terkirim: {str(gagal)}"""

    await msg.reply(text)
    await msg.delete()
    await message.delete()

async def close_cbb(client: Client, query: CallbackQuery):
    try:
        await query.message.reply_to_message.delete()
    except:
        pass
    try:
        await query.message.delete()
    except:
        pass

async def menfess_handler(client: Client, msg: Message):  
    user_db = Database(msg.from_user.id)
    helper = Helper(client, msg)
    user = db.get_data_pelanggan()  
        anu = await user_db.copy()
        markup = InlineKeyboardMarkup([
            [InlineKeyboardButton('Ya', 'kirim'), InlineKeyboardButton('Tidak', 'ttp')]
        ])
        await anu.reply('apakah kamu yakin akan mengirimkan pesan ini?', True, reply_markup=markup)

