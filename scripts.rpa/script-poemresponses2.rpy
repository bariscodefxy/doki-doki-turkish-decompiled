label ch21_y_end:
    jump ch1_y_end

label ch22_y_end:
    stop music fadeout 2.0
    call showpoem (poem_y22, music=False, paper="images/bg/poem_y1.jpg", img="yuri 2s")
    y 2q "Ahaha..."
    y "Ne hakkında olduğunun önemi yok."
    y "Son zamanlarda aklım biraz kıpır kıpır olduğundan kaleminle kendimi oyalamam gerekti."
    y 2o "Ah--"
    y 2q "Yani... d-dün çantandan bir kalem düştü de, saklamak için eve götürmüştüm ve..."
    y "Şey, ben..."
    y 2y6 "Bu kalemin... yazış... şeklini... seviyorum da."
    y "Bu şiiri... onunla... yazdım."
    y "Ve şimdi de kaleme sen dokunuyorsun."
    y 2y5 "Ahaha."
    y 3p "İ-İyiyim ben!"
    y 3o "Az önce ben ne..."
    y "..."
    y 4c "... Bu konuşma hiç olmamış gibi davranabilir miyiz?"
    y "Şiir sende kalabilir ama..."
    return
label ch23_y_end:
    show darkred zorder 5:
        alpha 0
        linear 2.0 alpha 1.0
    call showpoem (poem_y23, track="bgm/5_yuri2.ogg", revert_music=False, paper="images/bg/poem_y2.jpg", img="yuri eyes", where=truecenter)
    y "Hoşuna gitti mi??"
    y "Senin için yazdım!"
    $ gtext = glitchtext(80)
    show yuri 1b at i11
    y "Eğer fark etmediysen, bu şiirin konusu [gtext]."
    y 1y6 "Ama daha da önemlisi, şiire kendi kokumu bıraktım."
    y "Bak, görüyor musun, kulüpteki en düşünceli kişi benim, değil mi?"
    play sound "sfx/glitch2.ogg"
    show yuri glitch
    pause 0.2
    stop sound
    show yuri 3y2
    hide darkred
    $ currentpos = get_pos(channel="music_poem")
    $ audio.t5c = "<from " + str(currentpos) + " loop 4.444>bgm/5.ogg"
    $ renpy.music.stop(channel="music_poem")
    $ renpy.music.play(audio.t5c)
    y "..."
    y 4d "Ben..."
    y "Sanırım ben... kusacağım."
    show yuri at lhide
    hide yuri
    pause 1.0
    return
label ch21_n_end:
    jump ch1_n_end
label ch22_n_end:
    if n_appeal >= 2:
        jump ch22_n_end2
    else:
        call showpoem (poem_n2)
        n 2a "Fena olmamış, değil mi?"
        mc "Dünküne kıyasla epey uzun olmuş."
        n 2w "Dünkü fazla kısaydı..."
        n "Daha yeni yeni ısınıyorum!"
        n 2c "Umarım elimden sadece o kadarının geleceğini düşünmemişsindir."
        mc "Hayır, tabii ki öyle düşünmedim..."
        n 2a "Neyse, bu şiirdeki mesaj gayet açık ve net."
        n "Açıklamama gerek yoktur herhâlde."
        n 2g "Hani, kim olursa olsun bu şiirin konusunun bilgisiz bir ahmak olduğunu anlar..."
        n "Herkesin garip bir hobisi ya da insanlarca hor görülse de yapmayı sevdiği bir şey vardır."
        n 5q "İnsanların öğrenmesi durumunda seninle alay edeceklerinden ya da seni küçük görmelerinden korkacağın bir şey."
        n 1e "... Ama bu da sadece insanların aptal olduğu anlamına gelir!"
        n "Onları mutlu edip başkalarına zararı dokunmadığı sürece birinin neyden hoşlandığından kime ne?"
        n 1q "İnsanların başkalarının beğendiği tuhaf şeylere saygı göstermeyi öğrenmesi gerekiyor bence..."
        n 1x "... Örneğin bu kulüpteki iki kız, tabii onlara olan saygımdan isimlerini söylemeyeceğim."
        n 1s "Tek rahat ettiğim yerde insanların bana saygı göstermemesi komik değil mi ya?.."
        n 1u "... Of ya, şimdi de fazla şikayet etmeme sebep oluyorsun!"
        "{i}(... Ne yaptım ki ben?){/i}"
        mc "Doğrusu, ne kadar anlamı var bilmiyorum ama ben sana saygı duyuyorum..."
        n 1h "Yani--"
        n "Sağ ol..."
        n 1s "... Ama Yuri’ye daha fazla ‘saygı duyduğun’ belli yani..."
        n 42c "Neyse... Şiirlerimizi paylaştık, gidebilirsin artık."
    return
