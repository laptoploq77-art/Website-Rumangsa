import os

from flask import Flask, render_template

app = Flask(__name__)

# ---------------------------------------------------------------------------
# DATA MENU — ditranskrip dari menu board Rumangsa Kopi
# ---------------------------------------------------------------------------
MENU = {
    "Coffee": {
        "note": "Diseduh dari biji pilihan, untuk yang butuh kekuatan klasik.",
        "items": [
            {"name": "Espresso (Single/Double)", "price": 15, "photo": "espresso", "desc": "Shot kopi murni dan pekat, favorit yang butuh dorongan cepat."},
            {"name": "Americano", "price": 15, "photo": "americano", "desc": "Espresso dengan tambahan air panas, ringan namun tetap tegas rasanya."},
            {"name": "Long Black", "price": 15, "photo": "long-black", "desc": "Espresso dituang di atas air, crema lebih terjaga dibanding Americano."},
            {"name": "Café Latte", "price": 18, "photo": "caffe-latte", "desc": "Espresso berpadu susu steamed lembut, creamy dan mudah disukai."},
            {"name": "Cappuccino", "price": 18, "photo": "cappuccino", "desc": "Perpaduan seimbang espresso, susu, dan foam tebal di atasnya."},
            {"name": "Con Hielo", "price": 20, "photo": "con-hielo", "desc": "Espresso manis disiram es, gaya Spanyol yang segar dan simpel."},
            {"name": "Mockresso", "price": 21, "photo": "mockresso", "desc": "Racikan mocha dan espresso, manis cokelat bertemu pahit kopi."},
            {"name": "Affogato", "price": 21, "photo": "affogato", "desc": "Es krim vanilla disiram shot espresso panas, manis dan dingin sekaligus."},
            {"name": "Latte (Vanilla/Hazelnut/Caramel)", "price": 23, "photo": "latte", "desc": "Café latte dengan pilihan sirup vanilla, hazelnut, atau caramel."},
            {"name": "Macchiato", "price": 23, "photo": "macchiato", "desc": "Espresso 'dinodai' sedikit foam susu, kuat namun ada sentuhan lembut."},
        ],
    },
    "Drip Methods": {
        "note": "Untuk pencinta kopi manual brew yang sabar menunggu.",
        "items": [
            {"name": "V60", "price": 27, "photo": "v60", "desc": "Manual brew dengan pour over, menonjolkan karakter asli biji kopi."},
            {"name": "Japanese Ice Drip", "price": 27, "photo": "japanese-ice-drip", "desc": "Diseduh perlahan tetes demi tetes di atas es, hasil lebih halus dan aromatik."},
        ],
    },
    "Rumangsa Signature": {
        "note": "Racikan rumahan, hanya ada di Rumangsa.",
        "items": [
            {"name": "Rumansa", "price": 18, "photo": "rumansa", "desc": "Signature andalan Rumangsa, racikan kopi susu ciri khas kedai."},
            {"name": "Secret Mango", "price": 22, "photo": "secret-mango", "desc": "Kopi berpadu mangga segar, manis asam yang bikin penasaran."},
            {"name": "Tuku Taka", "price": 22, "photo": "tuku-taka", "desc": "Kreasi rumahan dengan rasa unik, wajib dicoba saat pertama kali datang."},
            {"name": "Harmoni", "price": 23, "new": True, "photo": "harmoni", "desc": "Menu baru dengan racikan seimbang, perpaduan rasa yang harmonis."},
            {"name": "Rumara", "price": 23, "new": True, "photo": "humara", "desc": "Menu baru signature Rumangsa dengan cita rasa creamy yang khas."},
            {"name": "Unicorn Milk", "price": 25, "photo": "unicorn-milk", "desc": "Susu warna-warni dengan rasa manis playful, favorit untuk difoto."},
            {"name": "Black Oreo Berry", "price": 25, "photo": "black-oreo-berry", "desc": "Perpaduan cokelat Oreo dan berry, manis legit dengan sedikit asam segar."},
        ],
    },
    "Non Coffee": {
        "note": "Untuk yang ingin ngopi tanpa kafein berlebih.",
        "items": [
            {"name": "Strawberry Latte", "price": 18, "photo": "strawberry-latte", "desc": "Susu latte dengan sirup stroberi manis segar, tanpa kopi."},
            {"name": "Taro Latte", "price": 21, "photo": "taro-latte", "desc": "Susu creamy rasa taro yang lembut dan sedikit gurih."},
            {"name": "Choco Latte", "price": 23, "photo": "choco-latte", "desc": "Cokelat susu kental dan creamy, manis yang menenangkan."},
            {"name": "Greentea Latte", "price": 23, "photo": "greentea-latte", "desc": "Matcha lembut berpadu susu, pahit khas teh hijau yang seimbang."},
            {"name": "Red Velvet Latte", "price": 23, "photo": "red-velvet-latte", "desc": "Susu dengan rasa red velvet yang manis dan creamy."},
            {"name": "Buttertones", "price": 25, "desc": "Racikan susu creamy dengan sentuhan rasa butter yang khas."},
        ],
    },
    "Tea Flavor": {
        "note": "Segar, ringan, cocok untuk siang hari Pontianak.",
        "items": [
            {"name": "Lychee", "price": 15, "photo": "lychee", "desc": "Teh segar dengan rasa leci manis yang ringan."},
            {"name": "Peach", "price": 15, "photo": "peach", "desc": "Teh dengan aroma dan rasa peach yang menyegarkan."},
            {"name": "Lemon", "price": 15, "photo": "lemon", "desc": "Teh dengan perasan lemon asam segar, pelepas dahaga di siang hari."},
        ],
    },
    "Summerel": {
        "note": "Squash segar untuk mengusir gerah.",
        "items": [
            {"name": "Lime Squash", "price": 18, "photo": "lime-squash", "desc": "Minuman soda segar dengan perasan jeruk nipis asam manis."},
            {"name": "Orange Squash", "price": 18, "photo": "orange-squash", "desc": "Soda segar rasa jeruk yang manis dan menyegarkan."},
            {"name": "Laquisha", "price": 20, "new": True, "desc": "Menu baru minuman segar dengan racikan rasa buah campuran."},
        ],
    },
    "Additional": {
        "note": "",
        "items": [
            {"name": "Air Mineral", "price": 10, "photo": "air-mineral", "desc": "Air mineral dalam kemasan botol untuk menemani menu lainnya."},
        ],
    },
    "Finger Food": {
        "note": "Teman ngobrol santai sore-malam.",
        "items": [
            {"name": "Kroket Goreng", "price": 15, "photo": "kroket-goreng", "desc": "Kroket renyah di luar, lembut berisi di dalam."},
            {"name": "Pisang Goreng (Srikaya/Keju/Coklat)", "price": 15, "photo": "pisang-goreng", "desc": "Pisang goreng crispy dengan topping srikaya, keju, atau cokelat."},
            {"name": "Sosis Goreng", "price": 15, "photo": "sosis-goreng", "desc": "Sosis goreng gurih, camilan simpel teman ngopi."},
            {"name": "Tela-Tela (Asin/Manis)", "price": 15, "photo": "tela-tela", "desc": "Singkong goreng renyah dengan pilihan rasa asin atau manis."},
            {"name": "Toast with Vanilla Ice Cream", "price": 15, "photo": "toast-with-vanilla-ice-cream", "desc": "Roti panggang hangat disandingkan es krim vanilla dingin."},
            {"name": "French Fries", "price": 18, "photo": "french-fries", "desc": "Kentang goreng renyah, camilan klasik yang selalu pas."},
            {"name": "Risoles", "price": 20, "photo": "risoles", "desc": "Risoles gurih dengan isian lembut di dalam kulit yang renyah."},
            {"name": "Chicken Shilin", "price": 20, "photo": "chiken-shilin", "desc": "Ayam crispy gaya Shilin dengan bumbu gurih pedas."},
            {"name": "Mix Platter", "price": 25, "photo": "mix-platter", "desc": "Kombinasi beberapa finger food dalam satu porsi, pas untuk berbagi."},
        ],
    },
    "Rice Bowl": {
        "note": "Buat yang datang sambil lapar serius.",
        "items": [
            {"name": "Crispy Chicken Mayo", "price": 25, "photo": "crispy-chicken-mayo", "desc": "Nasi dengan ayam crispy disiram saus mayo yang gurih creamy."},
            {"name": "Grilled Chicken", "price": 26, "photo": "grilled-chicken", "desc": "Nasi dengan ayam panggang berbumbu, gurih dan smoky."},
            {"name": "Sweet Chicken", "price": 26, "photo": "sweet-chicken", "desc": "Nasi dengan ayam berbalut saus manis gurih."},
            {"name": "Rendang", "price": 30, "photo": "rendang", "desc": "Nasi dengan rendang empuk berbumbu rempah kaya rasa."},
            {"name": "Sweet Beef Belly", "price": 30, "photo": "sweet-beef-belly", "desc": "Nasi dengan sandung lamur sapi bersaus manis yang lumer."},
        ],
    },
    "Berkuah": {
        "note": "Hangat, pas buat malam hujan.",
        "items": [
            {"name": "Indomie Lemak", "price": 15, "photo": "indomie-lemak", "desc": "Indomie kuah dengan tambahan susu/santan, gurih dan hangat."},
            {"name": "Sop Kroket Kikil", "price": 18, "photo": "sop-kroket-kikil", "desc": "Sop hangat berisi kroket dan kikil empuk."},
            {"name": "Chicken Ramen", "price": 22, "photo": "chicken-ramen", "desc": "Ramen kuah gurih dengan topping ayam."},
            {"name": "Beef Ramen", "price": 25, "photo": "beef-ramen", "desc": "Ramen kuah gurih dengan topping daging sapi."},
        ],
    },
    "Dimsum": {
        "note": "",
        "items": [
            {"name": "Lumpia Kukus", "price": 15, "photo": "lumpia-kukus", "desc": "Lumpia kukus lembut dengan isian gurih."},
            {"name": "Pao Pandan", "price": 15, "photo": "pao-pandan", "desc": "Bakpao lembut aroma pandan dengan isian manis."},
            {"name": "Pao Telur Asin", "price": 15, "photo": "pao-telur-asin", "desc": "Bakpao dengan isian telur asin yang gurih lumer."},
            {"name": "Siomay", "price": 15, "photo": "siomay", "desc": "Siomay kukus lembut, disajikan dengan saus pelengkap."},
        ],
    },
    "Other Choice": {
        "note": "",
        "items": [
            {"name": "Bound Salad", "price": 23, "photo": "bound-salad", "desc": "Salad segar dengan campuran sayur dan dressing pilihan."},
            {"name": "Crispy Chicken Burger", "price": 23, "photo": "crispy-chicken-burger", "desc": "Burger dengan ayam crispy renyah dan saus spesial."},
            {"name": "Crispy Chicken Steak", "price": 26, "photo": "crispy-chicken-steak", "desc": "Steak ayam crispy disiram saus lada hitam atau jamur."},
            {"name": "Spaghetti Carbonara", "price": 30, "photo": "spaghetti-carbonara", "desc": "Spaghetti dengan saus creamy carbonara yang gurih."},
        ],
    },
    "Dessert": {
        "note": "Penutup manis sebelum pulang.",
        "items": [
            {"name": "Puding Wennie Wence (S)", "price": 6, "photo": "puding-wennie-wence-small", "desc": "Puding lembut ukuran kecil, manis pas untuk penutup."},
            {"name": "Puding Wennie Wence (L)", "price": 35, "photo": "puding-wennie-wence-large", "desc": "Puding lembut ukuran besar, cocok untuk dinikmati bersama."},
            {"name": "Rumangsa Dessert", "price": 25, "photo": "rumangsa-dessert", "desc": "Dessert signature Rumangsa, manis dengan sentuhan khas kedai."},
        ],
    },
}

