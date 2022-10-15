init python:
    import datetime

image credits_cg1:
    "images/cg/credits/1.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg2:
    "images/cg/credits/2.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg3:
    "images/cg/credits/3.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg4:
    "images/cg/credits/4.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg5:
    "images/cg/credits/5.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg6:
    "images/cg/credits/6.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg7:
    "images/cg/credits/7.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg8:
    "images/cg/credits/8.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg9:
    "images/cg/credits/9.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg10:
    "images/cg/credits/10.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg1_locked:
    "images/cg/credits/1b.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg2_locked:
    "images/cg/credits/2b.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg3_locked:
    "images/cg/credits/3b.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg4_locked:
    "images/cg/credits/4b.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg5_locked:
    "images/cg/credits/5b.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg6_locked:
    "images/cg/credits/6b.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg7_locked:
    "images/cg/credits/7b.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg8_locked:
    "images/cg/credits/8b.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg9_locked:
    "images/cg/credits/9b.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg10_locked:
    "images/cg/credits/10b.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg1_clearall:
    "images/cg/credits/1.png"
    size (640, 360)

image credits_cg2_clearall:
    "images/cg/credits/2.png"
    size (640, 360)

image credits_cg3_clearall:
    "images/cg/credits/3.png"
    size (640, 360)

image credits_cg4_clearall:
    "images/cg/credits/4.png"
    size (640, 360)

image credits_cg5_clearall:
    "images/cg/credits/5.png"
    size (640, 360)

image credits_cg6_clearall:
    "images/cg/credits/6.png"
    size (640, 360)

image credits_cg7_clearall:
    "images/cg/credits/7.png"
    size (640, 360)

image credits_cg8_clearall:
    "images/cg/credits/8.png"
    size (640, 360)

image credits_cg9_clearall:
    "images/cg/credits/9.png"
    size (640, 360)

image credits_cg10_clearall:
    "images/cg/credits/10.png"
    size (640, 360)

image credits_logo:
    "gui/logo.png"
    truecenter
    zoom 0.6 alpha 0 subpixel True
    linear 2.0 alpha 1
    4.5
    linear 2.0 alpha 0

image credits_ts:
    "images/bg/splash-white.png"
    xalign 0.5 yalign 0.6
    zoom 0.65 alpha 0 subpixel True
    linear 2.0 alpha 1
    4.5
    linear 2.0 alpha 0

style credits_header:
    font "gui/font/RifficFree-Bold.ttf"
    color "#ffaae6"
    size 36
    text_align 0.5
    outlines []

style baqa:
    font "gui/font/RifficFree-Bold.ttf"
    color "#ffaae6"
    size 43
    text_align 0.5
    outlines []

style credits_text:
    font "gui/font/Halogen.ttf"
    color "#fff"
    size 36
    text_align 0.5
    outlines []

style baqa_y:
    font "gui/font/Halogen.ttf"
    color "#fff"
    size 43
    text_align 0.5
    outlines []

style monika_credits_text:
    font "gui/font/m1.ttf"
    color "#fff"
    size 40
    text_align 0.5
    outlines [ (absolute(3), "#000", absolute(0), absolute(0)) ]

style monikaraoke:
    font "gui/font/m1.ttf"
    color "#fff"
    size 40
    text_align 0.5
    outlines [ (absolute(3), "#000", absolute(0), absolute(0)) ]

image baqa = ParameterizedText(style="baqa", ypos=-40)
image baqa_y = ParameterizedText(style="baqa_y", ypos=40)
image credits_header = ParameterizedText(style="credits_header", ypos=-40)
image credits_text = ParameterizedText(style="credits_text", ypos=40)
image monika_credits_text = ParameterizedText(style="monika_credits_text", xalign=0.5)
image monikaraoke = ParameterizedText(style="monikaraoke", xalign=0.5, ypos=-150)


transform credits_scroll:
    subpixel True
    yoffset 740
    linear 15 yoffset -380

