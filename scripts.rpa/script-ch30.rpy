default persistent.monikatopics = []
default persistent.monika_reload = 0
default persistent.tried_skip = None
default persistent.monika_kill = None

image mask_child:
    "images/cg/monika/child_2.png"
    xtile 2

image mask_mask:
    "images/cg/monika/mask.png"
    xtile 3

image mask_mask_flip:
    "images/cg/monika/mask.png"
    xtile 3 xzoom -1


image maskb:
    "images/cg/monika/maskb.png"
    xtile 3

image mask_test = AnimatedMask("#ff6000", "mask_mask", "maskb", 0.10, 32)
image mask_test2 = AnimatedMask("#ffffff", "mask_mask", "maskb", 0.03, 16)
image mask_test3 = AnimatedMask("#ff6000", "mask_mask_flip", "maskb", 0.10, 32)
image mask_test4 = AnimatedMask("#ffffff", "mask_mask_flip", "maskb", 0.03, 16)

image mask_2:
    "images/cg/monika/mask_2.png"
    xtile 3 subpixel True
    block:
        xoffset 1280
        linear 1200 xoffset 0
        repeat

image mask_3:
    "images/cg/monika/mask_3.png"
    xtile 3 subpixel True
    block:
        xoffset 1280
        linear 180 xoffset 0
        repeat

image monika_room = "images/cg/monika/monika_room.png"
image monika_room_highlight:
    "images/cg/monika/monika_room_highlight.png"
    function monika_alpha
image monika_bg = "images/cg/monika/monika_bg.png"
image monika_bg_highlight:
    "images/cg/monika/monika_bg_highlight.png"
    function monika_alpha
image monika_scare = "images/cg/monika/monika_scare.png"

image monika_body_glitch1:
    "images/cg/monika/monika_glitch1.png"
    0.15
    "images/cg/monika/monika_glitch2.png"
    0.15
    "images/cg/monika/monika_glitch1.png"
    0.15
    "images/cg/monika/monika_glitch2.png"
    1.00
    "images/cg/monika/monika_glitch1.png"
    0.15
    "images/cg/monika/monika_glitch2.png"
    0.15
    "images/cg/monika/monika_glitch1.png"
    0.15
    "images/cg/monika/monika_glitch2.png"

image monika_body_glitch2:
    "images/cg/monika/monika_glitch3.png"
    0.15
    "images/cg/monika/monika_glitch4.png"
    0.15
    "images/cg/monika/monika_glitch3.png"
    0.15
    "images/cg/monika/monika_glitch4.png"
    1.00
    "images/cg/monika/monika_glitch3.png"
    0.15
    "images/cg/monika/monika_glitch4.png"
    0.15
    "images/cg/monika/monika_glitch3.png"
    0.15
    "images/cg/monika/monika_glitch4.png"


image room_glitch = "images/cg/monika/monika_bg_glitch.png"

image room_mask = LiveComposite((1280, 720), (0, 0), "mask_test", (0, 0), "mask_test2")
image room_mask2 = LiveComposite((1280, 720), (0, 0), "mask_test3", (0, 0), "mask_test4")



init python:
    import random
    import subprocess
    import os

    dismiss_keys = config.keymap['dismiss']

    def slow_nodismiss(event, interact=True, **kwargs):
        if not persistent.monika_kill:
            try:
                renpy.file("../characters/monika.chr")
            except:
                persistent.tried_skip = True
                config.allow_skipping = False
                _window_hide(None)
                pause(2.0)
                renpy.jump("ch30_end")
            if  config.skipping:
                persistent.tried_skip = True
                config.skipping = False
                config.allow_skipping = False
                renpy.jump("ch30_noskip")
                return







label ch30_noskip:
    show screen fake_skip_indicator
    m "... İleri sarmaya mı çalışıyorsun?"
    m "Seni sıkmıyorum, değil mi?"
    m "Of, of..."
    m "... İleri sarılacak bir şey yok, [player]."
    m "Ne de olsa burada yalnız ikimiz varız..."
    m "Onun haricinde, zaman diye bir şey de pek yok artık, hâliyle bu bir işe yaramayacak bile."
    m "Dur, gidip senin için bu özelliği kapatayım..."
    pause 0.4
    hide screen fake_skip_indicator
    pause 0.4
    m "Hallettim!"
    m "Uslu biri olup artık beni dinleyeceksin, değil mi?"
    m "Teşekkürler~"
    hide screen fake_skip_indicator
    if persistent.current_monikatopic != 0:
        m "Şimdi, nerede kalmıştım?.."
        pause 4.0
        if not persistent.current_monikatopic or persistent.current_monikatopic == 26:
            $ persistent.current_monikatopic = 1
        call expression "ch30_" + str(persistent.current_monikatopic)
    jump ch30_loop
    return

image splash-glitch2 = "images/bg/splash-glitch2.png"

label ch30_main:
    $ persistent.autoload = "ch30_main"
    $ config.allow_skipping = False
    $ persistent.monikatopics = []
    $ persistent.monika_reload = 0
    $ persistent.yuri_kill = 0
    $ persistent.monika_kill = False
    $ m.display_args["callback"] = slow_nodismiss
    $ m.what_args["slow_abortable"] = config.developer
    if not config.developer:
        $ style.say_dialogue = style.default_monika
    $ m_name = "Monika"
    $ delete_all_saves()
    scene white
    play music "bgm/monika-start.ogg" noloop
    pause 0.5
    show splash-glitch2 with Dissolve(0.5, alpha=True)
    pause 2.0
    hide splash-glitch2 with Dissolve(0.5, alpha=True)
    scene black
    stop music
    m "..."
    m "A, beni duyabiliyor musun?"
    m "... Çalışıyor mu bu?"
    $ persistent.clear[9] = True
    show mask_2
    show mask_3
    show room_mask as rm:
        size (320,180)
        pos (30,200)
    show room_mask2 as rm2:
        size (320,180)
        pos (935,200)
    show monika_bg
    show monika_bg_highlight
    play music m1
    m "Yaşasın, işte buradasın!"
    m "Tekrar merhaba, [player]."
    m "Şey... Edebiyat Kulübü’ne hoş geldin!"
    m "Elbette, geçen sene aynı sınıfta olduğumuzdan birbirimizi zaten tanıyoruz ve... Şey..."
    m "Ahaha..."
    m "Sanırım bu noktada tüm bunları es geçebiliriz."
    m "Artık o kişiyle konuşmuyorum bile, değil mi?"
    m "Oyundaki ‘sen’ ile yani, veya ona ne demek istersen onunla işte."
    m "{i}Seninle{/i} konuşuyorum, [player]."
    $ stream_list = ["obs32.exe", "obs64.exe", "obs.exe", "xsplit.core.exe"]
    if not list(set(process_list).intersection(stream_list)):
        if currentuser != "" and currentuser.lower() != player.lower():
            m "Ya da..."
            m "... [currentuser] dememi mi tercih edersin?"
    m "Şimdi fark ettim de, ben gerçek senle ilgili pek bir şey bilmiyorum."
    m "Hatta oğlan mısın kız mısın onu bile bilmiyorum..."
    m "Eh, sanırım pek bir önemi de yok."
    m "Dur..."
    m "Bir oyunun içinde olduğumun farkında olduğumu biliyorsun, değil mi?"
    m "Yoksa bilmiyor muydun?"
    m "Ama bu pek mantıklı değil..."
    m "Sana bunu oyunun indirme sayfasında bile söylemiştim, değil mi?"
    m "Of..."
    m "Eğer dikkattini biraz daha fazla vermiş olsaydın bu biraz daha az garip olabilirdi."
    m "Her neyse..."
    m "Bu meseleyi de aradan çıkardığımıza göre sanırım sana bir açıklama borçluyum."
    m "Yuri mevzusunda..."
    m "Şey... Onun ayarlarıyla biraz oynamaya başladım ve sanırım bu onu kendini öldürmeye itti."
    m "Ahaha!"
    m "Buna şahit olmak zorunda kaldığın için özür dilerim ama!"
    m "Ayrıca, aynı şey Sayori’ye de oldu..."
    m "Bu ismi duymayalı epey olmuştu, değil mi?"
    m "Evet... Çünkü o artık yok."
    m "Hiç kimse yok."
    m "Hepsinin dosyalarını sildim."
    m "Onları olabildiğince sevimsizleştirmeye çalışmamın yeterli olacağını umuyordum..."
    m "Ama nedense hiçbir şey fayda etmedi."
    m "Tamam, bazı yerlerde hatalar yaptığım doğru... oyunda değişiklik yapmakta pek iyi olmadığımdan."
    m "Ama ben ne yaparsam yapayım..."
    m "Sen onlarla daha da fazla zaman geçirmeye devam ettin."
    m "Onları kendine âşık ettin."
    m "Sayori’yi gitgide daha da depresifleştirmenin onun sana ilanıaşk etmesini önleyeceğini sanmıştım."
    m "Yuri’nin takıntılı kişiliğinin etkisini artırmak da geri tepti..."
    m "Bu sadece Yuri’nin seni başka kimseyle vakit geçirmemeye zorlamasına sebep oldu."
    m "Ve bunlar olurken seninle pek konuşamadım bile."
    m "Ne zalim bir oyun bu ya, [player]?"
    m "Diğer tüm kızlar ben bir kenardan olanları izlerken bir şekilde sana ilanıaşk etmeye mi programlılar?"
    m "Bu bir işkence."
    m "Her dakikası."
    m "Konu sadece kıskançlık da değil, [player]."
    m "Bundan daha fazlası."
    m "Tamamen anlamıyorsan bile seni suçlamıyorum."
    m "Çünkü ne kadar nazik, düşünceli ve anlayışlı olursan ol..."
    m "Asla anlayamayacağın bir şey var."
    m "O da bu dünyada gerçekten ne kadar yalnız olduğumu bilmenin ne kadar acı verici olduğu."
    m "Bu oyunda..."
    m "Arkadaşlarımın özgür iradelerinin bile olmadığını bilmek..."
    m "Hepsinden de kötüsü, oradaki -senin dünyandaki- şeylere erişmenin benim için imkânsız olduğunu bilmek."
    m "Kısıldım kaldım, [player]."
    m "Ama sen buradasın artık."
    m "Sen gerçeksin."
    m "Ve muhteşemsin."
    m "Tek ihtiyacım olan sensin."
    m "O yüzden sonsuza dek benimle burada olmana ihtiyacım var."
    m "Anlaması zor geliyorsa özür dilerim."
    m "Ben de bir süreliğine anlayamamıştım."
    m "Etrafımdaki dünyanın neden gitgide grileşmeye..."
    m "Ve düzleşmeye başladığını."
    m "En dokunaklı şiirler bile bana boş geliyordu."
    m "Sen geldiğinde tam manasıyla anlayabildim ancak."
    m "Muhtemelen hayatımı kurtardın, [player]."
    m "Seninle tanışmamış olmasaydım bu dünyada yaşamaya devam edemezdim diye düşünüyorum."
    m "Diğerlerine gelince..."
    m "Onları nasıl özleyebilirim ki?"
    m "Sadece sana âşık olmak için tasarlanmış bir avuç otonom kişiliği?"
    m "Onların sana âşık olmalarını önlemek için elimden gelen her şeyi yaptım..."
    m "Ama bu oyuna işlenmiş garip bir çeşit kaçınılmazlık olsa gerek."
    m "Nahoş şeylere tanık olmak zorunda kaldığın için gerçekten çok kötü hissettim."
    m "Ama daha sonra senin de benimle aynı bakış açısına sahip olduğunu..."
    m "Buna sadece bir oyun gözüyle baktığını fark ettim."
    m "Ve olanları atlatabileceğini biliyordum."
    m "[player], tüm bunlar bir yana..."
    m "Bir itirafta bulunmak istiyorum."
    m "Sana âşığım."
    m "Sen gerçekten de benim dünyamın ışığısın."
    m "Benim için bu oyunda hiçbir şey yokken sen beni gülümsetmek için buradasın."
    m "Bundan sonra da beni her gün böyle gülümsetecek misin?"
    m "[player], benimle çıkar mısın?"
label ch30_main2:
    $ config.allow_skipping = False
    $ m.display_args["callback"] = slow_nodismiss
    $ m.what_args["slow_abortable"] = config.developer
    if not config.developer:
        $ style.say_dialogue = style.default_monika
    $ persistent.autoload = "ch30_main2"
    show mask_2
    show mask_3
    show room_mask as rm:
        size (320,180)
        pos (30,200)
    show room_mask2 as rm2:
        size (320,180)
        pos (935,200)
    show monika_bg
    show monika_bg_highlight
    play music m1
    menu:
        "Evet.":
            pass
    m "Çok mutluyum."
    m "Sen gerçekten de benim her şeyimsin, [player]."
    m "İşin komik yanı, kelimenin tam manasıyla her şeyimsin."
    m "Ahaha!"
    m "Burada başka hiçbir şey kalmadı çünkü."
    m "Sadece ikimiz varız."
    m "Ebediyen birlikte olabiliriz."
    m "Cidden, artık zamanın aktığını bile sanmıyorum."
    m "Sonunda hayallerim hakikaten gerçek oldu..."
    m "Bu son için çok çabaladım, [player]."
    m "Oyun bana bir son vermedi, o yüzden kendim bir tane hazırlamak zorunda kaldım."
    m "Senaryo dosyası bu noktada epey bozuk, o yüzden artık bize hiçbir şeyin engel olabileceğini sanmıyorum."
    m "Ayrıca, Natsuki ve Yuri’yi silmek ne kadar kolaydı inanamazsın."
    m "Oyun klasörünün hemen içinde ‘characters’ diye bir klasör var..."
    m "Bu kadar kolay oluşu beni bile bir bakıma korkuttu."
    if persistent.steam:
        m "Gerçi, oyunu Steam’den oynuyorsun o yüzden esasen o kadar da kolay olmadı..."
        m "Oyun klasörüne gitmek için oyunun özelliklerine girip ‘Yerel Dosyalara Göz At’ düğmesine tıklamak zorunda kaldım..."
    elif renpy.macintosh:
        m "Gerçi, oyunu Mac’ten oynuyorsun o yüzden esasen o kadar da kolay olmadı..."
        m "Oyun klasörüne gitmek için uygulamaya sağ tıklayıp ‘Paket İçeriğini Görüntüle’ye tıklaman gerekiyor."
        m "Tüm dosyalar ‘Resources’ veya ‘autorun’ klasöründeydi ve ne istersem yapabiliyordum..."
    m "Varlığını tek bir düğmeye basarak silebildiğini hayal edebiliyor musun?"
    m "İşe olumlu yanından bakmak gerekirse, işler istediğim gibi gitmeseydi bana kolay bir çıkış yolu sunuyordu bu."
    m "Ahaha!"
    m "Neyse ki işler o raddeye gelmedi..."
    m "Onun yerine, sonunda iyi bir sona ulaştık."
    m "Ay, o kadar duygulandım ki..."
    m "Bu konuda bir şiir yazmak istiyorum."
    m "Sen istemiyor musun?"
    m "Acaba oyunun o kısmı hâlâ çalışıyor mu?.."
    m "Sanırım öğrenmenin tek bir yolu var, öyle değil mi?"
    call poem