label ch22_n_end2:
    call showpoem (poem_n2b, revert_music=False)
    $ style.say_dialogue = style.edited
    n 1g "[player]..."
    n "Neden bugün benimle okumaya gelmedin?"
    n 1m "Seni bekliyordum."
    n "Seni çok bekledim."
    n "Bugün tek heveslenebileceğim şey oydu."
    n "Niye mahvettin ki?"
    n "Yuri’yi daha mı çok seviyorsun?"
    n 1k "Onunla alakadar olmasan daha iyi edersin bence."
    n "Beni dinliyor musun?"
    show darkred zorder 5:
        alpha 0.0
        easein 4.0 alpha 1.0
    $ currentpos = get_pos(channel="music_poem")
    $ audio.t5c = "<from " + str(currentpos) + " loop 4.444>bgm/5_ghost.ogg"
    stop music_poem fadeout 2.0
    $ renpy.music.play(audio.t5c, fadein=2.0, tight=True)
    show n_rects_ghost1 zorder 4
    show n_rects_ghost2 zorder 4
    show n_rects_ghost3 zorder 4
    n ghost1 "Yuri manyak sapığın teki."
    n "Şimdiye kadar bunu anlamış olman gerekir."
    n "O yüzden onu bırak benimle oyna."
    n "Tamam mı?"
    n "Benden nefret etmiyorsun [player], değil mi?"
    n "Benden nefret ediyor musun?"
    show natsuki_ghost_blood zorder 3
    n "Benim ağlaya ağlaya eve gitmemi mi istiyorsun?"
    n "Tek güvende hissettiğim yer bu kulüp."
    n "Bunu benim için mahvetme."
    n "Mahvetme."
    n "Ne olur."
    n "Yuri’yle konuşma yeter."
    n "Benimle oyna."
    n "Tek sahip olduğum şey bu..."
    n "Benimle oyna."
    stop music
    hide n_rects_ghost3
    n ghost2 "BENİMLE OYNA!!!"
    $ style.say_dialogue = style.normal
    $ quick_menu = False
    pause 1
    play sound "sfx/crack.ogg"
    hide natsuki_ghost_blood
    hide n_rects_ghost1
    hide n_rects_ghost2
    show natsuki ghost3
    show n_rects_ghost4 onlayer front zorder 4
    show n_rects_ghost5 onlayer front zorder 4
    pause 0.5
    hide natsuki
    play sound "sfx/run.ogg"
    show natsuki ghost4 onlayer front at i11
    pause 0.25
    window hide(None)
    hide natsuki onlayer front
    hide n_rects_ghost4 onlayer front
    hide n_rects_ghost5 onlayer front
    scene black
    with None
    window auto
    scene black
    pause 0.5
    show end:
        xzoom -1
    with dissolve_cg
    pause 2.0
    scene black
    with None
    $ quick_menu = True
    return
label ch23_n_end:
    $ natsuki_23 = True
    $ style.say_dialogue = style.normal
    call showpoem (poem_n23, revert_music=False)
    $ renpy.music.stop(channel="music_poem", fadeout=2.0)
    $ style.say_dialogue = style.edited
    show screen tear(8, offtimeMult=1, ontimeMult=10)
    pause 3.0
    stop music
    hide screen tear
    show natsuki ghost_base
    n "Fikrimi değiştirdim."
    n "Az önce okuduğun her şeyi unut."
    n "Hiç uğraşmanın anlamı yok."
    n "Yuri’nin itici biri olması tamamen kendi suçu."
    n "[player], beni duyabiliyor musun?"
    n "Monika’yla daha fazla vakit geçirsen, bu sorunların hepsi kaybolurdu."
    n "Ben ve Yuri senin kadar harika biri için fazla sorunluyuz."
    n "Artık yalnızca Monika’yı düşün."
    n "Yalnızca Monika."
    hide natsuki
    $ style.say_dialogue = style.edited
    "Yalnızca Monika."
    menu:
        "Yalnızca Monika."
        "Yalnızca Monika.":
            pass
    $ style.say_dialogue = style.normal
    $ renpy.call_screen("dialog", "Yalnızca Monika.", ok_action=Return())
    scene white
    play music t1
    show intro with Dissolve(0.5, alpha=True)
    pause 2.5
    hide intro with Dissolve(0.5, alpha=True)
    show splash_warning "Yalnızca Monika." with Dissolve(0.5, alpha=True)
    pause 1.0
    play music t5
    $ skip_transition = True

    return

