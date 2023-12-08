import config
import asyncio
from PIL import Image, ImageFont, ImageDraw
from io import BytesIO 

from pyrogram import Client, types, enums
from plugins import Helper, Database
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

async def start_handler(client: Client, msg: types.Message):
    helper = Helper(client, msg)
    first = msg.from_user.first_name
    last = msg.from_user.last_name
    fullname = f'{first} {last}' if last else first
    username = (
        f'@{msg.from_user.username}'
        if msg.from_user.username
        else '@vxnjul'
    )
    mention = msg.from_user.mention
    buttons = [
        [           
            InlineKeyboardButton(
                "ʜᴇʟᴘ", callback_data="nsj"
            ),
            InlineKeyboardButton(
                "ʀᴜʟᴇs", url="https://t.me/jawafes/9"
            ),
        ],
    ]
    await msg.reply_text(
        text=config.start_msg.format(
            id=msg.from_user.id,
            mention=mention,
            username=username,
            first_name=await helper.escapeHTML(first),
            last_name=await helper.escapeHTML(last),
            fullname=await helper.escapeHTML(fullname),
        ),
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(buttons),
        quote=True
    )

async def status_handler(client: Client, msg: types.Message):
    helper = Helper(client, msg)
    db = Database(msg.from_user.id).get_data_pelanggan()
    keyboard = [
        [InlineKeyboardButton("HELP", callback_data="nsj")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    pesan = '<b>❏ User Info:</b>\n'
    pesan += f'├<b>Nama :</b> {db.mention}\n'
    pesan += f'├<b>User ID :</b> <code>{db.id}</code>\n'
    pesan += f'└<b>Status :</b> {db.status}\n\n'
    pesan += '<b>❏ User Stats:</b>\n'
    pesan += f'├<b>Saldo :</b> {helper.formatrupiah(db.coin)} Coin\n'
    pesan += f'├<b>Menfess Harian :</b> {db.menfess}/{config.batas_kirim}\n'
    pesan += f'├<b>Semua Menfess :</b> {db.all_menfess}\n'
    pesan += f'└<b>Bergabung :</b> {db.sign_up}\n\n'
    pesan += '<b>❏Topup coin:</b> @topupcoinbot'
    await msg.reply(pesan, True, reply_markup=reply_markup, enums.ParseMode.HTML,)

async def statistik_handler(client: Helper, id_bot: int):
    db = Database(client.user_id)
    bot = db.get_data_bot(id_bot)
    pesan = "<b>📊 STATISTIK BOT\n\n"
    pesan += f"▪️Pelanggan: {db.get_pelanggan().total_pelanggan}\n"
    pesan += f"▪️Admin: {len(bot.admin)}\n"
    pesan += f"▪️Talent: {len(bot.talent)}\n"
    pesan += f"▪️Daddy sugar: {len(bot.daddy_sugar)}\n"
    pesan += f"▪️Moans girl: {len(bot.moansgirl)}\n"
    pesan += f"▪️Moans boy: {len(bot.moansboy)}\n"
    pesan += f"▪️Girlfriend rent: {len(bot.gfrent)}\n"
    pesan += f"▪️Boyfriend rent: {len(bot.bfrent)}\n"
    pesan += f"▪️Banned: {len(bot.ban)}\n\n"
    pesan += f"🔰Status bot: {'AKTIF' if bot.bot_status else 'TIDAK AKTIF'}</b>"
    await client.message.reply_text(pesan, True, enums.ParseMode.HTML)

async def list_admin_handler(helper: Helper, id_bot: int):
    db = Database(helper.user_id).get_data_bot(id_bot)
    pesan = "<b>Owner bot</b>\n"
    pesan += "• ID: " + str(config.id_admin) + " | <a href='tg://user?id=" + str(config.id_admin) + "'>Owner bot</a>\n\n"
    if len(db.admin) > 0:
        pesan += "<b>Daftar Admin bot</b>\n"
        ind = 1
        for i in db.admin:
            pesan += "• ID: " + str(i) + " | <a href='tg://user?id=" + str(i) + "'>Admin " + str(ind) + "</a>\n"
            ind += 1
    await helper.message.reply_text(pesan, True, enums.ParseMode.HTML)

async def list_ban_handler(helper: Helper, id_bot: int):
    db = Database(helper.user_id).get_data_bot(id_bot)
    if len(db.ban) == 0:
        return await helper.message.reply_text('<i>Tidak ada user dibanned saat ini</i>', True, enums.ParseMode.HTML)
    else:
        pesan = "<b>Daftar banned</b>\n"
        ind = 1
        for i in db.ban:
            pesan += "• ID: " + str(i) + " | <a href='tg://openmessage?user_id=" + str(i) + "'>( " + str(ind) + " )</a>\n"
            ind += 1
    await helper.message.reply_text(pesan, True, enums.ParseMode.HTML)

async def gagal_kirim_handler(client: Client, msg: types.Message):
    helper = Helper(client, msg)
    first = msg.from_user.first_name
    last = msg.from_user.last_name
    fullname = f'{first} {last}' if last else first
    username = (
        f'@{msg.from_user.username}'
        if msg.from_user.username
        else '@vxnjul'
    )
    mention = msg.from_user.mention
    buttons = [
        [
            InlineKeyboardButton(
                "ʜᴇʟᴘ", callback_data="nsj"
            ),
            InlineKeyboardButton(
                "ʀᴜʟᴇs", url="https://t.me/jawafes/9"
            ),
    ],
[
            InlineKeyboardButton(
                "ᴛᴏᴘ ᴜᴘ ᴄᴏɪɴ💰", url="https://t.me/topupcoinbot?start=start"
            ),
        ],
    ]
    await msg.reply_text(
        text=config.gagalkirim_msg.format(
            id=msg.from_user.id,
            mention=mention,
            username=username,
            first_name=await helper.escapeHTML(first),
            last_name=await helper.escapeHTML(last),
            fullname=await helper.escapeHTML(fullname),
        ),
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(buttons),
        quote=True
    )

async def cb_help(client, callback_query):
    user_id = callback_query.from_user.id
    buttons = [
        [
            InlineKeyboardButton(
                "ᴛᴜᴛᴜᴘ", callback_data="ttp"
            ),
        ],
    ]
    await callback_query.edit_message_text(
        f"""
<b>Silahkan kirim pesan anda menggunakan hashtag dibawah ini:</b>

• <code>#mba</code> [ untuk identitas perempuan]
• <code>#mas</code> [ untuk identitas laki-laki ]

<b>Contoh pesan:</b> <code>#mas gabut banget gasi? callan yuk </code>
""",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(buttons),
    )


async def cb_close(client, callback_query):
    await callback_query.message.delete()

async def help_handler(client, msg):
    db = Database(msg.from_user.id)
    member = db.get_data_pelanggan()

    pesan = "Supported commands\n" + '/status — melihat status\n'    
    pesan += '/tf_coin — transfer coin\n'

    # Tambahkan InlineKeyboardButton "JASA" di sini
    keyboard = [
        [InlineKeyboardButton("HELP", callback_data="nsj")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    if member.status == 'admin':
        pesan += '\nHanya Admin\n'
        pesan += '/tf_coin — transfer coin\n'
        pesan += '/settings — melihat settingan bot\n'
        pesan += '/list_admin — melihat list admin\n'
        pesan += '/list_ban — melihat list banned\n\n'
        pesan += 'Perintah banned\n'
        pesan += '/ban — ban user\n'
        pesan += '/unban — unban user\n'
    elif member.status == 'owner':
        pesan += '\n=====OWNER COMMAND=====\n'
        pesan += '/tf_coin — transfer coin\n'
        pesan += '/settings — melihat settingan bot\n'
        pesan += '/list_admin — melihat list admin\n'
        pesan += '/list_ban — melihat list banned\n'
        pesan += '/stats — melihat statistik bot\n'
        pesan += '/bot — setbot (on|off)\n'
        
        pesan += '\n=====BROADCAST OWNER=====\n'
        pesan += '/broadcast — mengirim pesan broadcast kesemua user\n'
        pesan += '/admin — menambahkan admin baru\n'
        pesan += '/unadmin — menghapus admin\n'
        pesan += '/list_ban — melihat list banned\n'
        pesan += '\n=====BANNED COMMAND=====\n'
        pesan += '/ban — ban user\n'
        pesan += '/unban — unban user\n'

    await msg.reply_text(pesan, True, reply_markup=reply_markup)

async def reply_with_image_text(client: Client, msg: types.Message, text: str, image_path: str):
    helper = Helper(client, msg)
    first = msg.from_user.first_name
    last = msg.from_user.last_name
    fullname = f'{first} {last}' if last else first
    username = (
        f'@{msg.from_user.username}'
        if msg.from_user.username
        else '@OwnNeko'
    )
    mention = msg.from_user.mention
    with Image.open(image_path) as image:
        await msg.reply_photo(
            photo=image,
            caption=config.start_msg.format(
                id=msg.from_user.id,
                mention=mention,
                username=username,
                first_name=await helper.escapeHTML(first),
                last_name=await helper.escapeHTML(last),
                fullname=await helper.escapeHTML(fullname),
            ),
            disable_web_page_preview=True,
            quote=True
        )