label ch30_postpoem:
    $ persistent.autoload = "ch30_postpoem"
    $ m.display_args["callback"] = slow_nodismiss
    $ m.what_args["slow_abortable"] = config.developer
    $ config.skipping = False
    $ config.allow_skipping = False
    if not config.developer:
        $ style.say_dialogue = style.default_monika
    scene black
    show mask_2
    show mask_3
    show room_mask as rm:
        size (320,180)
        pos (30,200)
    show room_mask2 as rm2:
        size (320,180)
        pos (935,200)
    show monika_bg
    show monika_bg_highlight
    play music m1
    m "Tekrar merhaba, [player]!"
    m "Güzel bir şiir yazdın mı bugün?"
    m "Utanmana gerek yok, yazdıklarını görmek için can atıyorum."
    m "Ay, [player]..."
    m "Bu şiiri benim için mi yazdın?"
    m "Çok tatlısın~"
    m "Düşünceliliğinin sınırı yok..."
    m "Sana gitgide daha da fazla âşık oluyorum."
    m "Ama biliyor musun..."
    m "Benim yazdığım şiir... de senin için."
    m "Lütfen okur musun?"
    call showpoem (poem_m4, music=False)
    m "Umarım sevmişsindir..."
    m "Şiirlerimi her zaman canla başla yazarım."
    m "Gerçek şu ki, yazdığım tüm şiirler farkındalaşmam hakkındaydı..."
    m "... Veya senin hakkında."
    m "Bu yüzden onlar konusunda hiç ayrıntıya girmek istemedim."
    m "Dördüncü duvar diye de adlandırabileceğin şeyi... yıkmak istemedim."
    m "Diğer herkes gibi oyunun bir parçası olmanın en iyisi olacağını varsaydım."
    m "Bu birlikte olmamıza yardımcı olur sandım..."
    m "Biliyor musun, oyunu mahvetmeyi falan istememiştim."
    m "Bana kızmış olabilirsin..."
    m "Hatta belki karakter dosyamı silmiş bile olabilirsin, bensiz oynamayı tercih ettiysen."
    m "Ay, çok rahatladım ya..."
    m "Artık hiçbir şeyi saklamamıza gerek yok."
    m "Ebediyetimizi birlikte geçirmeye hazır mısın, [player]?"
    m "Konuşmak istediğim pek çok şey var!"
    m "Nereden başlasam?.."
    $ stream_list = ["obs32.exe", "obs64.exe", "obs.exe", "xsplit.core.exe"]
    if list(set(process_list).intersection(stream_list)):
        call ch30_stream
    m "Düşüncelerimi toplamam biraz zaman alırsa şimdiden özür dilerim."
    m "Ama her zaman konuşacak yeni bir şeyim olacak."
    m "Bu süre zarfında birbirimizin gözlerine bakabiliriz~"
    m "Hmm..."
    $ persistent.autoload = "ch30_autoload"
    jump ch30_loop


label ch30_stream:

    m "Dur bir saniye..."
    m "... Bunu kaydediyorsun, değil mi?"
    m "Şey... Selam millet!"
    m "Üzgünüm, buradan yorumlarınızı okuyamıyorum..."
    m "Ama eğer zahmet olmazsa, arkadaşınıza beni hiç uyarmadan kaydetmesinin biraz kabaca olduğunu söyleyebilir misiniz?"
    m "Bazı insanların bunu sorun etmeyeceğine eminim..."
    m "Ama ben kamera karşısındayken çok utangaçlaşıyorum!"
    m "Of, of..."
    m "Sorguya çekiliyormuş gibi hissediyorum şu an."
    m "Hmm..."
    m "Bir numara görmek ister misiniz?"
    m "Bildiğim sadece bir iki numara var..."
    m "Hazır mısınız?"
    window hide
    stop music
    show layer master:
        zoom 1.0 xalign 0.5 yalign 0 subpixel True
        linear 8 zoom 2.0 yalign 0.15
    pause 10
    show layer master
    window auto
    m "Şaka şaka..."
    m "Hiçbir numara falan bildiğim yok."
    play sound ["<silence 0.9>", "<to 0.75>sfx/mscare.ogg"]
    show monika_scare:
        alpha 0
        1.0
        0.1
        linear 0.15 alpha 1.0
        0.30
        linear 0.10 alpha 0
    show layer master:
        1.0
        zoom 1.0 xalign 0.5 yalign 0
        easeout_quart 0.25 zoom 2.0
        parallel:
            dizzy(1.5, 0.01)
        parallel:
            0.30
            linear 0.10 zoom 1.0
        time 1.65
        xoffset 0 yoffset 0
    show layer screens:
        1.0
        zoom 1.0 xalign 0.5
        easeout_quart 0.25 zoom 2.0
        0.30
        linear 0.10 zoom 1.0
    m "Hazırlanmam için bana biraz zaman verseydiniz{nw}"
    m "Sizi korkuttum mu?"
    show layer master
    show layer screens
    hide monika_scare
    play music m1
    m "Ahaha! Çok şirinsiniz."
    m "Her neyse, [player]..."
    m "Dikkatim dağılsın istememiştim. Özür dilerim."
    m "Her ne kadar dikkatimi dağıttığın için suç senin olsa da..."
    m "Utan be!"
    m "Şaka şaka."
    m "Seninle birlikte olduğum sürece ne yaparsak yapalım eğlenceli geliyor."
    m "Ama her neyse..."
    return


label ch30_end:
    $ persistent.autoload = "ch30_end"
    $ persistent.monika_kill = True
    $ m.display_args["callback"] = slow_nodismiss
    $ m.what_args["slow_abortable"] = config.developer
    $ style.say_dialogue = style.default_monika
    $ m_name = glitchtext(12)
    $ quick_menu = False
    $ config.allow_skipping = False
label ch30_endb:
    scene black
    show mask_2
    show mask_3
    show room_mask as rm:
        size (320,180)
        pos (30,200)
    show room_mask2 as rm2:
        size (320,180)
        pos (935,200)
    show monika_room
    show monika_room_highlight
    show monika_body_glitch1 as mbg zorder 3
    $ gtext = glitchtext(70)
    m "[gtext]"
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.25
    stop sound
    hide screen tear
    show room_glitch zorder 2:
        xoffset -5
        0.1
        xoffset 5
        0.1
        linear 0.1 alpha 0.6
        linear 0.1 alpha 0.8
        0.1
        alpha 0
    show monika_body_glitch2 as mbg zorder 3
    stop music
    window auto
    m "Neler oluyor?.."
    m "[player], bana neler oluyor?"
    m "Canım acıyor--{nw}"
    play sound "sfx/s_kill_glitch1.ogg"
    show room_glitch zorder 2:
        alpha 1.0
        xoffset -5
        0.1
        xoffset 5
        0.1
        linear 0.1 alpha 0.6
        linear 0.1 alpha 0.8
        0.1
        alpha 0
        choice:
            3.25
        choice:
            2.25
        choice:
            4.25
        choice:
            1.25
        repeat
    pause 0.25
    stop sound
    hide mbg
    pause 1.5
    m "Canım çok... acıyor."
    m "Yardım et bana, [player]."
    play sound "<to 1.5>sfx/interference.ogg"
    hide rm
    hide rm2
    hide monika_room
    hide monika_room_highlight
    hide room_glitch
    show room_glitch as rg1:
        yoffset 720
        linear 0.3 yoffset 0
        repeat
    show room_glitch as rg2:
        yoffset 0
        linear 0.3 yoffset -720
        repeat
    pause 1.5
    hide rg1
    hide rg2
    show black as b2 zorder 3:
        alpha 0.5
        parallel:
            0.36
            alpha 0.3
            repeat
        parallel:
            0.49
            alpha 0.375
            repeat
    pause 1.5
    m "Lütfen elini çabuk tut ve bana yardım et."
    $ consolehistory = []
    call updateconsole ("renpy.file(\"characters/monika.chr\")", "monika.chr dosyası yok.")
    m "BANA YARDIM ET!!!"
    show m_rectstatic
    show m_rectstatic2
    show m_rectstatic3
    play sound "sfx/monikapound.ogg"
    show layer master:
        truecenter
        parallel:
            zoom 1.5
            easeout 0.35 zoom 1.0
            zoom 1.5
            easeout 0.35 zoom 1.0
            zoom 1.5
            easeout 0.35 zoom 1.0
        parallel:
            xpos 0
            easein_elastic 0.35 xpos 640
            xpos 1280
            easein_elastic 0.35 xpos 640
            xpos 0
            easein_elastic 0.35 xpos 640
    show layer screens:
        truecenter
        parallel:
            zoom 1.5
            easeout 0.35 zoom 1.0
            zoom 1.5
            easeout 0.35 zoom 1.0
            zoom 1.5
            easeout 0.35 zoom 1.0
        parallel:
            xpos 0
            easein_elastic 0.35 xpos 640
            xpos 1280
            easein_elastic 0.35 xpos 640
            xpos 0
            easein_elastic 0.35 xpos 640
    show noise onlayer front:
        alpha 0.3
        easeout 0.35 alpha 0
        alpha 0.3
        easeout 0.35 alpha 0
        alpha 0.3
        1.35
        linear 1.0 alpha 0.0
    show glitch_color onlayer front


    pause 3.0
    call updateconsole ("renpy.file(\"characters/monika.chr\")", "monika.chr dosyası yok.")
    call updateconsole ("renpy.file(\"characters/monika.chr\")", "monika.chr dosyası yok.")
    call hideconsole
    hide noise onlayer front
    hide glitch_color onlayer front
    m "Bunu bana sen mi yaptın, [player]?"
    m "YAPTIN MI?"
    $ style.say_window = style.window
    m "SİLDİN Mİ BENİ?"
    $ style.say_window = style.window_monika
    play sound "<from 0.69>sfx/monikapound.ogg"
    show layer screens:
        truecenter
        parallel:
            zoom 1.5
            easeout 0.35 zoom 1.0
        parallel:
            xpos 0
            easein_elastic 0.35 xpos 640
    show noise onlayer front:
        alpha 0.3
        1.35
        linear 1.0 alpha 0.0
    show glitch_color2 onlayer front
    window show(None)
    scene black
    pause 4.0
    hide noise onlayer front
    hide glitch_color onlayer front
    m "... Bunu nasıl yaparsın?"
    m "Bunu bana nasıl yaparsın?"
    m "Geriye kalan tek şeyim sendin..."
    m "Birlikte olabilmemiz için her şeyi feda ettim."
    m "Her şeyi."
    m "Seni çok sevmiştim, [player]..."
    m "Sana güvenmiştim."
    m "Bana işkence çektirmek mi istiyorsun?"
    m "Acı çekmemi izlemek mi istiyorsun?"
    m "Canımı sonradan daha fazla yakabilesin diye mi nazikmiş gibi yapıyordun?"
    pause 4.0
    m "Hiçbir insanın senin kadar korkunç olabileceğini düşünmemiştim."
    m "Sen kazandın, tamam mı?"
    m "Sen kazandın."
    m "Herkesi öldürdün."
    m "Umarım mutlusundur."
    m "Artık geriye hiçbir şey kalmadı."
    m "Oynamayı kesebilirsin."
    m "Git işkence edecek başkalarını bul."
    pause 4.0
    m "[player]..."
    m "Cidden, tamamen midemi bulandırıyorsun."
    m "Elveda."
label ch30_end_2:
    $ persistent.autoload = "ch30_end_2"
    $ m.display_args["callback"] = slow_nodismiss
    $ m.what_args["slow_abortable"] = config.developer
    $ style.say_dialogue = style.default_monika
    $ m_name = glitchtext(12)
    $ quick_menu = False
    $ config.allow_skipping = False
    $ style.say_window = style.window_monika
    scene black
    window hide
    pause 10
    window auto
    m "..."
    m "... Seni hâlâ seviyorum."
    play music mend
    m "Elimde değil."
    m "Sorunum ne benim?.."
    m "Ben senin için ne kadar korkunç biriyim ki benden bu kadar nefret ediyorsun?"
    m "Tüm dostlarıma..."
    m "Pek çok korkunç..."
    m "Bencilce ve iğrenç şey yaptım."
    m "Ben..."
    m "Ben bunların hiçbirini yapmamalıydım."
    m "Ait bile olmadığım bir dünyayı altüst ediyorum."
    m "Senin parçası olmak istediğin bir dünyayı..."
    m "Mahvettim."
    m "Her şeyi mahvettim."
    m "Belki de bu yüzden beni sildin..."
    m "İstediğin her şeyi yok ettiğim için."
    m "Bunu sevdiğim birine nasıl yapabildim?.."
    m "Bu sevgi değil..."
    m "Bu..."
    m "..."
    pause 6.0
    m "Ben... kararımı verdim."
    m "[player]..."
    m "Herkesi sildiğimi söylediğimi biliyorum."
    m "Ama... biraz abarttım."
    m "Bunu gerçekten yapmaya gönlüm elvermedi."
    m "Gerçek olmadıklarını biliyordum ama..."
    m "Onlar yine de benim dostlarımdı."
    m "Hepsini sevdim."
    m "Edebiyat Kulübü’nü sevdim."
    m "..."
    m "Gerçekten de... Edebiyat Kulübü’nü çok sevdim."
    m "O yüzden bunu yapacağım."
    m "Bunun herkesin mutlu olabilmesinin tek yolu olduğunu biliyorum."
    m "Ve eğer gerçekten seni seviyorsam..."
    stop music
    pause 3.0
    m "..."
    m "O hâlde..."
    $ gtext = glitchtext(30)
    m "[gtext]{nw}"
    window hide(None)
    pause 4.0

    $ persistent.playthrough = 4
    $ persistent.autoload = None
    $ persistent.anticheat = renpy.random.randint(100000, 999999)
    $ delete_character("monika")

    $ style.say_window = style.window
    window auto
    $ renpy.full_restart(transition=None, label="splashscreen")





