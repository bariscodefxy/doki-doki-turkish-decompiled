image exception_bg = "#dadada"
image fake_exception = Text("Beklenmedik bir hata meydana geldi.", size=40, style="_default")
image fake_exception2 = Text("“game/script-ch5.rpy” dosyası, 307. satır\nAyrıntılar için traceback.txt’ye göz atın.", size=20, style="_default")

image splash_glitch:
    subpixel True
    "images/bg/splash-glitch.png"
    alpha 0.0
    pause 0.5
    linear 0.5 alpha 1.0
    pause 2.5
    linear 0.5 alpha 0.0
    "gui/menu_bg.png"
    topleft
    alpha 0.0
    parallel:
        xoffset 0 yoffset 0
        linear 0.25 xoffset -100 yoffset -100
        repeat
    parallel:
        linear 0.5 alpha 1.0
    parallel:
        ypos 0
        pause 1.0
        easeout 1.0 ypos -500
image splash_glitch2:
    subpixel True
    "gui/menu_bg.png"
    topleft
    block:
        xoffset 0 yoffset 0
        linear 0.05 xoffset -100 yoffset -100
        repeat

image splash_glitch_m:
    subpixel True
    "gui/menu_art_m.png"
    zoom 0.5
    xpos 0.5 ypos 0.5
    pause 0.1
    parallel:
        xpos 0.3 ypos 1.2
        linear 0.08 ypos 0.1
        repeat
    parallel:
        pause 0.5
        alpha 0.0

image splash_glitch_n:
    subpixel True
    "gui/menu_art_n.png"
    zoom 0.5
    pause 0.2
    xpos 0.8 ypos 0.8
    pause 0.05
    xpos 0.2 ypos 0.7
    pause 0.05
    xpos 0.4 ypos 0.2
    pause 0.05
    xpos 0.7 ypos 1.2
    pause 0.05
    xpos 0.1 ypos 1.0
    pause 0.05
    xpos 0.2 ypos 0.6
    pause 0.05
    xpos 0.9 ypos 0.4
    pause 0.05
    alpha 0.0

image splash_glitch_y:
    subpixel True
    "gui/menu_art_y.png"
    zoom 0.5
    ypos 1.3
    block:
        xpos 0.85
        pause 0.02
        xpos 0.81
        pause 0.02
        repeat


