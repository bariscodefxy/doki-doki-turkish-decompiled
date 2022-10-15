image noface1:
    topleft
    xtile 10 ytile 10
    block:
        block:
            choice:
                "images/sayori/noface1.png"
            choice:
                "images/sayori/noface1b.png"
        block:
            choice:
                0.075
            choice:
                0.3
            choice:
                0.4
            choice:
                0.5
            choice:
                0.6
        repeat
image noface2:
    "images/sayori/noface2.png"
    xalign 0.95 yalign 0.47

label ch23_main:
    if renpy.random.randint(0,15) == 0 and not seen_eyes_this_chapter:
        $ quick_menu = False
        scene white
        show noface1
        show noface2
        with dissolve_scene_half
        play sound "sfx/gnid.ogg"
        pause 7
        $ quick_menu = True
        scene bg club_day2
        show yuri 2 zorder 2 at i11
    else:
        scene bg club_day2
        with dissolve_scene_half

    play music t6
    show yuri 2y5 zorder 2 at t11
    y "Merhaba, [player]!"
    y "Ben de seni bekliyordum."
    y 2d "Okumaya devam etmeye hazır mısın?"
    y "Bugün en iyi çayımı getirdim--"
    show yuri 2f
    show natsuki 4w zorder 3 at f33
    n "Monika!"
    n "Sana demedim mi--"
    n 1g "Iğh..."
    n "Yine mi gecikti ya?"
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y 1h "Her zamanki gibi düşüncesizsin, Natsuki."
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f33
    n 4c "Anlamadım?"
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y 1r "Hep bitmek bilmeyen bağrışlarınla sözümü kesmek zorunda mısın?"
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f33
    n 1o "Sen neden bahsediyorsun?!"
    n 1q "Sanki bunu düzenli olarak yapıyormuşum gibi söylüyorsun."
    n "Dikkat etmemiştim, tamam mı? Özür dilerim."
    n 4u "Cidden... Ne oluyor sana ya son günlerde?"
    if n_appeal >= 2:
        n "Bak..."
        n "Dün hakkında biraz düşündüm."
        n 2q "Kast ettiğimden biraz fazla düşmanca davrandım..."
        n 1q "Sanırım kendimi gerçekten tehdit altında falan hissettim."
        n 1h "Ama bunun birlikte yaptığımız bir şey olduğunu biliyorum."
        n 1q "Yeni bir üye göz çıkarmaz, yeter ki nitelikli olsun..."
        n 5w "Ve sanırım bu sefer başka bir kız gelmesi güzel olur..."
        n 5u "O yüzden..."
        show natsuki zorder 2 at t33
        show yuri zorder 3 at f32
        $ style.say_dialogue = style.normal
        y 2u "Natsuki..."
        $ style.say_dialogue = style.edited
        y 1f "Kimsenin umurunda değilsin."
        y "Neden bir otomat makinesinin altında bozuk para falan aramıyorsun?"
        $ style.say_dialogue = style.normal
        show yuri zorder 2 at t32
        show natsuki zorder 3 at f33
        n 1p "--!"
        n 1r "..."
        n 12f "..."
        show natsuki at thide
        hide natsuki
        pause 1.0
        show monika 1g at l31
        m "Of ya..."
        m "Yine en son gelen benim!"
        show yuri zorder 3 at f32
        y 1f "Yine piyano mu çalışıyordun?"
        show yuri zorder 2 at t32
        show monika zorder 3 at f31
        m 5a "Evet..."
        m "Ahaha..."
        show monika zorder 2 at t31
        show yuri zorder 3 at f32
        y 1m "Çok azimli biri olmalısın."
        y "Bu kulübü kurmak şimdi de piyanoya başlamak..."
        show yuri 1a zorder 2 at t32
        show monika zorder 3 at f31
        m 1a "Tam azim değil belki..."
        m 3a "Ama tutku, sanırım."
        m "Beni festival için çabalamaya da motive ediyor."
    else:
        show natsuki zorder 2 at t33
        show yuri zorder 3 at f32
        y 2n "Ben mi?"
        y 2o "B-Boş ver..."
        show yuri zorder 2 at t32
        show natsuki zorder 3 at f33
        n "..."
        show natsuki zorder 2 at t33
        show yuri zorder 3 at f32
        y 2v "O kadar kötü mü gerçekten?.."
        show yuri zorder 2 at t32
        show natsuki zorder 3 at f33
        n 2m "İşte, bu bir {i}sorun{/i}."
        show natsuki zorder 2 at t33
        show yuri zorder 3 at f32
        y 3p "Bunu çözeceğim!"
        y 3y6 "Öyle kayda değer bir şey bile değil..."
        y 3o "Sadece şu sıralar kendimi biraz asabi hissediyorum..."
        y 3n "H-Her neyse, bundan bahsetmeye gerek yok!"
        show yuri zorder 2 at t32
        show natsuki zorder 3 at f33
        n 2q "Şey, sadece bunu söyleme gereği duydum."
        n 5q "Öyle çok umurumda olduğundan falan değil..."
        show natsuki zorder 2 at t33
        show yuri 3e
        show monika 1g at l31
        m "Of ya..."
        m "Yine en son gelen benim!"
        show natsuki zorder 3 at f33
        n 2c "Olsun, [player] da yeni geldi."
        show natsuki zorder 2 at t33
        show yuri zorder 3 at f32
        y 1f "Yine piyano mu çalışıyordun?"
        show yuri zorder 2 at t32
        show monika zorder 3 at f31
        m 5a "Evet..."
        m "Ahaha..."
        show monika zorder 2 at t31
        show yuri zorder 3 at f32
        y 1m "Çok azimli biri olmalısın."
        y "Bu kulübü kurmak şimdi de piyanoya başlamak..."
        show yuri 1a zorder 2 at t32
        show monika zorder 3 at f31
        m 1a "Tam azim değil belki..."
        m 3a "Ama tutku, sanırım."
        m "Beni festival için çabalamaya motive ediyor ve...."
        m 3n "A..."
        show monika zorder 2 at t31
        show natsuki zorder 3 at f33
        n 5s "..."
        show natsuki zorder 2 at t33
        show monika zorder 3 at f31
        m 1l "Şey..."
        m "U-Unuttum..."
        show monika zorder 1 at thide
        hide monika
        show yuri zorder 3 at f32
        y 2v "Şey, o konuda, Natsuki..."
        y "Hepimiz dün konuşuyorduk da..."
        y 2t "A... Biz de festivali desteklemek isteyeceğimize karar verdik."
        y 2l "Ancak!.."
        y 2h "Kulübün değişmesini istememeni anlıyorum."
        y "Bence hepimiz bir bakıma öyle düşünüyoruz."
        y 2f "Birlikte çalıştığımız sürece bu kulüp asla istemediğimiz bir şeye dönüşmeyecek."
        show yuri zorder 2 at t32
        show natsuki zorder 3 at f33
        n "..."
        show natsuki zorder 2 at t33
        show yuri zorder 3 at f32
        y 2v "A, bir de..."
        y "Festival konusunda bize yardım edersen..."
        y 3r "... Sana yeni bir manga alırım!"
        show yuri 3t zorder 2 at t32
        show natsuki zorder 3 at f33
        n 5h "..."
        n 2z "Ahahaha!"
        n "Pardon, o son kısım çok komikti."
        n 2c "Bak..."
        n "Dün hakkında biraz düşündüm."
        n 2q "Kast ettiğimden biraz fazla düşmanca davrandım..."
        n 1q "Sanırım kendimi gerçekten tehdit altında falan hissettim."
        n 1h "Ama bunun birlikte yaptığımız bir şey olduğunu biliyorum."
        n 1q "Yeni bir üye göz çıkarmaz, yeter ki nitelikli olsun..."
        n 5w "Ve sanırım bu sefer başka bir kız gelmesi güzel olur..."
        n 5e "... Daha önemlisi, ben mızıkçılık yaptım diye bir etkinliğin kötü geçtiğini görmeyi hiç istemem!"
        n "Ben bir profesyonelim yahu!"
        n 5c "O yüzden, ben de yardım edeceğim ve adamakıllı bir iş yapacağız."
        show natsuki zorder 2 at t33
        show yuri zorder 3 at f32
        y 2s "Şükürler olsun..."
        y "Bu harika değil mi, Monika?"
        show yuri zorder 2 at t32
        show natsuki zorder 3 at f33
        n 2k "... Monika?"
        show natsuki zorder 2 at t33
        show monika 1o zorder 3 at f31
        m "Ah--"
        m 1n "Evet, harika!"
        m "Sen olmadan hiçbir şey aynı olmaz, Natsuki."
    m 5 "Neyse, [player]..."
    m "Bugün ne yapmak istiyorsun?"
    m "Düşünmüştüm de, birlikte--"
    show monika zorder 2 at t31
    show yuri zorder 3 at f32
    y 1l "Bugün için plan yapmıştık zaten."
    show yuri zorder 2 at t32
    show monika zorder 3 at f31
    m 1r "Ah..."
    m "Öyle mi, Yuri?"
    show monika zorder 2 at t31
    show yuri zorder 3 at f32
    y 1y6 "Evet, öyle."
    y "[player] birlikte okuduğumuz romana kendini kaptırdı bile."
    y 1y5 "Onu edebiyata başlattığım için mutlu değil misin, Monika?"
    show yuri 1a zorder 2 at t32
    show monika zorder 3 at f31
    m 2l "Sa..."
    m "Sanırım öyleyim..."
    m "Ben sadece--"
    m 1r "Aslında bir önemi yok."
    m 1i "Gerçekten yok."
    m "Canınız ne istiyorsa yapabilirsiniz."
    show monika zorder 2 at t31
    show yuri zorder 3 at hf32
    y 2y1 "{i}(Evet!){/i}{w=0.5}{nw}"
    y 2u "Şey... Anlayışın için teşekkürler, Monika."
    if poemwinner[2] == "natsuki":
        $ poemwinner[2] = "yuri"
        $ y_appeal += 1

    scene bg club_day2
    show yuri 3 zorder 2 at t11
    with wipeleft_scene
    call yuri_exclusive2_2_ch22

    return



