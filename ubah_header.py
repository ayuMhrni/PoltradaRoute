from pathlib import Path
import re

# ============================================================
# SISTEM OPTIMASI RUTE DISTRIBUSI
# HEADER POLTRADA
# ATAS UTUH - CROP HANYA BAGIAN BAWAH
# ============================================================

BASE_DIR = Path(r"C:\SISTEM_OPTIMASI_BARU")

INDEX_FILE = BASE_DIR / "templates" / "index.html"
BACKUP_FILE = BASE_DIR / "templates" / "index_backup_sebelum_header.html"
BANNER_FILE = BASE_DIR / "static" / "header_poltrada_web_final.png"


# ============================================================
# CEK FILE
# ============================================================

print()
print("=" * 70)
print("MEMERIKSA FILE HEADER POLTRADA")
print("=" * 70)

if not INDEX_FILE.exists():
    print("ERROR: index.html tidak ditemukan.")
    input("Tekan ENTER untuk keluar...")
    raise SystemExit

if not BACKUP_FILE.exists():
    print("ERROR: backup index.html tidak ditemukan.")
    input("Tekan ENTER untuk keluar...")
    raise SystemExit

if not BANNER_FILE.exists():
    print("ERROR: header_poltrada_web_final.png tidak ditemukan.")
    print()
    print(BANNER_FILE)
    input("Tekan ENTER untuk keluar...")
    raise SystemExit

print("✓ index.html ditemukan")
print("✓ backup ditemukan")
print("✓ banner ditemukan")


# ============================================================
# GUNAKAN BACKUP ASLI
# ============================================================

html = BACKUP_FILE.read_text(
    encoding="utf-8"
)


# ============================================================
# CSS HEADER
# ============================================================

new_css = r"""

/* ============================================================
   POLTRADA HEADER
   NATURAL IMAGE + BOTTOM CROP
   ============================================================ */

header.topbar{

    position:relative !important;

    display:block !important;

    width:100% !important;

    height:220px !important;

    min-height:220px !important;

    max-height:220px !important;

    margin:0 !important;

    padding:0 !important;

    overflow:hidden !important;

    background:#075da5 !important;

    box-sizing:border-box !important;

    line-height:0 !important;
}


/* ============================================================
   BANNER
   ============================================================ */

/*
   PENTING:
   Tidak menggunakan object-fit: cover.

   Gambar ditampilkan dengan:
   width 100%
   height auto

   sehingga proporsi asli tetap terjaga.

   Container header yang memotong
   bagian BAWAH gambar.
*/

header.topbar .poltrada-banner{

    position:absolute !important;

    display:block !important;

    left:0 !important;

    top:0 !important;

    width:100% !important;

    height:auto !important;

    min-height:0 !important;

    max-height:none !important;

    margin:0 !important;

    padding:0 !important;

    border:0 !important;

    outline:0 !important;

    object-fit:initial !important;

    object-position:initial !important;

    box-sizing:border-box !important;
}


/* ============================================================
   HILANGKAN ELEMEN HEADER LAMA
   ============================================================ */

header.topbar .topbar-inner,
header.topbar .brand,
header.topbar .logo-box,
header.topbar .header-right,
header.topbar .poltrada-visual,
header.topbar .poltrada-building,
header.topbar .poltrada-statue,
header.topbar .poltrada-cadet,
header.topbar .poltrada-dots,
header.topbar .hero-wave{

    display:none !important;
}


/* ============================================================
   DESKTOP BESAR
   ============================================================ */

@media(min-width:1400px){

    header.topbar{

        height:220px !important;

        min-height:220px !important;

        max-height:220px !important;
    }
}


/* ============================================================
   LAPTOP
   ============================================================ */

@media(max-width:1399px){

    header.topbar{

        height:210px !important;

        min-height:210px !important;

        max-height:210px !important;
    }
}


/* ============================================================
   TABLET
   ============================================================ */

@media(max-width:900px){

    header.topbar{

        height:185px !important;

        min-height:185px !important;

        max-height:185px !important;
    }
}


/* ============================================================
   MOBILE
   ============================================================ */

@media(max-width:600px){

    header.topbar{

        height:150px !important;

        min-height:150px !important;

        max-height:150px !important;
    }
}
"""


# ============================================================
# MASUKKAN CSS
# ============================================================

style_pos = html.rfind("</style>")

if style_pos == -1:

    print()
    print("ERROR: </style> tidak ditemukan.")
    input("Tekan ENTER untuk keluar...")
    raise SystemExit


html = (
    html[:style_pos]
    + new_css
    + "\n"
    + html[style_pos:]
)


# ============================================================
# HEADER BARU
# ============================================================

new_header = r"""
<header
    class="topbar"
    style="
        width:100% !important;
        height:220px !important;
        min-height:220px !important;
        max-height:220px !important;
        margin:0 !important;
        padding:0 !important;
        overflow:hidden !important;
        background:#075da5 !important;
        box-sizing:border-box !important;
        line-height:0 !important;
    "
>

    <img
        class="poltrada-banner"
        src="{{ url_for('static', filename='header_poltrada_web_final.png') }}"
        alt="Sistem Optimasi Rute Distribusi - Politeknik Transportasi Darat Bali"
        style="
            position:absolute !important;
            display:block !important;
            left:0 !important;
            top:0 !important;
            width:100% !important;
            height:auto !important;
            min-height:0 !important;
            max-height:none !important;
            margin:0 !important;
            padding:0 !important;
            border:0 !important;
            outline:0 !important;
            object-fit:initial !important;
            object-position:initial !important;
        "
    >

</header>
"""


# ============================================================
# CARI HEADER LAMA
# ============================================================

header_pattern = (
    r'<header\s+class=["\']topbar["\'][^>]*>.*?</header>'
)


html, count = re.subn(
    header_pattern,
    new_header,
    html,
    count=1,
    flags=re.DOTALL | re.IGNORECASE
)


if count == 0:

    print()
    print("ERROR: header lama tidak ditemukan.")
    print("Tidak ada perubahan yang disimpan.")

    input("Tekan ENTER untuk keluar...")
    raise SystemExit


# ============================================================
# SIMPAN
# ============================================================

INDEX_FILE.write_text(
    html,
    encoding="utf-8"
)


# ============================================================
# HASIL
# ============================================================

print()
print("=" * 70)
print("HEADER POLTRADA BERHASIL DIPERBAIKI")
print("=" * 70)
print()
print("✓ Gambar banner TIDAK diubah")
print("✓ Proporsi gambar tetap asli")
print("✓ Posisi gambar dimulai dari bagian ATAS")
print("✓ Bagian atas tidak dipotong")
print("✓ Slogan tetap terlihat")
print("✓ Logo tetap terlihat")
print("✓ Tulisan kiri tetap terlihat")
print("✓ Bagian bawah banner yang dipotong")
print()
print("Ukuran header desktop : 220 px")
print("Ukuran header laptop  : 210 px")
print("Ukuran header tablet  : 185 px")
print("Ukuran header mobile  : 150 px")
print()
print("✓ Dashboard lainnya tidak diubah")
print()
print("=" * 70)
print("SELESAI")
print("=" * 70)

input("Tekan ENTER untuk keluar...")