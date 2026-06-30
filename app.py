from flask import Flask, render_template

app = Flask(__name__)

# ---------------------------------------------------------------------------
# DATA MENU — ditranskrip dari menu board Rumangsa Kopi
# ---------------------------------------------------------------------------
MENU = {
    "Coffee": {
        "note": "Diseduh dari biji pilihan, untuk yang butuh kekuatan klasik.",
        "items": [
            {"name": "Espresso (Single/Double)", "price": 15},
            {"name": "Americano", "price": 15},
            {"name": "Long Black", "price": 15},
            {"name": "Café Latte", "price": 18},
            {"name": "Cappuccino", "price": 18},
            {"name": "Con Hielo", "price": 20},
            {"name": "Mockresso", "price": 21},
            {"name": "Affogato", "price": 21},
            {"name": "Latte (Vanilla/Hazelnut/Caramel)", "price": 23},
            {"name": "Macchiato", "price": 23},
        ],
    },
    "Drip Methods": {
        "note": "Untuk pencinta kopi manual brew yang sabar menunggu.",
        "items": [
            {"name": "V60", "price": 27},
            {"name": "Japanese Ice Drip", "price": 27},
        ],
    },
    "Rumangsa Signature": {
        "note": "Racikan rumahan, hanya ada di Rumangsa.",
        "items": [
            {"name": "Rumansa", "price": 18},
            {"name": "Secret Mango", "price": 22},
            {"name": "Tuku Taka", "price": 22},
            {"name": "Harmoni", "price": 23, "new": True},
            {"name": "Rumara", "price": 23, "new": True},
            {"name": "Unicorn Milk", "price": 25},
            {"name": "Black Oreo Berry", "price": 25},
        ],
    },
    "Non Coffee": {
        "note": "Untuk yang ingin ngopi tanpa kafein berlebih.",
        "items": [
            {"name": "Strawberry Latte", "price": 18},
            {"name": "Taro Latte", "price": 21},
            {"name": "Choco Latte", "price": 23},
            {"name": "Greentea Latte", "price": 23},
            {"name": "Red Velvet Latte", "price": 23},
            {"name": "Buttertones", "price": 25},
        ],
    },
    "Tea Flavor": {
        "note": "Segar, ringan, cocok untuk siang hari Pontianak.",
        "items": [
            {"name": "Lychee", "price": 15},
            {"name": "Peach", "price": 15},
            {"name": "Lemon", "price": 15},
        ],
    },
    "Summerel": {
        "note": "Squash segar untuk mengusir gerah.",
        "items": [
            {"name": "Lime Squash", "price": 18},
            {"name": "Orange Squash", "price": 18},
            {"name": "Laquisha", "price": 20, "new": True},
        ],
    },
    "Additional": {
        "note": "",
        "items": [
            {"name": "Air Mineral", "price": 10},
        ],
    },
    "Finger Food": {
        "note": "Teman ngobrol santai sore-malam.",
        "items": [
            {"name": "Kroket Goreng", "price": 15},
            {"name": "Pisang Goreng (Srikaya/Keju/Coklat)", "price": 15},
            {"name": "Sosis Goreng", "price": 15},
            {"name": "Tela-Tela (Asin/Manis)", "price": 15},
            {"name": "Toast with Vanilla Ice Cream", "price": 15},
            {"name": "French Fries", "price": 18},
            {"name": "Risoles", "price": 20},
            {"name": "Chicken Shilin", "price": 20},
            {"name": "Mix Platter", "price": 25},
        ],
    },
    "Rice Bowl": {
        "note": "Buat yang datang sambil lapar serius.",
        "items": [
            {"name": "Crispy Chicken Mayo", "price": 25},
            {"name": "Grilled Chicken", "price": 26},
            {"name": "Sweet Chicken", "price": 26},
            {"name": "Rendang", "price": 30},
            {"name": "Sweet Beef Belly", "price": 30},
        ],
    },
    "Berkuah": {
        "note": "Hangat, pas buat malam hujan.",
        "items": [
            {"name": "Indomie Lemak", "price": 15},
            {"name": "Sop Kroket Kikil", "price": 18},
            {"name": "Chicken Ramen", "price": 22},
            {"name": "Beef Ramen", "price": 25},
        ],
    },
    "Dimsum": {
        "note": "",
        "items": [
            {"name": "Lumpia Kukus", "price": 15},
            {"name": "Pao Pandan", "price": 15},
            {"name": "Pao Telur Asin", "price": 15},
            {"name": "Siomay", "price": 15},
        ],
    },
    "Other Choice": {
        "note": "",
        "items": [
            {"name": "Bound Salad", "price": 23},
            {"name": "Crispy Chicken Burger", "price": 23},
            {"name": "Crispy Chicken Steak", "price": 26},
            {"name": "Spaghetti Carbonara", "price": 30},
        ],
    },
    "Dessert": {
        "note": "Penutup manis sebelum pulang.",
        "items": [
            {"name": "Puding Wennie Wence (S)", "price": 6},
            {"name": "Puding Wennie Wence (L)", "price": 35},
            {"name": "Rumangsa Dessert", "price": 25},
        ],
    },
}

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


@app.route("/galeri")
def gallery():
    return render_template("gallery.html", gallery=GALLERY, info=INFO)


@app.route("/tentang")
def about():
    return render_template("about.html", info=INFO)


if __name__ == "__main__":
    app.run(debug=True)
