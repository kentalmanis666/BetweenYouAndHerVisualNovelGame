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
    $ ketir_love = 0
    $ ica_love = 0
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

    show pajar at right
    p "kenalin ni temen temenku tir"
    hide pajar
    show robby at left
    r "haloo aku robby"
    hide robby
    show kipli at left
    k "hai aku kipli biasa dipanggil kopler"
    hide kipli
    show ketir at right
    kr "haloo aku ketir salam kenal ya  *sambil menyalami teman teman pajar*"

    scene black
    "Selang beberapa waktu kami bercanda jam sudah merujuk pada pukul 09:00. ketir memberi kode dia ingin pulang karena sudah terlalu malam."

    menu:
        kr "pulang yukk,udah malem jugaa"

        "mengantar dan mampir membeli makanan":
            jump great

        "aku tidak ingin mengantarnya pulang":
            jump notgreat

        "memesan gojek untuk ketir":
            jump notgreat1

    label great:
        scene cafe
        show pajar at left
        p  "sebentar ya aku ke toilet dulu"
        show ketir at right
        kr  "iyaa jar"
        hide pajar
        hide ketir
        scene black
        "5 menit setelah pajar pergi ke toilet"
        scene cafe
        show pajar at right
        p "ayo tirr"
        show ketir at right
        kr "yukk"
        hide pajar
        hide ketir
        show pajar at right
        p "gimana kalo kita mampir beli makanan atau cemilan, aku tau ada beberapa yang enak di sekitar sini"
        show ketir at left
        kr "boleh, kamu gapapa kah?"
        p "ngga kok gapapa  sans waee hahaha"
        kr "okide  *tersenyum malu*"
        scene black
        "mereka memutus kan untuk membeli camilan.setelah mereka makan camilan tersebut,tidak terasa sudah sampai di depan kos ketir"
        scene jalan malam
        "........."
        jump end


    label notgreat:
        scene cafe
        show ketir at left
        kr "jar udah malem pulang yuk"
        show pajar at right
        p "ntar dulu ya lagian masih jam 9 kok blom terlalu malem"
        hide pajar
        kr "jam set 10 kos ku udah ditutup aku ngga bawa kunci"
        show pajar at right
        p "iyaa bentar aja, atau kamu pulang dulu juga gapapa, gaenak sama yang lain ditinggal pulang"
        kr "yaudah aku pulang dulu yaa"
        p "yaudah iya, hati hati yaa"
        jump next
    label notgreat1:
        scene cafe
        show ketir at left
        kr "jar udah malem pulang yuk"
        show pajar at right
        p "ntaran dulu tir masih jam 9 blom terlalu malem kok"
        kr "tapi jam set 10 gerbang kos ku udah tutup aku ngga bawa kunci"
        p "yaudah aku pesenin gojek ya ngga enak sama yang lain masa aku tinggal"
        kr "yaudah kalo gitu"
        hide ketir
        show pajar at left
        show robby at right
        r "bodo lu jar astagaa"
        hide robby
        show kipli at right
        k "kurang berpendidikan hahahah!"
        hide kipli
        jump next
    label end:
        scene rumah ketir
        kr "makasih ya jarr,tadi seru banget!"
        p "tenang,yaudah masuk sana gih, jan tidur kemaleman :)"
        kr "okee byebye*sambil melambaikan tangan nya*"

    label next:
        scene black
        "akhirnya sampe kamar aku pun tertidur pulas"
        "Keesokan harinya aku diajak teman temanku nongkrong, disitu juga aku bertemu dengan ica cewe basket yang di idamkan dijurusannya, Selain cantik dan baik dia juga salah satu pemain inti di kampus."
        scene cafe
        show robby at right
        r "nih jar kenalin temenku Namanya ica dia anak basket di kampus"
        hide robby
        show pajar at left
        p "haii aku pajar"
        show ica at right
        i "halo jar"

    menu:
            i "halo jar"

            "kamu suka makan katak ga":
            jump great1
            "gimana latihan basketnya":
            jump average