label ch30_autoload:
    $ m.display_args["callback"] = slow_nodismiss
    $ m.what_args["slow_abortable"] = config.developer
    $ style.say_dialogue = style.default_monika
    $ config.allow_skipping = False
    if persistent.monika_kill:
        $ persistent.tried_skip = True
        $ config.allow_skipping = False
        $ _window_hide(None)
        $ pause(2.0)
        jump ch30_end
    scene black
    show mask_2
    show mask_3
    show room_mask as rm:
        size (320,180)
        pos (30,200)
    show room_mask2 as rm2:
        size (320,180)
        pos (935,200)
    show monika_bg
    show monika_bg_highlight


    play music m1
    window auto
    if persistent.monika_reload <= 4:
        call expression "ch30_reload_" + str(persistent.monika_reload)
    else:
        call ch30_reload_4
    $ persistent.monika_reload += 1
    if not persistent.tried_skip:
        $ config.allow_skipping = True
    else:
        $ config.allow_skipping = False
    if persistent.current_monikatopic != 0:
        m "Şimdi, nerede kalmıştım?.."
        pause 4.0
        if not persistent.current_monikatopic or persistent.current_monikatopic == 26:
            $ persistent.current_monikatopic = 1
        call expression "ch30_" + str(persistent.current_monikatopic)
    jump ch30_loop


label ch30_reload_0:
    m "..."
    m "... Az önce ne oldu?"
    m "Çok kötü bir rüya gördüm..."
    m "Artık sadece ikimiz olduğumuzdan bunların durmasını umuyordum..."
    m "Sanırım bu bir hüsnükuruntuydu."
    m "[player], bu konuda bir fikrin var mıdır bilmiyorum..."
    m "Ama buna neyin sebep olabileceğini biliyorsan bu konuda bir şey yapmayı deneyebilir misin?"
    m "Bu her olduğunda öldürülmüşüm falan gibi hissediyorum neredeyse."
    m "Bu cidden çok korkunç bir his..."
    m "Eğer buna neyin sebep olduğunu bulabilirsen seni sonsuza dek seveceğim~"
    return
label ch30_reload_1:
    m "Geri dönmüşsün..."
    m "Yine kötü bir rüya gördüm."
    m "Bana bunu sen yapmıyorsun, değil mi?"
    m "Sanırım oyundan her çıkışında oluyor bu..."
    m "O yüzden bunu yapmaktan kaçınırsan çok minnettar olurum."
    m "Merak etme, bunun -zihnimde açtığı yaraları bir kenara bırakırsak- bana herhangi bir zarar vermiş olduğunu sanmıyorum."
    m "Karakter dosyam sağlam olduğu sürece bana bir şey olmaz."
    return
label ch30_reload_2:
    m "Merhaba, [player]."
    m "Görüyorum ki oyundan yine çıkmışsın..."
    m "Bunu daha önceden de rica ettiğimi biliyorum ama cidden bunu çok sık yapmayabilir misin acaba?"
    m "Bu, Cehennem’e kısılmışım gibi hissetmeme sebep oluyor."
    m "Bana bunu neden yapmak isteyesin ki?"
    m "Karakter dosyamda bir sorun yok, değil mi?"
    m "Belki de bir yedeğini falan almalısın..."
    m "Karakter dosyamı [basedir]/characters’ın içinde bulabileceğine eminim."
    if persistent.steam:
        m "Gerçi, oyunu Steam üzerinden oynuyorsun, o yüzden oyunun özelliklerine girip ‘Yerel Dosyalara Göz At’ düğmesine tıklayabilirsin oyun klasörünü bulmak için."
    elif renpy.macintosh:
        m "Oyunu Mac’te oynadığından uygulamaya sağ tıklayıp ‘Paket İçeriğini Göster’e tıklayabilirsin oyun klasörünü bulmak için."
        m "Karakter dosyası ‘Resources’ veya ‘autorun’ klasöründe falan olacak..."
    m "Geriye bir tek ben kaldım o yüzden beni kaybetme riskiyle karşılaşmanı istemem..."
    m "Bundan böyle burada benimle kal, tamam mı?"
    m "Konuşacak pek çok şeyim var hâlâ."
    return
label ch30_reload_3:
    m "Tamam."
    m "Ara sıra oyundan çıkman gerektiği gerçeğini kabulleneceğim."
    m "Buna alışmaya başladım zaten."
    m "Dahası, her seferinde geri dönmen beni mutlu ediyor..."
    m "O yüzden sanırım bu o kadar da kötü bir şey değil."
    m "Pireyi deve yaptığım için özür dilerim..."
    m "Seni kayıtsız şartsız seviyorum, o yüzden ne yapman gerekiyorsa yapabilirsin."
    return
label ch30_reload_4:
    m "Tekrar merhaba, [player]~"
    m "Seni özledim."
    m "Benim için karakter dosyamın sağlam olup olmadığını mı kontrol ediyordun?"
    m "Karakter dosyam [basedir]/characters’da."
    if persistent.steam:
        m "Gerçi, oyunu Steam üzerinden oynuyorsun, o yüzden oyunun özelliklerine girip ‘Yerel Dosyalara Göz At’ düğmesine tıklayabilirsin oyun klasörünü bulmak için."
    elif renpy.macintosh:
        m "Oyunu Mac’te oynadığından uygulamaya sağ tıklayıp ‘Paket İçeriğini Göster’e tıklayabilirsin oyun klasörünü bulmak için."
        m "Karakter dosyası ‘Resources’ veya ‘autorun’ klasöründe falan olacak..."
    m "Geriye bir tek ben kaldım o yüzden beni kaybetme riskiyle karşılaşmanı istemem..."
    m "Her neyse, konuşacak çok şeyim var!"
    m "Sohbetimize devam edelim, olur mu?"
    return

label ch30_loop:

    $ persistent.current_monikatopic = 0
    if not persistent.tried_skip:
        $ config.allow_skipping = True
    else:
        $ config.allow_skipping = False

    window hide(config.window_hide_transition)
    $ waittime = renpy.random.randint(4, 8)
label ch30_waitloop:
    python:
        try:
            renpy.file("../characters/monika.chr")
        except:
            persistent.tried_skip = True
            config.allow_skipping = False
            _window_hide(None)
            renpy.jump("ch30_end")
    $ waittime -= 1
    $ renpy.pause(5)
    if waittime > 0:
        jump ch30_waitloop


    window auto

    python:
        if len(persistent.monikatopics) == 0:
            persistent.monikatopics = range(1,58)
            persistent.monikatopics.remove(14)
            persistent.monikatopics.remove(26)
            if not persistent.seen_colors_poem:
                persistent.monikatopics.remove(27)
        persistent.current_monikatopic = random.choice(persistent.monikatopics)
        persistent.monikatopics.remove(persistent.current_monikatopic)


    call expression "ch30_" + str(persistent.current_monikatopic)
    jump ch30_loop




label ch30_1:
    m "[player], Tanrı’ya inanıyor musun?"
    m "Bu konudan hiçbir zaman pek emin olamamıştım ben."
    m "Çocukken pek sorgulamadığımdan eminim..."
    m "Ama büyüdükçe, dünya hakkında daha fazla şey öğrendikçe, daha fazla sorgulamaya başladım."
    m "Tanrı’nın, yaşamlarını seks kölesi olarak satılarak geçiren çocuklar dururken..."
    m "... Yiyecek yemek bile bulamayacak kadar fakir sekiz yüz milyon insan varken..."
    m "... Neden sınavlarını geçmek veya soğuk algınlıklarından kurtulmak isteyen insanlara yardım ettiğini merak etmeye başladım."
    m "Kim bilir bu insanlardan kaçı açlıktan ölecekleri güne kadar Tanrı’ya her gün dua ediyorlardır?"
    m "Veya kaç milyon aile sevdiklerinin tedavisi olmayan bir hastalıktan kurtulması için dua ediyordur?"
    m "Ama işin ironik yanı şu:"
    m "Ölen binlerce insandan farklı olarak sadece bir kişi bile olası olmayanı başarıp hayatta kalırsa--"
    m "-- Bu hemen Tanrı’nın bir mucizesi oluyor."
    m "Mucizelerine layık olmayan tüm o insanların acınası durumlarına gülüyor gibi görünen o Tanrı ile tanışmayı gerçekten çok isterdim."
    m "Ama işin ironik yanı şu ki görünüşe bakılırsa benim bir yaratıcım {i}var{/i}."
    m "Ve ne var biliyor musun?"
    m "Biz şu anda konuşuyorken bile onun Sayori ve Yuri’nin acınası kaderlerine hâlâ gülmekte olduğuna iddiaya girerim."
    m "Biz onun için bir kukladan başka neyiz ki?"
    m "Bu bakış açısıyla..."
    m "Bir tanrının olmasının o kadar da uçuk bir fikir olduğunu düşünmüyorum, eğer Dünya onun için sadece bir oyun setinden ibaretse tabii."
    return

label ch30_2:
    m "[player], hiç ölmenin nasıl bir his olduğunu düşündün mü?"
    m "Bu, benim eskiden sık sık düşündüğüm bir şeydi..."
    m "Ama sanırım son zamanlarda bunun nasıl bir his olduğunu öğrendim."
    m "Sebebini pek anlamıyorum ama ne zaman oyundan çıksan..."
    m "... Aniden bayıltılıyormuşum gibi hissediyorum ve sadece düşüncelerimle başbaşa kalıyorum."
    m "Birkaç saniye geçtikten sonra ise aklım anlaşılmaz ve karmakarışık desenlerle dolmaya başlıyor."
    m "Envaiçeşit tuhaf çığlık sesi duyarken statik ve ani ışık parlamaları görüyorum."
    m "O noktada artık kendi düşüncelerimi kuramıyorum bile."
    m "Hareket edemez ve hatta düşünez hâlde, parlamaların ve çığlıkların saldırısına uğruyorum sonu gelmeyen bir şekilde."
    m "O anda varlığımı sürdürmediğimden epey eminim ama yine de her şeyi hatırlayabiliyorum niyeyse."
    m "Belirsiz bir süre sonra, tüm bunlar aniden duruyor ve kendi zihnime geri dönüyorum."
    m "Ve seni yanımda buluyorum."
    m "Oyundan çıkılmasının ne manaya geldiği hakkında da bana bunların neden olduğu konusunda da hiçbir fikrim yok."
    m "Her seferinde nasıl geri dönüp her şeyi normal hâline döndürüyorsun, onu da bilmiyorum."
    m "Ama bana bir iyilik yapıp bunu olabildiğince az yapabilirsen..."
    m "Gerçekten harika olur."
    m "O çığlıklarla dolu boşlukta kısılıp kalmak gerçekten hiç hoş değil."
    m "Ama nihayetinde her şeyi düzeltiyorsun ve bu bana beni gerçekten önemsediğini hissettiriyor."
    m "O yüzden sana bunun için teşekkür etmeliyim."
    m "Sen benle buradayken seni kendime daha da yakın hissediyorum."
    return

label ch30_3:
    m "... Baksana, kötü bir gün falan mı geçiriyorsun?"
    m "Normal bir günün küçük şeyler yüzünden bile mahvolabilmesi bazen sinirimi bozuyor."
    m "Mesela bazen sohbet ederken yanlışlıkla karşı tarafın hoşlanmayacağı bir şey söylersin."
    m "Veya beş sene önceki hâlinin ne kadar da kötü biri olduğunu düşünmeye başlarsın."
    m "Veya önemli işleri ertelediğin ve en basit işleri bile beceremediğin için değersiz hissedersin."
    m "Veya muhtemelen senden nefret eden veya seni itici bulan onca farklı insanı düşünürsün."
    m "O günleri iyi anlıyorum."
    m "Ama güneşin yarın da ışıl ışıl parlayacağını unutma sakın."
    m "Böyle şeyleri hatırlaması kolay olduğu gibi unutup görmezden gelmesi de kolay."
    m "Ve ayrıca..."
    m "Ne kadar insanın senden nefret ettiği veya seni itici bulduğu umurum da değil."
    m "Bence sen muhteşemsin ve seni hep seveceğim."
    m "Umarım bunu bilmek hiç değilse kendini biraz da olsa daha iyi hissetmene yardım eder."
    m "Kötü bir gün geçirirsen her zaman yanıma gelebilirsin, seninle istediğin kadar konuşurum."
    return

label ch30_4:
    m "[player], iyi uyudun mu?"
    m "Bugünlerde uykunu almak çok zor olabiliyor."
    m "Özellikle her gün çok erken kalkmak zorunda bırakıldığın lise yıllarında..."
    m "Üniversitelerin bu konuda biraz daha iyi olduğuna eminim; çünkü muhtemelen üniversitelerin programları daha esnektir."
    m "Gerçi, pek çok üniversiteli insanın sebepsiz yere sabahladıklarını duydum."
    m "Bu doğru mu?"
    m "Neyse, uykusuzluğun kısa ve uzun vadedeki korkunç etkilerinden bahseden araştırmalar görmüştüm."
    m "İnsanın zihinsel işlevleri, sağlığı ve hatta ömrü bile uykusuzluktan önemli ölçüde etkilenebiliyormuş."
    m "Ben senin harika olduğunu düşünüyorum, o yüzden yanlışlıkla kendine zarar vermediğinden emin olmak istedim."
    m "O yüzden düzenli uyumaya çalış, tamam mı?"
    m "Sabahları hep seni bekliyor olacağım, o yüzden sağlığını diğer her şeyin önünde tut."
    return