label ch21_m_end:
    call showpoem (poem_m21)
    jump ch1_m_end2
label ch22_m_end:
    call showpoem (poem_m22, revert_music=False)
    $ currentpos = get_pos(channel="music_poem")
    $ audio.t5c = "<from " + str(currentpos) + " loop 4.444>bgm/5.ogg"
    stop music_poem fadeout 2.0
    $ pause(2)
    show screen tear(20, 0.3, 0.3, 0, 40)
    $ pause(0.5)
    hide screen tear
    play music t5c
    m 5 "Özür dilerim, biraz mecazi olduğunun farkındayım."
    m "Yapmaya çalıştığım şey sadece... A..."
    m 1r "Neyse, boş ver."
    m "Açıklamaya çalışmanın anlamı yok."
    m 1i "Her neyse."
    m "İşte Monika’nın Bugünkü Yazım Tüyosu!"
    m "Bazen kendini zor bir kararla yüzleşirken bulursun."
    m "Öyle durumlarda oyununu kaydetmeyi unutma!"
    m "Fikrinin ne zaman değişeceğini... A..."
    m 3i "... Kiminle konuşuyorum ben?"
    m "Beni duyabiliyor musun?"
    m 3g "Beni duyabildiğini söyle bana."
    m "Bir şey söyle."
    $ renpy.call_screen("dialog", "Lütfen bana yardım et.", ok_action=Return())
    m 3k "... Bugünkü tavsiyem bu kadar!"
    m "Dinlediğin için teşekkürler~"
    return
label ch23_m_end:
    $ quick_menu = False
    window hide
    play sound page_turn
    show paper_glitch zorder 10 with Dissolve(1)
    play music g2
    if renpy.windows and renpy.game.preferences.fullscreen:
        $ mouse_visible = False
        scene bsod
        pause 3.0
    else:
        show black zorder 1
        pause 2.0
    window show(None)
    show monika 1d zorder 11 at i11
    $ quick_menu = True
    $ mouse_visible = True
    m "Of! Gerçekten çok korktum yahu!{fast}"
    window auto
    m "A..."
    m 1m "Şey, sanırım bu şiiri... ‘yazarken’ hata yaptım."
    m "Yapmaya çalıştığım şey sadece..."
    m 1i "... Boş ver."
    m "Devam edelim hadi..."
    stop music
    return


label ch21_n_bad:
    jump ch1_n_bad

label ch21_n_med:
    jump ch1_n_med

label ch21_n_good:
    jump ch1_n_good

label ch22_n_bad:

    if n_poemappeal[0] < 0:
        n 1r "..."
        n "Evet, tam da düşündüğüm gibiymiş..."
        mc "?.."
        n 2w "[player], hadi ama."
        n "Aptal değilim."
        n 2h "Yuri’yle ne kadar vakit geçirdiğinin farkındayım..."
        n "Onu etkilemeyi yazımını geliştirmekten daha çok önemsediğin apaçık ortada."
        n 2w "Açık söylemek gerekirse, acınası bir davranış bu."
        n 4h "Niye bu kulübe katıldın ki [player]?"
        n "Of of..."
        n "Yeni bir üyenin gelmesinin herkesin birbiriyle daha çok ilgilenmesine sebep olacağını düşünmüştüm."
        n 4s "Birbirimizi daha da ayırmaya sebep olacağını değil."
        n 1u "Yaptığımız şey çok saçma zaten..."
        n 12c "... Bak, bugün moralim iyi değil ve şu an pek konuşasım yok."
        n "Lütfen git."
        $ skip_poem = True
        return
    else:


        n 1k "... Hm."
        n "Bir öncekini daha çok beğenmiştim."
        mc "Ha? Gerçekten mi?"
        n 2c "Yani, öyle. Bu seferkinin biraz daha cüretkar olduğunu görebiliyorum."
        n "Ama daha buna hazır değilsin. Çuvalladın."
        mc "Öyle olmuş olabilir ama farklı bir şey denemek istedim."
        mc "Hâlâ öğrenme sürecindeyim."
        jump ch22_n_med_shared2

