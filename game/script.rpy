# # Kamu dapat taruh script game mu di file ini.

# # Deklarasikan gambar di bawah line ini, menggunakan pernyataan image.
# # cnth. image eileen happy = "eileen_happy.png"

# 1. Deklarasi Karakter dan Gambar Latar Belakang
define h = Character(_('Hoshiko'), color="#C4A484")
define w = Character(_('Wisteria'), color='#8f00ff')

define creator = Character(_("Khukoroshi"), color="#555555")


init python:
    # Kontainer utama untuk menyimpan daftar menu
    explorers = [ ]

    class Section(object):
        def __init__(self, title):
            self.kind = "section"
            self.title = title
            explorers.append(self)

    class Explorasi(object):
        def __init__(self, label, title, move=True):
            self.kind = "explorasi"
            self.label = label
            self.title = title
            
            if move and (move != "after"):
                self.move_before = True
            else:
                self.move_before = False

            if move and (move != "before"):
                self.move_after = True
            else:
                self.move_after = False

            explorers.append(self)

    # 2. Menyusun Isi Menu Sesuai Gambar (Bahasa Indonesia)
    Section(_("Mulai Cepat"))

    Explorasi("tutorial_playing", _("Pengalaman Pemain"))
    Explorasi("tutorial_create", _("Membuat Game Baru"))
    Explorasi("tutorial_dialogue", _("Menuliskan Dialog"))
    Explorasi("tutorial_images", _("Menambahkan Gambar"))

    Section(_("Lanjutan"))

    Explorasi("tutorial_simple_positions", _("Memposisikan Gambar"))
    Explorasi("tutorial_transitions", _("Transisi"))
    Explorasi("tutorial_music", _("Musik dan Efek Suara"))
    Explorasi("tutorial_menus", _("Pilihan dan Python"))
    Explorasi("tutorial_input", _("Input dan Interpolation"))
    Explorasi("tutorial_video", _("Pemutan Video"))

# 3. Membuat Tampilan Layar (Screen) Menu Seleksi
screen explorers(adj):
    frame:
        xsize 900
        xalign 0.65       # Menggeser kotak menu agak ke kanan seperti di gambar
        ysize 750
        ypos 30
        background "#000000a0" # Memberikan warna background transparan gelap pada kotak menu


        has side "c r b"

        viewport:
            yadjustment adj
            mousewheel True
            draggable True

            vbox:
                spacing 5
                for i in explorers:
                    if i.kind == "explorasi":
                        textbutton i.title:
                            action Return(i)
                            left_padding 35
                            xfill True
                            # Gaya teks tombol agar berwarna abu-abu muda mirip di gambar
                            text_idle_color "#8899a6" 
                            text_hover_color "#ffffff"
                    else:
                        null height 10
                        # Judul Section (Mulai Cepat) berwarna putih
                        text i.title: 
                            size 30 
                            color "#ffffff" 
                            alt ""
                            xoffset 10
                        null height 5

        bar adjustment adj style "vscrollbar"

        textbutton _("Cukup sekian untuk sekarang."):
            xfill True
            action Return(False)
            top_margin 10
            left_margin 17
            text_idle_color "#8899a6"
            text_hover_color "#ffffff"

# State untuk menyimpan posisi scrollbar agar tidak kembali ke atas
default explorers_adjustment = ui.adjustment()
default explorers_first_time = True

# 4. Alur Label Game saat Dijalankan
label start:

    # Menampilkan latar belakang dan karakter Eileen di sisi kiri
    # scene bg myroom
    # show hoshi normal2 at left
    # with dissolve

    # scene bg atapSekolah pagi
    window show

    scene bg atapSekolah pagi
    show hoshi senyum

    h "Hai aku Hoshiko, aku akan memandu kamu untuk menelusuri apa yang sudah dipelajari oleh [creator] creator game di ren'py ini."

    h "Ini adalah tempat history belajarnya [creator]."

    h "Ini mungkin akan seperti tutorialnya ren'py (dalam segi konsep), tetapi di dalamnya samasekali tidak ada tutorial."

    show hoshi terkejut
    show creator at right

    creator "{i}Yah karna aku ingin belajar dengan gaya yang berbeda.{/i}"

    hide creator 

    h "Woah...., orangnya muncul.{p}Yaa.... Gak tau sih, dia ngomong apa.{p}Dasar orang aneh"

    show creator at right

    creator "{i}Aku mengawasi di balik layar loh, {p}tetap waspada.{/i}"

    hide creator
    show hoshi marah

    h "Hah...!?, {p}Bukannya semua perkataanku di ketik langsung oleh mu?."

    show creator at right

    creator "he he"

    hide creator
    show hoshi sedih

    h "Sudah lah."





label explorers:

    

    # Eileen menanyakan pertanyaan yang tertera di bagian bawah gambar
    
    show hoshi senyum at left
    with move

    if explorers_first_time:
        $ h(_("Apa yang ingin kamu lihat?"), interact=False)
    else:
        $ h(_("Ada hal lain yang ingin kamu lihat?"), interact=False)

    $ explorers_first_time = False
    $ renpy.choice_for_skipping()

    # Memanggil screen menu tutorial
    call screen explorers(adj=explorers_adjustment)

    $ explorasi = _return

    if not explorasi:
        jump tamat

    if explorasi.move_before:
        show hoshi senyum at center
        with move

    $ reset_example()

    # Menjalankan label explorasi yang dipilih
    call expression explorasi.label from _call_expression
    
    if explorasi.move_after:
        hide example
        show hoshi senyum at left
        with move

    jump explorers

label tamat:
    show hoshi senyum at center
    with move
    h "Sampai jumpa lagi!"

    window hide
    return