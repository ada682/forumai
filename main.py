from forumaisdk.ModelMarket import Mixtral8x7BModelMarketTestnet
import time

# Masukkan kunci privat dan kunci publik Anda di sini
PRIVATE_KEY = 'masukan_priv_key'
PUBLIC_KEY = 'masukan_publickeymu/addresmu'

model_market = Mixtral8x7BModelMarketTestnet(PRIVATE_KEY, PUBLIC_KEY)

# Fungsi untuk mengirim permintaan dan mendapatkan respons
def get_response():
    chat = [{"role": "system", "content": "You are a helpful assistant!"}, {"role":"user", "content": "What is 2+2?"}]

    # Mengirim permintaan dan mendapatkan URL node serta kode hasil
    node_url, result_code = model_market.generate_self_requesting(3000, chat)

    full_resp = ""
    done = False
    while not done:
        # Mendapatkan output berikutnya
        resp, done = model_market.get_next_output(node_url, result_code, full_resp)
        full_resp += resp
        print(resp, end="")
        time.sleep(0.1)
    print("\n")  # Tambahkan baris baru setelah setiap respons

# Mengulang proses sebanyak 20 kali
for i in range(20):
    print(f"Iteration {i + 1}:")
    get_response()