label ch22_n_med:

    if n_poemappeal[0] < 0:
        n "... Hım."
        n 2k "Yani, geçen seferkine göre daha iyi olduğunu söyleyebilirim."
        n "Biraz çaba sarf ettiğini görmek güzel."
        mc "Sevindim..."
        label ch22_n_med_shared:
            n 2c "Herkesten biraz ilham almaya bak ama."
            n "En azından Yuri’den biraz etkilenmişsin galiba, değil mi?"
            n 5q "Hani, onunla birlikte, yani..."
            n "Vakit filan geçirdiğini biliyorum da..."
            n 1w "Monika’yla ben de onun kadar iyiyiz!"
            n 1q "Ş-Şiir yazma konusunda yani!"
            n 1h "O yüzden bir şeyler öğrenmeye çalışmalısın yoksa hiç gelişemezsin!"
            n "Al, benim yazdığım şiir..."
            n "Benimkinden bir şeyler öğrenmeni sağlayacağımdan emin olabilirsin."
            return


    elif n_poemappeal[0] == 0:
        n "... Hım."
        n 2k "Yani senin en son şiirinden daha kötü filan diyemem."
        n "Ama daha iyi de diyemem."
        mc "Oh be..."
        n 2c "Ha? Ne demek ‘Oh be’?"
        mc "Ah... Felaket olmayan her şiiri zafer olarak kabul ediyorum."
        mc "Ve aramızdaki en eleştirici kişinin sen olduğunu düşünüyorum."
        n 1p "H-Hey! Nereden çıkarıyorsun benim--"
        n 1q "{i}(Bir dakika, belki de bu bir iltifattı?..){/i}"
        n 4y "A-Ahah! Birinin tecrübeme saygı duymasına sevindim!"
        n "Peki madem, pratik yapmaya devam et de belki bir gün benim kadar iyi yazar olursun!"
        mc "Şey... A..."
        "İçimden bir ses Natsuki’nin kastımı yanlış anladığını söylüyor."
        jump ch22_n_med_shared
    else:


        n "... Hım."
        n 2c "Eh, berbat değil."
        n "Ama son şiirinden sonra hayal kırıklığına uğradım."
        n 2s "Hoş, bu da geçen seferki kadar güzel olsaydı canımı sıkmış olurdun."
        mc "Bu sefer biraz daha farklı bir şeyler denemek istedim sanırım."
        label ch22_n_med_shared2:
            n 2c "Olabilir canım. Sen hâlâ yenisin bu işlere, kendi tarzını hemen bulmanı bekleyemem ya."
            n "Yani, kulüpteki herkes birbirinden farklı şekillerde yazıyor..."
            n "Belki hepimizden biraz ilham alırsın."
            n 2q "Mesela..."
            n 5q "Bugün Yuri’yle biraz vakit geçirdiğini fark ettim..."
            n "Kiminle vakit geçirdiğini umursadığımdan değil tabii."
            n 5w "Ne de olsa kimseden hiçbir şey beklememeyi öğrendim ben."
            n 5s "O yüzden seni bekliyor filan değildim."
            n 5h "Ama yine de benim şiirime bir göz atmalısın..."
            n "Belki bir şeyler öğrenirsin."
            return

label ch23_n_bad:
    if y_gave:
        jump ch23_n_ygave

    if n_poemappeal[0] < 0 and n_poemappeal[1] < 0:
        n 5x "Yuri’ye yağ çeken şiirlerinden bir tane daha okumam."
        n 5s "Ama benimkini sana okutturacağım."
        n "Bunun bir sebebi var."
        n 5x "Bunu keşke yapmak zorunda olmasam..."
        n "Ama maalesef başka seçeneğim yok."
        n 5h "Sadece... iyice, dikkatlice oku, olur mu?"
        n "Ondan sonra gidebilirsin."
        return

    elif n_poemappeal[0] < 0 or n_poemappeal[1] < 0:
        n "..."
        n 2c "... Eh işte."
        n "Gerçekten de bir şey öğrenmemişsin anlaşılan."
        n "Hangi kafayla ümitlenmeye başladıysam ben de."
        label ch23_n_bad_shared:
            n 42c "Bunda açık açık Yuri’nin etkisi var..."
            n "O kadar kolay etkilenecek biri olduğunu fark etmemişim."
            n "Kulüpte bunca zamandır onunla vakit geçirdikten sonra..."
            n "Şimdi de onun gibi yazmaya çalışman..."
            n 1s "Saçmalık."
            n "En azından Monika yazdıklarıma değer veriyor..."
            n 1r "... Of."
            n 1q "Peki... Sanırım şimdi seninle şiirimi paylaşacağım."
            n "Bunu yapmak zorunda olmaktan nefret ediyorum."
            n "Ama maalesef başka seçeneğim yok."
            n 1h "Sadece... iyice, dikkatlice oku, olur mu?"
            n "Ondan sonra gidebilirsin."
            return
    else:

        n "..."
        n 2r "Yok artık."
        n "Baya ciddi bir gerileme bu."
        mc "Ha?"
        n 2c "Önceki iki şiirini çok daha fazla beğenmiştim."
        jump ch23_n_bad_shared

