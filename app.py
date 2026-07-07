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
            {"name": "Espresso (Single/Double)", "price": 15, "photo": "espresso", "slug": "espresso", "desc": "Shot kopi murni yang diekstrak singkat dari mesin espresso, menghasilkan rasa pekat dan aroma kuat khas biji pilihan Rumangsa. Cocok untuk yang ingin merasakan karakter kopi tanpa campuran apa pun, tersedia dalam pilihan single atau double shot sesuai selera."},
            {"name": "Americano", "price": 15, "photo": "americano", "slug": "americano", "desc": "Espresso yang diencerkan dengan air panas sehingga rasanya lebih ringan namun tetap mempertahankan ketegasan dan aroma khas kopi. Pilihan pas untuk yang suka kopi hitam tapi tidak terlalu pekat seperti espresso murni."},
            {"name": "Long Black", "price": 15, "photo": "long-black", "slug": "long-black", "desc": "Espresso dituangkan di atas air panas (bukan sebaliknya), sehingga lapisan crema tetap terjaga dan lebih kaya dibanding Americano. Rasanya tetap tegas namun dengan tekstur yang lebih halus di setiap tegukan."},
            {"name": "Café Latte", "price": 18, "photo": "caffe-latte", "slug": "caffe-latte", "desc": "Perpaduan satu atau dua shot espresso dengan susu steamed yang lembut serta sedikit foam tipis di atasnya. Rasa kopi tetap terasa namun creamy dan mudah diterima, cocok untuk yang baru mulai menikmati kopi susu."},
            {"name": "Cappuccino", "price": 18, "photo": "cappuccino", "slug": "cappuccino", "desc": "Kombinasi seimbang antara espresso, susu steamed, dan foam susu tebal yang menciptakan tekstur creamy nan ringan. Rasio susu dan foam yang lebih banyak membuat cappuccino terasa lebih ringan dibanding latte."},
            {"name": "Con Hielo", "price": 20, "photo": "con-hielo", "slug": "con-hielo", "desc": "Espresso manis yang disiram langsung ke atas es batu ala gaya Spanyol, menghasilkan sensasi dingin dan segar dengan rasa kopi yang tetap intens. Pilihan tepat untuk cuaca panas Pontianak."},
            {"name": "Mockresso", "price": 21, "photo": "mockresso", "slug": "mockresso", "desc": "Racikan yang memadukan mocha manis dengan espresso pekat, menghadirkan perpaduan rasa cokelat dan pahit kopi dalam satu gelas. Cocok untuk pencinta kopi yang ingin sentuhan manis tanpa kehilangan karakter kopinya."},
            {"name": "Affogato", "price": 21, "photo": "affogato", "slug": "affogato", "desc": "Satu scoop es krim vanilla lembut disiram langsung dengan shot espresso panas di atasnya, menciptakan kontras rasa manis dingin dan pahit hangat sekaligus. Disajikan simpel namun selalu jadi favorit sebagai penutup santai."},
            {"name": "Latte (Vanilla/Hazelnut/Caramel)", "price": 23, "photo": "latte", "slug": "latte", "desc": "Café latte klasik yang diberi tambahan sirup pilihan vanilla, hazelnut, atau caramel untuk sentuhan rasa dan aroma yang lebih kaya. Tetap creamy dan lembut, dengan tingkat manis yang bisa disesuaikan sesuai varian sirup yang dipilih."},
            {"name": "Macchiato", "price": 23, "photo": "macchiato", "slug": "macchiato", "desc": "Espresso yang 'dinodai' dengan sedikit foam susu di atasnya, sehingga rasa kopi tetap dominan namun ada sentuhan lembut dari susu. Pilihan pas untuk yang suka espresso namun ingin sedikit kelembutan tambahan."},
        ],
    },
    "Drip Methods": {
        "note": "Untuk pencinta kopi manual brew yang sabar menunggu.",
        "items": [
            {"name": "V60", "price": 27, "photo": "v60", "slug": "v60", "desc": "Metode manual brew pour-over menggunakan alat berbentuk kerucut V60, di mana air panas dituang perlahan dan merata ke atas bubuk kopi. Proses ini menonjolkan karakter asli biji kopi, mulai dari tingkat keasaman hingga aroma khasnya, tanpa campuran susu atau gula."},
            {"name": "Japanese Ice Drip", "price": 27, "photo": "japanese-ice-drip", "slug": "japanese-ice-drip", "desc": "Kopi diseduh perlahan tetes demi tetes langsung di atas es batu selama proses ekstraksi berlangsung, bukan didinginkan setelah diseduh. Hasilnya rasa yang lebih halus, aromatik, dan kompleks dibanding cold brew biasa, cocok dinikmati sambil bersantai."},
        ],
    },
    "Rumangsa Signature": {
        "note": "Racikan rumahan, hanya ada di Rumangsa.",
        "items": [
            {"name": "Rumansa", "price": 18, "photo": "rumansa", "slug": "rumansa", "desc": "Signature andalan Rumangsa berupa racikan kopi susu rumahan dengan resep rahasia kedai, jadi ciri khas yang membedakan dari menu kopi susu pada umumnya. Rasanya creamy dengan sentuhan manis yang pas dan tidak berlebihan."},
            {"name": "Secret Mango", "price": 22, "photo": "secret-mango", "slug": "secret-mango", "desc": "Perpaduan unik antara kopi dan mangga segar yang menciptakan rasa manis-asam yang menyegarkan sekaligus bikin penasaran. Kombinasi buah tropis dengan kopi ini jarang ditemui di kedai lain, jadi wajib dicoba."},
            {"name": "Tuku Taka", "price": 22, "photo": "tuku-taka", "slug": "tuku-taka", "desc": "Kreasi rumahan Rumangsa dengan racikan rasa unik yang sulit dideskripsikan tanpa mencobanya langsung. Menu ini sering direkomendasikan untuk pengunjung yang baru pertama kali datang dan ingin mencicipi sesuatu yang berbeda."},
            {"name": "Harmoni", "price": 23, "new": True, "photo": "harmoni", "slug": "harmoni", "desc": "Menu baru dengan racikan yang seimbang antara rasa manis, creamy, dan sedikit pahit kopi, menciptakan harmoni rasa di setiap tegukan. Cocok untuk yang ingin mencoba variasi baru dari menu signature Rumangsa."},
            {"name": "Rumara", "price": 23, "new": True, "photo": "humara", "slug": "rumara", "desc": "Menu baru signature Rumangsa dengan cita rasa creamy yang khas, dipadukan dengan sentuhan rasa lembut dan menenangkan. Racikan ini dirancang untuk melengkapi deretan menu signature yang sudah ada."},
            {"name": "Unicorn Milk", "price": 25, "photo": "unicorn-milk", "slug": "unicorn-milk", "desc": "Minuman susu warna-warni dengan rasa manis yang playful dan ringan, dirancang khusus untuk yang suka minuman estetik dan instagramable. Favorit untuk difoto sekaligus dinikmati bersama teman."},
            {"name": "Black Oreo Berry", "price": 25, "photo": "black-oreo-berry", "slug": "black-oreo-berry", "desc": "Perpaduan cokelat Oreo yang legit dengan sentuhan berry yang sedikit asam segar, menciptakan keseimbangan rasa manis dan segar dalam satu gelas. Teksturnya creamy dengan remahan Oreo yang menambah sensasi renyah."},
        ],
    },
    "Non Coffee": {
        "note": "Untuk yang ingin ngopi tanpa kafein berlebih.",
        "items": [
            {"name": "Strawberry Latte", "price": 18, "photo": "strawberry-latte", "slug": "strawberry-latte", "desc": "Susu latte lembut dengan sirup stroberi manis dan segar, tanpa campuran kopi sama sekali. Pilihan pas untuk yang ingin ngopi bareng teman tapi tidak mengonsumsi kafein."},
            {"name": "Taro Latte", "price": 21, "photo": "taro-latte", "slug": "taro-latte", "desc": "Susu creamy dengan rasa taro yang lembut dan sedikit gurih khas umbi talas ungu. Teksturnya kental dan menenangkan, cocok dinikmati dingin maupun panas."},
            {"name": "Choco Latte", "price": 23, "photo": "choco-latte", "slug": "choco-latte", "desc": "Cokelat susu kental dan creamy dengan rasa manis yang menenangkan, cocok untuk pencinta cokelat yang ingin minuman non-kopi yang tetap memuaskan. Disajikan dengan tekstur lembut di setiap tegukan."},
            {"name": "Greentea Latte", "price": 23, "photo": "greentea-latte", "slug": "greentea-latte", "desc": "Matcha berkualitas dipadukan dengan susu creamy, menciptakan keseimbangan antara pahit khas teh hijau dan manis lembut dari susu. Aroma matcha yang khas membuat minuman ini terasa menenangkan."},
            {"name": "Red Velvet Latte", "price": 23, "photo": "red-velvet-latte", "slug": "red-velvet-latte", "desc": "Susu dengan rasa red velvet yang manis dan creamy, menghadirkan sensasi seperti menikmati kue red velvet dalam bentuk minuman. Warnanya yang khas juga membuat tampilannya menarik."},
            {"name": "Buttertones", "price": 25, "slug": "buttertones", "desc": "Racikan susu creamy dengan sentuhan rasa butter yang khas, menciptakan rasa gurih-manis yang unik dan jarang ditemukan di menu kedai lain. Teksturnya lembut dengan aroma butter yang terasa sejak tegukan pertama."},
        ],
    },
    "Tea Flavor": {
        "note": "Segar, ringan, cocok untuk siang hari Pontianak.",
        "items": [
            {"name": "Lychee", "price": 15, "photo": "lychee", "slug": "lychee", "desc": "Teh segar dengan rasa leci yang manis dan ringan, cocok dinikmati dingin sebagai pelepas dahaga. Aroma leci yang khas membuat teh ini terasa menyegarkan tanpa rasa manis yang berlebihan."},
            {"name": "Peach", "price": 15, "photo": "peach", "slug": "peach", "desc": "Teh dengan aroma dan rasa peach yang menyegarkan, memberikan sensasi buah yang ringan di setiap tegukan. Pilihan tepat untuk yang ingin minuman manis namun tetap ringan di lidah."},
            {"name": "Lemon", "price": 15, "photo": "lemon", "slug": "lemon", "desc": "Teh dengan perasan lemon asam segar yang efektif melepas dahaga terutama di siang hari yang terik. Rasa asam dari lemon berpadu pas dengan manis teh, menghasilkan minuman yang menyegarkan."},
        ],
    },
    "Summerel": {
        "note": "Squash segar untuk mengusir gerah.",
        "items": [
            {"name": "Lime Squash", "price": 18, "photo": "lime-squash", "slug": "lime-squash", "desc": "Minuman soda segar dengan perasan jeruk nipis asam manis, menghasilkan sensasi berkarbonasi yang menyegarkan. Kombinasi asam dan manis yang seimbang membuatnya pas dinikmati saat cuaca panas."},
            {"name": "Orange Squash", "price": 18, "photo": "orange-squash", "slug": "orange-squash", "desc": "Soda segar dengan rasa jeruk yang manis dan menyegarkan, memberikan sensasi berkarbonasi yang ringan di tenggorokan. Cocok sebagai teman santai sambil menikmati suasana kedai."},
            {"name": "Laquisha", "price": 20, "new": True, "slug": "laquisha", "desc": "Menu baru berupa minuman segar dengan racikan rasa buah campuran yang unik, dirancang untuk melengkapi lini minuman squash Rumangsa. Rasanya manis dan segar, cocok dinikmati kapan saja."},
        ],
    },
    "Additional": {
        "note": "",
        "items": [
            {"name": "Air Mineral", "price": 10, "photo": "air-mineral", "slug": "air-mineral", "desc": "Air mineral dalam kemasan botol untuk menemani menu makanan maupun minuman lainnya. Pilihan simpel bagi yang ingin minuman netral tanpa rasa tambahan."},
        ],
    },
    "Finger Food": {
        "note": "Teman ngobrol santai sore-malam.",
        "items": [
            {"name": "Kroket Goreng", "price": 15, "photo": "kroket-goreng", "slug": "kroket-goreng", "desc": "Kroket dengan lapisan luar yang renyah dan garing, namun lembut serta gurih di bagian dalamnya. Camilan klasik yang pas dinikmati hangat-hangat sebagai teman ngobrol."},
            {"name": "Pisang Goreng (Srikaya/Keju/Coklat)", "price": 15, "photo": "pisang-goreng", "slug": "pisang-goreng", "desc": "Pisang goreng dengan tekstur crispy di luar dan lembut di dalam, disajikan dengan pilihan topping srikaya, keju, atau cokelat sesuai selera. Camilan manis yang cocok dinikmati kapan saja."},
            {"name": "Sosis Goreng", "price": 15, "photo": "sosis-goreng", "slug": "sosis-goreng", "desc": "Sosis goreng dengan rasa gurih yang pas, disajikan sebagai camilan simpel namun selalu menjadi teman ngopi yang cocok. Teksturnya renyah di luar dengan isian sosis yang juicy."},
            {"name": "Tela-Tela (Asin/Manis)", "price": 15, "photo": "tela-tela", "slug": "tela-tela", "desc": "Singkong goreng dengan tekstur renyah, tersedia dalam pilihan rasa asin gurih atau manis sesuai selera. Camilan tradisional yang cocok dinikmati sambil bersantai."},
            {"name": "Toast with Vanilla Ice Cream", "price": 15, "photo": "toast-with-vanilla-ice-cream", "slug": "toast-with-vanilla-ice-cream", "desc": "Roti panggang hangat yang disandingkan dengan satu scoop es krim vanilla dingin, menciptakan kontras rasa dan suhu yang menyenangkan. Cocok sebagai camilan santai maupun penutup ringan."},
            {"name": "French Fries", "price": 18, "photo": "french-fries", "slug": "french-fries", "desc": "Kentang goreng dengan tekstur renyah di luar dan lembut di dalam, camilan klasik yang selalu pas menemani obrolan santai. Disajikan hangat dan gurih."},
            {"name": "Risoles", "price": 20, "photo": "risoles", "slug": "risoles", "desc": "Risoles dengan kulit yang renyah membungkus isian gurih dan lembut di dalamnya. Camilan gorengan yang pas dinikmati selagi hangat bersama teman atau keluarga."},
            {"name": "Chicken Shilin", "price": 20, "photo": "chiken-shilin", "slug": "chicken-shilin", "desc": "Ayam crispy bergaya Taiwan dengan bumbu gurih pedas khas Shilin Night Market, disajikan dalam potongan besar yang renyah di luar dan juicy di dalam. Cocok untuk yang suka camilan pedas dengan porsi mengenyangkan."},
            {"name": "Mix Platter", "price": 25, "photo": "mix-platter", "slug": "mix-platter", "desc": "Kombinasi beberapa finger food favorit Rumangsa dalam satu porsi besar, pas untuk dinikmati bersama saat berkumpul dengan teman. Pilihan hemat dan praktis untuk mencicipi beberapa rasa sekaligus."},
        ],
    },
    "Rice Bowl": {
        "note": "Buat yang datang sambil lapar serius.",
        "items": [
            {"name": "Crispy Chicken Mayo", "price": 25, "photo": "crispy-chicken-mayo", "slug": "crispy-chicken-mayo", "desc": "Nasi hangat dengan ayam crispy yang disiram saus mayo gurih dan creamy, menciptakan perpaduan tekstur renyah dan lembut dalam satu mangkuk. Porsi yang pas untuk makan siang atau malam yang mengenyangkan."},
            {"name": "Grilled Chicken", "price": 26, "photo": "grilled-chicken", "slug": "grilled-chicken", "desc": "Nasi dengan ayam panggang berbumbu meresap, menghadirkan rasa gurih dan aroma smoky khas proses pemanggangan. Pilihan lebih ringan bagi yang menghindari gorengan namun tetap ingin porsi mengenyangkan."},
            {"name": "Sweet Chicken", "price": 26, "photo": "sweet-chicken", "slug": "sweet-chicken", "desc": "Nasi dengan potongan ayam yang dibalut saus manis gurih, menciptakan rasa yang disukai banyak kalangan termasuk anak-anak. Cocok untuk yang suka cita rasa manis pada menu utama."},
            {"name": "Rendang", "price": 30, "photo": "rendang", "slug": "rendang", "desc": "Nasi dengan rendang empuk yang dimasak dengan bumbu rempah kaya rasa khas masakan Nusantara. Daging yang empuk dan bumbu yang meresap sempurna menjadikan menu ini favorit pencinta masakan berat."},
            {"name": "Sweet Beef Belly", "price": 30, "photo": "sweet-beef-belly", "slug": "sweet-beef-belly", "desc": "Nasi dengan sandung lamur sapi (beef belly) bersaus manis yang lumer di mulut. Teksturnya empuk dengan lapisan lemak yang membuat rasanya semakin kaya dan gurih."},
        ],
    },
    "Berkuah": {
        "note": "Hangat, pas buat malam hujan.",
        "items": [
            {"name": "Indomie Lemak", "price": 15, "photo": "indomie-lemak", "slug": "indomie-lemak", "desc": "Indomie kuah dengan tambahan susu atau santan yang membuat kuahnya lebih gurih, kental, dan hangat. Menu ini cocok dinikmati saat cuaca dingin atau sekadar ingin comfort food yang mengenyangkan."},
            {"name": "Sop Kroket Kikil", "price": 18, "photo": "sop-kroket-kikil", "slug": "sop-kroket-kikil", "desc": "Sop hangat berisi kroket renyah dan kikil sapi yang empuk, disajikan dengan kuah gurih yang menghangatkan badan. Kombinasi tekstur renyah dan kenyal ini jadi daya tarik utama menu ini."},
            {"name": "Chicken Ramen", "price": 22, "photo": "chicken-ramen", "slug": "chicken-ramen", "desc": "Ramen dengan kuah gurih yang kaya rasa, dilengkapi topping ayam yang empuk dan mengenyangkan. Cocok dinikmati hangat-hangat, apalagi saat malam hari."},
            {"name": "Beef Ramen", "price": 25, "photo": "beef-ramen", "slug": "beef-ramen", "desc": "Ramen dengan kuah gurih yang kaya rasa, dilengkapi topping daging sapi yang empuk dan lezat. Porsi yang mengenyangkan cocok untuk makan malam yang hangat."},
        ],
    },
    "Dimsum": {
        "note": "",
        "items": [
            {"name": "Lumpia Kukus", "price": 15, "photo": "lumpia-kukus", "slug": "lumpia-kukus", "desc": "Lumpia kukus dengan tekstur lembut dan isian gurih di dalamnya, disajikan hangat sebagai camilan ringan. Cocok dinikmati dengan saus pelengkap sesuai selera."},
            {"name": "Pao Pandan", "price": 15, "photo": "pao-pandan", "slug": "pao-pandan", "desc": "Bakpao lembut dengan aroma pandan yang khas dan isian manis di dalamnya. Teksturnya empuk dengan wangi pandan yang terasa di setiap gigitan."},
            {"name": "Pao Telur Asin", "price": 15, "photo": "pao-telur-asin", "slug": "pao-telur-asin", "desc": "Bakpao dengan isian telur asin yang gurih dan lumer, menciptakan perpaduan rasa manis dari kulit bakpao dan gurih asin dari isiannya. Camilan yang mengenyangkan sekaligus nikmat."},
            {"name": "Siomay", "price": 15, "photo": "siomay", "slug": "siomay", "desc": "Siomay kukus dengan tekstur lembut, disajikan bersama saus pelengkap yang menambah cita rasa gurih. Camilan dimsum klasik yang cocok dinikmati kapan saja."},
        ],
    },
    "Other Choice": {
        "note": "",
        "items": [
            {"name": "Bound Salad", "price": 23, "photo": "bound-salad", "slug": "bound-salad", "desc": "Salad segar dengan campuran sayuran pilihan dan dressing yang bisa disesuaikan selera. Pilihan lebih ringan dan sehat bagi yang ingin menghindari makanan berat namun tetap mengenyangkan."},
            {"name": "Crispy Chicken Burger", "price": 23, "photo": "crispy-chicken-burger", "slug": "crispy-chicken-burger", "desc": "Burger dengan ayam crispy yang renyah, dipadukan saus spesial dan roti yang lembut. Menu praktis yang pas untuk makan cepat namun tetap memuaskan."},
            {"name": "Crispy Chicken Steak", "price": 26, "photo": "crispy-chicken-steak", "slug": "crispy-chicken-steak", "desc": "Steak ayam crispy yang disiram saus lada hitam atau saus jamur sesuai selera, menciptakan perpaduan renyah dan gurih dalam satu piring. Cocok untuk yang ingin menu ayam dengan sentuhan western."},
            {"name": "Spaghetti Carbonara", "price": 30, "photo": "spaghetti-carbonara", "slug": "spaghetti-carbonara", "desc": "Spaghetti dengan saus creamy carbonara yang gurih, dipadukan tekstur pasta yang pas dan aroma khas krim yang menggugah selera. Menu western yang cocok untuk makan siang maupun malam."},
        ],
    },
    "Dessert": {
        "note": "Penutup manis sebelum pulang.",
        "items": [
            {"name": "Puding Wennie Wence (S)", "price": 6, "photo": "puding-wennie-wence-small", "slug": "puding-wennie-wence-small", "desc": "Puding lembut ukuran kecil dengan rasa manis yang pas sebagai penutup, cocok dinikmati sendiri setelah makan berat. Teksturnya lembut dan tidak terlalu manis, sehingga cocok untuk semua kalangan."},
            {"name": "Puding Wennie Wence (L)", "price": 35, "photo": "puding-wennie-wence-large", "slug": "puding-wennie-wence-large", "desc": "Puding lembut ukuran besar dengan rasa manis yang pas, cocok dinikmati bersama-sama saat berkumpul dengan keluarga atau teman. Porsinya lebih besar dari versi small, pas untuk dibagi rata."},
            {"name": "Rumangsa Dessert", "price": 25, "photo": "rumangsa-dessert", "slug": "rumangsa-dessert", "desc": "Dessert signature Rumangsa dengan rasa manis dan sentuhan khas kedai yang sulit ditemukan di tempat lain. Cocok sebagai penutup sempurna setelah menikmati menu utama."},
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


def build_photo_categories():
    """Petakan slug foto -> kelompok ('minuman'/'makanan').

    Kelompok ditentukan dari kategori MENU tempat item tsb berada
    (lihat CATEGORY_GROUPS di bawah), lewat field 'photo' pada tiap item.
    Foto yang belum tersambung ke item MENU manapun akan diberi
    kelompok 'lainnya' agar tetap muncul di filter "Semua".
    """
    mapping = {}
    for cat_name, data in MENU.items():
        if cat_name in CATEGORY_GROUPS["Minuman"]:
            group = "minuman"
        elif cat_name in CATEGORY_GROUPS["Makanan"]:
            group = "makanan"
        else:
            continue
        for item in data["items"]:
            if item.get("photo"):
                mapping[item["photo"]] = group
    return mapping


def load_menu_photos():
    """Pindai folder static/img/menu-photos dan susun daftar foto menu.

    Nama tampilan (caption) dibuat otomatis dari nama file, misalnya
    'crispy-chicken-mayo.jpg' -> 'Crispy Chicken Mayo'. Tiap foto juga
    diberi label kelompok (Minuman/Makanan) berdasarkan data MENU.
    """
    photo_categories = build_photo_categories()
    photos = []
    if os.path.isdir(MENU_PHOTOS_DIR):
        for filename in sorted(os.listdir(MENU_PHOTOS_DIR), key=str.lower):
            if filename.lower().endswith(ALLOWED_PHOTO_EXTENSIONS):
                display_name = os.path.splitext(filename)[0]
                display_name = display_name.replace("_", " ").replace("-", " ").strip()
                display_name = " ".join(display_name.split())
                display_name = display_name.title()
                slug = os.path.splitext(filename)[0].lower()
                photos.append({
                    "src": f"img/menu-photos/{filename}",
                    "name": display_name or filename,
                    "slug": slug,
                    "group": photo_categories.get(slug, "lainnya"),
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
    return render_template(
        "foto-menu.html",
        photos=load_menu_photos(),
        photo_groups=["Semua", "Minuman", "Makanan"],
        info=INFO,
    )


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