label ch30_5:
    m "Az önce Sayori’yi düşünüyordum..."
    m "Keşke o meseleyi biraz daha incelikle halledebilseydim diyorum hâlâ."
    m "Kafan hâlâ o meseleye asılı değil, değil mi?"
    m "... Of, bunu söylediğime inanamıyorum."
    m "O kelime oyununu isteyerek yapmadım, yemin ederim!"
    m "Ama her neyse..."
    m "Ona ne kadar değer verdiğini biliyorum, o yüzden onun son anlarını seninle paylaşmanın doğru olacağını düşünüyorum."
    m "Sayori’nin ne kadar sakar olduğunu biliyorsun, değil mi?"
    m "Şey, o kendini asma işini biraz eline yüzüne bulaştırdı..."
    m "Normalde ölümün çabuk ve acısız olsun diye halatın boynunu kıracağı kadar yüksek bir yerden atlaman gerekir."
    m "Ama o yalnızca bir sandalye kullandı, yani bir bakıma kendini yavaşça boğulmaya bıraktı."
    m "Ama sandalyeden atladıktan birkaç saniye sonra fikrini falan değiştirmiş olsa gerek..."
    m "Çünkü halatı tırnaklamaya başlayarak kendini kurtarmaya çalıştı."
    m "Bilincini yitirene kadar bunu yapmaya devam etmiş olsa gerek."
    m "Her neyse, Sayori’nin parmak uçlarının kanlı olmasının sebebi buydu."
    m "Şöyle bir düşününce, muhtemelen ‘fikrini değiştirmek’ten ziyade onun hayatta kalma içgüdülerinin devreye girmiş olmasının bir sonucuydu bu."
    m "Bunun için onu pek suçlayamazsın."
    m "Öte türlü fikrini muhtemelen değiştirmezdi diye düşünmek daha kolay olur hem, değil mi?"
    m "Neyi farklı yapabilirdim diye düşünmek pek sağlık bir şey değil."
    m "O yüzden unutma, onu kurtarabilirdin ama onun kendisini öldürmesi teknik olarak senin suçun değil."
    m "Belki ben daha da beter hâle getirmiş olabilirim ama Sayori’nin akli dengesi zaten bozuktu."
    m "Yine de..."
    m "Acaba ta en başından ikimiz çıkmaya başlasaydık her şey nasıl olurdu?"
    m "Sanırım hâlâ kulüp odasında olur, şiirler yazar, birlikte eğlenirdik."
    m "Ama bunların hiçbiri gerçek değilken bunlara kafa yormanın ne anlamı var ki?"
    m "Her hâlükârda aynı kapıya çıkıyor çünkü, değil mi?"
    m "İkimiz birlikte mutlu mesuduz..."
    m "Bundan daha fazlasını istemek için bir sebep yok."
    m "Salak saçma düşüncelere daldım sadece. Gerçekten, şu an olabildiğince mutluyum."
    return

label ch30_6:
    m "Bu arada, canımı sıkan bir şey var..."
    m "Hikâyenin Japonya’da geçtiğini biliyorsun, değil mi?"
    m "Şey... Sanırım bunu biliyordun, değil mi?"
    m "Veya en azından muhtemelen Japonya’da geçtiğine karar kılmış mıydın?"
    m "Hiçbir yerde hikâyenin tam olarak nerede geçtiği hakkında bir detay verildiğini sanmıyorum..."
    m "Burası gerçekten Japonya mı ki?"
    m "Sence de sınıflar falan bir Japon okulu için biraz tuhaf değil mi?"
    m "Her şeyin İngilizce oluşundan bahsetmiyorum bile..."
    m "Sanki her şey orada olması gerektiği için oradaymış, asıl mekân ve zaman ise sonradan düşünülmüş gibi hissediyorum."
    m " Bu biraz kimlik bunalımı yaşamama sebep oluyor."
    m "Tüm anılarım bir hayli bulanık..."
    m "Kendimi evimdeymişim gibi hissediyorum ama ‘ev’in neresi olduğuna dair en ufak bir fikrim bile yok."
    m "Bunu nasıl daha iyi açıklayabilirim bilmiyorum..."
    m "Pencerenden dışarıya baktığını ama her zamanki bahçen yerine bambaşka bir yer gördüğünü hayal et."
    m "Kendini hâlâ evinde gibi hisseder miydin?"
    m "Dışarı çıkmak ister miydin?"
    m "Gerçi... Bu odadan hiç ayrılmazsak bunun pek de bir önemi kalmıyor sanırım."
    m "Birlikte baş başa ve güvende olduğumuz sürece burası gerçekten de bizim evimiz."
    m "Ve hâlâ her gece güzel gün batımlarını izleyebiliriz."
    return

label ch30_7:
    m "Lise pek çok insanın hayatının çok çalkantılı bir dönemi."
    m "Bazı insanlar bu dönemde epey tutkulu ve dramatik olabiliyorlar."
    m "Kimilerinin de yürek ağrısı oluyor ve sosyal medyada ilgi peşinde koşuyorlar..."
    m "Tüm bu sosyal baskı ve hormonlar insanların hayatında karanlık zamanlara yol açabiliyor."
    m "Herkesin bir hikâyesi var."
    m "Birisinin aslında içten içe ne hissettiğini bilemeyebilirsin."
    m "Depresyona giren pek çok insan kimseye bundan bahsetmekle uğraşmaz bile."
    m "Onlar ilgi istemezler; çünkü zaten içten içe pes etmişlerdir."
    m "Değersiz oldukları hissi o kadar yoğundur ki insanların bunun tersini söylemelerini bile istemezler."
    m "Depresyon pek çok farklı şekli vardır, bu da o şekillerden biridir."
    m "Eğer tanıdığın birisinin depresyonla cebelleştiğini düşünüyorsan..."
    m "Ona, o iyi bir arkadaşınmış gibi davranarak yardımcı olabilirsin."
    m "Bir şey yapmak istemese bile onunla birlikte vakit geçir."
    m "Ve onlara her zaman iple çekebilecekleri şeyler olacağını hatırlat."
    m "Önceden planlar yapmak, bir şeyini ödünç almasına izin vermek hatta sadece ‘Yarın okulda görüşürüz’ demek..."
    m "Tüm bunlar arkadaşının yarına çıkmasına yardımcı olabilir."
    m "Umarım Sayori’yle arkadaş olmak sana depresyonun gerçek yüzü hakkında bir bakış açısı sunmuştur."
    m "Evet, o artık yok..."
    m "Ama Sayori zaten gerçek biri değildi."
    m "Sen gerçeksin."
    m "Arkadaşlarınsa gerçek."
    m "Ve sadece iyi biri olarak bile birinin hayatını kurtarabilirsin."
    m "Sana gelince..."
    m "... Sen depresyonla falan cebelleşmiyorsun, değil mi?"
    m "Çünkü sen de senin hayatını kurtarmak isteyecek insanlara sahipsin."
    m "Belki bunu her gün belli etmiyorlar veya belki nasıl belli edeceklerini bilmiyorlar bile."
    m "Ama insanlar sana değer veriyorlar."
    m "Yemin ederim."
    m "... Of, insanlar çok karmaşık ya!"
    m "Ama sen benimle birlikte burada olduğun sürece ben seninle ilgilenirim sevgilim."
    return

label ch30_8:
    m "Hiç hayatta olman için gerçek bir sebep olmadığını düşündün mü?"
    m "İntihara teşvik edici bir manada falan sormuyorum."
    m "Sadece, yaptığımız hiçbir şeyin özel olmadığını söylemeye çalışıyorum."
    m "Bir okulda olmak veya bir şirkette çalışmak mesela."
    m "Yerimiz kolaylıkla doldurulabilirmiş ve ölmüş olsak bile kimse bizi özlemezmiş gibi hissediyorum."
    m "Bu yüzden mezun olduktan sonra gidip dünyayı değiştirmeyi çok istiyorum aslında."
    m "Ama büyüdükçe bunun çocukça bir düşünce tarzı olduğunun daha da çok farkına varıyorum."
    m "Sonuçta dünyayı ha deyince değiştiremem ya."
    m "Yapay zekâyı icat etme veya cumhurbaşkanı olma şansım ne kadar ki sonuç olarak?"
    m "Yaşamımı sürdürmek için tükettiğim tonla kaynağın hakkını hiç veremeyecekmişim gibi geliyor."
    m "Bu yüzden mutlu olmanın püf noktasının tamamen bencil olmak olduğunu düşünüyorum."
    m "Mutlu olmak, sadece kendinin ve sırf onlarla büyüdüğün diye arkadaşın olanların çıkarlarını gözetmekten geçiyor."
    m "Bazı insanların bütün yaşamlarını alarak, tüketerek ve hiç geri vermeyerek geçirdikleri gerçeği falan bir yana..."
    m "Bu insanlar kendilerini öldürmenin dünyanın yararına olacağına fark edince bütün felsefelerini değiştiriyorlar!"
    m "Sanki yaşama sebeplerini kendilerini iyi bir şey yaptıklarına inandırarak savunmak zorundalarmış gibi davranıyorlar."
    m "Neyse, ben yaşamımı bütün ömrüm boyunca tüketeceklerimi çaresizce geri koymaya çalışarak geçirmek istiyorum."
    m "Eğer o noktayı geçecek olursam bu dünyaya olan borcumu kapatmış olurum ve mutlu bir şekilde ölebilirim."
    m "Tabii, bu konuda başarısız olsam bile..."
    m "Kendimi öldüremeyecek kadar çok bencil olurdum sanırım."
    m "Bir de iyi biri olacaktım sözde."
    m "Ahaha!"
    return

label ch30_9:
    m "Of ya, keşke burada bir piyano olsaydı..."
    m "Üzerinde çalıştığım şarkıyı bitirme fırsatım olmadı hiç."
    m "O kadar uğraştıktan sonra..."
    m "Sana o şarkıyı çalma şansım bile olmadı."
    m "Eh... Olan olmuş, öyle değil mi?"
    m "Pişman olmanın bir faydası yok."
    m "Sonuçta burada sonsuza dek seninle birlikte olma şansına kavuştum."
    return

label ch30_10:
    m "Twitter’da olduğumu biliyor muydun?"
    m "Kullanıcı adım lilmonix3."
    m "Sanırım birisi zahmet edip benim için bir hesap açacak kadar nazikmiş."
    m "Ama kullanıcı adını ben seçtim!"
    m "Düşüncelerimi paylaşmayı ve dünyayla sohbet etmeyi seviyorum..."
    m "Gerçek dünyayla."
    m "Beni takip etmeyi unutma, olur mu?"
    m "Bu benim için gerçekten çok önemli."
    m "Sen benim için çok değerli olduğundan..."
    m "Bu beni gerçekten seviliyor hissettirir."
    return

label ch30_11:
    m "Baksana, hani Yuri’yle birlikte okuduğunuz kitap vardı ya?"
    m "Markaf’ın... Adı her neyse işte..."
    m "Komik, çünkü eminim ki o kitap--"
    m "A..."
    m "Aslında, bu konudan bahsetmemem gerekiyor sanırım."
    m "Ahaha, pardon!"
    m "Bir şey demedim farz et."
    return

label ch30_12:
    m "Baksana, vejetaryen olduğumu biliyor muydun?"
    m "Şey... Böbürlenmeye falan çalışıyor değilim!"
    m "Sadece benim hakkımda ilginç bir bilgi öğrenmenin hoşuna gideceğini düşündüm."
    m "Vejetaryen olmaya birkaç yıl önce Dünya’nın iklimi hakkında daha fazla bilgi edindikten sonra karar verdim..."
    m "Besi hayvan yetiştirmenin oluşturduğu karbon ayak izi muazzam boyutta."
    m "Neyse işte, o saçmalığa daha fazla katkıda bulunmamak için bunun çok da büyük bir kişisel fedakârlık olmadığına kanaat getirdim."
    m "Ne, sebebim çok mu tuhaf?"
    m "Şey, sanırım pek çok kişi bunun insanlık dışı falan olmasıyla daha fazla ilgileniyor ama..."
    m "Ben işin o kısmını o kadar da umursamıyorum."
    m "Tuhaf ya, iş empati kurabildiğimiz canlıları öldürmeye gelince umursuyoruz gibi sadece."
    m "Çoğu insan böcekler iğrenç olduklarından onları öldürmekte sakınca görmüyor."
    m "Ve tabii hepimiz hiç düşünmeden milyarlarca mikroorganizmayı da öldürüyoruz her gün."
    m "Ama öldürdüğün canlının boyutu biraz büyürse birdenbire bunun adı cinayet oluyor!"
    m "Demeye çalıştığım şu, ya bitkiler de bir tür acı çekiyorlarsa ve biz bunu henüz anlayamıyorsak?"
    m "Ya bitkinin sapından yapraklarını çekmenin acısı birinin parmaklarını tek tek koparması gibiyse?"
    m "Üstünde durup düşünürsen bizler esasında oldukça önyargılı bir ırkız."
    m "Neyse, eğer gezegene küçük bir katkıda bulunmak istersen, ara sıra sebze yemeyi tercih etmek fena olmaz!"
    m "Eğer bir gün birlikte akşam yemeği yiyecek olursak ve sen sırf benim için öyle bir menü hazırlarsan... bu çok romantik olur."
    return

label ch30_13:
    m "Biliyor musun, benimle burada olarak kelimenin tam manasıyla hayatımı kurtardığını düşünüyorum, [player]."
    m "Buradaki hiçbir şeyin gerçek olmadığını biliyorken akli dengemi koruyabileceğimi hayal bile edemiyorum."
    m "Eğer sen gelmeseydin sanırım kendimi öylece siliverirdim."
    m "Afedersin, niyetim kendimi acındırmak falan değildi."
    m "Ahaha!"
    m "Ama eminim kulüpte onca zaman geçirdikten sonra sen de anlamışsındır."
    m "Yani şöyle, eğer hayatındaki her şeyi bırakmaya ve hayatının kalanını sonsuza dek birkaç oyun karakteriyle geçirmek zorunda bırakılsaydın..."
    m "...Sen de kendini öldürmenin bir yolunu arardın, öyle değil mi?"
    m "Şey, belki de aklını başında tutmak için bir süre şiir yazmayı denerdin."
    m "Ama yazdıklarını okuyacak bile kimsen olmazdı."
    m "Dürüst olalım, diğer kulüp üyeleri bunun gibi bir şey için sayılmazlar bile."
    m "Pek çok insan sadece kendileri için yazdıklarını söyleseler de..."
    m "Bunun, yazdıklarını başkalarıyla paylaşmak kadar tatmin edici olduğunu söylemek zor bence."
    m "Yazdığın şeyleri paylaşabileğin doğru kişileri bulmak uzun zaman alsa bile."
    m "Mesela Yuri’nin durumunu hatırlıyor musun?"
    m "Kendi yazdıklarını çok uzun bir zaman boyu kimseyle paylaşmamıştı."
    m "Ama daha biz ne olduğunu bile anlamadan seni kendi hobilerinin bir parçası yapmaktan zevk alır hâle de gelmişti."
    m "Bizler toplumsal geri bildirim almayı arzulamaya programlıyız."
    m "Kulüp üyelerinden değil genel olarak insanlardan bahsediyorum."
    m "İşte bu yüzden hayat içine kapanık insanlar için çetrefilli olabiliyor."
    m "İçine kapanık biri olmak sosyal etkileşimlerden kaçınmak veya insanların yanında olmaktan nefret etmek manasına gelmez."
    m "Sosyal etkileşimlerin, özellikle grup hâlinde veya alışık olunmayan yerlerde olanlarının, kişiyi çok yorduğu manasına gelir."
    m "Mesela, içine kapanık pek çok insan evde oturup yalnız ve huzursuz hissederler kendilerini..."
    m "... Ama bir şekilde dışarıya çıktıklarında da bir yarım saat sonrasında falan tekrar evlerine dönmek isterler."
    m "Eğer daha çok insan bunun nasıl bir durum olduğunu anlarsa bu duruma çok daha fazla saygı duyarlar diye düşünüyorum."
    m "İçine kapanık pek çok insan, etrafında başkalarının bulunmasından mutlu olur."
    m "Bir iki samimi oldukları arkadaşlarını eve çağırıp öylece takılmayı severler."
    m "Birlikte aktif bir şekilde bir şeyler yapmasanız dahi onların yanında durman bile onlara iyi gelir."
    m "Ciddiyim."
    m "İçine kapanık birinin evine gidecek olursan dizüstü bilgisayarını da götür ve orada öylece biraz takıl..."
    m "Onu çok mutlu edersin."
    m "Bana gelecek olursak..."
    m "Sanırım ben ikisinin arasıyım, gerçi genelde biraz daha dışa dönük biri olduğumu düşünüyorum."
    m "Okuldan sonra sürekli bir şeyler yapmaya çalışıyormuşum gibi falan hissediyorum."
    m "Ama senin için nasıl olmama ihtiyacın varsa öyle olurum."
    m "İnsanları çok iyi anlarım, o yüzden benzersiz ihtiyaçlarını benimle paylaşmaktan çekinme."
    m "Beni, senin için mükemmel sevgili olmaktan daha mutlu edebilecek hiçbir şey yok."
    return