transform credits_text_scroll:
    anchor (0.5, 0.5) subpixel True
    yoffset 920
    linear 15 yoffset -200

transform credits_sticker_scroll:
    subpixel True
    yoffset 940
    7.8
    linear 15 yoffset -180

transform bakayume:
    yalign 0.8
    ypos credits_ypos + 310
    xalign 0.5
    zoom 0.6 alpha 0 subpixel True
    linear 2.0 alpha 1
    4.5
    linear 2.0 alpha 0

transform bakayume_alt:
    yalign 0.8
    ypos credits_ypos + 360
    xalign 0.5
    zoom 0.6 alpha 0 subpixel True
    linear 2.0 alpha 1
    4.5
    linear 2.0 alpha 0

transform credits_scroll_right:
    xalign 0.9
    credits_scroll

transform credits_scroll_left:
    xalign 0.1
    credits_scroll

transform credits_text_scroll_right:
    xpos 960
    credits_text_scroll

transform credits_text_scroll_center:
    xpos 640
    credits_text_scroll

transform credits_text_scroll_left:
    xpos 320
    credits_text_scroll

transform credits_sticker_1:
    yanchor 1.00
    xalign 0.32
    credits_sticker_scroll
transform credits_sticker_2:
    yanchor 1.00
    xalign 0.44
    credits_sticker_scroll
transform credits_sticker_3:
    yanchor 1.00
    xalign 0.56
    credits_sticker_scroll
transform credits_sticker_4:
    yanchor 1.00
    xalign 0.68
    credits_sticker_scroll

define credits_ypos = 250

image monikami_1:
    ypos credits_ypos + 420
    2.46
    Text("B...", style="monika_credits_text")
    pause 0.78
    Text("Beni...", style="monika_credits_text")
    pause 1.34
    Text("Beni duyabiliyor musun?", style="monika_credits_text")
    pause 1.62
    Text("A...", style="monika_credits_text")
    pause 1.44
    Text("Beni duyabiliyor musun?", style="monika_credits_text")
    pause 1.78
    Text("A, beni duyabiliyor musun?", style="monika_credits_text")
    pause 2.46
    Text("Öhöm.", style="monika_credits_text")
    pause 1.34
    Text("Selam, benim.", style="monika_credits_text")
    pause 2.26
    Text("Şey, hani ben piyano falan çalışıyordum ya, biliyorsun.", style="monika_credits_text")
    pause 6.40
    Text("Ve henüz pek ilerleme kat edemedim.", style="monika_credits_text")
    pause 2.78
    Text("Hatta hiç.", style="monika_credits_text")
    pause 2.00
    Text("Ama sana bir şarkı yazdım.", style="monika_credits_text")
    pause 2.14
    Text("Ve sana bu şarkımı dinletmeyi umuyordum çünkü üzerinde çok...", style="monika_credits_text")
    pause 5.42
    Text("Çok çalıştım.", style="monika_credits_text")
    pause 1.54
    Text("Öyle işte.", style="monika_credits_text")

image mcredits_1a:
    ypos credits_ypos
    xoffset -239
    "black"
    10.33
    Text("Her gün,", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 13.0, ramplen=4, alpha=False)
image mcredits_1b:
    ypos credits_ypos
    xoffset -43
    "black"
    11.75
    Text("seninle olabileceğim bir geleceğin", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 10.0, ramplen=4, alpha=False)
image mcredits_1c:
    ypos credits_ypos
    xoffset 202
    "black"
    13.76
    Text("hayalini kuruyorum", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 15.0, ramplen=4, alpha=False)
image mcredits_2a:
    ypos credits_ypos + 50
    xoffset -192
    "black"
    19.45
    Text("Elimde", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 13.0, ramplen=4, alpha=False)
image mcredits_2b:
    ypos credits_ypos + 50
    xoffset -57
    "black"
    20.9
    Text(" ikimizle ilgili bir şiir", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 11.3, ramplen=4, alpha=False)