# ---------------------------------------------------------------------------
# FOTO MENU — dibaca OTOMATIS dari folder static/img/menu-photos
# Ditampilkan apa adanya di halaman "Foto Menu", tidak disandingkan dengan
# data MENU di atas.
#
# Dulu daftar ini di-hardcode manual (hanya 20 foto), jadi setiap kali ada
# foto baru diupload ke folder, foto itu tidak muncul di website sampai
# kode ini diubah manual. Sekarang folder di-scan otomatis setiap halaman
# dibuka, jadi cukup upload file ke static/img/menu-photos/ dan foto akan
# langsung tampil tanpa perlu edit app.py sama sekali.
# ---------------------------------------------------------------------------
MENU_PHOTOS_DIR = os.path.join(app.root_path, "static", "img", "menu-photos")
ALLOWED_PHOTO_EXTENSIONS = (".jpg", ".jpeg", ".png", ".webp", ".gif", ".jfif")


def load_menu_photos():
    """Pindai folder static/img/menu-photos dan susun daftar foto menu.

    Nama tampilan (caption) dibuat otomatis dari nama file, misalnya
    'crispy-chicken-mayo.jpg' -> 'Crispy Chicken Mayo'.
    """
    photos = []
    if os.path.isdir(MENU_PHOTOS_DIR):
        for filename in sorted(os.listdir(MENU_PHOTOS_DIR), key=str.lower):
            if filename.lower().endswith(ALLOWED_PHOTO_EXTENSIONS):
                display_name = os.path.splitext(filename)[0]
                display_name = display_name.replace("_", " ").replace("-", " ").strip()
                display_name = " ".join(display_name.split())
                display_name = display_name.title()
                photos.append({
                    "src": f"img/menu-photos/{filename}",
                    "name": display_name or filename,
                    "slug": os.path.splitext(filename)[0].lower(),
                })
    return photos