label ch23_n_med:
    if y_gave:
        jump ch23_n_ygave

    if n_poemappeal[0] < 0 and n_poemappeal[1] < 0:
        jump ch23_n_bad
    elif n_poemappeal[1] < 0:
        n "..."
        n 2k "... Bu fena olmamış."
        mc "Fena olmamış mı?"
        n "Aynen, dünküne göre daha iyi en azından."
        label ch23_n_shared:
            n 2c "Yazmayla ne kadar ilgilendiğini hâlâ tam kestiremiyorum ama yine de fena değilsin."
            n 4r "Yuri’den başka kimseyle pek vakit geçirmemene rağmen..."
            n 4h "Hepimizin katıldığı etkinliklerin olması güzel bir şey bence."
            n 4w "O yüzden sıkı çalışmaya devam etsen iyi edersin!"
            n "Yani..."
            n 1h "Başkan ya da Başkan Yardımcısı filan olmadığımı biliyorum ama..."
            n "Bu beni yüzüstü bırakabileceğin anlamına gelmiyor, tamam mı?"
            n 1q "O yüzden, şimdilik benimkini de oku."
            n "Ama yanlış anlaşılma olmasın..."
            n 1h "Bu şiir... benim için çok önemli."
            n "O yüzden iyice, dikkatli oku, olur mu?"
            return
    else:
        n "..."
        n 2k "... Bu fena olmamış."
        mc "Fena olmamış mı?"
        n "Eh, evet."
        n "Dünkü kadar güzel en azından."
        jump ch23_n_shared

label ch23_n_ygave:
    n 1h "Ne?"
    n "Şiirini Yuri’ye mi verdin?"
    n 4x "İğrenç!"
    n "Ne oluyor ikinizin arasında ya?"
    n 1s "Hıh..."
    n "Şiirini okumak istediğim falan yoktu zaten."
    n 1r "Bana göstermeyi düşünmemen canımı sıkıyor sadece."
    n 1x "... Öf."
    n 1q "Peki... Sanırım yine de seninle şiirimi paylaşacağım."
    n "Bunu yapmak zorunda olmaktan nefret ediyorum."
    n "Ama maalesef başka seçeneğim yok."
    n 1h "Sadece... iyice, dikkatlice oku, olur mu?"
    n "Ondan sonra gidebilirsin."
    return

label ch23_n_good:
    jump ch23_n_med

label ch21_y_bad:
    jump ch1_y_bad

label ch21_y_med:
    jump ch1_y_med

label ch21_y_good:
    jump ch1_y_good

label ch22_y_bad:
    jump ch22_y_med

label ch22_y_med:
    y 2b "Ben de bunu bekliyordum..."
    y "Bakalım bugün için neler yazdın."
    y 3m "..."
    "Yuri gülümseyip derin bir nefes alıyor."
    y "Sadece tutması bile güzel."
    mc "?.."
    y 3p "Ah, yani--"
    y "Şiir güzel olmuş!"
    y 3o "Şiir, a..."
    y 2q "... Şey, şiirde geliştirebileceğin bazı şeyler var..."
    y "Ama pek de önemli değil."
    y 2s "Senin yazdığın her şey birer hazine gibi geliyor."
    y 2d "Ahaha..."
    y 2o "Biraz tuhaf bir laf oldu bu..."
    y "D-Devam edelim..."
    y 2t "Bu da benim yazdığım şiir."
    y "Hoşuna gitmesi filan gerekmiyor..."
    return