label ch23_end:
    stop music fadeout 1.0
    scene black
    with wipeleft_scene
    call screen confirm("", Return(True), Return(True))
    if _return:
        call expression "poem_special_" + str(persistent.special_poems[2])
        scene black with Dissolve(1.0)
    else:
        pass
    scene bg club_day2
    show monika 4b zorder 2 at t32
    with wipeleft_scene
    play music t3
    m "Pekâlâ, millet!"
    m "Festival hazırlıklarını kararlaştırma zamanı."
    m 1i "Acele edip bitirelim şu işi."
    if n_appeal >= 2:
        show natsuki 4q zorder 3 at f31
        n "..."
    else:
        show natsuki 4q zorder 3 at f31
        n "Of..."
        n "Bugün ortamın havası neden tuhaf?"
        n "Yuri bile etkilenmiş."
    show natsuki zorder 2 at t31
    show yuri 4b zorder 3 at f33
    y "Uu..."
    y "Durgunluk, kötü bir şeyin olmak üzere olduğunun habercisi olarak görülür..."
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m 2r "Neyse, şunu bitirebilir miyiz?"
    m 2d "Ben şiir broşürlerini yazdırıp toplayacağım."
    if n_appeal >= 2:
        m 2i "Natsuki, sen kapkek yapabilirsin."
        m "En azından bu konuda iyi olduğunu biliyorum."
        show monika zorder 2 at t32
        show natsuki zorder 3 at f31
        n 5u "..."
        show natsuki zorder 2 at t31
        show monika zorder 3 at f32
    else:
        m "Natsuki, düşünüyordum da--"
        show monika zorder 2 at t32
        show natsuki zorder 3 at f31
        n 2d "Kapkek yapmak istiyorum!"
        show natsuki 2a zorder 2 at t31
        show monika zorder 3 at f32
        m 2a "... Evet, o."
        m "Aynı fikirde olduğumuza sevindim."
    m 1m "Yuri, sen..."
    m 1r "... Şey, neyse."
    m 1i "Yardımı olacağını düşündüğün ne varsa onu yapabilirsin."
    show monika zorder 2 at t32
    show yuri zorder 3 at f33
    y 2h "Monika..."
    y "Bilgin olsun, ben işe yaramaz değilim!"
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m 2p "Bu-Bunu biliyorum!"
    show monika zorder 2 at t32
    show yuri zorder 3 at f33
    y 1l "Ne yapmak isteyeceğimi biliyorum zaten."
    y 1h "Doğru atmosferi oluşturmadan başarılı bir şiir etkinliği düzenleyemeyiz."
    y "O yüzden dekorasyonlar ve ortama uygun aydınlatmalar hazırlayacağım."
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m 2j "İşte, gördün mü?"
    m "Bu harika bir fikir!"
    m 1a "Hepimizin ne yapacağı belli oldu."
    show monika zorder 2 at t32
    show yuri zorder 3 at f33
    y 2f "Ha?"
    y "Ya [player] ne yapacak?"
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m 2b "[player] bana yardım edecek."
    show monika 2a zorder 2 at t32
    show natsuki zorder 3 at f31
    n 4e "Bir dakika, sana mı?"
    n "En kolayı senin görevin, Monika!"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 1i "Kusura bakma ama böyle olacak işte."
    show monika zorder 2 at t32
    show natsuki zorder 3 at f31
    n 1f "Bu ne be?!"
    n "Neyin peşindesin sen?"
    show natsuki zorder 2 at t31
    show yuri zorder 3 at f33
    y 3h "N-Natsuki’ye katılıyorum!"
    y "Senin görevin için bir kişi bir hayli yeterli zaten..."
    y 3l "Benim görevim bir çift ele daha ihtiyaç duyulacak kadar zahmetli."
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f31
    n 4c "Benimki de!"
    show natsuki zorder 2 at t31
    show yuri zorder 3 at f33
    y 1h "Ne, kapkeklerin mi?"
    y "Lütfen."
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f31
    n 1o "{i}Sen{/i} ne anlarsın ki, sikik?!"
    n 1x "Tek umurunda olan [player] ile aptal kitaplarına dalmak."
    n 1f "Monika için de {i}aynısı{/i} geçerli!"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 2g "Hey!"
    m "Ben bir şey yapmadım bile!"
    show monika zorder 2 at t32
    show natsuki zorder 3 at f31
    n 3e "Tamam, yetkini suistimal edeceğine bırak da [player] kime yardım edeceğine kendisi karar versin o zaman."
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 1p "Ben... Yetkimi suistimal etmiyorum."
    show monika zorder 2 at t32
    show yuri zorder 3 at f33
    y 2h "Ediyorsun, Monika."
    y "Bırak da [player] seçimini yapsın, tamam mı?"
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m 1r "Peki, tamam!"
    m "Tamam."
    show monika 1h zorder 2 at t32
    show natsuki zorder 3 at f31
    n 3w "Of..."
    n "[player], bu ikisinden artık bıktığını biliyorum."
    n 3c "Birlikte--"
    show natsuki zorder 2 at t31
    show yuri zorder 3 at f33
    y 2r "Natsuki, çeneni kapat da kendisi karar versin lan."
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f31
    n 1o "{i}Sen{/i} çeneni kapat!"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 1r "Tanrı aşkına..."
    m 1i "Bu hiç bitmeyecek. Seçimi yap gitsin, tamam mı?"
    show monika zorder 2 at t32
    python:
        madechoice = renpy.display_menu([("Natsuki.", "natsuki"), ("Yuri.", "yuri"), ("Monika.", "monika")], screen="rigged_choice")

    if madechoice != "monika":
        window hide(None)
        $ musicpos = get_pos()
        stop music
        scene white
        show yuripupils zorder 10
        pause 3.0
        show bg club_day:
            alpha 0.05
            yoffset 0 ytile 2
            linear 5.25 yoffset -720
            repeat
        show noise:
            alpha 0.1
        $ gtext = glitchtext(80)
        window auto
        menu:
            "[gtext]"
            "Monika":
                pass
            "Monika":
                pass
            "Monika":
                pass
            "Monika":
                pass
            "Monika":
                pass
            "Monika":
                pass
            "Monika":
                pass
            "Monika":
                pass
            "Monika":
                pass
            "Monika":
                pass
        scene bg club_day
        $ audio.t3m = "<from " + str(musicpos) + " loop 4.618>bgm/3.ogg"
        play music t3m
        show monika 5 at i11
    else:
        show natsuki zorder 1 at thide
        show yuri zorder 1 at thide
        hide natsuki
        hide yuri

    m 5a "Oley, beni seçtin!"
    m "Hafta sonu senin evinde buluşabiliriz."
    m "Eğlenceli olacağına söz veriyorum."
    m "Pazar günü sana uygun mu?"
    show natsuki 1e zorder 3 at f31
    n "Şaka mı yapıyorsun ulan?"
    n "Bu hiç de adil değil!"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 2i "Adil, Natsuki."
    m "Bunu o seçti."
    show monika zorder 2 at t32
    show yuri 3r zorder 3 at f33
    y "Hayır, adil değil!"
    y "Bize bu işleri yükleyip onu kendine saklıyorsun."
    y "Bu çok adice!"
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m 2r "Yuri, ben sana görev vermedim bile."
    m 2i "Buna sen karar verdin."
    m "Mantıksızca davranıyorsun."
    stop music
    show monika zorder 2 at t32
    show yuri zorder 3 at f33
    y 2y4 "Ben mi mantıksızca davranıyorum?"
    y 2y3 "Ahahaha!"
    y "Monika, ne kadar kuruntulu ve kendini beğenmiş biri olduğuna inanamıyorum!"
    y "Her seferinde seninle alakası olmayan bir şeyde onu elimden alıyorsun."
    y 1y1 "Kıskanıyor musun?"
    y "Deli misin?"
    y 1y3 "Veya belki de kendinden o kadar nefret ediyorsun ki öcünü başkalarından alıyorsun."
    y 1y4 "Al sana bir tavsiye. Hiç kendini öldürmeyi düşündün mü?"
    y "Akıl sağlığın için birebir."
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f31
    n 5u "Yuri, beni biraz korkutuyorsun..."
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 1r "Natsuki, gidelim biz."
    m 1i "Bizi şu an burada istediğini sanmıyorum."
    show monika zorder 2 at t32
    show yuri zorder 3 at f33
    y 2y3 "İşte, çok zor değilmiş."
    y "Tek istediğim biraz onunla vakit geçirmek."
    y "Çok mu görüyorsunuz bunu?"
    hide natsuki
    hide monika
    hide yuri
    with wipeleft
    "Yuri, Monika ve Natsuki’yi kapıya kadar geçiriyor."
    show monika 5a zorder 2 at t11
    m "Hey, [player]..."
    m "Yuri bir âlem, değil mi?"
    show monika zorder 1 at thide
    hide monika
    "Monika, Yuri onu kapıdan dışarı iterken kıkırdıyor."
    python:
        try: renpy.file(config.basedir + "/iyi hafta sonları dilerim!")
        except: open(config.basedir + "/iyi hafta sonları dilerim!", "w").write("C2DtHPVyxU9xcqU6HJ5nlE4hGQRibHNafENhxWMtQZNhxWNvQAXRsHViirJ2MSMzZFEMfcHnyTYzVGCtcuwtp2lfiTJ2SAOnKkPvuEaFy2tvQZZubHNslZMta2QaZE4zGJPPaYZalTzPaXhXapSqfMNnfYErGntljJV5KE4hiP5hLW4rjnDdiKIri2l/")
        try: os.remove(config.basedir + "/mxtlx duxunceler.png")
        except: pass
        try: os.remove(config.basedir + "/Beni duyabiliyor musun.txt")
        except: pass
        try: os.remove(config.basedir + "/iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.txt")
        except: pass

    play music t10y
    show yuri 2m zorder 2 at t11
    y "Sonunda."
    y 2y1 "Sonunda!"
    y 2s "Gerçekten tüm istediğim bu."
    y 1y6 "[player], hafta sonunu Monika’yla geçirmene gerek yok."
    y "Onu dinleme."
    y 1y5 "Onun yerine benim evime gel."
    y 3y5 "Bütün gün, ikimiz baş başa..."
    y "Kulağa harika gelmiyor mu?"
    y 3y1 "Ahahaha!"
    y 3y4 "Vay canına... Cidden bir sorunum var, değil mi?"
    y "Ama var ya..."
    y 1y3 "Artık umurumda değil."
    y "Hayatım boyunca hiç bu kadar iyi hissetmemiştim."
    y 1y4 "Sadece seninle birlikte olmak bile bana hayal edebileceğimden çok daha büyük bir zevk veriyor."
    y "Sana bağımlıyım."
    y 3y4 "Seninle aynı havayı solumazsam ölecekmişim gibi hissediyorum."
    y 4a "Seni bu kadar önemseyen birinin olması iyi hissettirmiyor mu?"
    y "Tüm hayatının senin çevrende dönmesini isteyen birinin olması?"
    y 2y6 "Ama iyi hissettiriyorsa..."
    y 2y4 "O hâlde neden gitgide korkunç bir şey olacakmış gibi hissediyorum?"
    y 2y6 "Belki de bu yüzden ilk başta kendimi durdurdum..."
    y "Ama duygu şu an çok güçlü."
    y 3y1 "Artık umursamıyorum, [player]!"
    y "Sana söylemeliyim!"
    y 3y4 "Sana... Sana deliler gibi aşığım!"
    y "Sanki vücudumun her parçası... İçimdeki her damla kan... Senin ismini haykırıyor."
    y 3y3 "Artık sonuçlar umurumda değil!"
    y "Monika’nın dinleyip dinlemediği umurumda değil!"
    y 3w "Lütfen, [player], seni ne kadar sevdiğimin farkında ol yeter."
    y 3m "Seni o kadar çok seviyorum ki senden çaldığım kalemle kendimi tatmin ediyorum."
    y 3y4 "Sadece derini yüzüp içine kıvrılmak istiyorum."
    y 3y6 "Seni sadece kendime istiyorum."
    y "Ve ben de sadece senin olacağım."
    y "Sence de bu kulağa mükemmel gelmiyor mu?"
    y 3s "Söyle, [player]."
    y "Sevgilim olmak istediğini söyle."
    y "İtirafımı kabul ediyor musun?"

    menu:
        "Evet.":
            jump yuri_kill
        "Hayır.":
            jump yuri_kill