image mcredits_2c:
    ypos credits_ypos + 50
    xoffset 137
    "black"
    23.27
    Text("yazacak bir kalem", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 15.0, ramplen=4, alpha=False)

image mcredits_3:
    ypos credits_ypos + 100
    "black"
    28.35
    Text("Mürekkep kara bir birikintiye akıyor", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 16.0, ramplen=4, alpha=False)

image mcredits_4:
    ypos credits_ypos + 150
    xoffset -5
    "black"
    32.9
    Text(" Elini hareket ettiriver de yolu onun kalbine yaz!", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 9.0, ramplen=4, alpha=False)

image mcredits_5:
    ypos credits_ypos + 200
    "black"
    37.5
    Text("Sonsuz seçeneğin olduğu bu dünyada", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 16.0, ramplen=4, alpha=False)

image mcredits_6a:
    ypos credits_ypos + 250
    xoffset -91
    "black"
    42.0
    Text(" O özel günü bulmak", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 12.0, ramplen=4, alpha=False)
image mcredits_6b:
    ypos credits_ypos + 250
    xoffset 102
    "black"
    43.47
    Text("neye mal olacak?", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 12.0, ramplen=4, alpha=False)

image mcredits_7:
    "black"
    alpha 0.0
    48.62
    linear 1.5 alpha 1.0

image mcredits_1_test:
    ypos credits_ypos + 300
    Text("O özel günü bulmak neye mal olacak?", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 15.0, ramplen=4)

image end_glitch1:
    "bg/end-glitch1.jpg"
    alpha 0.0
    time 1.0
    alpha 1.0
    block:
        yoffset 1280 ytile 2
        linear 1 yoffset 0
        repeat
    time 9.45
    "end_glitch2"
    time 22.1
    "end_glitch3"
    time 28.65
    "end_glitch4"

image end_glitch2:
    "bg/end-glitch2.jpg"
    block:
        yoffset 1280 ytile 2
        linear 4 yoffset 0
        repeat

image end_glitch3:
    "bg/end-glitch3.jpg"
    block:
        yoffset 1280 ytile 2
        linear 4 yoffset 0
        repeat

image end_glitch4:
    parallel:
        "bg/end-glitch4.jpg"
        1.25
        "bg/end-glitch3.jpg"
        0.1
        repeat
    parallel:
        yoffset 1280 ytile 2
        linear 4 yoffset 0
        repeat

label credits:
    $ persistent.autoload = "credits"
    $ config.keymap['game_menu'] = []
    $ config.keymap['hide_windows'] = []
    $ renpy.display.behavior.clear_keymap_cache()
    $ quick_menu = False
    $ config.skipping = False
    $ config.allow_skipping = False
    scene black
    play music "bgm/end-voice.ogg" noloop

    show monikami_1 zorder 20

    show noise zorder 9:
        alpha 0.0
        linear 1.5 alpha 1.0
        time 2.0
        parallel:
            0.05
            choice:
                alpha 0.5
            choice:
                alpha 0.75
            choice:
                alpha 1.0
            repeat
        parallel:
            linear 0.375 alpha 0.7
            linear 0.375 alpha 1.0
        time 2.75
        alpha 0.95
        time 6.45
        alpha 0.3
        time 6.95
        alpha 0.9
        time 8.65
        linear 0.8 alpha 0
        alpha 0.5
        time 22.1
        alpha 0.85
        time 22.35
        alpha 0.5
        time 28.20
        alpha 0.3
        linear 0.45 alpha 0.9
        alpha 0.4
    show vignette zorder 10:
        alpha 0.75
        parallel:
            0.36
            alpha 0.75
            repeat
        parallel:
            0.49
            alpha 0.7
            repeat
    show end_glitch1 zorder 2
    show black as bar zorder 9:
        alpha 0.3
        size (1280,500)
        block:
            ypos 720
            linear 15 ypos -500
            repeat


    pause 41
    scene black
    pause 0.5
    $ consolehistory = []
    call updateconsole ("renpy.music.play(\"ddek.ogg\")", "“ddek.ogg” dosyası çalınıyor...")
    pause 1.0
    call hideconsole
    play music "<to 50.0>bgm/credits.ogg" noloop
    show mcredits_1a zorder 50
    show mcredits_1b zorder 49
    show mcredits_1c zorder 48
    show mcredits_2a zorder 47
    show mcredits_2b zorder 46
    show mcredits_2c zorder 45
    show mcredits_3 zorder 44
    show mcredits_4 zorder 43
    show mcredits_5 zorder 42
    show mcredits_6a zorder 41
    show mcredits_6b zorder 40
    show mcredits_7 zorder 51

    pause 50
    jump credits2