# Kategori dikelompokkan untuk filter cepat di halaman menu
CATEGORY_GROUPS = {
    "Semua": list(MENU.keys()),
    "Minuman": ["Coffee", "Drip Methods", "Rumangsa Signature", "Non Coffee", "Tea Flavor", "Summerel", "Additional"],
    "Makanan": ["Finger Food", "Rice Bowl", "Berkuah", "Dimsum", "Other Choice", "Dessert"],
}

# Galeri — foto asli outlet (taruh file di static/img/gallery/1.jpg ... 10.jpg)
GALLERY = [
    {"src": "img/gallery/1.jpg"},
    {"src": "img/gallery/2.jpg"},
    {"src": "img/gallery/3.jpg"},
    {"src": "img/gallery/4.jpg"},
    {"src": "img/gallery/5.jpg"},
    {"src": "img/gallery/6.jpg"},
    {"src": "img/gallery/7.jpg"},
    {"src": "img/gallery/8.jpg"},
    {"src": "img/gallery/9.jpg"},
    {"src": "img/gallery/10.jpg"},
]

INFO = {
    "name": "Rumangsa Kopi",
    "address": "Komplek UNTAN, Jl. Karangan No.1, Bansir Laut, Kec. Pontianak Tenggara, Kota Pontianak, Kalimantan Barat 78124",
    "phone": "+62 819-2020-121",
    "hours_ptk": "08.00 – 24.00 WIB",
    "hours_skw": "24 Jam (Cabang Singkawang)",
    "instagram": "@rumangsa.kopi",
}


@app.route("/")
def home():
    return render_template("index.html", info=INFO, gallery=GALLERY[:4])


@app.route("/menu")
def menu():
    return render_template("menu.html", menu=MENU, groups=CATEGORY_GROUPS, info=INFO)


@app.route("/foto-menu")
def foto_menu():
    return render_template("foto-menu.html", photos=load_menu_photos(), info=INFO)


@app.route("/deskripsi-menu")
def deskripsi_menu():
    return render_template("deskripsi-menu.html", menu=MENU, groups=CATEGORY_GROUPS, info=INFO)


@app.route("/galeri")
def gallery():
    return render_template("gallery.html", gallery=GALLERY, info=INFO)


@app.route("/tentang")
def about():
    return render_template("about.html", info=INFO)


if __name__ == "__main__":
    app.run(debug=True)