label yuri_kill:
    $ quick_menu = False
    window hide(None)
    stop music
    pause 1.0


    window auto
    $ persistent.yuri_kill = 1
    $ in_yuri_kill = True
label yuri_kill_1:
    window auto
    $ persistent.autoload = "yuri_kill_1"
    $ quick_menu = False
    stop music
    scene bg club_day
    show yuri 3d at i11
    y "... Ahahaha."
    y "Ahahahahahaha!"
    $ style.say_dialogue = style.normal
    y 3y5 "Ahahahahahahahaha!"
    $ style.say_dialogue = style.edited
    y 3y3 "AHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA{nw}"
    window hide(None)
    window auto
    $ style.say_dialogue = style.normal

    play sound "sfx/yuri-kill.ogg"
    pause 1.43
    show yuri stab_1
    pause 0.75
    show yuri stab_2
    show blood:
        pos (610,485)
    pause 1.25
    show yuri stab_3
    pause 0.75
    show yuri stab_2
    show blood:
        pos (610,485)
    show yuri stab_4 with ImageDissolve("images/yuri/stab/4_wipe.png", 0.25)
    pause 1.25
    show yuri stab_5
    pause 0.70
    show yuri stab_6:
        2.55
        easeout_cubic 0.5 yoffset 300
    show blood as blood2:
        pos (635,335)
    pause 2.55
    hide blood
    hide blood2
    pause 0.25
    play sound fall
    pause 0.25
    scene black
    pause 2.0

    scene black
    show y_kill
    with dissolve_cg
