image yuri half = "images/yuri/1l.png"
image yuri_half2:
    "images/yuri/1r.png"
    block:
        xoffset -360
        linear 0.2 xoffset -280
        repeat

label ch22_main:
    scene bg club_day2
    with dissolve_scene_half
    play music t6
    "Bir gün daha bitiveriyor ve kulüp toplantısı zamanı geliyor."
    "Son birkaç gün içinde buraya biraz daha alıştım."
    "Kulüp odasına girişimde beni her zamanki manzara karşılıyor."
    if renpy.random.randint(0,2) == 0:
        show yuri half zorder 2 at i11
        show yuri_half2 zorder 1 at i11
    else:
        show yuri 1s zorder 2 at t11
    y "Hoş geldin, [player]..."
    hide yuri_half2
    mc "Ah, merhaba Yuri..."
    "Bana mı öyle geliyor yoksa Yuri’nin yüz ifadesinden mi, bilmiyorum..."
    "Ama dünkü tartışmanın etkisi hafiften sürüyor sanki."
    y 2v "Ş-Şey..."
    "Yuri omzunun arkasından odaya göz gezdiriyor."
    "Natsuki bir sıraya oturmuş manga okuyor."
    "Ve şaşırtıcı bir şekilde Monika henüz gelmemiş."
    "Aniden, Yuri kolumu tutup beni odanın bir köşesine götürüyor."
    show bg closet
    show yuri 2t zorder 2 at t11
    with wipeleft
    y "Dün hakkında..."
    y "Ben..."
    y 2v "Gerçekten özür dilemeliyim."
    y "Böyle bir şey daha önce hiç olmamıştı..."
    y 2t "Ve... Bir şekilde kendimi kaybettim sanırım..."
    y "Aklım başımda değildi."
    y 2w "Lütfen normalde böyle olduğumuzu düşünme!"
    y "Sadece ben değil, Natsuki de..."
    show yuri 2t
    mc "Yuri..."
    mc "Düşünceli davranıp özür dilemene sevindim."
    mc "Çok kafana takma."
    mc "Sadece birkaç gündür burada olsam da dün farklı bir şey olduğunu fark ettim..."
    mc "Belki de ilk defa şiirlerimizi paylaştığımız için biraz fazla hassastık."
    mc "Ama her ne olduysa..."
    mc "Sizin hakkınızda kötü düşünmeme sebep olmadı."
    mc "Senin kötü biri olamayacağına kanaat getirdim bile."
    mc "Şimdi özür dilediğine göre olayların böyle gelişmesini istememiş olmalısın."
    y 3t "A-Ah..."
    y "[player]..."
    y 3u "Böyle nazik şeyleri açık açık söyleme..."
    y "Beni biraz fazla mutlu ediyorlar."
    y 1s "Bu kadar anlayışlı biri olduğun için gerçekten çok mutluyum..."
    y "Ve bu kulübe katılmana çok sevindim."
    y "Sen varken her şey biraz daha parlak ve--"
    y 1t "Ah--"
    y 4c "Özür dilerim, ne diyorum ben?.."
    y "Ben sadece--"
    show natsuki 2c zorder 3 at f33
    n "Hey, Monika’yı gördünüz mü?"
    show natsuki zorder 2 at t33
    show yuri 3n at h32
    y "Ah--!"
    mc "Hayır, görmedim..."
    mc "Ben de merak ediyorum onun nerede olduğunu."
    show natsuki zorder 3 at f33
    n 5g "Of..."
    n 5c "Yuri, sen de görmedin onu sanırım?"
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y 4a "..."
    "Yuri, Natsuki’nin onunla bu kadar sakince konuşması üzerine bariz bir şekilde şaşırıyor."
    y "H-Hayır, görmedim..."
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f33
    n 1u "Püf, hiç geç kalmazdı."
    n "Aptalca olduğunu biliyorum ama endişelenmemek elimde değil..."
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y 2t "..."
    show yuri zorder 2 at t32
    show natsuki 1h zorder 3 at f33
    n "Ne?"
    n "Neden bana öyle bakıyorsun?"
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y "Ş-Şey..."
    y "Natsuki, dün için..."
    y 3w "Ö-Özür dilemek istiyorum!"
    y "Yemin ederim ki söylediklerimde ciddi değildim!"
    y 3t "Bugünden itibaren kendimi kontrol altında tutmak için elimden geleni yapacağım..."
    y "O yüzden--"
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f33
    n 2c "Yuri, neden bahsediyorsun be?"
    n "Dün bir şey mi yaptın ki?"
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y 3f "... Ha?"
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f33
    $ style.say_dialogue = style.normal
    n 2a "Of..."
    $ style.say_dialogue = style.edited
    n "Aklından ne geçtiğini bilmiyorum ama bir önemi yok."
    n "Kötü herhangi bir şey hatırlamıyorum bile."
    n "Küçük şeyler hakkında fazla endşelenen birisin, değil mi?"
    $ style.say_dialogue = style.normal
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y 2o "..."
    y "A-Ama..."
    if renpy.random.randint(0, 3) == 0:
        $ style.say_dialogue = style.edited
        show yuri zorder 2 at t32
        show natsuki mouth as nm zorder 3 at i33
        show n_moving_mouth zorder 3:
            xoffset 400
        n 2a "tofaşklar yelken körgörüş soy anan düzlük hatasızca skleromalasi sundu katoliklik kişnedi"
        hide nm
        hide n_moving_mouth
        $ style.say_dialogue = style.normal
    show natsuki zorder 3 at f33
    n 2j "Özrünü kabul edeceğim zaten, eğer kendini daha iyi hissedeceksen."
    n "Ayrıca, bunu duymak biraz güzel bir şey. Hep gizlice benden nefret ettiğinden falan korkuyordum."
    n 2z "Ehehe."
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y 3q "H-Hayır, hiç de bile!.."
    y "Senden nefret etmiyorum..."
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f33
    n 2l "Ahaha."
    n "Eh, biraz tuhafsın ama ben de senden nefret etmiyorum."
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y 3t "..."
    "Natsuki bana dönüyor."
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f33
    n 2a "Sen hâlâ gözetim aşamasındasın ama."
    show natsuki zorder 2 at t33
    mc "Hey!.."
    "Aniden kapı açılıyor"
    show monika 1g at l41
    m "Üzgünüm! Feci üzgünüm!"
    mc "A, sonunda gelebildin..."
    show monika zorder 3 at f41
    m "Geç kalmak istememiştim..."
    m "Umarım endişelenmemişsinizdir!"
    show monika zorder 2 at t41
    mc "Yok ya..."
    mc "Gerçi, Natsuki endişeliydi."
    show natsuki zorder 3 at f33
    n 1p "D-Değildim!!"
    show natsuki zorder 2 at t33
    show monika zorder 3 at f41
    m 1k "Ahaha."
    show monika zorder 2 at t41
    show natsuki zorder 3 at f33
    n 1s "... Neden bu kadar geciktin ki?"
    show natsuki zorder 2 at t33
    show monika zorder 3 at f41
    m 1e "Şey..."
    m "Şey, son dersim etüttü de."
    m "Açıkçası, zamanın nasıl geçtiğini anlamadım...."
    m "Ahaha..."
    show monika zorder 2 at t41
    show natsuki zorder 3 at f33
    n 2c "Bu hiç mantıklı değil ama."
    n "En azından zili duymuş olman gerekirdi."
    show natsuki zorder 2 at t33
    show monika zorder 3 at f41
    m 1m "Duymamış olmalıyım. Piyano çalışıyordum..."
    show monika zorder 2 at t41
    show yuri zorder 3 at f32
    y 1e "Piyano mu?.."
    y "Müzikle de uğraştığını bilmiyordum, Monika."
    show yuri zorder 2 at t32
    show monika zorder 3 at f41
    m 1l "Ah, beni gözünde büyütme."
    m 1m "Bir süredir çalışıyorum ama henüz pek de iyi değilim."
    show monika zorder 2 at t41
    show yuri zorder 3 at f32
    y 1a "Yine de..."
    y "Bu çok azim gerektiren bir şey olmalı."
    y "Etkilendim."
    show yuri zorder 2 at t32
    show monika zorder 3 at f41
    m 5 "Ay, sağ ol ya, Yuri~"
    show monika zorder 2 at t41
    show natsuki zorder 3 at f33
    n 2d "Bir ara bizim için bir şarkı çalmalısın!"
    show natsuki zorder 2 at t33
    show monika zorder 3 at f41
    m "Ahaha, şey..."
    "Monika bana bakıyor."
    m 1a "Şu an bir şarkı yazmaya çalışıyorum ama henüz bitmedi..."
    m "Biraz daha kendimi geliştirirsem çalarım belki."
    show monika zorder 2 at t41
    mc "Kulağa harika geliyor."
    mc "Bunu dört gözle bekliyorum."
    show monika zorder 3 at f41
    m 1b "Gerçekten mi?"
    m "Öyleyse..."
    m "Seni hayal kırıklığına uğratmayacağım, [player]."
    show yuri zorder 1 at thide
    show natsuki zorder 1 at thide
    hide yuri
    hide natsuki
    show monika 5 zorder 2 at t11
    "Monika tatlı bir şekilde gülümsüyor."
    mc "Ah..."
    mc "Kastım baskı kurmak falan değildi!"
    m 1a "Ahaha, merak etme."
    m "Zaten şarkımı paylaşmayı umuyordum."
    m "Sanırım bu yüzden son zamanlarda çok çalışıyorum."
    mc "Anladım..."
    "Monika bütün kulübü mü kastetti yoksa sadece beni mi, emin değilim..."
    mc "Öyleyse, iyi şanslar."
    m 1j "Teşekkürler~!"
    m 1a "E, bir şey kaçırmadım, değil mi?"
    mc "Pek... Pek sayılmaz."
    show monika zorder 1 at thide
    hide monika
    "Üçümüzün konuştuğu şeylerden bahsetmemeyi seçtim."
    "Hem, Natsuki çoktan dolaba kaçmıştı bile."
    show yuri 2q zorder 2 at t11
    y "[player]..."
    y "Şey..."
    y "Övgülerin moralimi yerine getirdiğine göre..."
    y "Bugün birlikte vakit geçirmek ister misin diye merak ediyordum."
    y 3o "Yani--kulüpte!"
    if poemwinner[0] == "natsuki":
        $ y_appeal = 1
        mc "Ah, olabilir."
        mc "O kitabı bana verdikten sonra sana hayır diyebileceğimi sanmıyorum."
        mc "Şey, Natsuki’nin beni beklemediğinden emin olmalıyım."
        mc "Dün okumayı bitirdikten sonra o--"
        if n_appeal >= 2:
            y 3r "Ona bir şey olmaz!"
            $ style.say_dialogue = style.normal
            y 3h "O zaten orada mangasını okuyor. Bak."
            $ style.say_dialogue = style.edited
            y 3f "Onu o kadar düşünme."
            y "O görmezden gelinmeye alışkın."
            y "Gel hadi, şuraya gidiyoruz."
            $ style.say_dialogue = style.normal
            window hide(None)
            $ currentpos = get_pos()
            stop music
            scene black
            window auto
            pause 2.0
            play music "<from " + str(currentpos) + " loop 10.893>bgm/6.ogg"
            jump ch22_main2
        else:
            y 3r "O, o iyi!"
            y 3h "Orada manga okuyor işte."
            y 3y6 "Olur o zaman, değil mi?"
            mc "Ah--"
            mc "Öyleyse, bir sorun göremiyorum..."
    else:
        $ y_appeal = 2
        mc "Evet, kesinlikle."
        mc "Zaten bunu planlamıştım."
    show yuri zorder 2 at h11
    y 3y5 "Tamam!"
    y "Şimdi başlayabilir miyiz?"
    y "Oturacak bir yer bula--"
    y 3n "A-Ah--"
    y "Biraz fazla zorlayıcı davranıyorum, değil mi?.."
    y 4c "Özür dilerim!"
    y "Kalbim... Nedense küt küt atmayı kesmiyor..."
    mc "Endişelenme."
    mc "Bilakis, seni bu kadar enerjik görmek güzel."
    y 3q "T-Tamam!"
    y "Ama..."
    y 3j "Sakinleşmeye çalışmalıyım."
    y "Böyleyken kitap okumaya odaklanamam..."
    mc "Tamam, aceleye gerek yok."
    "Yuri derin bir nefes alıyor ve ardından çantasından kitabı çıkarıyor."