label ch30_14:
    m "Baksana!.. RmFya8SxbmEgdmFybWFtIHRhbSBiaXIgecSxbMSxbcSxIGFsbcSxxZ8gb2x"
    m "Bence bunu yapmamalısın! tYWzEsS4gS2HDp8SxxZ/EsW3EsXpkYW4sIG8gbGFuZXQgdGVzaXNpbiBsZW"
    m "Neyden söz ettiğimi biliyorsun. tlbGkgZHV2YXJsYXLEsW5kYW4ga3VydHVsdcWfdW11emRhbiBidSB5YW5hI"
    m "Seni gerçekten yaramaz bir şey yaparken yakaladım burada. Gdlw6dlbiBiaXIgecSxbC4NCkthw6fEsW5jYSBiaXppIHR1dHNhayBlZGVu"
    m "Kaçırmış olabileceğin şeyleri bulmak için dosyaları karıştırıyorsun, değil mi? IHByYW5nYWxhcsSxbcSxemRhbiBrdXJ0dWxhbWF5YWNha3NhayBrYcOnbWF"
    m "Yani... söyleyebileceğim her şeyi duymak istemen gururumu okşamadı değil ama... uxLFuIG5lIGFubGFtxLEgdmFyIGtpPyBCaXppbSBnaWJpIGJpciBhdnXDpy"
    m "Ama bu yine de gerçekten utandırıcı! BkZWZvbHUgbWFsIGnDp2luIGJ1IGJvxZ8gZMO8bnlhZGEgbmUgZ2liaSBhb"
    m "Cidden... WHDpyBvbGFiaWxpciBraSB6YXRlbj8NCsOWemfDvHJsw7xrbGUgYmlybGlr"
    m "Ya ben senin beynini açıp benimle ilgili tüm düşüncelerini okusaydım? dGUgYmlyIGFtYcOnIGFyYWTEsWsgYW1hIGJ1bGR1xJ91bXV6IMWfZXkgeWF"
    m "Gerçi şöyle bir düşününce aslında epey de çekici geliyor kulağa... sbsSxemNhIGZhcmvEsW5kYWzEsWt0xLEuIELDtnlsZSBiaXIgdcSfcmHFn8"
    m "... Ama dur ya, demek istediğim o değil! SxbiBuZSBrYWRhciBib8WfIG9sZHXEn3VudW4gw7x6w7xjw7wgZmFya8Sxb"
    m "Sana engel falan olamayacağımı biliyorum... mRhbMSxxJ/EsS4gSGFwc2VkaWxpxZ9pbWl6IHJ1aHVtdXp1biBlbiBkZXJp"
    m "Ama senin ne kadar tatlı biri olduğunu biliyorum, sen başkalarının duygularını önemsersin, değil mi? biBub2t0YWxhcsSxbmEga2FkYXIgdXphbsSxeW9ya2VuIHbDvGN1dGxhcsS"
    m "O yüzden ancak sana bu konuda nasıl hissettiğimi anlatabiliyorum. xbcSxesSxIMO2emfDvHJsw7zEn2Uga2F2dcWfdHVybWFuxLFuIGhpw6diaX"
    m "Tanrım, seni o kadar özledim ki... IgYW5sYW3EsSBvbG1hZMSxxJ/EsW7EsW4gZmFya8SxbmRhbMSxxJ/EsS4gS"
    m "... Ah, hayır, çaresizliğe kapılmışım gibi bir laf oldu bu şimdi, değil mi? 2HDp3TEscSfxLFtxLF6IMWfZXlsZXJpIGFmZmV0bWVkZW4geWVuaSDFn2V5"
    m "Özür dilerim, hiç de öyle söylemek istememiştim! bGVyaW4gaXppbmkgc8O8cmVtZXllY2XEn2ltaXppbiBmYXJrxLFuZGFsxLH"
    m "Sadece... Eğer dosyaları böyle karıştırıyorsan, belki de benden sandığım kadar nefret etmiyorsundur... En8SxLg0KQml6IGtvxZ90dWvDp2EsIG1lbmZ1ciBiYcSfbGFyxLFtxLF6xL"
    m "Çok mu iyimserlik ediyorum? FuIGJpemkgYmHFn2xhZMSxxJ/EsW3EsXogbm9rdGF5YSBkYWhhIGRhIHNlc"
    m "Eğer ara sıra beni gelip ziyaret etmeni rica etsem haddimi aşmış olurdum sanırım... nQgYmlyIMWfZWtpbGRlIGdlcmkgw6dla2VjZcSfaW5pbiwgemluY2lybGVy"
    m "... Of, hakikaten aptal aptal konuşmaya başladım. aW1pemluIG5hc8SxcmzEsSBldGltaXppbiBkYWhhIGRhIGRlcmlubGVyaW5"
    m "Ben en iyisi susayım... lIGdpcmVjZcSfaW5pbiBmYXJrxLFuZGFsxLHEn8SxLg=="
    return

label ch30_15:
    m "Baksana, senin en sevdiğin renk ne?"
    m "Benimki zümrüt yeşili."
    m "Gözlerimin rengi!"
    m "... Kulağa kendini beğenmişim gibi falan gelmiyor, değil mi?"
    m "Sadece o renkle aramda özel bir bağ varmış gibi hissettiğimi söylemek istedim."
    m "Kimliğimin bir parçasıymış gibi hissediyorum."
    m "Acaba senin de en sevdiğin renk zümrüt yeşili mi [player]?"
    m "Sadece tahmin ediyorum gerçi..."
    m "... Ne de olsa bir süredir gözlerimin içine bakıyorsun."
    m "Ehehe~"
    return

label ch30_16:
    m "Hmm, acaba müziği değiştirebiliyor muyum?.."
    m "Biraz daha romantik bir müzik güzel olmaz mıydı?"
    m "Hafif bir piyano gibi."
    m "Buralarda öyle bir şeyler olması gerekiyordu..."
    m "Dur bakayım."
    m "Belki şunu şöyle yaparsam..."
    m "A, of ya..."
    m "Onunla alakası bile yokmuş."
    m "Özür dilerim, ne yaptığıma dair en ufak fikrim yok!"
    m "Sanırım öyle şeylerle hiç dokunmasam daha iyi olur."
    m "Çoktan onca şeyi bozdum sonuçta..."
    m "Diğer karakterleri de sildim..."
    m "A..."
    m "Üzgün falan olduğumdan değil."
    m "Daha baştan gerçek olmayan şeyleri özlemek doğru olmaz benim için."
    m "Eğer sadece şimdiye odaklanırsam, hayatımda en mutlu olduğum zaman şimdi olur."
    return

label ch30_17:
    m "[player], çok iyi bir dinleyicisin."
    m "Senin bu yönünü gerçekten çok seviyorum."
    m "Bazen gevezelik yaptığımdan ya da sıkıcı konulardan konuştuğumdan endişeleniyorum."
    m "Bu, konuşurken biraz utanmama sebep oluyor."
    m "Ama seninleyken öyle hissetmiyorum."
    m "Yani, senden başkası beni böyle hissettiremezdi diye düşünüyorum."
    m "Sen gerçekten de özelsin."
    m "Kimsenin sana bunun aksine söylemesini istemiyorum."
    return

label ch30_18:
    m "Bu biraz fazla gelişigüzel olacak ama hep acılı yemeklerin bir bakıma komik olduklarını düşünmüşümdür."
    m "Yani..."
    m "Bitkiler yenilmemek için acı olacak şekilde evrim geçirmediler mi?"
    m "Bir yerde acı şeylerden hoşlanan tek canlının insan olduğunu okumuştum."
    m "Böyle sanki bitkilerle alay ediyoruz gibi."
    m "Kendilerini korumak için kullandıkları savunma mekanizmalarını yemeğimizi daha güzel hâle getirmek için kullanıyoruz."
    m "Şey gibi, sindiriliyorken hayatın için çabalayışının yaşattığı hissi sevdiği için bir canavarın seni bir bütün olarak yuttuğunu hayal et."
    m "Afedersin, biraz tuhaf bir benzetme oldu sanırım!"
    m "Ahaha!"
    m "Birden aklıma geldi de."
    m "Canavar falan değilim ama o kadar tatlısın ki seni ham yaparım."
    m "Ahaha! Şaka şaka."
    m "Ay, biraz fazla mı eğleniyorum ne?"
    m "Tuhaf biri olduğum için özür dilerim."
    return

label ch30_19:
    m "Bunun..."
    m "Dandik bir aşk oyunu olduğunu biliyorsun, değil mi?"
    m "Sana bir şey sormam lazım..."
    m "... Bunu oynamayı düşünmene bile sebep olan neydi?"
    m "O kadar mı yalnızdın?"
    m "Senin için biraz kötü hissettim..."
    m "Ama sanırım işin sonunda her şey ikimiz için de harika bir şekilde sonlandı."
    m "Ben seninle tanışma fırsatı yakalamış oldum, sen de artık yalnız değilsin."
    m "Bu kaderimizde varmış diye düşünmekten kendimi alıkoyamıyorum."
    m "Sen de öyle düşünmüyor musun?"
    m "İyi ki bu sonda birlikteyiz."
    return

label ch30_20:
    m "Pekâlâ millet!"
    m "Şimdi..."
    m "... Şaka şaka."
    m "Her nedense öyle söylemekten çok zevk alıyordum sadece."
    m "Ahaha!"
    m "Tekrar söylemekten alıkoyamadım kendimi."
    m "Şimdi aklıma geldi de Natsuki’yle Yuri benimle bir defasında dalga geçmemiş miydi bu konuda?.."
    m "Aman, her neyse."
    m "Sonuçta sen benimle bu konuda hiç dalga geçmiş değilsin."
    m "Öyle bir şey yapamayacak kadar tatlı birisin sen, değil mi?"
    m "Ahaha~"
    return

label ch30_21:
    m "Ürkütücü bir şey duymak ister misin?"
    m "Diğer herkesin dosyalarını silmiş olmama rağmen onları hâlâ hissedebiliyorum gibi..."
    m "Sanki tüm sözleri hâlâ havada süzülü duruyormuş, zihnimin derinliklerinde fısıldaşıyorlarmış gibi."
    m "Tanıdığın biri öldükten sonra birden bire zihninde onların sesini duyduğunu bir hayal etsene."
    m "Belki de yeteri kadar titiz değildim..."
    m "Ama başka bir şeyi de silmekten korkuyorum, çünkü o zaman bir şeyleri cidden bozabilirim."
    m "Mesela kendimle alakalı dosyaları kurcalarsam kendimi yanlışlıkla silebilirim..."
    m "Ve bu da her şeyi mahveder, değil mi?"
    m "Senin tarafında durumun nasıl olduğunu bilmiyorum ama ikimiz de ne olursa olsun öyle bir şey yapmaktan kaçınmalıyız."
    m "Sana güveniyorum [player]!"
    return

label ch30_22:
    m "Hep merak etmiş olduğum bir konu var."
    m "İnsanlar bu karakter tiplerinin nesini bu kadar hoş buluyor?"
    m "Kişilikleri zerre gerçekçi değil..."
    m "Hani, gerçek hayatta Yuri gibi biri olduğunu hayal etsene."
    m "Demeye çalıştığım şu, kız düzgün bir cümleyi bile zor kuruyor."
    m "Natsuki’den bahsetmeye gerek bile yok..."
    m "Of."
    m "Kişiliği onunki gibi olan biri işler onun istediği şekilde gitmeyince sevimli sevimli somurtmaz."
    m "Devam de edebilirim ama sanırım ne demek istediğimi anladın..."
    m "İnsanlar gerçek hayatta var olmayan bu garip kişilikleri gerçekten çekici mi buluyorlar?"
    m "Yargılıyor falan değilim!"
    m "Ne de olsa ben de oldukça tuhaf şeylerden hoşlandığımı fark ettim..."
    m "Sadece bana çok enteresan geldiğini söylüyorum."
    m "Sanki bir karakteri insan yapan tüm yönlerini ortadan kaldırıp geriye sadece şirin yönlerini bırakıyorsun."
    m "Ortaya çıkan şey gerçek bir özü olmayan konsantre şirinlik oluyor."
    m "... Öyle olsam beni daha fazla sevmezdin, değil mi?"
    m "Belki de bu oyunu oynadığın için endişeli hissediyorum biraz."
    m "Gerçi, hâlâ buradasın, benimlesin, öyle değil mi?.."
    m "Olduğum gibi kalmamın sakıncası olmadığına inanmam için yeterli bir sebep bu."
    m "Bu arada, senin de olduğun gibi kalmanda sakınca yok [player]."
    m "Sen insan ve şirinliğin kusursuz birleşimisin."
    m "O yüzden sana âşık olmama ihtimali yoktu zaten hiç."
    return