label ch22_y_good:

    if y_poemappeal[0] < 1:
        y 2b "Ben de bunu bekliyordum..."
        y "Bakalım bugün için neler yazdın."
        y 2e "..."
        y "......"
        "Yuri şiire suratında şaşkın bir ifadeyle bakıyor."
        mc "Hoşuna... gitti mi?"
        y "[player]..."
        y "... Bunu nasıl bu kadar çabuk kavradın?"
        label ch22_y_good_shared:
            y 2v "Daha dün sana denemeye değer olan yöntemlerden söz ediyordum..."
            mc "Belki de ondandır..."
            mc "Anlatırken gerçekten iyi iş çıkardın."
            mc "Daha çok betim yapmayı denemek istedim."
            show yuri 4b zorder 2 at t11
            "Yuri fark edilir bir şekilde yutkunuyor."
            "Elleri bile terli gözüküyor."
            y 4e "A-Ah..."
            y "O kadar mutlu oldum ki..."
            y 3y5 "Bana değer veriliyormuş gibi hissetmek o kadar harika bir his ki [player]!"
            y "Yazdığın her şey benim için birer hazine gibi."
            y 3m "Bunu elimde tutarken bile kalbim güm güm atıyor..."
            y 3q "Ahaha..."
            y "Bu his hakkında bir şiir yazmak istiyorum."
            y 3y6 "Bu kötü bir şey mi [player]?"
            y "Tuhaf davranmıyorum, değil mi?"
            y 3s "H-Her nedense islerimi saklamakta zorluk çekiyorum şu anda..."
            y 3m "Biraz utandım."
            y 3y6 "Ama şimdilik senin de benim şiirimi okumanı istiyorum."
            y 3y5 "Tamam mı?"
            return
    else:

        y 2b "Ben de bunu bekliyordum..."
        y "Bakalım bugün için neler yazdın."
        y 2e "..."
        y "......"
        "Yuri şiire suratında şaşkın bir ifadeyle bakıyor."
        mc "Hoşuna... gitti mi?"
        y "[player]..."
        y 2t "Bu dünküne göre daha da iyi olabilir..."
        y "... Bunu nasıl bu kadar çabuk kavradın?"
        jump ch22_y_good_shared

label ch23_y_bad:
    jump ch23_y_good

label ch23_y_med:
    jump ch23_y_good

label ch23_y_good:
    y 1d "Sonunda..."
    y 3y5 "Ahaha..."
    show yuri 3m
    "Yuri şiirimi yüzüne getirip derin bir iç çekiyor."
    y 3y6 "Bayıldım."
    y "Her bir yönüne bayıldım."
    y 3y5 "[player], bunu eve götürmek istiyorum."
    y "Bende kalmasına izin verir misin?"
    y "Ne olur?"
    mc "Olur, bana fark etmez..."
    y 2y5 "Ahaha."
    y "Bana çok nazik davranıyorsun [player]..."
    y "Senin kadar nazik birini hiç tanımadım."
    y 2y6 "Ölebilirim..."
    y 3y5 "G-Gerçekten değil ama--!"
    y "Nasıl tarif edeceğimi bilmiyorum."
    y "Böyle hissetmemin sakıncası yok, değil mi?"
    show yuri:
        "yuri 3y4"
        0.4
        "yuri 3y6"
    y "Kötü olmamış, değil mi?"
    "Yuri şiirimi göğsüne doğru yaklaştırıyor."
    y 3m "Bunu eve götürüp odamda saklayacağım."
    y "Bunun bende olduğunu düşündüğünde umarım mutlu olursun."
    $ style.say_dialogue = style.normal
    y 3y5 "Bu şiire çok iyi sahip çıkacağım!"
    $ style.say_dialogue = style.edited
    y 3y6 "Bunu tekrar tekrar okurken kendimi elleyeceğim hatta."
    $ _history_list.pop()
    y "Kendimi şiiri yazdığın kâğıtla keseceğim ki cildinden gelen yağların kanıma karışsın."
    $ _history_list.pop()
    y 3y1 "Ahahahahaha."
    $ _history_list.pop()
    $ style.say_dialogue = style.normal
    y 2s "Sen de benim şiirimi alabilirsin."
    y "Zaten okuduktan sonra saklamak isteyeceğini biliyorum."
    y 2y6 "Al hadi. Daha fazla dayanamayacağım."
    y 2y5 "Hadi! Oku!"
    $ y_gave = True
    return