label yuri_kill_2:
    $ quick_menu = True
    $ persistent.autoload = "yuri_kill_2"
    python:
        _history_list = []
        m.add_history(None, "", """Edebiyat Kulübü’ne hoş geldin! Sevdiğim şeylerden özel şeyler yaratmak hep hayalim olmuştur. Artık kulübün bir üyesi olduğuna göre, bu şirin oyunda hayalimi gerçekleştirmemde bana yardımcı olabilirsin!Günler sohbet ve eğlenceli aktivitelerle geçiyor şirin ve eşsiz kulüp üyelerimle birlikte:Sayori, her şeyden evvel mutluluğa önem veren, her yere ışık saçan çocuksu kişilik;Natsuki, şirin görünümüne rağmen bir o kadar da eli sert olan kız;Yuri, rahatı kitapların dünyasında bulan çekingen ve gizemli kişi;... Ve, elbette, Monika, kulübün lideri! O ben oluyorum!Herkesle arkadaşlık kurman ve Edebiyat Kulübü’nün üyelerim için daha samimi bir yer olmasına yardım etmen konusunda çok heyecanlıyım. Şimdiden senin tatlı bir insan olduğunu anlayabiliyorum. En çok benimle zaman geçireceğine söz verir misin?Edebiyat Kulübü’ne hoş geldin! Sevdiğim şeylerden özel şeyler yaratmak hep hayalim olmuştur. Artık kulübün bir üyesi olduğuna göre, bu şirin oyunda hayalimi gerçekleştirmemde bana yardımcı olabilirsin!Günler sohbet ve eğlenceli aktivitelerle geçiyor şirin ve eşsiz kulüp üyelerimle birlikte:Sayori, her şeyden evvel mutluluğa önem veren, her yere ışık saçan çocuksu kişilik;Natsuki, şirin görünümüne rağmen bir o kadar da eli sert olan kız;Yuri, rahatı kitapların dünyasında bulan çekingen ve gizemli kişi;... Ve, elbette, Monika, kulübün lideri! O ben oluyorum!Herkesle arkadaşlık kurman ve Edebiyat Kulübü’nün üyelerim için daha samimi bir yer olmasına yardım etmen konusunda çok heyecanlıyım. Şimdiden senin tatlı bir insan olduğunu anlayabiliyorum. En çok benimle zaman geçireceğine söz verir misin?Edebiyat Kulübü’ne hoş geldin! Sevdiğim şeylerden özel şeyler yaratmak hep hayalim olmuştur. Artık kulübün bir üyesi olduğuna göre, bu şirin oyunda hayalimi gerçekleştirmemde bana yardımcı olabilirsin!Günler sohbet ve eğlenceli aktivitelerle geçiyor şirin ve eşsiz kulüp üyelerimle birlikte:Sayori, her şeyden evvel mutluluğa önem veren, her yere ışık saçan çocuksu kişilik;Natsuki, şirin görünümüne rağmen bir o kadar da eli sert olan kız;Yuri, rahatı kitapların dünyasında bulan çekingen ve gizemli kişi;... Ve, elbette, Monika, kulübün lideri! O ben oluyorum!Herkesle arkadaşlık kurman ve Edebiyat Kulübü’nün üyelerim için daha samimi bir yer olmasına yardım etmen konusunda çok heyecanlıyım. Şimdiden senin tatlı bir insan olduğunu anlayabiliyorum. En çok benimle zaman geçireceğine söz verir misin?En çok benimle zaman geçireceğine söz verir misin?En çok benimle zaman geçireceğine söz verir misin?En çok benimle zaman geçireceğine söz verir misin?En çok benimle zaman geçireceğine söz verir misin?En çok benimle zaman geçireceğine söz verir misin?En çok benimle zaman geçireceğine söz verir misin?En çok benimle zaman geçireceğine söz verir misin?En çok benimle zaman geçireceğine söz verir misin?En çok benimle zaman geçireceğine söz verir misin?En çok benimle zaman geçireceğine söz verir misin?En çok benimle zaman geçireceğine söz verir misin?En çok benimle zaman geçireceğine söz verir misin?En çok benimle zaman geçireceğine söz verir""")

    $ style.say_dialogue = style.edited
    scene black
    window show(None)
    if not renpy.music.get_playing(channel='music') == audio.t6s:
        $ audiostart = str(renpy.random.random() * 360)
        $ audio.t6s = "<from " + audiostart + " loop 43.572>bgm/6s.ogg"
        play music t6s
    show y_kill
    label yuri_kill_loop:
        $ persistent.yuri_kill += 1
        if persistent.yuri_kill < 1440:
            $ gtext = glitchtext(renpy.random.randint(8, 80))
            if config.developer:
                y "[persistent.yuri_kill] [gtext]"
            else:
                y "[gtext]"
            $ _history_list.pop()
            jump yuri_kill_loop
        else:
            $ delete_all_saves()
            jump yuri_kill_3

