# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character("Pajar")
define kr = Character("Ketir")
define i = Character("Ica")
define k = Character("Kipli")
define r = Character("Robby")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene p2kk

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show pajar at left

    # These display lines of dialogue.

    p "wohooo akhir nya selesai juga acaranya"

    p "hai aku pajar yang tadi minta foto"

    show ketir at right
    hide pajar

    kr "oh. iya hai ada apa??"

    show pajar at left

    p "btw,kamu dari jurusan apa si??"


    show ketir at right
    kr "hukum jar, kalo kamu?"
    p "coba tebak hahaha *tertawa sedikit*"
    kr "hmmm apa yaa, mungkin HI"
    p "HI juga"
    kr "ihhh ngga gitu, hubungan internasional maksudnya *sedikit kesal*"
    p "aku dari jurusan informatika, btw boleh minta ignya? Punya ga?"
    kr "iyaa boleh, ini” *sembari membuka hp nya menunjukan ke pajar*"
    scene black
    "Singkat cerita kita banyak bercerita tentang satu sama lain dan aku memberanikan diri mengajaknya bertemu teman temanku di salah satu café  dekat kampus."
    scene cafe

    show pajar at left
    p "kenalin ni temen temenku tir"
    hide pajar
    show robby at left
    r "haloo aku robby"
    hide
    k "hai aku kipli biasa dipanggil kopler"
    r "haloo aku robby"







    scene jalan malam

    scene cafe

    scene kamar pajar

    scene kamar ketir

    scene kamar ica

    scene kamar pajar

    scene jalan parkiran

    scene bu tatik

    scene jalan malam

    scene kamar pajar

    scene kampus malam

    scene  kamar pajar

    scene cafe

    scene jalan malam

    scene lapangan

    scene resto

    scene jalan malam

    scene ending bahagia

    # this is the end of the game
    return