label ch5_main:
    stop music fadeout 2.0
    scene bg residential_day
    with dissolve_scene_full

    "Festival bugün."
    "Özellikle bugün okula Sayori’yle birlikte gitmeyi umuyordum."
    "Ama Sayori telefonunu açmıyor."
    "Onu uyandırmaya evine gitmeyi düşündüm ama bunun biraz aşırıya kaçacağına karar verdim."
    "Bu sırada, etkinlik hazırlıkları tamamlanmak üzere."
    if ch4_scene == "natsuki":
        "Kapkekleri dikkatlice, iki tepsiyi üst üste koyarak kendi başıma taşımayı başardım."
        "Natsuki beni mesaj yağmuruna tutuyor; ama ellerim dolu olduğundan yanıt veremiyorum."
    else:
        "Yuri’yle birlikte boyadığımız pankart kurudu bile. Pankartı nazikçe rulo yapıp yanımda getiriyorum."
        "Yuri bana hiçbir şeyi unutmamam gerektiğini hatırlatan güzel bir mesaj attı, ben de ona endişelenmemesini söyledim."
    "İşin komiği, etkinlik hakkında hissettiklerim muhtemelen Natsuki’nin hissettikleriyle aynı."
    "Etkinliğin bitimi için daha heyecanlıyım çünkü Sayori ve [ch4_name] ile birlikte zaman geçirebileceğim."
    "Ama Monika’yı tanıyorsam etkinlik de harika geçecek."

    scene bg club_day with wipeleft_scene
    show monika 5 zorder 2 at t11
    m "[player]!"
    m "İlk gelen sensin."
    m "Erken geldiğin için teşekkürler!"
    mc "Tuhaf, en azından Yuri gelmiştir diye düşünmüştüm."
    "Monika sınıftaki sıraların her birinin üstüne küçük broşürler koyuyor."
    "Bu broşürler, Monika’nın sunacağımız şiirler için hazırladıkları broşürler olsa gerek."
    "Neticede gidip internetten Monika’nın beğeneceğini düşündüğüm bir şiir bulup onu yolladım."
    "Sunacağım şiir de o şiir olacak yani."
    m 1d "Sayori’yi yanında getirmemene şaşırıdm."
    mc "Evet, yine uyuyakalmış..."
    mc "Şu budala yok mu."
    mc "Bu kadar önemli bir günü biraz diye ciddiye alır sanıyor insan..."
    "Öyle diyorum ama aniden dün Sayori’nin bana söylediklerini hatırlıyorum..."
    "Ve birden bunun, Sayori için o kadar da basit olamayacağının bilincine varıp kendimi kötü hissediyorum."
    "Eskiden onun hakkında böyle düşündüğüm için böyle söylemiştim."
    "Ama..."
    "Belki de gidip onu uyandırmalıydım?"
    m 1k "Ahaha."
    m 4b "Onun hakkında biraz sorumluluk almalısın, [player]!"
    m "Özellikle dünkü karşılaşmanızdan sonra yani..."
    m "Onu bu sabah biraz muallakta bıraktın."
    show monika 4a
    mc "Karşılaşma mı?.."
    mc "Monika-- Bunu biliyor muydun??"
    m 2a "Tabii ki biliyorum."
    m "Kulüp başkanıyım ne de olsa."
    mc "Ama--!"
    "Kekeliyorum, utanarak."
    "Sayori her şeyi ona bu kadar çabuk mu anlattı?"
    if sayori_confess:
        "Sevgili... olduğumuzu yani."
        "Henüz kimseye bundan bahsetmemeyi planlıyordum..."
    else:
        "Düpedüz onun duygularını geri çevirişimi yani."
        "Böyle olunca kötü taraf benmişim gibi duruyor..."
        "Ama onun için en iyisini ben biliyorum, değil mi?"
    mc "Of..."
    mc "Olanların hepsini bilmiyorsun..."
    m 2j "Merak etme."
    m "Muhtemelen sandığından daha fazlasını biliyorum."
    mc "Ha?.."
    "Monika her zamanki gibi canayakın davranıyor; ama nedense bunu deyişinden sonra tüylerim diken diken oldu."
    m 5 "Hey, broşürlere bir bakmak ister misin?"
    m "Çok iyi oldular!"
    mc "Tabii, olur."
    "Sıralara konulmuş broşürlerden birini aldım."
    mc "Evet, gerçekten güzel olmuşlar."
    mc "Böyle bir şey kesinlikle insanların kulübümüzü ciddiye almalarını sağlayacak."
    m "Evet, ben de öyle düşündüm!"
    show monika zorder 1 at thide
    hide monika
    "Sayfaları çeviriyorum."
    "Herkesin şiirinin ayrı sayfalara güzelce bastırılmış olması broşürlere profesyonellik katmış."
    "Natsuki ve Yuri’nin şiirleri, provada okudukları şiirler olduklarından onları hemencecik tanıyorum."
    mc "Bu da ne?"
    "Sayori’nin şiirine bakıyorum."
    "Provada okuduğundan farklı bir şiir."
    "Bu şiirini daha önce okumamıştım..."
    call showpoem (poem_s3, music=False)
    mc "Ah--"
    "Bu ne ya?.."
    "Şiiri okuyunca içim ürperiyor."
    show monika 1d zorder 2 at t11
    m "[player]?"
    m "Sorun ne?"
    mc "Şey, hiç..."
    "Bu şiir Sayori’nin yazdığı her şeyden tamamen farklı görünüyor."
    "Ama dahası..."
    mc "F-Fikrimi değiştirdim!"
    mc "Sayori’yi almaya gideceğim..."
    m "A--"
    m 1b "Pekâlâ, tamam!"
    m "Geç kalmayın, tamam mı?"
    scene bg corridor with wipeleft
    "Çabucak sınıftan çıkıyorum."
    m "Kendini yorma~"
    "Diyor Monika, peşimden."
    "Adımlarımı hızlandırıyorum."

    scene bg residential_day with wipeleft_scene
    "Ne düşünüyordum ben?"
    "Sayori için biraz daha çabalamam gerekirdi."
    "En azından onu beklemek veya onu uyandırmak zahmetli bir şey değil."
    "Okula birlikte gitmek gibi basit bir şey bile onu gerçekten mutlu ediyor."
    "Ayrıca..."
    "Dün ona her şeyin eskisi gibi olacağını söyledim."
    "Tüm ihtiyacı olan ve benim vermek istediğim şey de bu."

    scene bg house with wipeleft
    "Sayori’nin evine varıyorum ve kapıyı tıklatıyorum."
    "Telefonunu da açmadığından cevap vermesini beklemiyorum."
    "Dünkü gibi kapıyı açıp içeri giriyorum."
    scene black with wipeleft
    mc "Sayori?"
    "Uykusu cidden ağır..."
    "Yutkunuyorum."
    "Bunu yapmak zorunda kaldığıma inanamıyorum çünkü."
    "Onu evine gelip uyandırmak..."
    if sayori_confess:
        "Bu gerçekten bir sevgilinin yapacağı türden bir şey, değil mi?"
    else:
        "Bu daha çok bir sevgilinin yapacağı türden bir şey değil mi?"
    "Her neyse..."
    "Bir sorun olacağını düşünmüyorum."

    "Sayori’nin odasının kapısını tıklatıyorum."
    mc "Sayori?"
    mc "Uyansana budala şey..."
    "Cevap yok."
    "Gerçekten odasına bu şekilde girmeyi istemezdim..."
    "Bu bir nevi özel hayatın gizliliğine aykırı değil mi?"
    "Ama bana başka çare bırakmıyor."
    "Kapıyı yavaşça açıyorum."
    mc "{cps=30}....... Sayo--{/cps}{nw}"
    $ persistent.playthrough = 1
    $ persistent.anticheat = renpy.random.randint(100000, 999999)
    $ delete_character("sayori")
    $ in_sayori_kill = True
    window hide(None)
    window auto
    play music td
    show s_kill_bg2
    show s_kill2
    show s_kill_bg as s_kill_bg at s_kill_bg_start
    show s_kill as s_kill at s_kill_start
    pause 3.75
    show s_kill_bg2 as s_kill_bg
    show s_kill2 as s_kill
    pause 0.01
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.25
    stop sound
    hide screen tear
    hide s_kill_bg
    hide s_kill
    show s_kill_bg_zoom zorder 1
    show s_kill_bg2_zoom zorder 1
    show s_kill_zoom zorder 3
    show s_kill2_zoom zorder 3
    show s_kill as s_kill_zoom_trans zorder 3:
        truecenter
        alpha 0.5
        zoom 2.0 xalign 0.5 yalign 0.05
        pause 0.5
        dizzy(1, 1.0)
    pause 2.0
    show noise zorder 3:
        alpha 0.0
        linear 3.0 alpha 0.25
    show vignette zorder 3:
        alpha 0.0
        linear 3.0 alpha 0.75
    pause 1.5
    show white zorder 2
    show splash_glitch zorder 2
    pause 1.5
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.2
    stop sound
    hide screen tear
    pause 4.0
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.2
    stop sound
    hide screen tear
    hide splash_glitch
    show splash_glitch2 zorder 2
    show splash_glitch_m zorder 2
    show splash_glitch_n zorder 2
    show splash_glitch_y zorder 2
    pause 0.75
    hide white
    hide splash_glitch2
    hide splash_glitch_m
    hide splash_glitch_n
    hide splash_glitch_y
    show exception_bg zorder 2
    show fake_exception zorder 2:
        xpos 0.1 ypos 0.05
    show fake_exception2 zorder 2:
        xpos 0.1 ypos 0.15
    python:
        try: sys.modules['renpy.error'].report_exception("Of ya... Bir şeyi bozmadım değil mi? Dur bi' saniye, bunu düzeltebilirim... sanırım... Aslında var ya, onu silmek çok daha kolay olur. Her şeyi zorlaştıran o ne de olsa. Ahaha! Her neyse, hadi bakalım.", False)
        except: pass
    pause 6.0


    "..."
    hide fake_exception
    hide fake_exception2
    hide exception_bg
    "Ne oluyor lan?.."
    "{i}Ne oluyor lan??{/i}"
    "Kabus mu bu?"
    "Kabus... olmalı."
    "Bu gerçek değil."
    "Bu gerçek olamaz."
    "Sayori bunu yapmaz."
    "Her şey birkaç gün öncesine kadar normaldi."
    "Bu yüzden gözlerimin bana gösterdiği şeye inanamıyorum!.."
    scene black with dissolve_cg
    "Kusma isteğimi bastırıyorum."
    "Daha dün..."
    "Sayori’ye destek olacağımı söyledim."
    "Ona onun için en iyisinin ne olduğunu bildiğimi, her şeyin düzeleceğini söyledim."
    "Öyleyse neden?.."
    "Bunu neden yapsın?.."
    "Nasıl bu kadar çaresiz olabilirim?"
    "Nerede hata yaptım?"
    if sayori_confess:
        "Ona duygularımı itiraf ettim..."
        "Ona itirafta bulunmamalıydım."
        "Sayori’nin ihtiyacı olan şey bu değildi."
        "Bana insanların onu önemsemesinin ona ne kadar acı verdiğini söylemişti bir de."
        "Öyleyse neden ona itirafta bulunup daha da kötü hissetmesine sebep oldum?"
    else:
        "Duygularını geri çevirdim..."
        "Bardağı taşıran son damla bu olmalıydı."
        "Onun acı içindeki çığlığı hâlâ kulaklarımda yankılanıyor."
        "Neden bana en çok ihtiyacı olduğu anda böyle bir şey yaptım?"
    "Neden bu kadar bencilce davrandım?"
    "Her şey benim suçum--!"
    "Beynime hücum eden düşüncelerim, bunu önlemek için zamanında yapmış olmam gereken şeyleri söyleyip duruyor durmadan."
    "Sadece onunla biraz daha fazla zaman geçirseydim."
    "Okula onunla birlikte gitseydim."
    if sayori_confess:
        "Ve her zaman olduğu gibi onunla arkadaş kalsaydım..."
    else:
        "Ve ilişkimizden beklediğini bildiğim şeyleri karşılasaydım..."
    "... Bunu önleyebilirdim."
    "Bunu önleyebilirdim, bundan eminim!"
    "Edebiyat Kulübü’nün de..."
    "... festivalin de canı cehenneme."
    "En iyi... arkadaşımı kaybettim ben."
    "Birlikte büyüdüğüm birisini."
    "O sonsuza dek gitti."
    "Yapabileceğim hiçbir şey onu geri getiremez."
    "Her şeyi sıfırlayıp farklı bir şey deneyebileceğim bir oyunda değilim ben."
    "Tek bir şansım vardı; ama iyi değerlendirmedim."
    "Şimdi ölene dek bu suçluluk duygusuyla yaşayacağım."
    "Hayatımdaki hiçbir şey onun hayatından değerli değil..."
    "Ama yine de onun benden ihtiyaç duyduğu şeyi yapamadım."
    "Ve şimdi..."
    "Olanları asla geri alamam."
    "Asla."
    "Asla."
    "Asla."
    "Asla."
    "Asla..."
    $ in_sayori_kill = False


    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
