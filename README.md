# Rumangsa Kopi — Website (Flask)

## Cara menjalankan
```bash
pip install -r requirements.txt
python app.py
```
Lalu buka `http://127.0.0.1:5000` di browser.

## Struktur halaman (4 halaman)
1. **Beranda** (`/`) — hero video, alasan memilih Rumangsa, teaser galeri.
2. **Menu** (`/menu`) — seluruh menu dari foto menu board, dengan filter kategori (Semua / Minuman / Makanan).
3. **Galeri** (`/galeri`) — 10 foto suasana kedai.
4. **Tentang & Lokasi** (`/tentang`) — cerita singkat, info kontak/jam buka, dan peta lokasi.

## Yang perlu Anda ganti dengan aset asli

### 1. Foto outlet (WAJIB diganti)
Karena Anda belum punya foto outlet, saya isi sementara dengan foto stok bertema cozy/earthy dari Picsum
(lihat `GALLERY` dan beberapa `<img>` di `app.py` & template). Untuk mengganti:
- Simpan foto asli di `static/img/` (misalnya `static/img/outlet-1.jpg`)
- Di `app.py`, ganti nilai `src` pada list `GALLERY` menjadi `/static/img/outlet-1.jpg`, dst.
- Lakukan hal sama pada `templates/index.html` dan `templates/about.html` untuk foto besar (`about-photo`).

### 2. Video hero
Saat ini menggunakan video contoh publik (`Big Buck Bunny`) sebagai placeholder di `templates/index.html`.
Ganti dengan video asli suasana kedai:
- Simpan video di `static/video/hero.mp4`
- Ubah `<source src="...">` di bagian `<video>` pada `index.html` menjadi `{{ url_for('static', filename='video/hero.mp4') }}`

### 3. Audio latar (backsound)
Saat ini memakai contoh musik instrumental publik (`SoundHelix`) di `templates/base.html`.
Ganti dengan musik/backsound resmi milik Rumangsa (pastikan Anda punya hak pakainya):
- Simpan file di `static/audio/backsound.mp3`
- Ubah `<source src="...">` pada elemen `<audio id="bgAudio">` di `base.html`

Audio **tidak diputar otomatis** (browser modern memblokir autoplay bersuara) — pengunjung perlu menekan
tombol musik bulat di pojok kanan bawah untuk menyalakannya. Ini sengaja dibuat begitu agar tidak mengganggu.

### 4. Harga menu
Harga di menu board tertulis seperti "15", "23", dst — saya asumsikan ini dalam ribuan rupiah (Rp 15.000, Rp 23.000).
Format ini diatur otomatis lewat CSS (`.menu-item .price::before/::after` di `style.css`).
Jika satuan aslinya berbeda, edit bagian tersebut atau ubah nilai `price` langsung di `app.py`.

## Catatan teknis
- Data menu didefinisikan di `app.py` (dict `MENU`) — tambah/ubah item di sana, tidak perlu sentuh HTML.
- Peta di halaman Tentang memakai Google Maps embed berdasarkan alamat (bisa diganti dengan link Google Maps resmi outlet untuk akurasi pin yang lebih tepat).
- Desain responsif sampai ke layar mobile, termasuk menu hamburger.
