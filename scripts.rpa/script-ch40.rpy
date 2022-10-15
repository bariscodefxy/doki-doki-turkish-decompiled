image sayori end-glitch:
    "sayori/end-glitch1.png"
    0.15
    "sayori/end-glitch2.png"
    0.15
    "sayori/end-glitch1.png"
    0.15
    "sayori/end-glitch2.png"
    1.00
    "sayori/end-glitch1.png"
    0.15
    "sayori/end-glitch2.png"
    0.15
    "sayori/end-glitch1.png"
    0.15
    "sayori/end-glitch2.png"

label ch40_main:
    $ s_name = "Sayori"
    stop music fadeout 2.0
    scene bg residential_day
    with dissolve_scene_full

    python:
        if not persistent.monika_back:
            try:
                renpy.file("../characters/monika.chr")
                renpy.call_screen("dialog", message="Lütfen kalbimle oynamayı kes.\nGeri dönmek istemiyorum", ok_action=Return())
                persistent.monika_back = True
            except:
                pass

    $ delete_character("monika")
    play music t2
    "Yine sıradan bir okul günü."
    "Her zamanki gibi etrafım okula giden arkadaş grupları ve çiftlerle sarılı."
    "Her zaman kendime birkaç kızla tanışma vaktinin geldiğini söylüyorum..."
    show sayori 1a at t11
    s "Hey, [player]..."
    "... Gerçi, bir kız var zaten."
    "O kız Sayori, komşum ve çocukluktan beri iyi bir arkadaşım."
    "Eskiden her gün okula birlikte giderdik..."
    "... Ve son zamanlarda, bu alışkanlığı yeniden kazandık."
    s "[player], benimle gurur duyuyor musun?"
    mc "Ha? Ne konuda?"
    s 1c "Şey ya..."
    s "Zamanında kalktığım için!"
    mc "Eh, bunu bir süredir yapıyorsun..."
    s "Evet!"
    s 4h "Ama bu konuda bir kez olsun bir şey söylemedin!"
    show sayori at s11
    s "Her gün okula birlikte gitmemize rağmen..."
    mc "Şey, evet..."
    mc "Senle gurur duyduğumu belli ettiğimi sanıyordum."
    mc "Bunu sesli söylemek utanç verici."
    s 1d "Hadi ama. Lütfen."
    s "Beni motive ediyor~"
    mc "Tamam, tamam..."
    mc "Seninle gurur duyuyorum, Sayori."
    show sayori at t11
    s 1q "Ehehe~"
    show sayori zorder 1 at thide
    hide sayori
    "Birlikte karşıya geçip okula doğru yürüyoruz."
    "Okula yaklaştıkça yol diğer öğrencilerle dolmaya başlıyor."
    show sayori 3a zorder 2 at t11
    s "Bu arada, [player]..."
    s "Bir kulübe katılmaya karar verdin mi?"
    mc "Kulüp mü?"
    mc "Sana dedim ya, öyle bir--"
    "Hep söylediğim şeyi söylemeye başlıyorum - herhangi bir kulübe katılmaya ilgim olmadığını."
    "Ama içimden bir ses Sayori’nin şu an buna daha fazla alınacağını söylüyor."
    "Ona kulüplerin vakit kaybı olduğunu nasıl söyleyebilirim ki..."
    "... O kendi kulübünü kurmuşken?"
    mc "... Aslında, evet."
    mc "Sanırım bir kulübe katılmaya karar verdim."
    show sayori at h11
    s 1m "Gerçekten mi?!"
    s 1r "Hangisi? Söyle!"
    mc "Hmm..."
    mc "Sürpriz olsun."
    s 5d "Off..."
    s "Çok gıcıksın."
    mc "Sabırlı ol, yakında öğreneceksin."
    "Eskiden kendimi neden böyle vurdumduymaz bir kıza azarlattığımı merak ederdim."
    "Ama sebebini anlamaya başladım: Ona imreniyorum."
    "Sayori bir şeye kafasını koydu mu büyük başarılar elde edebiliyor."
    "O yüzden onun için özel bir şey yapmalıymışım gibi hissediyorum."

    scene bg class_day
    with wipeleft_scene

    "Bugün de okuldaki vaktim oldukça sıradan geçti, farkında olmadan gün bitti."
    "Eşyalarımı topladıktan sonra ayağa kalkıyor, motive oluyorum."
    mc "Bir bakalım..."
    stop music fadeout 2.0

    scene bg corridor
    with wipeleft_scene
    "Daha önceden gördüğüm bir broşürden, kulübün oda numarasını hatırlıyorum."
    "Okulda gezinip yukarı kata, genellikle üçüncü sınıflar ve okul aktiviteleri için kullanıldığından okulun nadiren gittiğim kısmına çıkıyorum."
    "Kısa süre içinde odayı buluyorum."
    "Önümdeki kapıyı çekinerek açıyorum."
    scene bg club_day
    with wipeleft
    play music t3
    mc "Merhaba?.."
    show sayori 1m at t32
    s "Ah!"
    s "[player]?!"
    s 1c "B-Burada ne arıyorsun?"
    mc "Şey... Ben sadece--"
    "Ha? Gözlerimi odanın etrafında gezdiriyorum."
    show natsuki 3a at f31
    n "Hm."
    n "Demek Sayori’nin hep bahsettiği [player] sensin?"
    show natsuki at t31
    show yuri 2t at f33
    y "U-Uğradığın için teşekkürler!"
    y 2m "Seninle tanışmak bir zevk, [player]."
    y "Biz Edebiyat Kulübü’yüz."
    y 3v "U-Umarım ziyaretinin tadını çıkarırsın!"
    show yuri at t33
    show natsuki at f31
    n 3g "Hadi ama, Yuri..."
    n "Bu kadar resmî olmana gerek yok."
    n "Çok katı olduğumuzu falan düşünecek..."
    show natsuki at t31
    $ y_name = "Yuri"
    $ n_name = "Natsuki"
    show yuri at f33
    y 3q "Ah..."
    y "Üzgünüm, Natsuki..."
    show yuri at t33
    "Adı görünüşe bakılırsa Yuri olan uzun kız, diğerlerine kıyasla oldukça utangaç görünüyor."
    "Ona kıyasla Natsuki adlı kız - boyutuna rağmen - sözünü geçiren birine benziyor."
    mc "Tanıştığımıza sevindim."
    mc "Sizinle birlikte çalışmak için sabırsızlanıyorum."
    show sayori at f32
    s 1n "Ç-Çalışmak mı?.."
    s 1b "[player], yoksa..."
    s "Sen..."
    show sayori at t32
    mc "Evet."
    mc "Katılmaya karar verdiğim kulüp senin kulübün, Sayori."
    mc "Edebiyat Kulübü."
    "Sayori’nin gözleri parlıyor."
    show sayori at f32
    s 1n "... Yok artık."
    s 1s "Yok artık!"
    show sayori at hf32
    s 4s "Aaaahhhhhh!"
    "Sayori bana sarılıyor, zıplayıp duruyor."
    show sayori at t32
    mc "H-Hey--"
    show natsuki at f31
    n 3y "Ehehe."
    n "Eh, Sayori bu kadar mutluysa eminim seni ağırlamak o kadar da kötü olmayacaktır."
    show natsuki 3a at t31
    show yuri at f33
    y 1s "Bir de, artık dört kişiyiz."
    y "Bu da demek oluyor ki, resmî olarak kulüp statüsüne erişebiliriz."
    show yuri at t33
    show sayori at f32
    s 1x "Ne diyeceğimi bilmiyorum!"
    s "Bunu kutlamalıyız!"
    show sayori at t32
    show yuri at f33
    y 1m "Huhu."
    y "Bunun için ne kadar uygun bir gün, değil mi?"
    show yuri 1a at t33
    show sayori at f32
    s 1r "Evet!"
    s 1x "Ne de olsa Natsuki--"
    show sayori at t32
    show natsuki at f31
    n 1w "Hey, sürprizi bozma!"
    show natsuki at t31
    show sayori at f32
    s 5a "Ehehe, üzgünüm..."
    show sayori at t32
    show natsuki at f31
    n 1k "Herkes masaya otursun, tamam mı?"
    show natsuki at t31
    show yuri at f33
    y 1a "O hâlde, ben de biraz çay yapayım mı?"
    hide sayori
    hide natsuki
    hide yuri
    with wipeleft
    "Kızlar birkaç sırayı birleştirerek bir masa oluşturmuşlar."
    "Natsuki ve Yuri odanın bir köşesine gidiyorlar. Natsuki üstü örtülü bir tepsi alıyor, Yuri de dolabı açıyor."
    "Kendimi hâlâ tuhaf hissettiğimden Sayori’nin yanındaki sandalyeye oturuyorum."
    "Natsuki elinde tepsiyle birlikte, gururla masaya doğru yaklaşıyor."
    show natsuki 2z zorder 2 at t22
    n "Tamaaam, hazır mısınız?"
    n "... Ta-daa!"
    show sayori 4m zorder 2 at t21
    s "Uvooooah!"
    "Natsuki tepsinin üstündeki folyoyu kaldırıyor ve bir sürü beyaz, pofuduk, kediye benzeyen kapkekler ortaya çıkıyor."
    "Kedilerin bıyıkları kremayla çizilmiş ve kulakları yapmak için de küçük çikolata parçaları kullanılmış."
    show sayori at f21
    s 4r "Çok şiriiiin~!"
    show sayori at t21
    mc "Vay be, inanılmaz görünüyorlar."
    show natsuki at f22
    n 2d "Ehehe. Şey, öyle işte."
    n "Hadi, alın bir tane!"
    show natsuki at t22
    "Önce Sayori bir tane alıyor, ardından ben de alıyorum."
    show sayori at f21
    s 4q "Çok lezzetli!"
    show sayori at t21
    "Sayori ağzı doluyken konuşuyor. Şimdiden yüzüne krema bulaştırmayı başarmış."
    "Kapkeki elimde döndürüp ısıracak en iyi yeri bulmaya çalışıyorum."
    show sayori zorder 1 at thide
    hide sayori
    show natsuki 1c zorder 2 at t32
    "Natsuki sessiz."
    "Ara ara bana doğru baktığını fark ediyorum."
    "Kekin tadına bakmamı mı bekliyor?"
    "En sonunda keki yiyorum."
    "Krema tatlı ve lezzetli. Kendisi mi yaptı acaba?"
    mc "Bu çok güzel."
    mc "Teşekkürler, Natsuki."
    n 42c "Ş-Şey... elbette güzel olacak!"
    n "Ben bir profesyonelim ne de olsa!"
    n 42a "Bana teşekkür etmene falan gerek yok..."
    show natsuki zorder 1 at thide
    hide natsuki
    "Natsuki övgüyü kabul etmekte zorlanırken Yuri ellerinde bir çay setiyle masaya geri dönüyor."
    "Çaydanlığı kapkek tepsisinin önüne koymadan önce dikkatlice her birimizin önüne bir fincan koyuyor."
    show yuri 1a zorder 2 at t11
    mc "Sınıfta çay seti mi tutuyorsunuz?"
    y "Merak etme, öğretmenler izin verdi."
    y "Hem, sıcak bir fincan çay kitap okurken iyi gelir, değil mi?"
    mc "Ah... sa-sanırım..."
    show natsuki 2y at f31
    n "Ehehe. Şimdiden yeni üyemizi etkilemeye çalışıyorsun ha, Yuri?"
    show natsuki at t31
    show yuri at f11
    y 3n "Ha?! B-Ben öyle..."
    show yuri at t11
    show natsuki at thide
    hide natsuki
    "Alınan Yuri bakışlarını kaçırıyor."
    y 4b "İçimden geldiğinden, cidden..."
    mc "Sana inanıyorum."
    mc "Şey, kitabın yanında çay içmeyi denemedim ama en azından çayı severim."
    y 2u "Sevindim..."
    "Yuri rahatlayarak gülümsüyor kendine hafif bir şekilde."
    y 1a "E, [player], ne gibi şeyler okumayı seversin?"
    mc "Şey... Ah..."
    "Son yıllarda ne kadar az şey okuduğumu hesaba katarsak, bu soruya verebileceğim çok iyi bir yanıt yok."
    mc "... Manga..."
    "Diyorum kısık bir sesle, biraz da şaka yaparmışçasına."
    show natsuki 1c zorder 2 at t41
    "Natsuki aniden kafasını kaldırıyor."
    "Sanki bir şey söylemek istiyormuş gibi, ama susuyor."
    show natsuki zorder 1 at thide
    hide natsuki
    y 3u "P-Pek kitap okuyan birisi değilsin galiba..."
    mc "... Öyle, ama bu değişebilir..."
    "Ne diyorum ben?"
    "Yuri’nin üzgün gülümsemesini gördükten sonra düşünmeden konuştum."
    mc "Her neyse, ya sen, Yuri?"
    y 1l "Bakalım..."
    "Yuri parmaklarını fincanın ağzında gezdiriyor."
    y 1a "Ben en çok derin ve karmaşık fantastik evrenleri konu alan romanları seviyorum."
    y "Onların arkasındaki yaratıcılık ve incelik beni büyülüyor."
    y 1f "Ve böylesine yabancı bir dünyada geçen güzel bir hikâyeyi aktarabilmek de eşit derecede inanılmaz."
    "Yuri tutkulu bir şekilde kitap zevkinden bahsetmeye devam ediyor."
    "Yuri, içeri ilk girdiğimde epey çekingen davranıyordu. Şimdi kitaplardan bahsederken gözlerinin parlamasından anlıyorum ki, kitapların dünyasında daha çok rahat buluyor, insanların dünyasında değil."
    y 2m "Ama doğrusu, birçok şeyden hoşlanırım."
    y 2a "Çok kitap okumuyor olsan da gözün korkmasın, tamam mı?"
    y "İkimizin de ortak olarak seveceği bir şey bulabileceğimize eminim."
    show yuri at t22
    show natsuki 2c at f21
    n "Hey, Yuri..."
    show natsuki at t21
    show yuri at f22
    y 2f "Ha?"
    show yuri at t22
    show natsuki at f21
    n 2h "Şey, hani... İlk dediği şey var ya..."
    show natsuki at t21
    mc "Manga mı?"
    show yuri at f22
    y 2i "Evet..."
    y "Natsuki kulüp odasında manga okur da--"
    show yuri at t22
    show natsuki at f21
    n 1r "S-Söylemesene!!"
    "Nedense Natsuki bundan utanıyor gibi görünüyor."
    n 1q "Ayrıca..."
    n "Manga... da edebiyattır, biliyor muydun?"
    n 1w "O yüzden... eğer [player] mangalarımı okumak isterse onu durdurmaya falan kalkma!"
    show natsuki 1i at t21
    show yuri at f22
    y 1l "Natsuki..."
    y "Öyle bir şey yapmam."
    y 1i "Ancak, farklı şeyler denememiz de iyi olabilir..."
    y "O bu şansı değerlendirip yeni bir şeyler deneyebilir."
    y 1s "Sence de öyle değil mi, [player]?"
    show yuri at t33
    show natsuki at t32
    show sayori 1l at f31
    s "B-Belki--"
    "Ortalığın kızıştığını anlayan Sayori araya giriyor."
    s 1x "Belki hepimiz yeni bir şey deneyebiliriz!"
    s 1l "Bence eğlenceli olabilir..."
    s 1c "Hem böylelikle birbirimizi biraz daha tanımış oluruz!"
    s 1l "Demek istiyorum ki..."
    s "Edebiyat kulüpleri böyle şeyler yapıyor... değil mi?"
    show sayori at t31
    show yuri at f33
    y 1v "..."
    y "K-Katılmıyor falan değilim..."
    show yuri at t33
    show natsuki at f32
    n 2j "Evet..."
    n "Her zamanki gibi haklısın, Başkan."
    show natsuki at t32
    show sayori at f31
    s 1q "Ehehe~"
    show sayori at t31
    show natsuki at f32
    n 2c "Galiba bu bir roman falan okumaya başlamam gerektiği anlamına geliyor, ha?.."
    show natsuki at t32
    mc "Eh, buna ben de dahilim..."
    mc "Bunu tek ben yapmadığım sürece bir sorun olmaz benim için."
    show sayori at thide
    hide sayori
    show natsuki at f21
    show yuri at t22
    n 2y "Yuri de..."
    show natsuki at t21
    show yuri at f22
    y 2n "Ha?.."
    y "Bir... Bir manga mı okumalıyım?.."
    show yuri at t22
    show natsuki at f21
    n 4i "Of..."
    n 4h "Farklı şeyler denememizi öneren sendin!"
    n "Biraz daha açık fikirli olmalısın..."
    n 4u "Böylesi biraz can yakıcı..."
    show natsuki at t21
    show yuri at f22
    y 2t "Can yakıcı mı?.."
    y 2v "F-Fark etmedim..."
    y "..."
    "Yuri suçlu bir yüz ifadesiyle kendi düşüncelerine dalıyor."
    y 2w "Zevklerine saygısızlık ettiğim için üzgünüm, Natsuki."
    y "Eğer... Eğer mangalar ilgi alanınsa eminim ki edebiyatın saygıdeğer bir biçimidir."
    show yuri at t22
    show natsuki at f21
    n 5q "... Bunu cidden sen mi söylüyorsun?"
    show natsuki at t21
    show yuri at f22
    y "Hayır..."
    y "Hatamın farkına vardım."
    y 2t "O yüzden, eğer bir romana başlamak istiyorsan..."
    y 2u "... Sana olan şükranımı seve seve bir manga okumaya başlayarak gösteririm."
    show yuri at t22
    show natsuki at f21
    n 1l "Gerçekten mi?!"
    n 12c "Y-Yani..."
    n "Benim... için bunu yapman beni mutlu eder, Yuri."
    n 2c "Sana gerçekten seveceğin bir şey bulacağıma dair bana güvenebilirsin, tamam mı?"
    show natsuki at t21
    show yuri at f22
    y 1m "Aynen, sen de bana güvenebilirsin..."
    y 1h "Kulüp toplantısından sonra kitapçıya gideceğim muhtemelen."
    show yuri at t22
    show natsuki at f21
    n 1q "Tek... Tek başına mı?"
    show natsuki at t21
    show yuri at f22
    y 3q "A-Ah--"
    y 4a "Benimle birlikte... gelmek ister misin?"
    show yuri at t22
    show natsuki at f21
    n 5s "Şey..."
    n "Senin için sıkıntı olmayacaksa..."
    show natsuki at t21
    show yuri at f22
    y 3t "Hiç de bile!"
    y "Hep yalnız gidiyorum zaten..."
    show yuri at t22
    show natsuki at f21
    n "Evet, ben de..."
    show natsuki at t21
    show sayori 4s at l41
    s "Çok şirin~!"
    mc "Sayori, kapa çeneni..."
    show sayori at lhide
    hide sayori
    show natsuki at f21
    n 2j "Oraya gidince sana birkaç manga gösteririm, tamam mı?"
    show natsuki at t21
    show yuri at f22
    y 1a "Tamam."
    y "Bunun için sabırsızlanıyorum."
    show natsuki at thide
    show yuri at thide
    hide natsuki
    hide yuri
    "Natsuki ve Yuri ortalığı toplamaya başlıyor."
    show sayori 1q at t11
    s "Ehehe~"
    s 1x "Galiba toplantı bitti, ha?"
    mc "Evet, öyle görünüyor..."
    mc "Herkesin iyi anlaştığını görmek güzel."
    s 1q "Değil mi ya?"
    s 1d "Sanırım herkes senden hoşlandı, [player]."
    mc "Öyle mi düşünüyorsun?.."
    mc "Sen varken herkes biraz daha iyi anlaşıyor gibi görünüyor, Sayori."
    s 1y "Yaaa, [player]~"
    s "Deme öyle, utandırıyorsun beni!"
    mc "Her neyse."
    mc "Bir kulüp kuracağını söylediğinde şaşırmıştım..."
    mc "Ama bence işleri iyi hallediyorsun."
    s 1r "Bu kulübü en iyi kulüp hâline getireceğiz!"
    s 1x "Şimdi sen de katılınca her gün çok eğlenceli olacak."
    stop music fadeout 2.0
    s 1a "Hey, [player]..."
    s "Sana gerçekten teşekkür etmek istiyorum."
    s "Ya, kulübe katıldığın için falan çok mutluyum..."
    s "Ama gerçek şu ki, katılacağını zaten biliyordum."
    s 1q "Ehehe~"
    s 1a "Aslında başka bir şey daha var."
    $ if all(clear for clear in persistent.clear): persistent.clearall = True
    if persistent.clearall:
        call ch40_clearall
    else:
        call ch40_clearnormal
    window hide(None)
    window auto
    $ quick_menu = False
    return

    label ch40_clearnormal:
        show sayori 1a zorder 2 at t11
        s "Monika’dan kurtulduğun için teşekkür etmek istedim."
        play music hb
        show black:
            alpha 0.5
            parallel:
                0.36
                alpha 0.5
                repeat
            parallel:
                0.49
                alpha 0.475
                repeat
        show layer master at heartbeat
        s 1b "Bu doğru..."
        s "Onun yaptığı her şeyi biliyorum."
        s 1x "Belki de Başkan artık ben olduğumdan."
        s "Ama gerçekten her şeyi biliyorum, [player]."
        s 1q "Ehehe~"
        s 1d "Herkesi mutlu etmek için ne kadar çabaladığını biliyorum."
        s "Monika’nın herkesi üzmek için yaptığı bütün o kötü şeyleri biliyorum..."
        s 1b "Ama artık bunların bir önemi yok."
        s "Artık sadece biz varız.{nw}"
        show screen tear(20, 0.1, 0.1, 0, 40)
        play sound "sfx/s_kill_glitch1.ogg"
        pause 0.25
        stop sound
        hide screen tear
        show room_glitch zorder 1:
            xoffset -5
            0.1
            xoffset 5
            0.1
            linear 0.1 alpha 0.6
            linear 0.1 alpha 0.8
            0.1
            alpha 0
        s "Artık sadece biz varız.{fast}"
        hide room_glitch
        s 1d "Ve sen beni bütün dünyanın en mutlu kızı yaptın."
        s "Her günü böyle geçirmek için sabırsızlanıyorum..."
        s "Seninle birlikte."
        play sound "sfx/s_kill_glitch1.ogg"
        show room_glitch zorder 1:
            xoffset -10
            0.1
            xoffset 0
            0.1
            linear 0.1 alpha 0.6
            linear 0.1 alpha 0.8
            0.1
            alpha 1.0
        pause 0.3
        stop sound
        s 1q "İlelebet..."
        hide sayori
        show sayori 1a onlayer screens zorder 101 at face
        s "İ"
        s "l"
        s "e"
        show screen tear(20, 0.1, 0.1, 0, 40)
        play sound "sfx/s_kill_glitch1.ogg"
        pause 0.25
        stop sound
        hide screen tear
        s "l"
        s "e"
        s "b"
        window show(None)
        stop music
        call screen dialog("Hayır...", ok_action=Return())
        show layer master
        hide black
        show sayori end-glitch onlayer screens
        s "... Ha?"
        s "N-Neler oluyor?.."
        call screen dialog("Onu incitmene izin vermeyeceğim.", ok_action=Return())
        s "Kim..."
        s "C-Canım yanıyor--"
        show screen tear(20, 0.1, 0.1, 0, 40)
        window hide(None)
        play sound "sfx/s_kill_glitch1.ogg"
        hide sayori onlayer screens
        pause 0.35
        stop sound
        hide screen tear
        window show(None)
        s "Ah--"
        call screen dialog("Üzgünüm... Yanıldım.", ok_action=Return())
        call screen dialog("Burada sahiden hiç mutluluk yok...", ok_action=Return())
        call screen dialog("Elveda, Sayori.", ok_action=Return())
        call screen dialog("Elveda, [player].", ok_action=Return())
        call screen dialog("Elveda, Edebiyat Kulübü.", ok_action=Return())
        $ gtext = glitchtext(120)
        s "[gtext]{nw}"
        show screen tear(20, 0.1, 0.1, 0, 40)
        window hide(None)
        play sound "sfx/s_kill_glitch1.ogg"
        pause 0.35
        stop sound
        hide screen tear
        scene black
        pause 3.0
        return

    label ch40_clearall:
        s "Hepimizle bu kadar vakit geçirdiğin için teşekkür etmek istedim."
        play music mend
        s 2d "Her birimizi mutlu etmek için çok çabaladın."
        s "Zor zamanlarımızda bize destek oldun."
        s "Ve birbirimizle iyi geçinmemiz için yardımcı oldun."
        s 1a "Anlıyor musun, [player]?"
        s "Artık Başkan ben olduğum için her şeyi anlıyorum."
        s 1q "Bu oyunda hiçbir şeyi görmeden geçmek istemedin, değil mi?"
        s 1a "Oyunu pek çok kez kaydedip farklı yerlerden devam ettin, sırf herkesle olabildiğince vakit geçirdiğinden emin olmak için."
        s "Sadece Edebiyat Kulübü’nü içtenlikle önemseyen biri bu kadar ileri gider."
        s "Ama..."
        s 4d "En başından beri tek istediğim şey buydu."
        s "Herkesin mutlu olması ve birbirini önemsemesi."
        s 4q "Ahaha..."
        s 1t "Bu biraz üzücü ya, biliyor musun?"
        s "Bizim için yaptıklarının karşılığında senin için yapabileceğim çok fazla bir şey yok."
        s "Oyunun sonuna geldik."
        s 1y "O yüzden..."
        s "Burada birbirimize veda edeceğiz."
        s 1d "{i}Doki Doki Edebiyat Kulübü{/i}’nü oynadığın için teşekkürler."
        s "Seni özleyeceğim, [player]."
        s "Arada sırada uğra, olur mu?"
        s "Biz hep senin için burada olacağız."
        s 1t "Hepimiz..."
        scene black with dissolve_cg
        s "Hepimiz seni seviyoruz."
        stop music fadeout 2.0
        scene black
        with Dissolve(2.0)
        return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
