import os

api_id = int(os.environ.get("API_ID", "21484185"))
api_hash = os.environ.get("API_HASH", "42589444b3ee86b1286f01d966989214")
bot_token = os.environ.get("BOT_TOKEN", "6872017467:AAFx_RzH9bGA13iolTAYJNJlDWUfLjQ_C14")
# =========================================================== #

db_url = os.environ.get("DB_URL", "mongodb+srv://neko:<password>@nekomenfess.ss5r7je.mongodb.net/?retryWrites=true&w=majority")
db_name = os.environ.get("DB_NAME", "menfess")
# =========================================================== #

channel_1 = int(os.environ.get("CHANNEL_1", "-1002089195394"))
channel_2 = int(os.environ.get("CHANNEL_2", "-1002098707945"))
channel_log = int(os.environ.get("CHANNEL_LOG", "-1002088952110"))
# =========================================================== #

id_admin = int(os.environ.get("ID_ADMIN", "6725628980"))
# =========================================================== #

batas_kirim = int(os.environ.get("BATAS_KIRIM", "3"))
biaya_kirim = int(os.environ.get("BIAYA_KIRIM", "10"))
 =========================================================== #

hastag = os.environ.get("HASTAG", "#pft #pftt #mas #mba #story #spill #story").replace(" ", "|").lower()
# =========================================================== #

pesan_join = os.environ.get("PESAN_JOIN", "Tidak dapat diakses harap join terlebih dahulu")
start_msg = os.environ.get("START_MSG", """"
{mention},Silahkan gunakan hastag:

#NekoBoy / #NekoGirl untuk Mencari Pasangan,Teman , Partner dll
#NekoAsk untuk Bertanya
#NekoStory untuk Berbagi Cerita
#NekoSpill untuk Spill Masalah
#NekoFind untuk Mencari Pasangan, Teman, Partner dll

{fullname} 🌱\n\nIni adalah bot menfess, semua pesan yang kamu kirim akan masuk ke channel secara anonymous. ketik /help""")

gagalkirim_msg = os.environ.get("GAGAL_KIRIM", """
{mention}, pesan mu gagal terkirim silahkan gunakan hastag:

#NekoBoy / #NekoGirl untuk Mencari Pasangan, Teman , Partner dll
#NekoAsk untuk Bertanya
#NekoStory untuk Berbagi Cerita
#NekoSpill untuk Spill Masalah
#NekoFind untuk Mencari Pasangan, Teman, Partner dll
""")