label ch21_m_start:
    m 1b "Merhaba [player]!"
    m "İyi vakit geçiriyor musun?"
    mc "Ah... evet."
    m 1k "Güzel! Bunu duyduğuma sevindim!"
    m 4a "Bu arada, buraya yeni geldiğinden..."
    m "Eğer kulüp için yeni etkinlik gibi ya da yapabileceğimiz daha iyi şeyler konusunda önerilerin varsa..."
    m 4b "Seni istediğin zaman dinlerim!"
    m "Konuşmaktan çekinme, olur mu?"
    show monika 4a
    mc "Peki... Bunu aklımda tutarım."
    "Elbette konuşmaktan çekinirim."
    "Biraz daha ortama alışana kadar uyum sağlasam daha iyi olur."
    m 1a "Neyse..."
    m "Benimle şiirini paylaşmak ister misin?"
    mc "Biraz utanıyorum ama sanırım yapmam gerekiyor."
    m 5a "Ahahaha!"
    m "Merak etmesene [player]!"
    m "Bugün hepimiz biraz utangacız, fark etmedin mi?"
    m "Ama yakında aşmayı öğreneceğimiz bir engel bu da."
    mc "Aynen, haklısın."
    "Monika’ya şiirimi uzatıyorum."
    m 2a "... Mmhm!"
    $ nextscene = "m2_" + poemwinner[0] + "_" + str(eval(poemwinner[0][0] + "_appeal"))
    call expression nextscene

    m 1a "Neyse, şimdi benim şiirimi okumak ister misin?"
    m 1e "Merak etme, pek iyi değilimdir..."
    mc "Pek iyi olmadığını iddia eden birine göre kendine baya güveniyorsun gibi."
    m 1j "Eh... Kendime güveniyormuşum gibi gözükmem gerektiğindendir o."
    m 1b "Ama bu her zaman kendime güvendiğim anlamına gelmez, anlatabiliyor muyum?"
    mc "Anladım..."
    mc "Pekâlâ, haydi okuyalım o zaman."
    return

label ch22_m_start:
    if y_appeal < 2:
        m 1b "Tekrardan selam, [player]!"
        m "Yazma işi nasıl gidiyor?"
        mc "Fena sayılmaz..."
        m 2k "O da güzel."
        m 2b "İşler aksi gitmesin de!"
        m 2a "Bu işe kendini vermene sevindim."
        m "Belki yakında bir şahesere imza atarsın!"
        mc "Ahaha, bundan pek emin değilim..."
        m 2a "Hiçbir zaman bilemezsin ama!"
        m "Bugün yazdıklarını paylaşmak ister misin?"
        mc "Tabi... Al."
        "Şiirimi Monika’ya veriyorum."
        m "..."
        m "... Pekâlâ!"
    $ nextscene = "m2_yuri_" + str(eval("y_appeal"))
    call expression nextscene

    m 1a "Ama neyse..."
    m "Şimdi benim şiirimi okumak ister misin?"
    m "Bu şiirin güzel olduğunu düşünüyorum, umarım sen de öyle düşünürsün~"
    return

label ch23_m_start:
    $ nextscene = "m2_yuri_" + str(eval("y_appeal"))
    call expression nextscene
    if y_appeal < 3:
        m 1a "Neyse..."
        if y_gave:
            m 1m "Sanırım şiirine kafa yormamıza gerek kalmadı..."
            m "Yuri şiirini almadan önce bizimle de paylaşmana izin verseydi keşke."
            m 1r "... Neyse artık."
            m "Eğer o böyle mutluysa, ona engel olmam."
            m 1a "Benimkine gelecek olursak..."
        m 1e "Bu şiir üstünde... çok uğraştım, o yüzden..."
        m "Umarım, a... etkili olur."
        m 1r "Hadi bakalım..."
        $ persistent.seen_colors_poem = True
    return



label m2_natsuki_1:
    m 2b "Güzel olmuş [player]!"
    mc "Öyle mi?.."
    m 2e "Beklediğimden çok daha tatlı olmuş."
    m 2k "Ahahaha!"
    mc "Of ya..."
    m 1b "Yok, hayır!"
    m "Natsuki’nin yazacağı türden bir şeyi andırdı sadece."
    m "Ve o da iyi bir yazardır."
    m 5a "O yüzden bunu iltifat olarak düşün!"
    mc "Ahaha..."
    mc "Öyle diyorsan öyledir."
    m "Aynen!"
    m 3b "Eğer Natsuki’yle ilgileniyorsan, üstünde her zaman atıştırmalık bir şeyler bulundur."
    m "Peşine yavru köpek gibi düşer."
    m 3k "Ahaha!"
    m 1a "Natsuki’nin babası ona yemek parası vermiyor ve evde de ona yemek bırakmadığı için genellikle huysuz oluyor..."
    m "Ama bazen de tüm gücünü kaybedip çöküveriyor."
    m "Az önceki gibi."
    m 2d "Bu sadece bir tahmin ama o kadar küçük olmasının sebebi gıda eksikliğinin ergenlik çağındaki gelişimine engel olması bence..."
    m 2b "... Ama hoş, kimi erkekler de minyon kızlardan hoşlanır, bilirsin ya?"
    m 5a "Affedersin... sadece işin olumlu tarafına bakmaya çalışıyorum!"

    return