label credits2:
    python:
        sayoriTime = renpy.random.random() * 4 + 4
        natsukiTime = renpy.random.random() * 4 + 4
        yuriTime = renpy.random.random() * 4 + 4
        monikaTime = renpy.random.random() * 4 + 4
        sayoriPos = 0
        natsukiPos = 0
        yuriPos = 0
        monikaPos = 0
        sayoriOffset = 0
        natsukiOffset = 0
        yuriOffset = 0
        monikaOffset = 0
        sayoriZoom = 1
        natsukiZoom = 1
        yuriZoom = 1
        monikaZoom = 1
        imagenum = 0
    scene black
    $ consolehistory = []
    play music "<from 50.0>bgm/credits.ogg" noloop
    $ starttime = datetime.datetime.now()
    pause 0.88
    show credits_logo
    show baqa "Türkçe Çeviri" as baqa_1 at bakayume
    show baqa_y "BakaYume Çeviri Ekibi" as baqa_y_1 at bakayume_alt
    pause 9.12
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    show expression ("credits_cg1" + lockedtext) as credits_image_1 at credits_scroll_right
    show monikaraoke "{i}Herkese yapacak eğlenceli bir iş buldum mu bugün?{/i}" as monikaraoke_1 at credits_text_scroll_left
    show credits_header "Konsept ve Oyun Tasarımı" as credits_header_1 at credits_text_scroll_left
    show credits_text "Dan Salvato" as credits_text_1 at credits_text_scroll_left
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    $ pause(16.95 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        call updateconsole ("os.remove(\"images/cg/n_cg1.png\")", "n_cg1.png başarıyla silindi")
    else:
        call updateconsole_clearall ("os.remove(\"images/cg/n_cg1.png\")", "n_cg1.png başarıyla silindi")
    show expression ("credits_cg2" + lockedtext) as credits_image_2 at credits_scroll_left
    show monikaraoke "{i}Sen buradayken yaptığımız her şey\nonlar için eğlenceli nasılsa{/i}" as monikaraoke_2 at credits_text_scroll_right
    show credits_header "Karakter Çizimleri" as credits_header_2 at credits_text_scroll_right
    show credits_text "Satchely" as credits_text_2 at credits_text_scroll_right
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    $ pause(26.05 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        call updateconsole ("os.remove(\"images/cg/n_cg2.png\")", "n_cg2.png başarıyla silindi")
    else:
        call updateconsole_clearall ("os.remove(\"images/cg/n_cg2.png\")", "n_cg2.png başarıyla silindi")
    show expression ("credits_cg3" + lockedtext) as credits_image_1 at credits_scroll_right
    show monikaraoke "{i}Ben kendi hislerimi bile okuyamıyorken\nSözcükler ne işe yarar ki,\nbir gülümseme her şeyi söylüyorken?\n{/i}" as monikaraoke_3 at credits_text_scroll_left
    show credits_header "Arkaplan Çizimleri" as credits_header_1 at credits_text_scroll_left
    show credits_text "Velinquent" as credits_text_1 at credits_text_scroll_left
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    $ pause(35.15 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        call updateconsole ("os.remove(\"images/cg/y_cg1.png\")", "y_cg1.png başarıyla silindi")
    else:
        call updateconsole_clearall ("os.remove(\"images/cg/y_cg1.png\")", "y_cg1.png başarıyla silindi")
    show expression ("credits_cg4" + lockedtext) as credits_image_2 at credits_scroll_left
    show monikaraoke "{i}Eğer bu dünya bana bir son yazmayacaksa\nBenim her şeye sahip olmam neye mal olacak?{/i}" as monikaraoke_4 at credits_text_scroll_right
    show credits_header "Senaryo" as credits_header_2 at credits_text_scroll_right
    show credits_text "Dan Salvato" as credits_text_2 at credits_text_scroll_right
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    $ pause(44.25 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        call updateconsole ("os.remove(\"images/cg/y_cg2.png\")", "y_cg2.png başarıyla silindi")
    else:
        call updateconsole_clearall ("os.remove(\"images/cg/y_cg2.png\")", "y_cg2.png başarıyla silindi")
    show expression ("credits_cg5" + lockedtext) as credits_image_1 at credits_scroll_right
    show credits_header "Müzik" as credits_header_1 at credits_text_scroll_left
    show credits_text "Dan Salvato" as credits_text_1 at credits_text_scroll_left
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    $ pause(53.35 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        call updateconsole ("os.remove(\"images/cg/n_cg3.png\")", "n_cg3.png başarıyla silindi")
    else:
        call updateconsole_clearall ("os.remove(\"images/cg/n_cg3.png\")", "n_cg3.png başarıyla silindi")
    show expression ("credits_cg6" + lockedtext) as credits_image_2 at credits_scroll_left
    show credits_header "Vokal" as credits_header_2 at credits_text_scroll_right
    show credits_text "Jillian Ashcraft" as credits_text_2 at credits_text_scroll_right
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    $ pause(62.45 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        call updateconsole ("os.remove(\"images/cg/y_cg3.png\")", "y_cg3.png başarıyla silindi")
    else:
        call updateconsole_clearall ("os.remove(\"images/cg/y_cg3.png\")", "y_cg3.png başarıyla silindi")
    show expression ("credits_cg7" + lockedtext) as credits_image_1 at credits_scroll_right
    show monikaraoke "{i}Kalemim benim için değerli olanlara\nacı sözler mi yazıyor sadece?\n\n{/i}" as monikaraoke_5 at credits_text_scroll_left
    show credits_header "Özel Teşekkürler\n\n\n\n" as credits_header_1 at credits_text_scroll_left
    show credits_text "Masha Gutin\nKagefumi\nDavid Evelyn\nCorey Shin\nAlecia Bardachino\nMatt Naples" as credits_text_1 at credits_text_scroll_left
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    $ pause(71.55 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        call updateconsole ("os.remove(\"images/cg/s_cg1.png\")", "s_cg1.png başarıyla silindi")
    else:
        call updateconsole_clearall ("os.remove(\"images/cg/s_cg1.png\")", "s_cg1.png başarıyla silindi")
    show expression ("credits_cg8" + lockedtext) as credits_image_2 at credits_scroll_left
    show monikaraoke "{i}Seni alırsam mı aşk olur bu\nyoksa seni özgür bırakırsam mı?\n\n{/i}" as monikaraoke_6 at credits_text_scroll_right
    show credits_header "Türkçe Çeviri\n\n\n" as credits_header_2 at credits_text_scroll_right
    show credits_text "Bipa\nEcciel\nFunyarinpa\nrampaa" as credits_text_2 at credits_text_scroll_right
    show s_sticker at credits_sticker_1
    show n_sticker at credits_sticker_2
    show y_sticker at credits_sticker_3
    show m_sticker at credits_sticker_4
    $ pause(80.60 - (datetime.datetime.now() - starttime).total_seconds())
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    if not persistent.clearall:
        call updateconsole ("os.remove(\"images/cg/s_cg2.png\")", "s_cg2.png başarıyla silindi")
    else:
        call updateconsole_clearall ("os.remove(\"images/cg/s_cg2.png\")", "s_cg2.png başarıyla silindi")
    $ pause(88.00 - (datetime.datetime.now() - starttime).total_seconds())
    show expression ("credits_cg9" + lockedtext) as credits_image_1 at credits_scroll_right
    show monikaraoke "{i}Mürekkep kara bir birikintiye akıyor\nAşkı gerçekliğe nasıl yazabilirim?\n\n{/i}" as monikaraoke_7 at credits_text_scroll_left
    show credits_header "Türkçe Düzenleme\n\n\n" as credits_header_1 at credits_text_scroll_left
    show credits_text "Bipa\nEcciel\nFunyarinpa\nloykad\nrampaa" as credits_text_1 at credits_text_scroll_left
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ pause(95.00 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        call updateconsole ("os.remove(\"images/cg/s_cg3.png\")", "s_cg3.png başarıyla silindi")
    else:
        call updateconsole_clearall ("os.remove(\"images/cg/s_cg3.png\")", "s_cg3.png başarıyla silindi")
    show expression ("credits_cg10" + lockedtext) as credits_image_2 at credits_scroll_left
    show monikaraoke "{i}Eğer kalp atışının sesini duyamıyorsam\nAşka ne diyorsun senin gerçekliğinde?{/i}" as monikaraoke_8 at credits_text_scroll_right
    show credits_header "Özel Teşekkürler" as credits_header_2 at credits_text_scroll_right
    show credits_text "Monika\n[player]" as credits_text_2 at credits_text_scroll_right
    $ pause(104.10 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        call updateconsole ("os.remove(\"images/cg/m_cg1.png\")", "m_cg1.png başarıyla silindi")
    else:
        call updateconsole_clearall ("os.remove(\"images/cg/m_cg1.png\")", "m_cg1.png başarıyla silindi")

    show monikaraoke "{i}Ve senin gerçekliğinde; eğer seni nasıl seveceğimi bilmiyorsam{/i}" as monikaraoke_9 at credits_text_scroll_center
    call updateconsole ("os.remove(\"game/screens.rpy\")", "screens.rpy başarıyla silindi.")
    call updateconsole ("os.remove(\"game/gui.rpy\")", "gui.rpy başarıyla silindi.")
    call updateconsole ("os.remove(\"game/menu.rpy\")", "menu.rpy başarıyla silindi.")
    call updateconsole ("os.remove(\"game/script.rpy\")", "script.rpy başarıyla silindi.")
    $ pause(113.72 - (datetime.datetime.now() - starttime).total_seconds())
    show monikaraoke "{i}Seni rahat bırakacağım{/i}" as monikaraoke_10 with dissolve:
        xalign 0.5
        yalign 0.5
    hide monikaraoke_9 with None
    $ pause(115.72 - (datetime.datetime.now() - starttime).total_seconds())
    call hideconsole
    hide monikaraoke_10 with None
    show credits_ts
    show credits_text "tarafından sevgiyle yapıldı":
        zoom 0.75 xalign 0.5 yalign 0.80 alpha 0 subpixel True
        linear 2.0 alpha 1
        4.5
        linear 2.0 alpha 0
    pause 9.3
    play sound page_turn
    show poem_end with Dissolve(1)
    label postcredits_loop:
        $ persistent.autoload = "postcredits_loop"
        $ config.keymap['game_menu'] = []
        $ config.keymap['hide_windows'] = []
        $ renpy.display.behavior.clear_keymap_cache()
        $ quick_menu = False
        $ config.skipping = False
        $ config.allow_skipping = False
        scene black
        show poem_end
        $ pause()
        call screen dialog(message="Hata: Kod dosyası kayıp ya da bozuk.\nLütfen oyunu yeniden yükleyin.", ok_action=Quit(confirm=False))
        return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
