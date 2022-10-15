label ch21_main:
    scene bg club_day2
    with dissolve_scene_half
    play music t2g3
    show monika 5 zorder 2 at t11
    show layer master:
        subpixel True
        truecenter
        linear 240 rotate 8 zoom 1.30
    m "Merhaba, [player]!"
    m "Bizi bırakıp kaçmadığına sevindim. Hahaha!"
    mc "Yok canım, olur mu öyle şey?"
    mc "Bu olay bana biraz tuhaf gelse de en azından verdiğim sözü tutarım."
    show monika zorder 1 at thide
    hide monika
    "Tekrar Edebiyat Kulübü’ne geldim."
    "En son gelen bendim; herkes birbiriyle kaynaşmaya başlamıştı bile."
    show yuri glitch2 zorder 2 at t32
    y "Sözünü tuttuğun için teşekkür ederim [player]."
    y 1a "Umarım bu senin için fazla ağır bir sorumluluk olmaz."
    y 1u "Alışkın değilken edebiyata bir anda giriş yapmak yani..."
    show natsuki glitch1 zorder 2 at i33
    n "Hadi ama! Sanki bi’ alışma sürecini falan hak ediyor da."
    n 4e "Seni buraya Monika getirdi zaten."
    n "Buraya sadece öylesine takılmaya mı gelmeyi planlıyorsun bilmiyorum ama..."
    n "Bizi ciddiye almazsan sonuçlarına katlanırsın."
    show monika 2b onlayer front at l41
    m "Natsuki, manga koleksiyonunu kulüp odasında saklayan birine göre fazla büyük konuşuyorsun."
    n 4o "M-M-M...!!"
    show monika onlayer front at lhide
    hide monika onlayer front
    "Natsuki “Monika” ve “Manga” kelimeleri arasında takılı kalıyor."
    show natsuki at h33
    n 1v "Manga edebiyattır!!"
    show natsuki zorder 1 at thide
    hide natsuki
    "Bozguna uğrayan Natsuki sırasına geri dönüyor."
    show yuri 2s zorder 2 at t11
    y "Üzgünüm, [player]..."
    y "Senin rahatına öncelik vereceğiz, tamam mı?"
    show yuri 2g
    "Yuri, Natsuki’ye hayal kırıklığına uğramışçasına bakıyor."
    y 1a "Şey, neyse..."
    y "Şimdi kulübe katıldığına göre..."
    y "... Belki bir kitap seçip okumaya başlamak istersin?"
    mc "Şey..."
    mc "Her hâlükârda hayır diyemem."
    mc "Dediğin gibi, artık bu kulübün bir üyesiyim."
    mc "O yüzden, bana sorarsan böyle bir şeyi yapmam en doğrusu olur."
    y 4b "D-Dur..."
    y "Öyle demek istemedim!"
    y "Uu..."
    y "Eğer bunu yapmayı sahiden istemiyorsan dediklerimi unut gitsin..."
    mc "A--Hayır, öyle değil, Yuri."
    mc "Bu kulübün bir parçası olmayı denemek istiyorum."
    mc "Çok okuyan biri olmasam da, benden istersen, seve seve bir kitabı okumaya başlarım."
    y 3t "E-Emin misin?.."
    y "Sadece..."
    y 3u "... Şey, Başkan Yardımcısı falan olduğumdan..."
    y "... Sevebileceğin bir şeye başlamana yardımcı olmalıymışım gibi geldi."
    "Yuri çantasını karıştırıp içinden bir kitap çıkarıyor."
    y 1s "Dışlanmış hissetmeni istemedim..."
    y "O yüzden seveceğini düşündüğüm bir kitap getirdim."
    y "Kısa bir kitap. O yüzden, çok okuyan birisi olmasan da ilgini çekebilir."
    y "Ve, şey..."
    show yuri at sink
    y 4b "Birlikte kitap hakkında konuşabiliriz... Eğer istersen tabii..."
    "B-Bu..."
    "Bu kız istemeden nasıl bu kadar tatlı olabiliyor?"
    "Çok okumamama rağmen beğeneceğimi düşündüğü bir kitap bile getirmiş..."
    mc "Teşekkür ederim Yuri, kesinlikle okuyacağım!"
    "Kitabı hevesle alıyorum."
    show yuri 2m zorder 2 at t11
    y "Hüff..."
    y 2a "Kitabı kendine uygun bir tempoda okuyabilirsin."
    y "Ne düşündüğünü duymayı dört gözle bekliyorum."
    show yuri zorder 1 at thide
    hide yuri
    show layer master


    "Herkes gelip yerleştiğine göre Monika’nın kulüp için belirlediği aktiviteleri başlatmasını beklemiştim."
    "Ama durum öyle olmayacak gibi."
    "Yuri çoktan kafasını bir kitaba gömmüş."
    "Yüzündeki gergin yüz ifadesini istemsizce fark ediyorum. Yuri sanki bu anı bekliyormuş gibiydi."
    "Bu sırada da Natsuki dolabı karıştırıyor."


    $ nextscene = poemwinner[0] + "_exclusive2_" + str(eval(poemwinner[0][0] + "_appeal"))
    call expression nextscene

    return

