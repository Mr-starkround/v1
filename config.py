import os

api_id = int(os.environ.get("API_ID", "22132140"))
api_hash = os.environ.get("API_HASH", "326ba61167a7513e85c9d8699b345b75")
bot_token = os.environ.get("BOT_TOKEN", "6985345708:AAHrA6zEOYuSwyc4fZ5nVHufa93Cioh_cwY")
# =========================================================== #

db_url = os.environ.get("DB_URL", "mongodb+srv://agatha:agatha@cluster0.ebztq9n.mongodb.net/True?retryWrites=true&w=majority")
db_name = os.environ.get("DB_NAME", "menfess")
# =========================================================== #

channel_1 = int(os.environ.get("CHANNEL_1", "-1001935857563"))
channel_2 = int(os.environ.get("CHANNEL_2", "-1001869711042"))
channel_log = int(os.environ.get("CHANNEL_LOG", "-1002015387015"))
# =========================================================== #

id_admin = int(os.environ.get("ID_ADMIN", "1020381855"))
# =========================================================== #

batas_kirim = int(os.environ.get("BATAS_KIRIM", "5"))
biaya_kirim = int(os.environ.get("BIAYA_KIRIM", "25"))
# =========================================================== #

hastag = os.environ.get("HASTAG", "#pft #pftt #mas #mba #story #spill #story #pap").replace(" ", "|").lower()
# =========================================================== #

pesan_join = os.environ.get("PESAN_JOIN", "<b>Hallo</b>\n\n<b>Anda harus bergabung di Channel & Group terlebih dahulu untuk mengirim pesan ke channel</b> @JAWAFES. \n\n<b>Silakan Join Channel dan Group dulu ⤵️</b>")
start_msg = os.environ.get("START_MSG", """
<b>❏ Hallo</b> {mention}

<b>𝗝𝗮𝘄𝗮𝗳𝗲𝘀𝘀 𝗔𝘂𝘁𝗼 𝗽𝗼𝘀𝘁 akan membantumu mengirimkan pesan secara anonim ke channel</b> @JAWAFES.

<b>silahkan baca rules dan help terlebih dahulu</b>""")
# =========================================================== #

gagalkirim_msg = os.environ.get("GAGAL_KIRIM", """
<b>Maaf</b> {mention},\n\n<b>Pesan anda gagal terkirim.\nsilahkan klik button help jika anda butuh bantuan</b>
""")
# =========================================================== #

topup_msg = os.environ.get("PESAN_TOPUP", """
❏ Haii {mention} \n\nJawafess coin di gunakan untuk biaya mengirim menfess/promote ke @JAWAFES jika batas kirim harian sudah habis. biaya untuk sekali mengirim adalah 25 coin. \ncoin akan berkurang secara otomatis jika batas harian sudah habis. <b>harga 100 coin = 1000 rupiah</b> \n\napabila batas kirim harian belum habis. coin tidak akan berkurang \n\n<b>❏ Cara Membeli Coin Jawafess:</b> \n├ 1. Salin format top up dibawah👇🏻👇🏻 \n├ 2. Klik /belicoin \n├ 3. save qris dan lakukan pembayaran. \n├ 4. kirimkan bukti pembayaran beserta format topup \n└ <b>BENEFIT TOPUP COIN JAWAFESS:</b> bisa kirim menfess sebanyak-banyaknya diluar batasan harian
""")