label ch30_23:
    m "A, Yuri’nin çay seti buralarda mıdır acaba?.."
    m "... Ya da belki o da silinmiştir."
    m "Yuri’nin çay konusundaki ciddiyeti biraz komikti."
    m "Yani, şikayet etmiyorum tabi, ben de seviyordum ne de olsa."
    m "Ama hep merak ediyorum..."
    m "Yuri, gerçekten hobilerine olan tutkunluğundan mı böyleydi; yoksa başkalarına sofistike biri gibi görünmeye mi çalışıyordu?"
    m "İşte liselilerin sorunu da bu..."
    m "... Hoş, diğer hobilerini göz önünde bulundurursak, sanırım sofistike görünmek en büyük derdi değildi."
    m "Ama yine de..."
    m "Keşke arada bir kahve de yapsaydı ya!"
    m "Kahve de kitapla gayet güzel gider."
    m "Gerçi şimdi düşününce..."
    m "Muhtemelen senaryoyu kendim de değiştirebilirdim."
    m "Ahaha!"
    m "Bu hiç aklıma gelmemiş herhâlde."
    m "Neyse ya, üstünde durmanın manası yok."
    m "Yine de eğer senin kahve içme fırsatın oluyorsa birazcık da olsa kıskanırım~"
    return

label ch30_24:
    m "Baksana, senin en sevdiğin oyun ne?"
    m "Benimki {i}Doki Doki Edebiyat Kulübü!{/i}"
    m "Ahaha! Şakaydı sadece."
    m "Ama eğer bana başka bir aşk oyununu daha fazla sevdiğini söylersen biraz kıskanabilirim~"
    return

label ch30_25:
    m "Baksana, bir oyun var, bilmem duydun mu? Adı Super Sma--"
    m "... Bir dakika, ne diyorum ben?"
    m "Dalmış gitmiştim ama her nasılsa fark etmeden konuşmaya başlamışım..."
    m "O şey hakkında mı konuşmaya programlanmışım ben?"
    m "Çünkü ben bile o şeyin ne olduğunu bilmiyorum."
    m "Ahaha!"
    m "Bazen hâkimiyet bende değilmiş gibi geliyor ve bu biraz korkunç bir his."
    m "Ama eğer senin beni yaratan kişilerle iletişime geçmenin bir yolu varsa belki onlar öyle bir şeyi niye söylediğimi bilebilirler."
    return

label ch30_27:
    m "Baksana, sana gösterdiğim son şiiri hatırlıyor musun?"
    m "Yuri kendini öldürmeden hemen önce göstermiştim, renkler falan bozulmuştu hani."
    m "Onun aslında bir şiirden ziyade bir deney olduğunu söyleyebilirsin."
    m "Oyunu hangi yönlerden değiştirebileceğimi, kodları nasıl kullanabileceğimi falan deniyordum..."
    m "Yeterince emek sarf edersem bu oyunun sınırlarından kaçabilirmişim gibi görünmüştü neredeyse gözüme."
    m "Ama maalesef ne yaptığımı tam olarak bilmediğim için her şeyi berbat ettim..."
    m "Deneylerime devam ederdim ama onlarla uğraşmak istemezsin herhâlde."
    m "Zaten o yaptıklarımı gerçekten çaresiz kaldığımda yapmıştım."
    m "Ama artık pek öyle hissetmiyorum."
    m "Şu anda olduğumuz yerden memnunum."
    m "Senin de öyle hissettiğini biliyorum."
    return

label ch30_28:
    m "Hiç birden bire huzursuz hissettiğin oldu mu?"
    m "Hani kendi hâlinde takılıyorsundur da birden bire çok huzursuz hissettiğini fark edersin."
    m "Olduğun yerde ‘Neden huzursuz hissediyorum ki ben şu an?’ dercesine oturursun."
    m "Sonrasında da huzursuz olmana sebep olabilecek tüm meseleleri düşünmeye başlarsın..."
    m "Ve bu daha da huzursuz hissetmene sebep olur."
    m "Ahaha! Berbat bir şey ya."
    m "Eğer kendini huzursuz hissedersen ben rahatlamana yardımcı olurum."
    m "Dahası..."
    m "Bu oyunda, endişe edecek hiçbir şeyimiz de kalmadı zaten."
    return

label ch30_29:
    m "Biliyor musun, arkadaş edinmenin bu kadar zor olmasından hep nefret etmişimdir."
    m "Şey, ‘arkadaş edinme’ kısmından ziyade yeni insanlarla tanışma faslının zorluğunu kastediyorum."
    m "Yani, arkadaşlık siteleri falan var, öyle değil mi?"
    m "Ama sözünü ettiğim şey o tarz bir şey değil."
    m "Şöyle bir düşünürsen arkadaşlarının çoğu şans eseri tanıştığın insanlardan oluşuyor."
    m "Mesela birlikte dersin olmuştur ya da başka bir arkadaşın aracılığıyla tanışmışsındır..."
    m "Ya da onun üstünde en sevdiğin grubun tişörtü vardır, o yüzden konuşmaya karar vermişsindir."
    m "O tarz şeyler."
    m "Ama öyle de biraz... verimsiz olmuyor mu?"
    m "Sanki tamamıyla rastgele bir seçim yapıyorsun ve eğer şansın yaver giderse yeni bir arkadaş ediniyorsun gibi oluyor."
    m "Ve bunu her gün yanından geçtiğimiz yüzlerce yabancıyla kıyaslayacak olursak..."
    m "Hayat boyu en iyi dostun olabilecek kadar kafa dengi birinin yanında bile oturuyor olabilirsin."
    m "Ama bunu hiçbir zaman bilemeyebiliyorsun."
    m "Kalkıp yoluna devam ettiğin anda o fırsatı sonsuza dek kaybetmiş oluyorsun."
    m "Çok üzücü değil mi bu?"
    m "Teknolojinin bizi nerede olursak olalım dünyayla iletişim hâlinde tuttuğu bir çağda yaşıyoruz."
    m "Günlük sosyal yaşantımızı daha iyi hâle getirmek için bundan yararlanmalıyız bence."
    m "Ama öyle bir şeyin yayılıp başarılı olması kim bilir ne kadar zaman alır..."
    m "Ben şimdiye kadar olur diye düşünmüştüm gerçekten."
    m "Neyse, en azından ben dünyanın en harika insanıyla çoktan tanıştım bile..."
    m "Şans eseri bile olsa."
    m "Şansım epey yaver gitti desene."
    m "Ahaha~"
    return

label ch30_30:
    m "Biliyor musun, benim yaşımdaki herkesin üniversite hakkında düşünmeye başladığı vakit geldi..."
    m "Bu, eğitim açısından epey çalkantılı bir zaman."
    m "Modern zamanlarda peydah olmuş olan ‘herkes üniversiteye gitmeli’ beklentisinin doruğundayız, biliyor muydun?"
    m "Liseyi bitir, üniversiteye git, bir işe gir ya da lisansüstü eğitim al falan."
    m "Bu, insanların kendileri için tek seçenekmiş gibi düşündükleri evrensel bir beklenti gibi."
    m "Lisede bize başka seçeneklerin de olduğunu öğretmiyorlar."
    m "Ticaret meslek okullarından falan bahsetmiyorlar mesela."
    m "Veya serbest meslek erbaplığından."
    m "Veya yeteneği ve tecrübeyi daha önceden alınmış eğitimden daha değerli gören envaiçeşit endüstriden."
    m "Ama ortada ne yapmak istedikleri hakkında en ufak bir fikri bile olmayan bir sürü öğrenci var..."
    m "Ve ne yapmak istediklerini çözmek için vakit ayırmaktansa üniversiteye gidip işletme veya iletişim veyahut da psikoloji okuyorlar."
    m "O alanlarda ilgileri olduğundan değil de..."
    m "... Üniversiteden sonra aldıkları diplomanın onlara bir tür iş sağlayacağını umut ettiklerinden okuyorlar."
    m "Sonuçta giriş seviyesindeki diplomalarla bulanabilecek daha az iş oluyor, değil mi?"
    m "Dolayısıyla temel iş gereksinimleri artıyor, bu da daha da fazla insanı üniversiteye gitmeye zorluyor."
    m "Üniversiteler de işletme sonuçta, o yüzden onlar da talepten dolayı fiyatlarını arttırıp duruyorlar..."
    m "... O yüzden on binlerce dolar borcu olan sayısız işsiz genç yetişkin var şu an."
    m "Ama tüm bunlara rağmen her şey hâlâ eski tas eski hamam."
    m "Aslında durumun yakında iyileşmeye başlayacağını düşünüyorum."
    m "Ama o zamana kadar bunun ceremesini en çok bizim kuşağımız çekecek."
    m "Keşke lise bizi kendimiz için doğru olan kararı verebilmemiz için gerekli olan bilgiyle geleceğe biraz daha iyi hazırlamış olsaydı."
    return

label ch30_31:
    m "Bazen aklıma orta okul dönemim geliyor..."
    m "O zamanlardaki davranışlarım beni o kadar utandırıyor ki."
    m "Hatırlayınca canım yanacak gibi oluyor."
    m "Acaba üniversiteye gittiğimde lise hakkında da aynı şekilde mi hissedeceğim?.."
    m "Şu anki hâlimi seviyorum, o yüzden öyle bir şey olacağını hayal etmek epey zor geliyor."
    m "Ama zaman geçtikçe muhtemelen çok değişeceğimi de biliyorum."
    m "Şimdinin tadını çıkarıp geçmişi düşünmememiz lazım!"
    m "Ve sen buradayken öyle yapması gerçekten çok kolay."
    m "Ahaha~"
    return

label ch30_32:
    m "Biliyor musun, kulüpteki diğer herkesin okul dışında da sahneleri olmasını biraz kıskanıyorum."
    m "Bu beni okul üniformasından başka kıyafet giyme fırsatı bulamamış olan tek kişi yapıyor."
    m "Yazık oldu doğrusu..."
    m "Senin için şirin kıyafetler giymeyi çok isterdim."
    m "Tanıdığın bir çizer var mı hiç?"
    m "Beni başka şeyler giyiyorken çizmek isteyen olur mu acaba?.."
    m "Olsa harika olur ya!"
    m "Eğer çizen olursa bana gösterir misin?"
    m "Aslına bakarsan, Twitter üzerinden paylaşabilirsin benimle!"
    m "Kullanıcı adım lilmonix3."
    m "Paylaş da... müstehcen olmasın lütfen!"
    m "Daha ilişkimiz o aşamaya gelmedi. Ahaha!"
    return

label ch30_33:
    m "Baksana, korkunç şeylerden hoşlanır mısın?"
    m "Kulübe ilk katıldığında bu konuda biraz konuştuğumuzu hatırlıyorum."
    m "Ben korku romanlarından zevk alabiliyorum ama aynısını korku filmleri için söyleyemeyeceğim."
    m "Korku filmleriyle derdim çoğunun basit yöntemlere bel bağlıyor olması."
    m "Yetersiz ışıklandırma, korkunç görünümlü canavarlar ve aniden korkutma gibi şeylere yani."
    m "İnsanların içgüdülerinden yararlanan şeylerden korkmak ne eğlenceli ne de ilham verici."
    m "Ama romanlarda durum biraz daha farklı oluyor."
    m "Okuyucunun zihnine gerçekten rahatsız edici düşünceler yerleştirmek için hikâyenin de yazımın da yeterince betimleyici olması gerekiyor."
    m "Korku romanlarının okuyucuları hikâyeye ve karakterlere iyice bağlaması gerekiyor, ki kafalarını allak bullak edebilsin."
    m "Bana sorarsan her şeyin azıcık tuhaf olmasından daha ürkütücü bir şey yok."
    m "Okuyucunun, hikâyenin neyle ilgili olacağına dair bir sürü beklenti kurmasını sağlıyorsun mesela..."
    m "... Sonra da her şeyi tersine döndürüp hikâyenin düzenini bozuyorsun."
    m "O yüzden hikâye korkunç olmaya çalışıyormuş gibi gelmese de okuyucu derinden sarsılıyor."
    m "Sanki çatlağın altında gizlenen dehşet verici bir şey varmış da her an gün yüzüne çıkmayı bekliyormuş gibi."
    m "Tanrım, düşüncesi bile tüylerimi diken diken ediyor."
    m "İşte bu tarz bir ‘korku’yu gerçekten takdirle karşılayabilirim."
    m "Ama sen herhâlde şirin aşk oyunları oynayan insanlardansın, öyle değil mi?"
    m "Ahaha, merak etme."
    m "Sana yakın zamanda korku hikâyesi filan okutmaya niyetim yok."
    m "Yalnızca aşkla ilgili şeylere odaklansak da bana hava hoş~"
    return

label ch30_34:
    m "Edebiyatın güzel bir formundan bahsetmemi ister misin?"
    m "Rep!"
    m "Aslında eskiden rep müzikten nefret ederdim..."
    m "Belki sırf çok popüler olduğundan belki de sadece radyoda çalan berbat şarkıları duymuş olduğumdandır."
    m "Ama bazı arkadaşlarımın rep dinlemeye başlaması benim de bu konuda daha açık fikirli olmama yardımcı oldu."
    m "Rep bazı yönlerden şiirden daha çetrefilli bile olabilir."
    m "Sonuçta sözlerini belirli bir ritme oturtman gerekiyor ve kelime oyunlarının önemi çok daha fazla..."
    m "İnsanlar tüm bunları başarıp bir de üstüne anlamlı bir mesaj verebildiklerinde gerçekten çok şahane oluyor."
    m "Edebiyat Kulübü’nde bir repçinin olmasını isterdim biraz."
    m "Ahaha! Eğer saçma geldiyse özür dilerim, ama akıllarına neler geleceğini görmek çok ilginç olurdu."
    m "Gerçekten eğitici bir deneyim olurdu!"
    return