label great1:
        scene cafe
        show pajar at left
        p "kamu suka makan katak ga?"
        show ica at right
        i "apa si jar hahahaha” *tertawa terbahak bahak*"
        p "gapapa si tanya aja biar ada yang bisa diobrolin hwhaha"
        i "kamu lucu juga ya ternyata anaknya ngga kaya yang diomongin sama robby & kipli"
        p "selain lucu aku juga rajin menabung kok"
        i "AHAHAHAHAHA!!!!!"
        jump next1

label average:
        scene cafe
        show pajar at left
        p "gimana Latihan baskenya ca"
        show ica at right
        i "ya gitu si, cape tapi seru juga"
        p "denger denger kemaren menang lawan anak ub ya"
        i "iyaa, tau dari mana?"
        p "kemaren aku nonton sama temenku kamu jago ya maen basketnya"
        i "oalah, iyaaa makasih ya"
        jump next1

label next1:
        scene black
        "pulang dari sana aku langsung menuju kos hendak untuk beristirahat. Tapi, setelah melihat hp ternyata ada pesan yang belum kubalas dari ketir, akhirnya aku menelfon dia untuk mengatahui bagaimana kabarnya hari ini."
        scene kamar pajar
        show pajar in left
        p "haloo tir"
        hide pajar
        scene kamar ketir
        kr "haloo jarr"
        hide ketir

menu:
        kr "haloo jar"
        "meminta maaf karena lama membalas pesan":
            jump notgreat2
        "memulai obrolan ringan":
            jump great2

label great2:
    scene kamar pajar
    show pajar at left
    p "sorry ya tir baru sempet ngabarin"
    hide pajar
    scene kamar ketir
    show ketir at right
    kr "iya gapapa jar"
    hide ketir
    scene kamar pajar
    show pajar at left
    p "sibuk ga?"
    hide pajar
    scene kamar petir
    show ketir at right
    kr "ngga juga si jar kenapa?"
    hide ketir
    scene kamar pajar
    show pajar at left
    p "ngga ada tugas apa? Kok santai banget?"
    hide pajar
    scene kamar ketir
    show ketir at right
    kr "baru selesai ngerjain, kamu gimana ngga ada tugas?"
    hide ketir
    scene kamar pajar
    show pajar at left
    p "ngga ada buat minggu ini tapi hari hari buat kamu selalu ada *jihahahahah*"
    hide pajar
    scene kamar ketir
    show ketir at right
    kr "hahahaha bisa aja, ih apasi dasar buaya"
    hide ketir
    scene kamar pajar
    show pajar at left
    p "AHAHAHAHAHHA!!!!! "
    hide pajar
    jump next2
label notgreat2:
    scene kamar pajar
    show pajar at left
    p "maaf ya tir baru bisa ngabarin kamu"
    hide pajar
    scene kamar ketir
    show ketir at right
    kr "gapapa kok jar santaii aja"
    hide ketir
    scene kamar pajar
    show pajar at left
    p "ngga enak aja si soalnya udah ngga bales lama"
    hide pajar
    scene kamar ketir
    show ketir at right
    kr "gapapa kok jar"
    hide ketir

    menu:
        kr "gapapa kok jar"
        "aku ajak makan deh":
        jump great21
"aku kerumah mu":
        jump notgreat21
label great21:
    scene kamar pajar
    show pajar at left
    p "aku traktir makan deh nanti"
    hide pajar
    scene kamar ketir
    show ketir at right
    kr "gausah jar ngerepotin nanti"
    hide ketir
    scene kamar pajar
    show pajar at right
    p "gapapa kok skalian ketemu sama kamu"
    hide pajar
    kr "yaudah kalo gitu"
    jump next2
label notgreat21:
    scene kamar pajar
    show pajar at left
    p "aku kerumahmu ya"
    hide pajar
    scene kamar ketir
    show ketir at right
    kr "ngapainnn???"
    hide ketir
    scene kamar pajar
    show pajar at left
    p "mau ketemu kamu skalain ngajak keluar"
    hide pajar
    scene kamar ketir
    show ketir at right
    kr "ngga usah udah malem” *menolak keras*"
    scene kamar pajar
    show pajar at left
    p "yaudah kalo gitu,..."
    jump next2
label next2:
    scene black
    "Setelah mengobrol lama dengan ketir tiba tiba aku mendapat notif dari ica temen dari si robby & kipli. "


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