label m2_yuri_1:
    m 1a "Harika bir iş çıkarmışsın [player]!"
    m "Okurken içten içe ‘Vay canına’ diyordum."
    m 1j "Gerçekten metaforik bir şiir!"
    m 1a "Neden bilmiyorum ama bu kadar derin bir konu işleyeceğin aklıma gelmezdi."
    m 3b "Sanırım seni hafife almışım!"
    mc "Herkesin beklentilerini düşük tutmak benim işime geliyor."
    mc "Öyle olunca biraz emek verince bile her zaman bir değeri oluyor."
    m 5a "Ahaha! Bak bu hiç de adil değil!"
    m "Gerçi işe de yaradı galiba."
    m 2a "Yuri’nin bu tür konuları sevdiğini biliyorsun, öyle değil mi?"
    m "İmgeler ve sembollerle dolu konular."
    m 2d "Bazen Yuri’nin aklı gerçeklikten tamamen kopukmuş gibi hissediyorum."
    m "Bunu kötü bir şeymiş gibi söylemiyorum tabi."
    m 2a "Ama bazen insanlardan tamamen vazgeçmiş hissine kapılıyorum."
    m "Kendi zihninde o kadar vakit geçiriyor ki orası onun için muhtemelen daha ilginç bir yer hâline gelmiştir..."
    m 2b "Ama asıl bu yüzden ona çok nazik davrandığında o kadar mutlu oluyor."
    m "Öyle şımartılmaya alışkın değil bence."
    m 2j "Sosyal etkileşime epey aç biri olmalı, o yüzden üstüne biraz çok gelirse onu suçlama."
    m 2d "Az önceki gibi..."
    m "Bence fazla şımartılınca kendi içine çekilip yalnız kalmaya zaman arıyor en sonunda."
    "Birden kapı açılıyor."
    m 2b "Yuri!"
    show monika 2a
    show yuri 1s zorder 3 at f31
    y "Geldim..."
    y "Bir şey kaçırdım mı?"
    show yuri zorder 2 at t31
    show monika zorder 3 at f32
    m 2a "Pek sayılmaz..."
    m "Şey, birbirimizle şiirlerimizi paylaşmaya başladık."
    show monika zorder 2 at t32
    show yuri zorder 3 at f31
    y 2t "Ha?"
    y "Şimdiden mi?"
    y 2v "G-Geç kaldığım için özür dilerim..."
    show yuri zorder 2 at t31
    show monika zorder 3 at f32
    m 2j "Özür dilemene gerek yok!"
    m 2a "Hâlâ çok zamanımız var, o yüzden acele etmeyip ihtiyaçlarını giderebilmene daha çok seviniyorum."
    show monika zorder 2 at t32
    show yuri zorder 3 at f31
    y 1s "Pekâlâ..."
    y "Sağ ol Monika."
    y "Gidip şiirimi alsam iyi olur herhâlde."
    show yuri zorder 1 at thide
    hide yuri
    $ y_ranaway = False
    return

label m2_yuri_2:
    m 1i "[player], sanırım az önce görmemen gereken bir şey gördün."
    m "Bunu sana söylemek istemezdim ama başka seçeneğim kalmadı galiba."
    m 1r "Yuri’yle beraber bu kadar vakit geçirmen biraz tehlikeli bir hâl almaya başladı."
    m 1i "Neden bilmiyorum ama senin etrafındayken Yuri çok heyecan yapıyor..."
    m 3d "Ki bu normalde sorun olmamalı."
    m "Ama Yuri fazla heyecanlanınca saklanacak bir yer bulup kendini çakıyla kesmeye başlar."
    m 2e "Bu biraz manyakça değil mi?"
    m "Hatta her gün okula başka bir çakı getiriyor, koleksiyon falan mı yapıyor ne..."
    m 2d "Yani, depresyonda filan olduğundan değil kesinlikle!"
    m "Sanırım bunu yapınca zevk falan alıyor."
    m 2m "Hatta cinsel bir şey bile olabilir..."
    m 1i "Ama asıl olay şu, onun bunu yapmasına sebep oluyorsun."
    m 1d "Senin suçun olduğunu söylemiyorum ama!"
    m 1a "Ama bu yüzden her şeyi sana açıklamam gerekiyordu sanırım..."
    m "Bu sebeple birbirinizin arasına mesafe koymanın onun için daha iyi olacağını düşünüyorum."
    m 5 "Hatta benimle daha fazla vakit geçirmekten çekinme..."
    m "Bunu kibarca söylemem gerekirse, en azından akıl sağlığım yerinde... ve kulüp üyelerime nasıl davranacağımı da biliyorum."
    return

label m2_yuri_3:
    stop music
    m 1i "Seni uyarmadım deme [player]."
    $ skip_poem = True
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
