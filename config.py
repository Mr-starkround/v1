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

hastag = os.environ.get("HASTAG", "#pfrtddtzt #pfttzz #mas #mba #story #spill #tanya #pap").replace(" ", "|").lower()
# =========================================================== #
start_msg = os.environ.get("START_MSG", """
❏ Hallo {mention}

𝗝𝗮𝘄𝗮𝗳𝗲𝘀𝘀 𝗔𝘂𝘁𝗼 𝗽𝗼𝘀𝘁 akan membantumu mengirimkan pesan secara anonim ke channel @JAWAFES.

silahkan baca help dan rules terlebih dahulu.""")
# =========================================================== #

gagalkirim_msg = os.environ.get("GAGAL_KIRIM", """
pesan anda gagal terkirim. silahkan klik button help jika anda butuh bantuan.
""")
# =========================================================== #

topup_msg = os.environ.get("PESAN_TOPUP", """
Jawafess coin di gunakan untuk biaya mengirim menfess/promote ke @JAWAFES jika 5x batas kirim harian sudah habis. biaya untuk sekali mengirim adalah 25 coin.

❏ Cara Membeli Coin Jawafess
├1. klik button top up dibawah ini
├2. kirim bukti pembayaran anda <a href='https://t.me/GJNadminbot?start=start'>disini</a>
├3. nama [ nama telegram anda ]
└4. code topup anda » <code>fess {id} </code>

coin akan berkurang secara otomatis jika batas harian sudah habis. <b>harga 100 coin = 1000 rupiah</b>
""")