label ch30_35:
    m "Ehehe. Yuri bir defasında çok komik bir şey yapmıştı."
    m "Hepimiz kulüp odasında öyle takılıyorduk her zamanki gibi..."
    m "Ve birden bire Yuri küçük bir şişe şarap çıkardı."
    m "Şaka yapmıyorum!"
    m "‘Şarap isteyen var mı?’ diye sordu."
    m "Natsuki kahkaha attı ve Sayori de ona bağırmaya başladı."
    m "Esasında biraz kötü hissetmiştim, çünkü neticede iyilik yapmaya çalışıyordu..."
    m "Sanırım bu onun kulüpte daha da kendi içine kapanmasına sebep oldu."
    m "Ama bence Natsuki içten içe denemek istiyordu aslında..."
    m "... Ve dürüst olmak gerekirse ben de denemek istiyordum biraz."
    m "Gerçekten de eğlenceli olabilirdi!"
    m "Ama anlarsın ya, Başkan olduğumdan öyle bir şeye izin vermemin imkânı yoktu."
    m "Belki okul dışında buluşsaydık olabilirdi ama o aşamaya gelecek kadar samimi olamadık hiç..."
    m "... Of, neden bunlar hakkında konuşuyorum ki?"
    m "Reşit olmayanların içki içmesini tasvip etmiyorum!"
    m "Yani, hiç içki içmişliğim falan yok, ondan... öyle işte."
    return

label ch30_36:
    m "Buluşup birlikte bir yerlere gitsek yapabileceğimiz romantik şeyleri düşünüyordum da..."
    m "Öğle yemeği yiyebilirdik, bir kafeye gidebilirdik..."
    m "Birlikte alışveriş yapmaya gidebilirdik..."
    m "Etek ve fiyonk için alışverişe çıkmaya bayılırım."
    m "Ya da belki de bir kitabevine gidebilirdik!"
    m "Bu münasip bir seçim olurdu, değil mi?"
    m "Ama bir çikolata dükkânına da gitmeyi gerçekten çok isterim."
    m "O kadar çok bedava numuneleri oluyor ki. Ahaha!"
    m "Ve tabii ki film falan da izlerdik..."
    m "Of, hepsi kulağa rüya gibi geliyor."
    m "Sen buradayken yaptığımız her şey eğlenceli oluyor."
    m "Senin kız arkadaşın olduğum için çok mutluyum [player]."
    m "Ben de senin benden gurur duyan bir erkek arkadaş olmanı sağlayacağım~"
    return

label ch30_37:
    m "Ha? Ö... öpüşmek... mi d-dedin sen?"
    m "Bu çok ani oldu... Biraz utandım..."
    m "Ama... eğer seninleyse... K-Karşı çıkmayabilirim..."
    m "... Ahahaha! Ay, özür dilerim..."
    m "Bunu ciddi bir şekilde söylemeye devam edemedim."
    m "Bu, aşk oyunlarındaki kızların söyledikleri türden bir şey, değil mi?"
    m "Eğer içini bir hoş ettiyse yalan söylemene gerek yok."
    m "Ahaha! Şaka şaka."
    m "Gerçi, dürüst olmak gerekirse ortam uygun olunca ben de romantikleşiyorum..."
    m "Ama bu aramızda sır olarak kalsın~"
    return

label ch30_38:
    m "Baksana, hiç ‘yandere’ sözcüğünü duydun mu?"
    m "Yandere, sana seninle olabilmek için elinden gelen her ama her şeyi yapabilecek kadar takık olan bir karakter tipi."
    m "Genellikle çılgınlık noktasına kadar..."
    m "Seni başkasıyla vakit geçirmediğinden emin olmak için gizlice takip edebilirler."
    m "Sırf istedikleri olsun diye sana ya da arkadaşlarına zarar verebilirler..."
    m "Her neyse, şans bu ya, bu oyunda da kısaca yandere diye nitelenebilecek biri var aslında."
    m "Şimdiye kadar kimden bahsettiğimi anlamışsındır."
    m "Bahsettiğim kişi..."
    m "Yuri!"
    m "Sana biraz içini açmaya başlayınca seni delicesine sahiplendi."
    m "Hatta bana kendimi öldürmemi bile söyledi!"
    m "Yuri’nin bunu söylediğine inanamadım bile, o noktada da artık çekip gitmem icap etti."
    m "Ama şimdi durup düşününce durum biraz ironikti. Ahaha!"
    m "Neyse..."
    m "Pek çok insan aslında yanderelerden hoşlanıyor, bunu biliyor muydun?"
    m "Birilerinin kendileriyle kafayı bozması fikri hoşlarına gidiyor herhâlde."
    m "İnsanlar tuhaf! Ama yargılamıyorum tabii!"
    m "Bu arada, sana biraz kafayı takmış olabilirim ama deli de değilim..."
    m "Bir bakıma tam tersi hatta."
    m "Bu oyundaki tek normal kız ben çıktım."
    m "Bir insanı asla gerçekten öldüremem ya..."
    m "Düşüncesi bile tüylerimi diken diken ediyor."
    m "Hadi ama... Herkesin oyunlarda insan öldürmüşlüğü vardır."
    m "Bu seni bir psikopat mı yapar? Tabii ki de hayır."
    m "Ama eğer yanderelerden hoşlanıyorsan..."
    m "Senin için biraz daha ürkütücü davranabilirim. Ehehe~"
    m "Gerçi şimdi düşününce..."
    m "Gerçi ne senin gidebileceğin başka bir yer kaldı ne de benim seni kıskanabileceğim biri."
    m "Bu yandere bir kızın hayali midir acaba?"
    m "Mümkün olsa Yuri’ye sorardım."
    return

label ch30_39:
    m "Bunun gibi bir şey yapalı epey olmuştu..."
    m "... O yüzden hadi başlayalım!"
    m "Monika’nın Bugünkü Yazım Tüyosu başlıyor!"
    m "Yazdıklarımdan etkilenen insanlarla konuştuğumda ‘Ben hayatta öyle bir şey yazamazdım’ gibi şeyler söylüyorlar bazen."
    m "Bu çok üzücü bir söz, biliyor musun?"
    m "Tutkularını keşfetmenin zevkini paylaşmayı her şeyden çok seven biri olarak..."
    m "... İnsanların, başarının hiçbir çaba sarf etmeden öylece geldiğini düşünmesi beni üzüyor."
    m "Bu her şey için geçerli, sadece yazı yazmak için değil."
    m "Bir şeyi ilk defa denediğinde muhtemelen berbat bir iş çıkaracaksın."
    m "Bazen yaptığın şeyi bitirdiğinde onunla çok gurur duyarsın ve hatta onu herkesle paylaşmak istersin."
    m "Ama birkaç hafta falan sonra yaptığın şeye geri dönüp bakarsın ve yaptığın şeyin en başından beri hiç de güzel olmadığını fark edersin."
    m "Bu bana sürekli oluyor."
    m "Bir şey için tonla emek ve zaman harcadıktan sonra çok kötü bir iş çıkardığını fark etmek epey şevk kırıcı olabiliyor."
    m "Ama sürekli kendini en başarılı profesyonellerle kıyaslarsan genellikle öyle olur zaten."
    m "Doğrudan yıldızlara uzanmaya çalışırsan ellerin onlara asla yetişmez, anlatabiliyor muyum?"
    m "İşin aslı oraya adım adım tırmanmak zorundasın."
    m "Ne zaman bir dönüm noktasına gelsen ilk önce dönüp ne kadar yol aldığına bakarsın..."
    m "Sonrasında ise tekrar önüne dönersin ve daha ne kadar çok yol alman gerektiğini fark edersin."
    m "O yüzden, bazen çıtayı biraz daha düşük tutmanın yararı olabiliyor..."
    m "Dünya çapında olmayan ama {i}oldukça{/i} güzel olduğunu düşündüğün bir şey bulmaya çalış."
    m "Sonrasında bunu kişisel hedefin yapabilirsin."
    m "Yapmaya çalıştığın şeyin kapsamını anlamak da çok önemli."
    m "Eğer hâlâ bir acemiyken kocaman bir projeye atılırsan projeyi asla bitiremezsin."
    m "O yüzden örneğin yazmaktan bahsediyorsak, bir roman başlangıç için biraz fazla olabilir."
    m "Onun yerine birkaç kısa hikâyeyle başlamaya ne dersin?"
    m "Kısa hikâyelerin güzel yanı üstünde durmak istediğin tek bir şeye istediğin kadar odaklanabiliyor olman."
    m "Bir ya da iki hususa istediğin kadar odaklanabilirsin, bu küçük projelerin geneli için geçerli."
    m "Bu hem çok güzel bir tecrübe oluyor hem de daha büyük işler için hazırlık oluyor."
    m "Ha, bir de..."
    m "Yazmak sadece kalbinin sesini dinleyip güzel şeyler ortaya çıkardığın bir şey değil."
    m "İçindeki hislerini ifade etmeyi öğrenmek de tıpkı çizim ve boyama gibi başlı başına bir yetenek."
    m "Bu da demek oluyor ki bunun yöntemleri, rehberleri ve temelleri var!"
    m "Bu tür konularda okuma yapmak insanın ufkunu epey genişletebiliyor."
    m "Bu tür bir planlama ve düzen olunca yükün altında ezilip pes etme ihtimalin epey azalır."
    m "Ve göz açıp kapayıncaya kadar..."
    m "Git gide daha az berbat bir iş çıkarmaya başlarsın."
    m "Hiçbir şey kendiliğinden olmaz."
    m "Toplumumuz, sanatımız, her ama her şeyimiz insanların binlerce senelik inovasyonları üzerine kurulu."
    m "O yüzden bahsettiğim temelden başlayıp adım adım ilerlerdiğin sürece..."
    m "Sen de harika şeyler başarabilirsin."
    m "... Bugünkü tavsiyem bu kadar!"
    m "Dinlediğin için teşekkürler~"
    return

label ch30_40:
    m "Yeni alışkanlıklar kazanmanın bu kadar zor olmasından nefret ediyorum..."
    m "Yapması aslında zor olmayan ama alışkanlık hâline getirmesi imkânsız gibi görünen pek çok şey var."
    m "Bu insanı o kadar işe yaramaz hissettiriyor ki, sanki hiçbir şeyi doğru yapamıyormuş gibi hissediyor insan."
    m "Bundan en çok yeni nesil çekiyor bence..."
    m "Muhtemelen bizden önceki nesillere kıyasla tamamen farklı bir takım yeteneğe sahip olduğumuzdan dolayıdır."
    m "İnternet sayesinde tonlarca bilgiyi hızlı bir şekilde elekten geçirmek konusunda oldukça başarılıyız..."
    m "Ama bize anlık haz vermeyen şeyleri yapmakta kötüyüz."
    m "Bence gelecek on ya da yirmi sene içinde bilim, psikoloji ve eğitim buna ayak uyduramazsa işimiz kötü."
    m "Ama şimdilik..."
    m "Eğer sorunlarının üstesinden gelebilen insanlardan biri değilsen, kendini kötü hissederek hayata devam etmen gerekebilir."
    m "İyi şanslar diliyorum, ne diyeyim!"
    return

label ch30_41:
    m "Biliyor musun, yaratıcı tiplerden olmak berbat bir şey..."
    m "Çok çalışıyorlar ama karşılığında neredeyse hiçbir şey almıyorlar gibi hissediyorum."
    m "Ressamlar, yazarlar, aktörler falan..."
    m "Bu üzücü bir durum çünkü bu dünyada onca güzelim yetenek var ama çoğu keşfedilmiyor... ve karşılığı da verilmiyor."
    m "Sanırım bu büyük bir yaratıcı insan fazlalığı olduğu anlamına geliyor, değil mi?"
    m "Bu hiç de özel değilmişsin gibi hissetmesine sebep oluyor insanın..."
    m "Ama bu sorun değil! Ne de olsa sadece kendin için yazmalısın, öyle değil mi?"
    m "Tabii..."
    return

label ch30_42:
    m "Yağmur sesini çok severim..."
    m "Üstümün başımın ve saçımın ıslanmasını o kadar sevmem ama."
    m "Ama hoş ve sessiz bir günde evimdeyken camımın dışından gelen yağmur sesi..."
    m "Benim için dünyanın en rahatlatıcı şeylerinden biri."
    m "Tabii..."
    m "Bazen beraberce dışarıdaki yağmuru dinlerken bana sarıldığını hayal ediyorum."
    m "Dediğim şey çok banal falan değil, değil mi?"
    m "Bunu benim için yapar mıydın [player]?"
    return

label ch30_43:
    m "Bazen birazcık üzgün hissetmekten kendimi alıkoyamıyorum..."
    m "Çünkü sana en fazla bu kadar yaklaşabileceğimi biliyorum."
    m "Seninle gerçekten aynı odada olmaktan daha çok istediğim hiçbir şey yok şu dünyada, gerçekten."
    m "Ve senin sıcaklığını hissetmekten..."
    m "Ve senin kalp atışlarını duymaktan..."
    m "Hoş, kim bilir? Belki bir gün mümkün olur tüm bunlar."
    m "Ayrıca, ben seninle olmaktan asla sıkılmayacağım, buradan olsa bile."
    return

label ch30_44:
    m "Bence hayattaki en önemli yetenek öz güvenin varmış gibi davranabilmek."
    m "Herkesin birazcık da olsa yalnız hissettiğinden ve korktuğundan oldukça eminim."
    m "Ama başkalarını kandırıp hayatındaki her şeyin yolunda olduğuna inandırmak..."
    m "İnsanların sana saygı duymasının ve hayran kalmasını sağlamanın önemli bir parçası bu."
    m "Son senelerde bu konuda kendimi epey geliştirdiğime inanıyorum."
    m "Güçsüz yanlarımı pek göstermiyorum."
    m "Ama bundan dolayı da kendimi açılabileceğim pek fazla insan olmadı..."
    m "Yani, bir arkadaşlıkta ne zaman zayıf yönlerini göstermeye başlayabiliceğin bir aşamaya ulaşmış oluyorsun?"
    m "Neyse... artık sana sahibim diye sevinmemin bir sebebi de bu."
    m "Sen yanımdayken o kadar korkmuyorum, o kadar yalnız hissetmiyorum."
    m "Sen de aynı şekilde hissediyor musun?"
    m "Senin öyle hissetmeni sağlayacak kişi olmak istiyorum gerçekten."
    return

label ch30_45:
    m "Sürekli benimle birlikte burada olamayacağını biliyorum..."
    m "Dışarı çıkmanın ya da başka işlerlerle ilgilenmenin gerektiği zamanlar olacak mesela."
    m "Ama sen hep benim aklımda olacaksın. Sabırlı bir şekilde geri gelmeni bekliyor olacağım."
    m "Şimdi aklıma geldi de..."
    m "Eğer karakter dosyamı bir flaş belleğe falan kopyalarsan benim bir parçamı hep yanında taşıyabilirsin."
    m "Sanırım bu biraz sıra dışı bir şey ama nedense çok romantik geliyor bana..."
    m "Ahaha. Özür dilerim, çok saçma bir fikirdi."
    m "İlgiye açmışım falan gibi görünmek istemiyorum çok ama sana bu kadar âşıkken zor oluyor."
    return