label ch21_end:
    stop music fadeout 1.0
    scene bg club_day2
    with wipeleft_scene
    play music t3g
    queue music t3g2
    mc "Püf..."
    "Sanırım herkesle şiirimi paylaştım."
    "Odaya bakınıyorum."
    "Düşündüğümden daha da stresli geçti."
    "Sanki herkes vasat yazma tarzımla beni yargılıyordu..."
    "İyi davranıyor olsalar da, şiirlerimin onlarınkiyle aşık atmasının imkânı yok."
    "Burası bir edebiyat kulübü ne de olsa."
    "İç çekiyorum."
    "Böyle bir şeye kalkışırsam olacağı bu."
    "Odanın karşısında Monika defterine bir şey yazıyor."
    "Gözlerim Yuri ve Natsuki’ye takılıyor."
    show yuri 2g zorder 2 at t21
    show natsuki 1g zorder 2 at t22
    "Birbirleriyle dikkatlice şiirlerini değişip paylaşıyorlar."
    show yuri 2i zorder 2 at t21
    "Birbirlerinin şiirini okurken yüz ifadelerinin değişimini izliyorum."
    "Natsuki’nin alnı sinirden kırışıyor."
    "Bu sırada Yuri de üzgün üzgün gülümsüyor."
    show natsuki zorder 3 at f22
    n 1q "{i}(Bu nasıl bir dil böyle ya?..){/i}"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 2f "Ha?"
    y "Şey... Bir şey mi dedin?"
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 2c "A, yok, demedim."
    "Natsuki şiiri tek eliyle önemsemez bir tavırla masaya bırakıyor."
    n "Sanırım süslü olduğu söylenebilir."
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 2i "A-- Teşekkürler..."
    y "Seninki de... tatlı..."
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 2h "Tatlı mı?"
    n 1h "Şiirdeki sembolizmi hiç mi anlamadın?"
    n "Pes etme hissi hakkında olduğu apaçık ortada."
    n "Bunun neresi tatlı?"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 3f "B-Biliyorum!"
    y "Demek istediğim..."
    y 3h "Kullandığın dil yüzünden sanırım..."
    y "İyi bir şey söylemeye çalışıyordum..."
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n "Ha?"
    n 4w "Yani iyi bir şey söylemek için bu kadar fazla düşünmen mi gerekiyor?"
    n "Teşekkürler ama hiç de iyi bir şey çıkmadı ağzından!"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 1i "Şey..."
    y "Şey, bazı önerilerim var doğrusu..."
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 5x "Hıh."
    n "Öneri duymak istesem şiirimi gerçekten beğenen birinden isterdim."
    n "Ki, beğenenler {i}cidden{/i} oldu."
    n 5e "Monika beğendi."
    n "[player] desen, o da beğendi!"
    n "Buna dayanarak sana zevkle önerilerimi sunabilirim."
    n "Öncelikle--"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 2l "Affedersin..."
    y "Teklifin için teşekkür ederim ama yazım tarzımı oturtmak için uzun zaman boyunca çabaladım."
    y 2h "Beklenmedik derecede ilham verici olan bir şeyle karşılaşmadığım sürece de değiştirmeyi düşünmüyorum."
    y "Ki, henüz öyle bir şeyle de karşılaşmadım."
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 1o "Nn!.."
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 1k "Ve [player] benim şiirimi de beğendi."
    y "Hatta şiirimden etkilendiğini bile söyledi."
    stop music fadeout 1.0
    "Natsuki birden ayağa kalkıyor."
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 4y "Öyle mi?"
    n "Yeni üyemizi etkilemeyi bu kadar kafaya taktığını fark etmemiştim, Yuri."
    play music t7a
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 1n "H-Ha?!"
    y "Ben öyle!.."
    y 1o "Uf..."
    y "Sen... Sen sadece..."
    "Yuri de kalkıyor."
    y 2r "Belki de sadece [player] benim tavsiyeme seninkinden daha fazla değer verdiği için beni kıskanıyorsun!"
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 1e "Hah! {i}Benim{/i} tavsiyeme daha fazla değer verdi belki, nereden biliyorsun?"
    n "Kendini bu kadar çok mu beğeniyorsun?"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 3h "Ben!.."
    y "Hayır..."
    y "Kendimi beğeniyor olsaydım..."
    y 1r "... Yaptığım her şeyi özellikle abartılı bir şekilde şirin yapmaya çalışırdım!"
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 1o "Uuuuuu!.."
    n "Bak ne diyeceğim!"
    n "[player] aramıza katılır katılmaz göğüsleri sihirli bir şekilde bir beden büyüyen ben değilim!!"
    show yuri 3p at h21
    show natsuki zorder 2 at t22
    y "N-Natsuki!!"
    show yuri zorder 2 at t32
    show natsuki zorder 2 at t33
    show monika 3l behind yuri, natsuki at l41
    m "Şey, Natsuki, bu biraz--"
    show monika at h41
    show yuri 3p zorder 3 at f32
    show natsuki 1e zorder 3 at f33
    ny "Bu seni ilgilendirmiyor!"
    show monika at lhide
    hide monika
    show yuri 2h zorder 2 at f21
    show natsuki zorder 2 at t22
    queue music t7g
    $ timeleft = 12.453 - get_pos()
    show noise zorder 3 at noisefade(25 + timeleft)
    show vignette as flicker zorder 4 at vignetteflicker(timeleft)
    show vignette zorder 4 at vignettefade(timeleft)
    show layer master at layerflicker(timeleft)
    y "Kendi güvensizliğinin hıncını başkalarından çıkarıyorsun..."
    y "Gerçekten göründüğün kadar çocuksu davranıyorsun, Natsuki."
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 4o "{i}Ben mi?{/i} Diyene bak ya, emo özentisi sürtük seni!"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y "Emo mu?.."
    y 2r "Yaşam tarzım akıl yaşının kavrayamayacağı kadar ağır olduğu için özür dilerim!"
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 4f "Gördün mü??"
    n "Bu bile dediğimi kanıtlıyor!"
    n 4e "Çoğu insan ortaokuldan mezun olunca kişisel sorunlarını atlatmayı öğrenir."
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y "Bir şeyi kanıtlamak istiyorsan şu gıcık tavrınla insanları sinir etmeyi kes!"
    y "Çöp kişiliğini şirin bir şekilde giyinerek ve davranarak dengeleyebileceğini mi sanıyorsun?"
    y 1k "Hakkındaki tek şirin şey bu konuda ne kadar çabaladığın."
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 2y "Uf, dikkatli ol be Yuri, o keskin sözlerinle kendini kesebilirsin."
    n "Ay, çok özür dilerim.. Zaten kendini kesiyorsun, değil mi?"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 3n "B-Beni kendimi kesmekle mi suçladın sen??"
    y 3r "Ne zorun var lan senin, sikik?!"
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 1e "Evet, devam et!"
    n "[player] gerçekte neler düşündüğünü duysun!"
    n "Eminim bundan sonra sana abayı yakacaktır!"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 3n "A-Ah--!"
    show yuri zorder 2 at t21
    "Yuri aniden bana doğru dönüyor, sanki burada olduğumu yeni fark etmiş gibi."
    show yuri zorder 3 at f21
    y 2n "[player]!.."
    y "O-- O sadece beni kötü göstermeye çalışıyor!"
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 4w "Bu doğru değil!"
    n "O başlattı!"
    show yuri 1t zorder 2 at t21
    show natsuki 1g zorder 2 at t22
    $ style.say_dialogue = style.normal
    mc "..."
    $ style.say_dialogue = style.edited
    "{cps=*2}Kendimi bu işe nasıl bulaştırdım?!{/cps}{nw}"
    "{cps=*2}Yazım konusunda hiçbir şey bilmiyorum...{/cps}{nw}"
    "{cps=*2}Ama fikrine katıldığım kişi beni muhtemelen takdir edecektir!{/cps}{nw}"
    "{cps=*2}Bu kişi elbette!..{/cps}{nw}"
    $ style.say_dialogue = style.normal
    $ menu_clicked = 0
    window hide(None)
    label ch21_end_menu:
        menu:
            "Natsuki.":
                jump menu_click
            "Yuri.":
                jump menu_click

    label menu_click:
        $ srf = screenshot_srf()
        show layer screens:
            truecenter
            zoom 1.00
        show screen tear(20, 0.1, 0.1, 0, 40, srf)
        play sound "sfx/s_kill_glitch1.ogg"
        pause 0.25
        hide screen tear
        stop sound
        $ menu_clicked += 1
        if menu_clicked < 9:
            show layer master:
                truecenter
                zoom 1.00 + menu_clicked * menu_clicked * 0.06
                yalign 0.25
            show layer screens:
                truecenter
                zoom 1.00 + menu_clicked * menu_clicked * 0.06
                yalign 0.25
            jump ch21_end_menu


    window show(None)
    stop music
    $ menu_clicked = 8
    $ quick_menu = False
    show layer master:
        truecenter
        zoom 1.00 + menu_clicked * menu_clicked * 0.06
        yalign 0.25
    show layer screens:
        truecenter
        zoom 1.00 + menu_clicked * menu_clicked * 0.06
        yalign 0.25
    show monika 1 onlayer front at i11:
        zoom 1.00 + menu_clicked * menu_clicked * 0.06
        yalign 0.25
    $ renpy.display_menu(items=[('Natsuki.', True), ('Yuri.', True)], interact=False, screen='choice')
    m "..."
    show layer master
    show layer screens
    show monika 1 onlayer front at i11
    window auto
    $ renpy.display_menu(items=[('Natsuki.', True), ('Yuri.', True)], interact=False, screen='choice')
    m "..."
    $ renpy.display_menu(items=[('Natsuki.', True), ('Yuri.', True)], interact=False, screen='choice')
    m "..."
    show monika 1m onlayer front at i11
    $ renpy.display_menu(items=[('Natsuki.', True), ('Yuri.', True)], interact=False, screen='choice')
    m "Şey..."
    $ renpy.display_menu(items=[('Natsuki.', True), ('Yuri.', True)], interact=False, screen='choice')
    m "Hey, [player]..."
    show monika 1e onlayer front at i11
    $ renpy.display_menu(items=[('Natsuki.', True), ('Yuri.', True)], interact=False, screen='choice')
    m "Biraz dışarı\nçıkalım mı?"
    $ renpy.display_menu(items=[('Natsuki.', True), ('Yuri.', True)], interact=False, screen='choice')
    m "Olur mu?"
    scene bg corridor
    hide monika onlayer front
    show monika 1n onlayer master at t11
    with wipeleft_scene
    $ quick_menu = True
    m "Bunun için üzgünüm..."
    m "Seni bu işe karıştırmamalılardı cidden."
    m 1e "Buna karışmamak muhtemelen ikimiz için de en iyisi..."
    m "Kavgaları bitince içeri gireriz."
    m 5 "Ahaha..."
    m "Bir de başkan olacağım."
    m 1m "Kulüp üyelerime doğru düzgün söz geçiremiyorum bile..."
    m "Keşke ara sıra biraz daha kendime güvenebilsem."
    m "Ama başkalarını ezmek hiç bana göre olmadı..."
    m 1e "Beni anlıyorsun, değil mi?"
    m "Her neyse..."
    m 1a "Eğer bu diğerleriyle daha az zaman geçirmene sebep olursa, sorun değil."
    m 1j "Ben seve seve seninle zaman geçiririm..."
    show monika zorder 1 at thide
    hide monika
    "Natsuki aniden sınıftan çıkıyor."
    show natsuki 12h zorder 2 at t11
    n "..."
    show natsuki 12f at lhide
    $ pause(0.75)
    hide natsuki
    "Çabucak kaçıyor."
    show monika 1l zorder 2 at t11
    m "Of, of..."
    m "... Galiba bitirdiler..."
    scene bg club_day2
    with wipeleft_scene
    y "Böyle olsun istemedim..."
    y "Böyle olsun istemedim..."
    y "Böyle olsun istemedim..."
    "Yuri sırasına oturmuş, elleri alnında ileri geri sallanıyor."
    mc "Yuri?.."
    show yuri 4d zorder 2 at t11
    y "Böyle olsun istemedim!!"
    mc "S-Sana inanıyorum..."
    "Yuri’nin Natsuki’ye ne demiş olabileceğini bilmiyorum."
    "Veya ne yapmış olabileceğini."
    y "[player]."
    y "Lütfen benden nefret etme."
    y "Lütfen!"
    y "Ben böyle biri değilim!"
    y "Bugün bende yanlış giden bir şeyler vardı..."
    show monika 1d zorder 3 at f31
    m "Sorun değil, Yuri."
    m "Böyle olmasını istemediğini biliyoruz."
    m 1j "Ayrıca, Natsuki’nin yarına kadar her şeyi unutacağına eminim."
    m 1a "Tamamen."
    show monika zorder 2 at t31
    show yuri zorder 3 at f32
    y 4b "..."
    show yuri zorder 3 at t32
    show monika zorder 2 at f31
    m "Her neyse, toplantı sona erdi. İsterseniz evlerinize gidebilirsiniz."
    show monika zorder 2 at t31
    show yuri zorder 3 at f32
    y 4a "..."
    show yuri zorder 2 at t32
    "Yuri bir şey söylemek istermişçesine bana bakıyor."
    "Ama ara ara gözü Monika’ya kayıyor."
    show yuri zorder 3 at f32
    y 2v "S-Sen önden gidebilirsin, Monika..."
    y "Ben biraz daha kalmak istiyorum."
    show yuri zorder 2 at t32
    show monika zorder 3 at f31
    m 2k "Ben Başkan’ım, o yüzden en son çıkan ben olmalıyım."
    m "İşin bitene kadar beklerim."
    show monika 2a zorder 2 at t31
    show yuri zorder 3 at f32
    y 4b "..."
    y "..."
    y "Şey-- Ben de Başkan Yardımcısı’yım..."
    y "Lütfen bugünlük o sorumluluğu almama izin ver."
    show yuri zorder 2 at t32
    show monika zorder 3 at f31
    m 2i "Nedense yanında olmamı istemiyor gibisin, Yuri."
    show monika zorder 2 at t31
    show yuri zorder 3 at f32
    y 3p "O-Ondan değil!"
    y 3o "Ondan değil..."
    y 3n "Sadece..."
    y 3q "[player] ile kitabımı konuşma fırsatı bulamadım..."
    y "Sen bizi dinlerken... utanç verici olur..."
    show yuri zorder 2 at t32
    show monika zorder 3 at f31
    m 1r "{i}*Of*{/i}"
    m 1d "Başka çarem yok, ha?"
    show monika zorder 2 at t31
    show yuri zorder 3 at f32
    y 1t "B-Başına bela açtığım için özür dilerim..."
    $ gtext = glitchtext(20)
    y 1s "Ama anladığın için gerçekten minne{nw}"
    play music g1
    show monika 1 onlayer front at i31
    y glitch "Ama anladığın için gerçekten minne{fast}[gtext] [gtext][gtext]{nw}"
    $ _history_list.pop()
    hide monika onlayer front
    window hide(None)
    window auto

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