label yuri_kill_3:
    python:
        try: os.remove(config.basedir + "/iyi hafta sonları dilerim!")
        except: pass
    $ persistent.autoload = "yuri_kill_3"
    $ config.skipping = False
    $ config.allow_skipping = False
    $ allow_skipping = False
    $ quick_menu = False
    $ style.say_dialogue = style.normal
    $ gtext = glitchtext(renpy.random.randint(8, 80))
    if not renpy.music.get_playing(channel='music') == audio.t6s:
        $ audiostart = str(renpy.random.random() * 360)
        $ audio.t6s = "<from " + audiostart + " loop 43.572>bgm/6s.ogg"
        play music t6s
    scene bg club_day
    "[gtext]"
    window auto
    n "Pekâlâ, festival zamanı!"
    show natsuki 4k zorder 2 at t11
    n "Vay canına, benden erken mi geldin?"
    n "Ben de en erken ben ge--{nw}"
    show natsuki scream at h11
    n "İYAH!"
    n "AAAAAAAAAAAAAAAHHHH!!!"
    pause 1.0
    show natsuki scream at h11
    pause 0.75
    show natsuki vomit at h11
    pause 1.25
    show natsuki at lhide
    hide natsuki
    "Natsuki kaçıyor."
    m "..."
    show monika 2b zorder 2 at t11
    m "Ben geldim!"
    m 2d "[player], bir şey mi oldu?"
    m "Natsuki az önce kaçıp gitti..."
    m 2i "... A..."
    m "... Ah."
    m 2r "..."
    m 2l "Ahahaha!"
    m "Eh, yazık olmuş."
    m 2d "Dur biraz, bütün hafta sonu burada mıydın, [player]?"
    m "Of, şu işe bak..."
    m 2g "Senaryonun bu kadar bozulmuş olduğunun farkına varmadım."
    m "Çok üzgünüm!"
    m "Çok sıkıcı olmuş olmalı..."
    m 2e "Bunu telafi edeceğim, tamam mı?"
    m "Bana bi’ saniye ver..."
    $ consolehistory = []
    call updateconsole ("os.remove(\"characters/yuri.chr\")", "yuri.chr başarıyla silindi.")
    $ delete_character("yuri")
    pause 1.0
    call updateconsole ("os.remove(\"characters/natsuki.chr\")", "natsuki.chr başarıyla silindi.")
    $ delete_character("natsuki")
    pause 1.0
    m 2a "Neredeyse bitti."
    m 2j "Önce hemen bir kapkek yemek istiyorum sadece!"
    $ gtext = glitchtext(10)
    "Monika, [gtext]’nin tepsisindeki folyoyu kaldırıp bir kapkek alıyor."
    m 2b "Cidden, bunlar en iyisi!"
    m "Gerçekten bir tane yemeliydim, çünkü başka şansım olmayacaktı."
    m 2a "Varlıkları silinecek falan ya hani."
    m "... Ama neyse, seni daha fazla bekletmemem gerekiyor."
    m 2j "Biraz sık dişini, tamam mı?"
    m 2a "Bu sadece bir saniye sürecek."

    show screen tear(8, offtimeMult=1, ontimeMult=10)
    pause 1.5

    $ delete_all_saves()
    $ persistent.playthrough = 3
    $ persistent.anticheat = renpy.random.randint(100000, 999999)
    $ persistent.autoload = "ch30_main"
    $ renpy.full_restart(transition=None, label="splashscreen")

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