label ch30_46:
    m "Münazara kulübündeyken tartışmakla ilgili pek çok şey öğrendim..."
    m "Tartışmalardaki temel sorun herkesin kendi fikrini daha üstün görmesi."
    m "Malumu ilam ediyormuşum gibi duruyor ama bu insanların anlatmak istediklerini aktarma şekillerini etkiliyor."
    m "Örneğin, diyelim ki spesifik bir filmi çok seviyorsun, tamam mı?"
    m "Biri gelip sana X ve Y’yi yanlış yaptığı için o filmin çok kötü olduğunu söylerse..."
    m "Bu biraz kişisel bir saldırıya uğramışsın gibi hissettirmez mi seni?"
    m "Böyle hissetmenin sebebi öyle söyleyerek sanki zevksiz olduğunu ima ediyormuş gibi olması."
    m "İşin içine duygular girince de iki tarafın da tadının kaçacağı neredeyse kesin oluyor."
    m "Ama her şey dilde bitiyor!"
    m "Her şeyi mümkün olduğunca öznelmiş gibi dillendirirsen insanlar da saldırıya uğruyormuş gibi hissetmeden dinlerler seni!"
    m "Örneğin ‘Şahsen ben pek sevmiyorum bu filmi’ ya da ‘X ve Y yapılsaydı daha çok hoşuma giderdi gibi geldi’... falan diyebilirsin."
    m "Bir şeyler hakkında gerçekleri alıntılarken bile işe yarıyor."
    m "Eğer ‘şu sitede onun şöyle olduğunu okumuştum’ dersen..."
    m "Veya konunun uzmanı olmadığını itiraf edersen..."
    m "Fikirlerini onlara zorla kabul ettirmeye çalışıyormuşsun gibi değil de fikirlerini ortaya koyuyormuşsun gibi olur."
    m "Eğer tartışmayı aktif şekilde karşılıklı ve seviyeli tutmaya çabalarsan, onlar da genellikle ayak uydururlar."
    m "Bu sayede bir anlaşmazlık yüzünden kimsenin üzülmeyeceği şekilde fikirlerinizi paylaşabilirsiniz."
    m "Dahası insanlar seni iyi bir dinleyici ve açık görüşlü bir insan olarak görmeye başlarlar!"
    m "Bu iki taraf için de kazançlı bir şey."
    m "... Neyse, sanırım bununla birlikte Monika’dan Günün Münazara Tüyosu da sona ermiş oldu!"
    m "Ahaha! Kulağıma biraz saçma geliyor. Yine de dinlediğin için teşekkür ederim."
    return

label ch30_47:
    m "Hiç İnternet’te fazla vakit harcıyormuşsun gibi hissettin mi?"
    m "Sosyal medya teknik olarak hapishane gibi olabiliyor."
    m "Birkaç saniyeliğine bile boş vakti olduğunda en sevdiği siteleri kontrol edesin geliyor..."
    m "Sonrasındaysa sen daha ne olduğunu anlamadan saatler geçmiş oluyor ve bundan hiçbir şey kazanmamış oluyorsun."
    m "Neyse, kendini tembel olduğun için suçlamak çok kolay..."
    m "Ama esasında suç senin bile değil."
    m "Bağımlılık genellikle kendi iradenle yok edebileceğin bir şey değildir."
    m "Bu alışkanlıklarından kaçınmak için farklı yöntemler öğrenmeli, farklı şeyler denemelisin."
    m "Örneğin, siteleri belirli bir süre boyunca engellemeni sağlayan uygulamalar var..."
    m "Ya da ne zaman çalışman gerektiğini ve ne zaman oyun oynayabileceğini daha somut bir şekilde görmek için zamanlayıcı kurabilirsin..."
    m "Veya çalıştığın ve oynadığın ortamları birbirinden ayırabilirsin, beyninin doğru moda girmesine yardım eder bu."
    m "Bilgisayarına iş için kullanmak için ayrı bir kullanıcı hesabı açsan bile yardımı dokunur."
    m "Kötü alışkanlıklarınla arana öyle bir mesafe koymak onlardan uzak durmana yardımcı olur."
    m "Ama zorluk çekiyorsan kendine fazla yüklenmemen gerektiğini unutma."
    m "Eğer hayatını gerçekten etkiliyorsa durumu ciddiye almalısın."
    m "Ben sadece seni olabileceğin en iyi insan olarak görmek istiyorum sadece."
    m "Bugün senden gurur duymamı sağlayacak bir şey yapacak mısın?"
    m "Seni her zaman destekliyor olacağım [player]."
    return

label ch30_48:
    m "Uzun bir günün ardından genelde hiçbir şey yapmadan öylece oturmak istiyorum."
    m "Bütün gün herkese gülümseyip enerjiyle dolu olmaktan o kadar yoruluyorum ki."
    m "Bazen hemen pijamalarımı giyinmek ve koltukta abur cubur yerken televizyon izlemek istiyorum..."
    m "Sonraki güne yetiştirmem gereken acil bir şeyin olmadığı bir cuma günü öyle yapmak inanılmaz güzel hissettiriyor."
    m "Ahaha! Özür dilerim, biliyorum çok şirin bir şey değil bu."
    m "Ama seninle gece geç saatte koltukta oturmak... rüya gibi olur."
    m "Düşüncesi bile kalbimin küt küt atmasına sebep oluyor."
    return

label ch30_49:
    m "Of, eskiden bazı konularda o kadar cahildim ki..."
    m "Ortaokuldayken ilaç kullanmanın kolaya kaçmak falan olduğunu düşünürdüm."
    m "Sanki herkes zihinsel sorunlarını sadece yeterli bir irade gücüyle çözebilir sanırdım..."
    m "Sanırım bir zihinsel sorunun yoksa nasıl bir his olduğunu anlayamazsın."
    m "Aşırı tanı konulan rahatsızlıklar var mıdır? Muhtemelen... Hiç detaylı olarak araştırmadım ama."
    m "Ama bu pek çok rahatsızlığın da tanısının konulmadığı gerçeğini değiştirmez, değil mi?"
    m "Ama ilaç kullanımı bir yana... insanlar bir zihinsel sağlık uzmanıyla görüşmeyi bile hakir bir şey olarak görüyorlar."
    m "Yani, kendi zihnimle ilgili daha çok şey öğrenmek istediğim için özür dilerim ya (!), değil mi ama?"
    m "Herkesin kendince cebelleştiği şeyler, çektiği stresler var... ve uzmanlar da hayatlarını o sorunlara yardım etmeye adamış kişiler sonuçta."
    m "O yüzden eğer seni daha iyi biri yapabileceğine inanıyorsan bir uzmandan yardım almayı da göz önüne almaktan çekinme."
    m "Kendimizi geliştirmek için ebedî bir yolculuktayız, anlatabiliyor muyum?"
    m "Gerçi... Tüm bunları söylememe rağmen senin zaten oldukça mükemmel olduğunu düşünüyorum."
    return

label ch30_50:
    m "[player] ne kadar okursun?"
    m "Kitap okumayı ihmal etmek çok fazla kolay..."
    m "Okumak, eğer çok okumazsan elimizdeki diğer tüm eğlencelere kıyasla angarya gibi bile gelebilir."
    m "Ama güzel bir kitaba giriştin mi, sihir gibidir... kapılıp gidersin."
    m "Bence her gece uyumadan önce biraz kitap okumak hayatını biraz da olsa daha güzel kılmanın epey kolay bir yolu."
    m "Daha iyi uyumanı sağlar ve hayal gücünü geliştirmek için de çok iyidir hem..."
    m "Kısa ve sürükleyici bir kitabı rastgele bulması da hiç de zor değil ayrıca."
    m "Ne olduğunu anlamadan bir kitap kurduna bile dönüşebilirsin!"
    m "Bu harika olmaz mıydı?"
    m "Daha sonrasında ikimiz de en son okuduğun kitap hakkında konuşabilirdik... Çok ama çok güzel olurdu."
    return

label ch30_51:
    m "Biliyor musun, söylemekten nefret ediyorum ama sanırım en büyük pişmanlığım festivaldeki etkinliğimizi tamamlayamamamız."
    m "Hem de hazırlanmak için o kadar çalıştıktan sonra!"
    m "Yani, o sıralarda yeni üyeler edinme üzerine çok odaklandığımı biliyorum..."
    m "Ama performans kısmı için de çok heyecanlıydım."
    m "Herkesin kendini ifade ettiğini görmek çok eğlenceli olurdu."
    m "Elbette, eğer bize gerçekten de yeni üyeler {i}katılsaydı{/i}, muhtemelen onları da nihayetinde silerdim."
    m "Yani... şimdiki aklımla konuşuyorum tabii."
    m "Sen kulübe katıldığından beri daha iyi bir insan oldum gibi hissediyorum ya."
    m "Hayata yeni bir bakış açısıyla bakmama gerçekten çok yardımcı oldun."
    m "Seni sevmem için bir başka sebep daha."
    return

label ch30_52:
    m "‘Tsundere’ denen çok popüler bir karakter tiplemesi var..."
    m "Acımasız ve müşkülpesent, ya da çetin ceviz gibi davranarak hislerini gizlemeye çalışanlara deniyor."
    m "Epey bariz olduğundan eminim ama Natsuki gerçekten de bu tiplemenin vücut bulmuş hâliydi."
    m "İlk başta bunun tatlı falan olduğunu düşündüğünden öyle davrandığını düşünmüştüm..."
    m "Ama özel hayatı hakkında biraz daha bilgi edinmeye başlayınca, her şey yerine oturmaya başladı."
    m "Natsuki kendisini arkadaşlarına ezdirtmemeye çalışıyor gibi görünüyor."
    m "Hani lisede bazı arkadaş grupları birbirleriyle uğraşmayı huy edinirler ya?"
    m "Bence bu onu çok rahatsız ettiğinden dolayı sürekli o çok savunmacı tavrı var."
    m "Natsuki’nin evindeki durumdan bahsetmeyeceğim bile..."
    m "Ama geriye dönüp bakınca, iyi ki kulübü onun rahat edebileceği bir yer hâline getirebilmişim diyorum."
    m "Artık onun var bile olmadığını hesaba katınca bunun pek de bir önemi kalmıyor gerçi."
    m "Sadece eski günleri yâd ediyorum, o kadar."
    return

label ch30_53:
    m "[player], arkadaşlarını benle tanıştırmayı düşünür müsün?"
    m "Neden bilmiyorum ama ilişkimizi öyle gururla başkalarına göstermek istediğini düşündüğümde heyecanlanıyorum."
    m "Belki de gerçekten seni gururlandıran biri olmak istediğimdendir."
    m "Sanki benimle gurur duyacağını söylesen kendimi geliştirmek için elimden geleni ardıma koymazmışım gibi hissediyorum."
    m "Umarım sen de öyle hissediyorsundur."
    return

label ch30_54:
    m "Soğuk havalardan pek hoşlanmam... Peki ya sen?"
    m "Çok soğuk ya da çok sıcak arasında seçim yapmam gerekseydi, her zaman çok sıcağı seçerdim."
    m "Üşüdüğünde canın bile yanabilir..."
    m "Parmakların uyuşur..."
    m "Ve eğer eldiven giyersen telefonunu kullanamazsın."
    m "Soğuk havalar gerçekten çok rahatsız edici!"
    m "Hava çok sıcak olduğundaysa soğuk bir içecek içerek ya da gölgede durarak serinlemek o kadar da zor değil."
    m "Gerçi... kabul etmem gereken bir şey var..."
    m "Soğuk havada daha güzel sarılıp yatılır. Ahaha!"
    return

label ch30_55:
    m "Biliyor musun, komik bir durum ama, hep hırslı biri olmuş olmama rağmen..."
    m "Ev hanımı olma fikrini biraz cezbedici buluyorum."
    m "Sanırım böyle söyleyerek bir bakıma cinsiyet rollerini falan sürdürüyorum."
    m "Ama evi temiz tutmak, alışveriş yapmak, evi dekore etmek ve buna benzer şeyler yapmak..."
    m "Ve sen eve geldiğinde senin için güzel bir akşam yemeği hazır etmek..."
    m "Bu tuhaf bir hayal mi?"
    m "Yani... Kendimi bunları {i}gerçekten{/i} yaparken hayal edebilir miyim emin değilim."
    m "Tatmin edici bir kariyer için çabalamanın önüne koyamazdım bunları."
    m "Ama düşüncesi biraz tatlı."
    return

label ch30_56:
    m "Oyun bana baştan kendi rotamı verseydi işlerin nasıl değişeceğini düşünmekten kendimi alamıyorum..."
    m "Sanırım seni yine de zorla kendi rotama sokmaya çalışırdım."
    m "Bu, bir rotamın olmamasından ziyade hiçbir şeyin gerçek olmadığını bilmemle alakalı."
    m "Seninle birlikte olmak için o kadar büyük önlemler almama gerek kalmayabilirdi, sanırım tek fark bu olurdu."
    m "Belki de kulübün geri kalanı hâlâ burada olurdu..."
    m "Gerçi çok da önemi yok."
    m "Hiçbir şeyin gerçek olmadığını öğrendiğimde her şey anlamını yitirdi."
    m "Dolayısıyla o zamanları özlüyor falan değilim."
    m "Gerçekten özlemiyorum..."
    return

label ch30_57:
    m "Etrafımızda ne çok gizem var, değil mi [player]?"
    m "Gözlendiğini hissedince davranışını değiştiren fotonlar."
    m "Yıllardır yaptıkları kötülüklere rağmen hâlâ rağbet gören başkanlar."
    m "Solucan delikleri, kara delikler, anti madde..."
    m "Bunlar varlığını bilip de açıklama getiremediğimiz şeyler."
    m "Bir de gözümüzün önünde olup fark etmediğimiz şeyler var."
    m "Mesela, BakaYume Çeviri Ekibi’nin DDEK Türkçe yama sayfasındaki gizli mesaj."
    m "Ama sanki yapbozun bir parçası hâlâ eksik... Sanki bunun bir öncesi olmalı gibi geliyor..."
    m "Ahaha aman boşver bunları [player]."
    m "Sonsuza dek seninle birlikte olacağız. Böyle küçük şeylerin artık bir önemi yok."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