label ch22_main2:
    if n_poemappeal[1] == 1:
        $ n_poemappeal[1] = 0
    $ poemwinner[1] = "yuri"


    scene bg club_day2
    show yuri 3a at i11
    with wipeleft
    $ nextscene = "yuri_exclusive2_" + str(eval("y_appeal")) + "_ch22"
    call expression nextscene

    return

label ch22_end:
    stop music fadeout 1.0
    scene black
    with wipeleft_scene
    call screen confirm("Özel bir şiir açtınız.\nOkumak ister misiniz?", Return(True), Return(False))
    if _return:
        call expression "poem_special_" + str(persistent.special_poems[1])
        scene black with Dissolve(1.0)
    else:
        pass
    if not faint_effect and renpy.random.randint(0,2) == 0:
        $ faint_effect = True
    else:
        $ faint_effect = None
    scene bg club_day2
    show monika 4b zorder 2 at t32
    if faint_effect:
        show layer master at dizzy(0.5, 1.0)
        show layer screens at dizzy(0.5, 1.0)
        show expression Solid("ff0000") as i1 onlayer front:
            additive 1.0
        show expression Solid("#440000") as i2 onlayer front:
            additive 0.4
        show veins onlayer front:
            additive 0.5
    with wipeleft_scene
    if faint_effect:
        play music t3g3
    else:
        play music t3
    if renpy.random.randint(0,2) == 0:
        $ config.mouse = {"default": [
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head.png", 0, 0),
                                    ("gui/mouse/s_head.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head.png", 0, 0),
                                    ]}



    m "Pekâlâ millet!"
    m "Hepimiz birbirimizin şiirlerini okumayı bitirdik, değil mi?"
    $ config.mouse = None
    m "Bugün üzerinde durmamız gereken bir şey var, o yüzden herkes odanın önüne gelip oturabilirse eğer..."
    show natsuki 3c zorder 3 at f31
    n "Festival hakkında mı?"
    show natsuki zorder 2 at t31
    show monika 1j zorder 3 at f32
    m "Eh, sayılır~"
    show monika 1a zorder 2 at t32
    show natsuki 1m zorder 3 at f31
    n "Of, gerçekten festival için bir şey yapmak zorunda mıyız?"
    n "Birkaç gün içinde ortaya güzel bir şey çıkartabilecek değiliz ne de olsa."
    n "Yeni üye toplamak yerine kendimizi gülünç duruma düşüreceğiz sadece."
    if faint_effect:
        $ currentpos = get_pos() + 2.0
        stop music fadeout 2.0
        show black onlayer front:
            alpha 0.0
            linear 2.0 alpha 1.0
    show natsuki zorder 2 at t31
    show yuri 2g zorder 3 at f33
    y "Bu konuda ben de endişeliyim."
    if faint_effect:
        hide black onlayer front
        hide veins onlayer front
        hide i1 onlayer front
        hide i2 onlayer front
        show layer master
        show layer screens
        play music "<from " + str(currentpos) + " loop 4.618>bgm/3.ogg"
    y "Son dakika hazırlıklarında pek iyi değilim..."
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m 1b "Çok fazla endişelenmeyin!"
    m "Basit bir şey yapacağız sadece, tamam mı?"
    m 2a "Bakın..."
    m 2m "[player] aramıza katıldığından ve kulüp aktiviteleri yapmaya başladığımızdan beri herkesin biraz daha... canlandığını... biliyorum"
    m 2d "Ama şimdi rehavete kapılma zamanı değil."
    m "Hâlâ sadece dört üyeden oluşuyoruz..."
    m 2a "Ve festival daha fazla üye bulabilmemiz için tek gerçek şansımız."
    show monika zorder 2 at t32
    show natsuki zorder 3 at f31
    n 5g "Yeni üye toplamanın nesi iyi ki?"
    n "Zaten resmî bir kulüp sayılmaya yetecek sayıda üyemiz var."
    n "Daha fazla üye daha fazla gürültü demek. Kulübü idare etmek de zorlaşacak."
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 1g "Natsuki..."
    m "Bence bu meseleye hiç de doğru açıdan bakmıyorsun."
    m "Tutkunu olabildiğince çok insanla paylaşmak istemiyor musun?"
    m 3e "Seni buraya getiren aynı duyguları bulmalarını sağlamak için ilham vermeyi?"
    m "Edebiyat Kulübü insanların kendini en iyi ifade edebildiği bir yer olmalı."
    m "Hiç ayrılmayı istemeyeceğin kadar samimi bir yer olmalı."
    m 2e "Senin de öyle düşündüğünü biliyorum."
    m 2b "Hepimizin öyle düşündüğünü biliyorum!"
    m "Bu yüzden çok çalışıp birlikte festival için bir şeyler hazırlamalıyız... Küçük bir şey bile olsa!"
    m "Değil mi, [player]?"
    show monika 2a zorder 2 at t32
    mc "Ah..."
    show natsuki zorder 3 at f31
    n 42c "Ah, hadi ama!"
    n "Hayır demeyi bilmiyor diye ondan faydalanamazsın."
    stop music fadeout 1
    n 1c "Bak, Monika."
    n "Sence birimiz bile gerçekten başka insanları düşünerek mi katıldık bu kulübe?"
    n "Yuri, [player] katılana kadar hiç konuşmadı bile."
    n 2b "Ben ise evde kalacağıma burada olmayı tercih ediyorum."
    n "Ve [player] edebiyat konusunda tutkulu bile değil zaten."
    n "Durumumuz bu."
    n 4w "Üzgünüm ama yeni üye edinmekle ilgilenen tek kişi sensin."
    n "Biz hâlimizden memnunuz."
    n 4q "Başkan falan olduğunu biliyorum ama cidden bir kez olsun bizim görüşlerimizi de göz önüne almalısın."
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 1g "..."
    "Monika’nın Natsuki’nin sözlerine şaşırdığı bariz."
    play music t9
    m 1m "Bu... hiç doğru değil."
    m 2m "Eminim ki [player] ve Yuri de daha fazla üye toplamak istiyordur..."
    m 2p "... Değil mi?"
    show monika zorder 2 at t32
    show yuri zorder 3 at f33
    y 4b "..."
    show yuri zorder 2 at t33
    mc "..."
    "Yuri’yi bilmiyorum ama benim için pek de fark etmez."
    "Monika’nın istediği kadar hevesli davranırsam yalan söylemiş olurum."
    "Yine de, durumu kurtarmak bana düştüyse..."
    mc "A--"
    show monika zorder 3 at f32
    m 1i "Hayır."
    m "Natsuki haklı, değil mi?"
    m 1g "Bu kulüp..."
    m "Birkaç kişinin takılmaya geldiği bir yerden fazlası değil."
    m 1r "Neden herkesin burayı benim gördüğüm gibi gördüğünü düşündüm ki?"
    show monika zorder 2 at t32
    mc "Ama bu bizim yeni üye toplamaya karşı olduğumuz falan anlamına gelmiyor..."
    show monika zorder 3 at f32
    m 1i "[player], bu kulübe neden katıldın?"
    m "Bu kulüpten ne gibi bir beklentin vardı?"
    show monika zorder 2 at t32
    mc "Şey--"
    "Bu, dürüst olabileceğim bir şey değil, değil mi?"
    show monika zorder 3 at f32
    m 1p "Hatta..."
    m "Doğru hatırlıyorsam sana katılmama seçeneği sunulmamıştı bile."
    show monika zorder 1 at thide
    hide monika
    "Monika oturup sırasına bakıyor."
    m "Bütün bunların amacı ne ki?"
    m "Ya bu kulübü kurmak bir hataydıysa?"
    mc "..."
    show yuri zorder 3 at f33
    y 2g "Aferin sana, Natsuki..."
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f31
    n 1p "Ne, ben mi?"
    n 1s "Ben sadece fikrimi belirttim..."
    n "Dürüst olmak suç mu?"
    show natsuki zorder 2 at t31
    show yuri zorder 3 at f33
    y 2l "Mesele dürüst olmak değil."
    y "Kullandığın kelimeler."
    y 2h "Ayrıca kulüpteki herkes adına böyle konuşmaya hakkın yok..."
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f31
    n 1e "Hiç anlamıyorsun!"
    n 5s "Ben sadece..."
    n "Ben sadece birkaç arkadaşla birlikte takılacak iyi bir yer istiyorum."
    n 5u "Kulübün benim için böyle olmasında bir sorun mu var?"
    n "Benim için... Benim için böyle olan çok yer yok..."
    n 5x "Şimdi de Monika bunu benden almak istiyor!"
    show natsuki zorder 2 at t31
    mc "O hiçbir şeyi almıyor--"
    show natsuki zorder 3 at f31
    n 1g "Hayır, [player]."
    n "Aynı şey değil."
    n 1q "Onun izlemek istediği yol kulübü değiştirecek."
    n "Böyle bir şey isteseydim başka salakça bir kulübe katılırdım."
    n 12d "Ama burası..."
    n "Yani..."
    n 12e "En azından bir süreliğine..."
    n "Her şey güzeldi."
    "Natsuki eşyalarını toplamaya başlıyor."
    n 12d "Ben eve gidiyorum."
    n "Sanki... Artık buraya ait değilmişim gibi hissediyorum."
    show natsuki zorder 2 at t31
    show yuri zorder 3 at f33
    y 3t "Natsuki..."
    show natsuki zorder 1 at thide
    hide natsuki
    "Natsuki, Yuri’yi görmezden gelip sınıftan çıkıyor."
    show yuri zorder 2 at t11
    y 3v "..."
    y "Bu çok kötü..."
    y "Ne yapacağımı bilmiyorum..."
    mc "Şey..."
    mc "Festival hakkında düşündüğün bir şey var mı?"
    y 4b "B-Bilmiyorum..."
    $ style.say_dialogue = style.normal
    y "Biraz isteksizim sanırım..."
    show black zorder 3
    show y_glitch_head zorder 3:
        xpos 630 ypos -50 zoom 2.0
    $ style.say_dialogue = style.edited
    $ currentpos = get_pos() / 2.07
    play music "<from " + str(currentpos) + " loop 1.532>bgm/9g.ogg"
    y "O itici velet kimin umurunda?"
    $ style.say_dialogue = style.normal
    $ currentpos = get_pos() * 2.07
    play music "<from " + str(currentpos) + " loop 3.172>bgm/9.ogg"
    hide black
    hide y_glitch_head
    y "Yani, kulübün şu anki sessiz ve güzel hâlini seviyorum..."
    y "Ve... sen burada olduğun için mutluyum..."
    y 2t "Ama yine de!"
    y "Ben Başkan Yardımcısı’yım..."
    y "Sorumluluklarımı böyle görmezden gelmem uygun değil..."
    show black zorder 3
    show y_glitch_head zorder 3:
        xpos 430 ypos -450 zoom 4.5
    $ style.say_dialogue = style.edited
    $ currentpos = get_pos() / 2.07
    play music "<from " + str(currentpos) + " loop 1.532>bgm/9g.ogg"
    y "O, kendisini öldürse kimse ağlamazdı."
    $ style.say_dialogue = style.normal
    $ currentpos = get_pos() * 2.07
    stop music
    pause 0.5
    play sound "sfx/stab.ogg"
    show blood_eye zorder 3:
        pos (710,380) zoom 2.5
    pause 0.75
    stop sound
    play music "<from " + str(currentpos) + " loop 3.172>bgm/9.ogg"
    hide black
    hide y_glitch_head
    hide blood_eye
    y 2l "Herkesin bakış açısını hesaba katarak kulüp için doğru olan kararı vermek için elimden geleni yapmalıyım."
    y 1t "Peki ya sen, [player]?"
    y "Bu kulüpten ne gibi bir beklentin var?"
    "Yuri, Monika’nın sorduğu soruyu soruyor."
    "Dolaylı bir cevap vermenin hiç yoktan iyi olacağına karar veriyorum."
    mc "... Bence en önemli şey herkesin anlaşması..."
    mc "... Ve kulübün başka hiçbir yerde bulunmayacak bir şey sunması."
    mc "Bence üyelerin sayısı değil de her bir üyenin niteliği daha önemli."
    mc "Edebiyat Kulübü’nü özel bir yer yapacak olan şey bu farklılık olacak."
    y 1u "Anladım..."
    y "Sana epey katılıyorum."
    show blood_eye2 zorder 3:
        pos (568, 165)
    y 1f "Her bir üye kendi niteliklerini özel bir şekilde belli ediyor."
    y "Üyelerde meydana gelen her bir değişiklikle kulübün kimliği de değişecek."
    y 1h "Bence bu çok kötü bir şey değil."
    y "Arada bir alıştığımızın dışına çıkmak yani..."
    y 1a "Yani, eğer Monika’ya festival için yardım etmek istersen ben de senin tarafındayım."
    hide blood_eye2
    mc "Tamam."
    mc "Şey, belki yarın Natsuki’yle hep birlikte konuşabiliriz..."
    "Yuri başını sallayarak onaylıyor."
    show monika 1g zorder 3 at f21
    show yuri zorder 2 at t22
    m "Hey, Yuri..."
    show monika zorder 2 at t21
    show yuri zorder 3 at f22
    y 1t "Ha?"
    show yuri zorder 2 at t22
    show monika zorder 3 at f21
    m 1p "Şey, dün olanların biraz tuhaf olduğunu biliyorum..."
    m "Ama bence harika bir başkan yardımcısı olduğunu bilmeyi hak ediyorsun."
    m 1e "Aynı zamanda harika bir arkadaş olduğunu."
    show monika zorder 2 at t21
    show yuri zorder 3 at f22
    y 3s "M-Monika..."
    show yuri zorder 2 at t22
    show monika zorder 3 at f21
    m 2e "Burayı en iyi kulüp hâline getirmek için elimden gelen her şeyi yapmak istiyorum."
    m "Tamam mı?"
    show monika zorder 2 at t21
    show yuri zorder 3 at f22
    y "... Ben de."
    show yuri zorder 2 at t22
    show monika zorder 3 at f21
    m 1a "Pekâlâ..."
    m "Bugünlük evlerimize gidelim."
    m "Yarın festival işini konuşuruz."
    show monika zorder 2 at t21
    show yuri zorder 3 at f22
    y 1m "Tamam."
    y "Dört gözle bekliyorum."
    y 1a "Gidelim mi, [player]?"
    show yuri zorder 2 at t22
    show monika zorder 3 at f21
    m 1d "A--"
    m 1p "Lütfen bunu yanlış anlama ama..."
    m "Gitmeden önce [player] ile biraz konuşmak istiyorum."
    m 1d "Burada geçirdiği zamanla ilgili falan görüşünü almak için..."
    m "Bu, Başkan olarak benim için önemli."
    show monika zorder 2 at t21
    show yuri zorder 3 at f22
    y 2v "..."
    "Yuri, biraz hoşnutsuz görünüyor ama itiraz etmiyor."
    y 2t "Tamam."
    y 2s "Kararına güveniyorum, Monika."
    y "Öyleyse yarın görüşürüz."
    show yuri zorder 2 at t22
    show monika zorder 3 at f21
    m 1j "Görüşürüz~"
    show yuri zorder 1 at thide
    hide yuri
    "Monika, Yuri sınıftan çıkarken el sallıyor."

    show monika 2a zorder 2 at t11
    m "Oh be..."
    m 2e "Son günlerde burası biraz hararetliydi, değil mi?"
    show darkred:
        additive 0.2
        alpha 0
        linear 20 alpha 1.0
    show noise:
        alpha 0
        linear 20 alpha 0.1
    m "[player], sadece kulüpte iyi zaman geçirdiğinden emin olmak istiyorum."
    m "Seni mutsuz görmeyi hiç istemem."
    m 2m "Başkan olarak bu konuda kendimi sorumlu hissediyorum..."
    stop music
    m 4e "Ve gerçekten seni önemsiyorum... Biliyor musun?"
    m "Diğer kızların sana zor zaman yaşattığını görmek hoşuma gitmiyor."
    m 4r "Natsuki sana kaba davranıyor falan..."
    m 4m "Yuri de biraz... Şey işte."
    m 5a "Ahaha..."
    m "Bazen buradaki tek gerçek insanların seninle ben olduğumu düşünüyorum."
    m "Ne demek istediğimi biliyor musun?"
    m 1g "Ama bu tuhaf, çünkü burada geçirdiğin süre boyunca birlikte zar zor vakit geçirebildik."
    m 1n "Ah... Yani..."
    m "Sanırım teknik olarak sadece birkaç gün falan olacak..."
    m 1l "Özür dilerim, tuhaf bir şey demek istemedim!"
    m 1e "Sadece, seninle konuşmayı umduğum bazı şeyler vardı..."
    m "Sadece senin anlayabileceğin şeyler."
    stop music fadeout 3.0
    show black onlayer front:
        alpha 0.0
        0.25
        linear 3.0 alpha 1.00
    m "İşte o yüzden--\"{space=5000}{w=0.75}{nw}"
    m 1g "Hayır, şimdi değil!\"{space=5000}{w=0.5}{nw}"
    m "Hayır!\"{space=5000}{w=0.5}{nw}"
    m "Dur!\"{space=5000}{w=1.0}{nw}"
    window hide(None)
    window auto
    hide black onlayer front





    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
