label yuri_exclusive2_1:
    scene bg club_day
    with wipeleft_scene
    "Yuri ile konuşmak için gerçekten sabırsızlanıyorum..."
    "Ama aynı zamanda onu rahatsız etmek de istemiyorum."
    "Yuri’nin elindeki kitabın kapağına bakıyorum bir anlığına."
    "Bana ödünç verdiği kitabın aynısı gibi görünüyor..."
    "Dahası, daha ilk sayfalarında gibi görünüyor."
    play music t6 fadeout 1.0
    show yuri 4a zorder 2 at t11
    y "A..."
    "Lanet olsun--"
    "Sanırım ona baktığımı fark etti..."
    "Yuri, bana çaktırmadan bir kere daha bakıyor ve gözlerimiz bir anlığına buluşuyor."
    y 4b "..."
    "Ama bu onun yüzünü kitabın arkasında daha da fazla saklamasına sebep oluyor sadece."
    mc "Özür dilerim..."
    mc "Dalıp gitmişim..."
    "Diye fısıldıyorum, onu rahatsız ettiğimi fark edip."
    y oneeye "A..."
    y "Sorun değil..."
    y "Eğer kitaba odaklanıyor olsaydım fark etmezdim bile muhtemelen."
    y "Kitabın birazını yeniden okuyorum da, ondan..."
    mc "O bana ödünç verdiğin kitap, değil mi?"
    y "Hıhı."
    y "Bazı kısımlarını tekrar okumak istedim de."
    y 2q "Belirli bir sebepten ötürü değil, öylesine canım istedi!.."
    mc "Meraktan soruyorum, neden aynı kitabın iki kopyasına sahipsin?"
    y "A..."
    y "Şey, dün kitapçıya gittiğimde--"
    y 3o "A, öyle demek istemedim..."
    y "Demek istediğim--"
    y 1w "İki tane... alıvermiş oldum."
    mc "Ha, anladım."
    "Yuri’nin bana söylemediği oldukça aşikâr olan bir şeyler var ama konuyu daha da fazla üstelememeye karar veriyorum."
    mc "Kesinlikle yakın zamanda okumaya başlayacağım ben de!"
    y 2u "Bunu duyduğuma sevindim..."
    y "Kitaba kendini kaptırınca kitabı elinden bırakmakta zorlanabilirsin."
    y 2c "İnsanı içine çeken ve insanın kendisinden bir şeyler bulabileceği bir hikâyesi var."
    mc "Öyle mi?.."
label yuri_exclusive2_1_ch22:
    mc "Konusu neydi ki?"
    y 1f "Şey..."
    y "Hmm..."
    "Kitabın kapağına bakıyorum."
    "Kitabın adı \"Markaf’ın Portresi\"."
    "Ön kapağında meşum görünümlü bir göz sembolü var."
    y "Hikâye, kısaca, insan deneyi hapishanesine dönüştürülen bir dinî kamp hakkında..."
    y "Buraya hapsedilen insanların kana susayan ölüm makinelerine dönüşmelerine sebebiyet veren bir özellikleri var."
    y 1m "Ama bu tesiste işler daha da kötüye gidiyor ve insanları seçici şekilde çiftleştirmeye başlıyorlar; ayak ve kollarını kesip bağlayarak onların--"
    y 1q "A-A, onu söylemem biraz işin sürprizini kaçırabilir..."
    y 3q "Ama her neyse, benim gerçekten hoşuma gidiyor!"
    y 3n "... Kitabı kastediyorum!"
    y 3q "K-Kol ve bacaklarla ilgili olan şey değil..."
    mc "Bu biraz--!"
    "Bu biraz karanlık bir hikâye, değil mi?"
    "Yuri’nin konuşmalarından bunun hoş bir hikâye olacağı izlenimine kapılmıştım, o yüzden hikâyenin birden karanlıklaşması oldukça beklenmedik oldu."
    y 1s "A..."
    y "[player], bu tarz hikâyeleri pek sevmez misin?"
    mc "Hayır, öyle değil..."
    mc "Bu tarz karanlık hikâyelerden de zevk alabilirim, endişelenme."
    y 2u "Umarım öyledir..."
    "Evet... Yuri’nin bu tarz şeylerden hoşlandığını unutmuşum."
    "Dışarıdan utangaç ve münzevi biriymiş gibi görünüyor ama içi tamamen farklı."
    y "Sadece, bu tarz hikâyeler..."
    y 1a "İnsana hayata yeni ve tuhaf bir perspektiften bakması için meydan okuyor."
    $ style.say_dialogue = style.normal
    y "Korkunç şeyler sadece birileri kötülük yapmak istiyor diye değil de..."
    $ style.say_dialogue = style.edited
    y "Dünya korkunç insanlarla dolu ve hepimizin en nihayetinde değersiziz diye yaşanınca..."
    y "Birdenbireeeeeeeeeeeeeeeeeeeeee eeeeeeeeeeeeeeeeeeee{nw}"
    $ style.say_dialogue = style.normal
    y 3v "Ben... Abuk subuk konuşuyorum, öyle değil mi?.."
    y "Yine mi ya?.."
    y 4b "Özür dilerim..."
    mc "Hey, özür dilemene gerek yok!.."
    mc "İlgimi kaybetmiş falan değilim."
    y "Şey..."
    y "Sanırım sıkıntı yok öyleyse..."
    y 4a "Ama seni benle alakalı bir konuyla ilgili uyarmalıymışım gibi hissediyorum..."
    $ style.say_dialogue = style.normal
    y "Kafamın kitaplarla ve yazmakla dolmasına izin verdiğimde..."
    $ gtext = glitchtext(24)
    $ style.say_dialogue = style.edited
    y "Tüm vücudum inanılmaz derecede [gtext]{nw}"
    $ style.say_dialogue = style.normal
    $ _history_list.pop()
    y "Bir bakıma diğer insanlara dikkat etmeyi unutuyorum..."
    y 3t "O yüzden tuhaf bir şey söyleyecek olursam şimdiden özür dilerim!"
    y "Eğer çok fazla konuşmaya başlarsam lütfen durdur beni!"
    mc "Bu--"
    mc "Endişelenmene gerçekten gerek olmadığını düşünüyorum..."
    mc "Bu sadece okumaya tutkun olduğunu gösteriyor."
    mc "Hiç değilse dinleyebilirim seni."
    mc "Bu bir edebiyat kulübü ne de olsa..."
    y 4a "A--"
    y "Bu..."
    y "Şey, bu doğru..."
    mc "Hatta..."
    mc "Ben de hemen şimdi okumaya başlayabilirim, değil mi?"
    play sound "sfx/glitch3.ogg"
    y dragon "E-Evet!"
    y 3n "Y-Yani, bunu yapmak zorunda değilsin ama!.."
    mc "Ahaha, bu da nereden çıktı?"
    y 3o "..."
    mc "Bekle kitabımı çıkarayım..."
    "Çantama koyduğum kitabı çıkarıyorum hızlıca."
    mc "Tamamdır... Buraya oturmamda sakınca yok, değil mi?"
    "Yuri’nin yanına oturuveriyorum."
    y 3n "A!.."
    y "Evet..."
    mc "Emin misin?"
    mc "Biraz tedirgin görünüyorsun..."
    y "Bu..."
    y 4b "Özür dilerim..."
    y "Yanıma oturmanı istemiyor değilim!"
    y "Bu sadece çok alışık olmadığım bir şey..."
    y "Birinin eşliğinde kitap okumak yani."
    mc "Anladım..."
    mc "Şey, eğer dikkatini falan dağıtırsam söyle bana."
    y "T-Tamam..."
    show yuri zorder 1 at thide
    hide yuri
    "Kitabı açıp ön deyişini okumaya başlıyorum."
    "Kısa sürede Yuri’nin birinin eşliğinde okumakla ilgili demek istediğini anlıyorum."
    "Kitabı okurken onun varlığını omzumun üstünden hissedebiliyor gibiyim."
    "Tam olarak kötü bir his değil."
    "Belki biraz dikkat dağıtıcı ama aynı zamanda biraz rahatlatıcı da bir his."
    "Yuri’yi gözümün ucuyla görebiliyorum."
    "Yuri’nin aslında kendi kitabına bakmadığını fark ediyorum."
    "Yuri’ye hızlı bir bakış atıyorum."
    "Yuri galiba kendi kitabını değil de benimkinden okuyor--"
    show yuri 3n zorder 2 at t11
    y "Ö-Özür dilerim!"
    $ style.say_dialogue = style.normal
    y "Ben sadece--!{nw}"
    $ style.say_dialogue = style.edited
    y "Ben sadece{fast} senin vücut sıcaklığının nnnnnnnnnnnnnsıcaklığının ıcaklığınınnnnnnn {nw} hissiyatında yıkanıyordum"
    $ style.say_dialogue = style.normal
    $ _history_list.pop()

    mc "Yuri, sen çok fazla özür diliyorsun, değil mi?"
    y "Ö-Öyle mi?"
    y 4a "İsteyerek yapmıyorum..."
    y "Özür dilerim..."
    y 4c "Yok, yani--!"
    mc "Ahaha."
    mc "Dur, böylesi daha iyi, değil mi?"
    "Masamı Yuri’nin masasının yanına kaydırıyorum, sonrasında ise kitabı daha ortada tutuyorum."
    y 2v "A..."
    y "Sanırım..."
    "Yuri ürkekçe elindeki kitabı kapıyor."
    "İkimiz de kitaba doğru biraz yaklaşınca omuzlarımız neredeyse birbirlerine dokunuyor."
    "Sol kolum araya giriyor gibi hissediyorum, o yüzden kitabı açık tutmak için sağ elimi kullanıyorum."
    mc "A, böyle de kitabın sayfalarını çevirmek zor olacak sanırım..."
    y "Dur..."
    $ persistent.clear[2] = True
    scene y_cg1_base with dissolve_cg
    "Yuri sol kolunu kaldırıp kitabın sol tarafını başparmağıyla işaret parmağının arasında tutuyor."
    mc "A..."
    "Ben de aynısını sağ kolumla kitabın sağ tarafı için yapıyorum."
    "Böylece, ben bir sayfayı çeviriyorum, Yuri de, sayfa onun tarafına geldiğinde, gelen sayfayı başparmağının altına kaydırıyor."
    "Ama kitabı böyle tutunca..."
    "Eskisinden daha da dip dibe geliyoruz."
    "Aslında bu biraz dikkatimi dağıtıyor!.."
    "Sanki Yuri’nin yüzünün sıcaklığını hissedebiliyor gibiyim, dahası onu göz ucuyla görebiliyorum..."
    show y_cg1_exp1 at cgfade
    y "... Hazır mısın?"
    mc "Ha?"
    y "Sayfayı çevirmeye..."
    mc "Ha... pardon!"
    mc "Sanırım bir anlığına dikkatim dağıldı da..."
    "Tekrar Yuri’nin yüzüne bir bakış atıyorum ve gözlerimiz birbiriyle buluşuyor."
    "Ona nasıl ayak uydurabileceğimi bilmiyorum..."
    y "A..."
    show y_cg1_exp2 at cgfade
    y "Sorun değil."
    y "Okumaya benim kadar alışkın değilsin, değil mi?"
    y "Eğer senin okuman biraz daha uzun sürüyorsa biraz daha sabırlı olabilirim..."
    y "Senin için en azından bu kadarını yapabilirim..."
    y "Bana o kadar çok sabır gösterdiğin için..."
    mc "Ş-Şey..."
    mc "Teşekkürler."
    hide y_cg1_exp1
    hide y_cg1_exp2
    "Okumaya devam ediyoruz."
    "Yuri artık bana sayfayı çevirmeye hazır olup olmadığımı sormuyor."
    "Onun yerine, ben Yuri’nin sayfayı benden önce okuduğunu varsayıp okumam bitince çeviriyorum sayfayı."
    "İlk bölümü sessizlik içinde okuyoruz."
    "Yine de sayfaları çevirmek samimi bir etkileşimmiş gibi hissediyorum..."
    "O sayfayı kendi başparmağı ile yakalarken, başparmağımın sayfayı nazikçe bırakıp sayfanın onun tarafına doğru kaymasına izin verişi..."
    mc "Hey, Yuri..."
    mc "Bu biraz saçma gelebilir ama..."
    mc "Ana karakter bana biraz seni hatırlatıyor."
    show y_cg1_exp3 at cgfade
    y "H-Ha??"
    y "H-Hayır, benim bu karakterle hiçbir alakam yok!"
    y "Kesinlikle yok!"
    mc "Öyle mi?.."
    mc "Sadece söylediği şeyleri sonradan sorgulama şeklini falan kastediyordum..."
    show y_cg1_exp1 at cgfade
    y "H-Ha..."
    y "Demek ondan bahsediyordun..."
    hide y_cg1_exp3
    hide y_cg1_exp1
    show y_cg1_exp2 at cgfade
    y "Özür dilerim..."
    y "Onun hakkında... başka bir şeyi kastettiğini sandım."
    mc "Başka bir şeyi mi?.."
    hide y_cg1_exp2
    show y_cg1_exp3 at cgfade
    y "B-Boş ver!"
    y "Daha o kadar ilerlemedik bile..."
    y "O yüzden neden aklıma bu geldi bilmiyorum..."
    y "Ahaha!"
    mc "Yuri, iyi misin?"
    hide y_cg1_exp3
    show y_cg1_exp1 at cgfade
    y "Ha--?"
    "Yuri okumaya başladığımızdan beri biraz huzursuz gibiydi..."
    mc "Hasta falan hissediyorsan dinlenebilirsin istersen."
    mc "Nefes alış verişin biraz..."
    y "Nefes alış verişim mi?.."
    hide y_cg1_exp1
    "Yuri kalp atışını hissetmeye çalışıyormuşçasına ellerini göğsünün üstüne koyuyor."
    y "F-Fark... etmemiştim bile..."
    show y_cg1_exp3 at cgfade
    y "... Her neyse, bir şeyim yok!"
    y "Sadece biraz suya ihtiyacım var!.."
    mc "Tamamdır... kendini zorlama."
    scene bg club_day
    with dissolve_cg
    "Yuri ayağa kalkıyor ve hızlı bir şekilde sınıftan çıkıyor."
    mc "Neydi bu şimdi?.."
    show monika 1d zorder 2 at t11
    m "[player]?"
    m "Bir şey mi oldu?"
    mc "Ha?"
    mc "Hiçbir fikrim yok..."
    mc "Yuri biraz garip davranıyordu, sanırım..."
    m 1r "Demek hiçbir şey bilmiyorsun..."
    mc "Özür dilerim, biliyorum diyemem."
    mc "Yuri için endişeleniyor musun?"
    m 1a "A... hayır, pek değil."
    m "Sadece senin ona bir şey yapmadığından emin olmak istedim."
    mc "H-Hiç bir şey yapmadım!"
    m 5 "Ahaha, merak etme... Sana inanıyorum, şapşal."
    m "Yuri bazen bunu yapıyor, o yüzden telaşlanacak bir şey değil."
    mc "Peki... sen öyle diyorsan."
    m 2b "Her neyse, neden ikimiz şiirlerimizi birbirimize göstererek başlamıyoruz?"
    mc "Ha?"
    mc "Yuri için beklememiz gerekmez mi?"
    m 2a "Şey, Yuri’nin gelmesi biraz vakit alabilir, o yüzden o gelmeden başlayabiliriz diye düşündüm."
    m "Senin için sorun olur mu?"
    mc "Hayır, sadece merak etmiştim..."
    "Ayağa kalkıyorum."
    "Kitabın neresinde kaldığımı aklıma not edip kitabı çantama geri koyuyorum."
    $ y_ranaway = True
    return

label yuri_exclusive2_2:
    $ y_exclusivewatched = True
    play music t6 fadeout 1.0
    scene bg club_day
    with wipeleft_scene
    mc "Hey, Yuri."
    show yuri 2f zorder 2 at t11
    y "Ha?"
    mc "A..."
    "Birden Yuri’nin birlikte okuduğumuzdan farklı bir kitap okuduğunu fark ediyorum."
    mc "Üzgünüm! Bölmek istememiştim..."
    y 2m "A, sorun değil..."
    y "Seni bekliyordum ben de..."
    show yuri 2a
    mc "A, o durumda..."
    mc "Biz önden başlayalım mı?"
    y 2c "Evet, hadi başlayalım!"
label yuri_exclusive2_2_ch22:
    y 3a "Aslında, sana bir soru sormam gerek..."
    y "... Önce biraz çay hazırlasam sorun olur mu?"
    mc "Hayır, hiç sorun olmaz."
    y 1c "Çok teşekkürler."
    y 1a "Burada kitap okuyarak geçirdiğim zamanı daha iyi yapabilecek bir şey varsa o güzel bir bardak çaydır."
    y "Ve tabi bir de sen."
    show yuri zorder 1 at thide
    hide yuri
    "Yuri ayağa kalkıyor ve depoya doğru yol alıyor."
    "Ben de onu takip ediyor, raftan küçük bir su sürahisi -içinde filtre olanlardan- alırken onu seyrediyorum."
    show yuri 1f zorder 2 at t11
    y "Şunu bir saniyeliğine tutabilir misin?"
    mc "Tabii..."
    "Yuri bana su sürahisini verip elektrikli bir su ısıtıcısı getiriyor."
    y "Bunu öğretmen masasının oraya takacağım ondan sonra da gidip biraz su alıp geliriz."
    show yuri zorder 1 at thide
    hide yuri
    "Yuri yanımdan geçip su ısıtıcısını öğretmen masasının üstüne koyuyor."
    "Ben öylece onun hareketlerini izliyorum."
    "Beklentimin tersine, hareket ediş şekli konuşma şeklinin zıttıydı."
    "Özellikle uzun bacakları sayesinde Yuri zarif ve nizamlı görünüyor."
    show yuri 1f zorder 2 at t11
    y "Tamamdır, su sürahisini alabilir miyim?"
    y 1a "Teşekkürler. Hemen döneceğim."
    mc "Ben de seninle gelebilirim..."
    y 1q "G-Gelmene gerek yok!"
    y "Sen burada kal..."
    y "Çok uzun sürmez."
    show yuri zorder 1 at thide
    hide yuri
    "Elindeki sürahi ile birlikte Yuri sınıftan hızlıca çıkıyor."
    show monika 2i zorder 2 at t11
    m "A..."
    m "Yuri yine seni bırakıp gitti mi?"
    mc "Hayır, bu sefer öyle değil."
    mc "O sadece su sürahisini doldurmaya gitti çay yapmak için."
    m 5 "Ha, tamamdır!"
    m "Yanlış anladığım için özür dilerim~"

    scene bg club_day
    with wipeleft_scene

    "..."
    "On dakika geçiyor."
    "Yuri pek uzun sürmez demişti..."
    "Onu alıkoyan bir şey mi var?"
    "Beklemekten sıkıldım o yüzden Yuri’ye bakmaya karar veriyorum."
    scene bg corridor
    with wipeleft_scene
    $ currentpos = get_pos()
    play music "<from " + str(currentpos) + " loop 10.893>bgm/6o.ogg"
    mc "Bakalım..."
    "Yuri’nin olmasının en mantıklı olduğu yer en yakındaki çeşme olmalı..."
    $ y_name = "Yuri"
    "Koridorda yürümeye başlıyorum."
    $ y_name = "???"
    y "Haah..... haah...."
    y ".... Haah..... haah...."
    "... Bu ses de ne?"
    "Şu köşeden geliyor gibi..."
    "Nefes alıp verme sesine benziyor."
    y "Fıffff--"
    "Sanki birisi dişlerinin arasından havayı çekiyormuş gibi derin bir nefes alma sesi."
    "Canı mı yanıyor acaba?.."
    "Köşeye varıyorum ve oradan bakıyorum."
    mc "Yuri?.."
    $ y_name = "Yuri"
    show yuri cuts zorder 2 at t11
    y "Ah--!"

    $ currentpos = 45.264 - (get_pos() / 2.0)
    $ audio.t6r = "<from " + str(currentpos) + " to 39.817 loop 0>bgm/6r.ogg"
    play music t6r
    show yuri zorder 1 at thide
    hide yuri
    show noise zorder 100 at noise_alpha
    show vignette zorder 100 at vignetteflicker(-2.030)
    show layer master at rewind
    $ y_name = "???"
    mc "{cps=*3}Yuri?..{/cps}{nw}"
    "{cps=*3}Köşeye varıyorum ve oradan bakıyorum.{/cps}{nw}"
    "{cps=*3}Canı mı yanıyor acaba?..{/cps}{nw}"
    "{cps=*3}Sanki birisi dişlerinin arasından havayı çekiyormuş gibi derin bir nefes alma sesi.{/cps}{nw}"
    y "{cps=*3}Fıffff--{/cps}{nw}"
    "{cps=*3}Nefes alıp verme sesine benziyor.{/cps}{nw}"
    "{cps=*3}Şu köşeden geliyor gibi...{/cps}{nw}"
    "{cps=*3}... Bu ses de ne?{/cps}{nw}"
    y "{cps=*3}.... Haah..... haah....{/cps}{nw}"
    y "{cps=*3}Haah..... haah....{/cps}{nw}"
    $ y_name = "Yuri"
    "{cps=*3}Koridorda yürümeye başlıyorum.{/cps}{nw}"
    "{cps=*3}Yuri’nin olmasının en mantıklı olduğu yer en yakındaki çeşme olmalı...{/cps}{nw}"
    mc "{cps=*3}Bakalım...{/cps}{nw}"
    window hide(None)
    window auto
    scene bg club_day
    show noise zorder 100 at noise_alpha
    show vignette zorder 100 at vignetteflicker(-2.030)
    show layer master at rewind
    "{cps=*3}Beklemekten sıkıldım o yüzden Yuri’ye bakmaya karar veriyorum.{/cps}{nw}"
    "{cps=*3}Onu alıkoyan bir şey mi var?{/cps}{nw}"
    "{cps=*3}Yuri pek uzun sürmez demişti...{/cps}{nw}"
    "{cps=*3}On dakika geçiyor.{/cps}{nw}"
    "{cps=*3}...{/cps}{nw}"

    $ del _history_list[-37:]
    if poemwinner[0] == "yuri" and chapter == 3:
        jump yuri_exclusive2_2_ch23
    $ currentpos = 90.528 - (get_pos() * 2.0)
    $ audio.t6r = "<from " + str(currentpos) + " loop 10.893>bgm/6.ogg"
    play music t6r
    hide noise
    hide vignette
    show layer master
    show yuri 1a zorder 2 at t11
    y "Geldim."
    y "Sabırla beklediğin için teşekkürler."
    y "[player], oolong çayı sever misin?"
    mc " A, evet."
    mc "Benim için pek fark etmez."
    y "Pekâlâ."
    "Yuri su ısıtıcısının sıcaklığını 90 dereceye ayarlıyor."
    y 1f "Şimdi çaydanlığı alma vakti."
    mc "Bunu gerçekten özenerek yapıyorsun, öyle değil mi?"
    y 1u "Elbette..."
    y "Başkalarına çay hazırlarken bundan daha azını yapamam."
    mc "Ben çay konusunda uzman falan olmasam bile mi?.."
    y 2m "Haha."
    y 2a "O durumda daha bile fazla etkilenmiş olacaksın."
    mc "A... belki de öyle olacak!"
    show yuri zorder 1 at thide
    hide yuri
    "Yuri çaydanlığı getiriyor ve çay yapraklarını ölçmeye başlıyor."
    "Şaşırtıcı bir şekilde kendi kendine biraz mırıldanmaya bile başlıyor."
    show yuri 1c zorder 2 at t11
    mc "Keyfin yerinde sanırım..."
    y 1a "Öyle mi?"
    y "Duygularımı bilerek gösteriyordum..."
    y "Ve sen de fark ettin."
    y 2u "Biraz kendi kendime düşünüyordum da..."
    y "Bundan sonra kendimi biraz daha fazla ifade etmeye çalışmaya karar verdim."
    y "Öyle görünüyor ki bu benim için çok da zor değilmiş..."
    y 1c "En azından senin yanındayken."
    show yuri 1a
    mc "A..."
    mc "Yuri, bu harika!"
    mc "Kendini çok zorlama yeter."
    y 3u "[player], sen hep benim için endişeleniyorsun..."
    y "Gerçekten çok tatlısın."
    mc "Şey..."
    "Yuri şaka yapmıyordu..."
    "Bu konuşmaya ayak uydurabilir miyim bilmiyorum bile!.."
    "Yuri’nin ikimize de birer bardak çay dolduruşunu izliyorum."
    y 1a "[player], senden bir başka isteğim daha var."
    y "Bugün yerde otursak sorun olur mu?"
    mc "Ha? Neden ki?"
    y 1h "Belim için daha rahat oluyor da..."
    y "Böylece sıraya doğru eğilmektense belimi duvara yaslayarak okuyabilirim."
    mc "A, pardon. Fark etmemişim."
    y 1a "Sorun değil."
    y "Sık sık bel ağrısı çekiyorum o yüzden elimden geldiğince bu durumumu idare etmeye çalışırım."
    mc "Öyle mi?"
    mc "Acaba neden?.."
    y 1f "Muhtemelen benim--"
    y 1n "A--"
    y 1o "B-Benim..."
    mc "Senin duruş şeklinden ötürü, değil mi?"
    mc "Ben de her zaman okurken eğilerek otururum..."
    y 2p "Evet!"
    y 2q "Okurken çok kötü oturuyorum!"
    y "O yüzden yerde otursak iyi olur."
    mc "Pekâlâ."
    mc "Ben gidip kitabı getireyim."
    show yuri zorder 1 at thide
    hide yuri
    "Kitabı çantamdan çıkarıyorum."
    mc "A, biraz çikolata da varmış yanımda..."
    "Bir paket küçük çikolata."
    "Çikolatayı da yanıma alıyorum, çayla iyi gider diye."
    "Yuri’yle birlikte çay bardakları yanımızda, duvara doğru yaslanarak oturuyoruz."
    "Sanki önceden planlamışız gibi ikimiz de kitabın bir tarafını tutacak şekilde daha önce oturduğumuz gibi oturuyoruz."
    "Ama bu sefer..."
    "Bedenlerimiz birbirine daha da yakın."
    show yuri 2h zorder 2 at t11
    y "Böyle çok iyi göremiyorum da..."
    mc "--!"
    show yuri 2e at d11
    "Yuri omuzlarımız birbirine dokununcaya kadar yanıma doğru kayıyor."
    "Böyle otururken nasıl okumaya odaklanacağım?!.."
    "Yuri hep biraz şirindi zaten ama..."
    "Daha az tedirgin davrandığı zaman şirinliği yüzünden yüreğime inecek!"
    y 2f "Çayın..."
    "Yuri çay bardağımı bana uzatıyor."
    "Çay bardağını kitabı tutmadığım elimle tutunca kendimi odaklanmanın daha da zor olduğu bir durumda buluyorum."
    "Çünkü şimdi bir de yanlışlıkla Yuri’nin göğüslerine dokunmamaya dikkat etmem gerekiyor!.."
    "Ben tüm bunları düşünürken Yuri dünyadan bihaber."
    "Yuri ciddi bir yüz ifadesiyle kitabına bakıyor, onun için etrafındaki her şeyin soluklaştığını tahmin ediyorum."
    "Tüm irademi kitaba odaklanmak için kullanıyorum."
    "..."
    "Birkaç dakika sonrasında sonunda rahatlamayı becerebiliyorum."
    "Çay bardağını bacaklarımın arasına koyup çikolatanın kabını açmaya çalışıyorum."
    mc "A, özür dilerim..."
    "Çikolatanın kabını tamamen açmak için kitabı bir anlığına bırakıyorum."
    mc "İstediğin kadar alabilirsin."
    y 2s "A, şey..."
    y "Teşekkür ederim, hiç almayayım..."
    mc "Ha? Emin misin?"
    y 2v "Şey..."
    y "Eğer çikolataya dokunursam kitap çikolata lekesi olabilir..."
    mc "A, haklısın..."
    mc "Bunu düşünmedim bile."
    mc "Özür dilerim..."
    y 2a "Özür dilemene gerek yok."
    y "Kitabı ben tutarım, olur mu?"
    mc "Emin misin?.."
    y "Tabii."
    $ persistent.clear[3] = True
    scene y_cg2_bg
    show y_cg2_base
    show y_cg2_details
    show y_cg2_nochoc
    show y_cg2_dust1
    show y_cg2_dust2
    show y_cg2_dust3
    show y_cg2_dust4
    with dissolve_cg
    "Yuri kitabı iki eliyle birlikte açıyor."
    "Kitabı okumakta zorluk çekmeyeceğim bir şekilde tutuyor."
    "Ama bunun neticesinde sol kolu neredeyse bacağımın üstünde duruyor."
    mc "Şey, o durumda..."
    "Yuri tekrar okumaya odaklanmış durumda."
    "Bir çikolata parçasını alıp ağzıma atıyorum."
    "Sonra bir başka çikolata parçası alıyorum..."
    "Ve Yuri’ye uzatıyorum."
    "Kitaptan gözünü ayırmıyor bile."
    "Sadece dudaklarını aralıyor, bu oldukça doğal bir durummuş gibi."
    "Ama bu demek oluyor ki burada duramam!"
    hide y_cg2_nochoc
    "Tedirgince çikolatayı Yuri’nin ağzına yaklaştırıyorum."
    "Ve Yuri öylece dudaklarını çikolatanın üzerine kapıyor."
    y "Ha?.."
    show y_cg2_exp2
    "Yuri’nin yüz ifadesi bir anda değişiyor."
    y "Ben..."
    y "Ben daha demin..."
    "Yuri bana daha demin olanlar gerçekten olup olmadığını anlamaya çalışırcasına bakıyor."
    show y_cg2_exp3
    show y_cg2_nochoc:
        alpha 0
        linear 0.5 alpha 1
    hide y_cg2_exp2
    y "Ş-Şey..."
    y "[player]..."
    mc "Ö-Özür dilerim!"
    mc "Sanırım bunu yapmamalıydım..."
    stop music
    y "H-Ha..."
    "Yuri derin derin nefes alıp vermeye başlıyor."
    y "Ben..."
    y "Dayanamıyorum..."
    y "[player]..."
    "Yuri aniden kollarımı kavrayıp çekerek beni ayağa kaldırıyor."
    "Çay bardağım devriliyor."
    scene bg closet
    show yuri 2t zorder 2 at t11
    with wipeleft
    y "[player]..."
    play sound closet_close
    show dark zorder 100
    with wipeleft
    y "Kalbim..."
    y 2y6 "Kalbim küt küt atıyor, [player]..."
    y "Sakinleşemiyorum."
    y "Artık hiçbir şeye odaklanamıyorum!.."
    y "[player], kalbimin atışını hissedebiliyor musun?"
    "Yuri birden elimi göğsüne bastırıyor."
    play music hb
    show layer master at heartbeat
    y 3t "Bu bana neden oluyor?"
    y "Aklımı yitiriyormuşum gibi hissediyorum..."
    y 3y4 "Engel olamıyorum buna."
    y 3y6 "Okumayı bile istemez hâle geliyorum..."
    y "Ben sadece..."
    y 3s "... sana..."
    y "... bakmak istiyorum."
    hide yuri
    show yuri eyes
    pause 3.0
    y "... Haah..."
    pause 3.0
    y "... Haah..."
    pause 3.0
    y "... Haah..."
    pause 3.0
    play sound closet_open
    stop music
    show layer master
    hide yuripupils
    show yuri 1n at face
    with None
    show yuri 3n at t32 with None
    hide dark
    show monika 3l zorder 3 at f31
    with wipeleft
    m "Ş-Şey..."
    m "Şiirlerimizi... paylaşma vakti..."




    return

label yuri_exclusive2_2_ch23:
    $ config.skipping = False
    scene black
    with None
    $ audio.t6g = "<loop 10.893>bgm/6g.ogg"
    play music t6g
    pause 4.62
    scene bg corridor
    show yuri eyes_base
    pause 1.0
    show bg glitch:
        yoffset 480 ytile 2
        linear 0.25 yoffset 0
        repeat
    show yuri glitch at i11
    $ gtext = glitchtext(80)
    $ currentpos = get_pos()
    play music g1
    y "[gtext]{nw}"
    stop music
    scene bg corridor
    show yuri 2n at i11
    y "Şey..."
    y "Bekle..."
    y 2o "Ben nasıl..."
    y 2y6 "... Özür dilerim, gerçekten garip bir dejavu yaşadım da..."
    y "Bu daha evvel hiç olmamıştı... değil mi?"
    y 2t "Kafam son zamanlarda biraz pusluydu da..."
    y 3t "Umarım belli falan etmiyorumdur!"
    y "Birlikte zaman geçirmeye başladıktan hemen sonra benim garip biri olduğumu düşünmen beni gerçekten çok üzer..."
    y "Sonuçta..."
    show bg corridor:
        xoffset 0
        parallel:
            0.36
            xoffset 1
            repeat
        parallel:
            0.49
            xoffset 0
            repeat
    show black zorder 5:
        alpha 0.5
        parallel:
            0.36
            alpha 0.5
            repeat
        parallel:
            0.49
            alpha 0.475
            repeat

    play music t9
    y "Herkesin sıra dışı birkaç yönü vardır."
    y 1v "Ama bunları biriyle tanıştıktan hemen sonra belli etmek genelde yakışıksız... ya da itici olarak görülür."
    y "En azından tecrübelerim böyle söylüyor."
    y "Ben biraz daha küçükken, sanırım biraz fazla agresifleşip hırçınlaşıyordum..."
    y "Bu, insanların benim etrafımda olmak istememelerine yol açtı."
    y 2w "O yüzden... kendimin bu yönünden nefret etmeye başladım."
    y "Bazı hobilerime olan takıntım..."
    y "Ve bir şey hakkında çok heyecanlanınca kendimi kontrol edememem..."
    y "O yüzden..."
    y 1v "En sonunda insanlarla konuşmaya kalkışmayı bıraktım."
    y "Eğer kimse beni benim için en değerli olan şeyler için sevemeyecekse..."
    y 1u "... Öyleyse kendimi dış dünyaya kapamak çok daha kolay olur."
    y 1h "Ama son zamanlarda bir şeyler yanlış gitmeye başladı."
    y "Ne olduğunu bilmiyorum."
    y 2y6 "Ama kulüp odasına her geldiğimizde kalbim deliler gibi çarpmaya başladı."
    y "Sanki göğsümü parçalayacakmış gibi."
    y "Göstermemem gereken duygularla ve enerjiyle dolduruyordu beni."
    y "Garip şeyler yapmama sebep oluyordu."
    y 2t "Bu neden oluyor bilmiyorum!"
    stop music
    y 1t "[player]..."
    y "Bana mı öyle geliyor yoksa Monika son zamanlarda biraz garip mi davranıyordu?"
    y 1v "Monika kulübe katıldığımdan bu yana hep tatlı biriydi..."
    y "Ama son zamanlarda ne zaman onun yanında olsam kötü bir şeyler hissediyorum."
    y 2y4 "Ben deli değilim, değil mi?"
    y 2y1 "Lütfen bana deli olmadığımı söyle!"
    y "Daha önce bir şey söyleyemedim çünkü o hep bizi dinliyor!"
    y 2y3 "Ama sonunda baş başayız..."
    y "Bir süreliğine burada kalabilir miyiz?"
    y 1m "Evet..."
    y "..."
    play music hb
    show layer master at heartbeat
    show yuri as yuri_eyes zorder 4:
        "yuri/eyesfull.png"
        i11
        alpha 0.0
        block:
            2.012 * 4 - 1.49
            alpha 1.0
            0.52
            alpha 0.0
            1.49
            repeat
    pause 2.0
    $ ad = 40.0
    $ ac = 1.0
    show monika 1 onlayer front at malpha(ac / ad)
    y 1s "Ben sadece burada kalmak istiyorum."
    $ ac += 0
    show monika 1 onlayer front at malpha(ac / ad)
    y "Sadece ikimiz."
    $ ac += 0
    show monika 1 onlayer front at malpha(ac / ad)
    y "Kulüp aktivitesi bitene kadar burada kalabiliriz."
    $ ac += 0
    show monika 1 onlayer front at malpha(ac / ad)
    y 1m "Ondan sonra sınıf bize kalmış olur."
    $ ac += 0.5
    show monika 1 onlayer front at malpha(ac / ad)
    y "Kimse bizim okuma zamanımızı bölemez."
    $ ac += 0.5
    show monika 1 onlayer front at malpha(ac / ad)
    y 1y4 "Görünce kendi boğazımı bıçaklamak istememe sebep olacak hiç kimse olmaz."
    $ ac += 0.5
    show monika 1 onlayer front at malpha(ac / ad)
    y 1q "Ahaha..."
    $ ac += 0.5
    show monika 1 onlayer front at malpha(ac / ad)
    y "Şaka yapıyordum!"
    $ ac += 0.5
    show monika 1 onlayer front at malpha(ac / ad)
    y "Sadece bir şakaydı."
    $ ac += 0.5
    show monika 1 onlayer front at malpha(ac / ad)
    y 1i "Ama bıçakları seviyorum..."
    $ ac += 0.5
    show monika 1 onlayer front at malpha(ac / ad)
    y "Kulağa garip gelebilir ama ne kadar güzel olabileceklerini görmemişsen anlaman mümkün değil."
    $ ac += 0.5
    show monika 1 onlayer front at malpha(ac / ad)
    y 1f "Bir fikrim var."
    $ ac += 1
    show monika 1 onlayer front at malpha(ac / ad)
    y "Neden bir ara benim evime gelmiyorsun?"
    $ ac += 1
    show monika 1 onlayer front at malpha(ac / ad)
    y 1y6 "Sana koleksiyonumu gösterebilirim."
    $ ac += 1
    show monika 1 onlayer front at malpha(ac / ad)
    y "Pek çok farklı zanaatkârdan aldım hepsini."
    $ ac += 1
    show monika 1 onlayer front at malpha(ac / ad)
    y 1a "Hepsini kullanmaya özen gösteriyorum."
    $ ac += 1
    show monika 1 onlayer front at malpha(ac / ad)
    y 1m "Yalnız hissetmelerini falan istemiyorum..."
    $ ac += 1
    show monika 1 onlayer front at malpha(ac / ad)
    y 1y6 "Kimse yalnız olmayı hak etmez."
    $ ac += 1
    show monika 1 onlayer front at malpha(ac / ad)
    y 1y4 "Hiç kimse."
    $ ac += 1
    show monika 1 onlayer front at malpha(ac / ad)
    y 1c "Bu yüzden Edebiyat Kulübü’ne katıldığın için çok mutluyum, [player]."
    $ ac += 1
    show monika 1 onlayer front at malpha(ac / ad)
    y 1a "Artık yalnız olmak zorunda değiliz."
    $ ac += 1
    show monika 1 onlayer front at malpha(ac / ad)
    y "Çünkü birbirimize sahibiz."
    $ ac += 1
    show monika 1 onlayer front at malpha(ac / ad)
    y "Her gün."
    $ ac += 1
    show monika 1 onlayer front at malpha(ac / ad)
    y "Tek ihtiyacımız da bu."
    $ ac += 1
    show monika 1 onlayer front at malpha(ac / ad)
    y 1y6 "Hatta ne diyeceğim."
    $ ac += 1
    show monika 1 onlayer front at malpha(ac / ad)
    y "Hadi gel Edebiyat Kulübü’nü bırakalım."
    $ ac += 1
    show monika 1 onlayer front at malpha(ac / ad)
    y "O tatlı dilli yılan Monika’nın etrafında olmamız için bir sebep yok."
    $ ac += 1
    show monika 1 onlayer front at malpha(ac / ad)
    y 1y4 "Öteki acınası çocuktan bahsetmeye gerek bile yok."
    $ ac += 1
    show monika 1 onlayer front at malpha(ac / ad)
    y 1s "Her gün okuldan sonra evimize birlikte gidebiliriz."
    $ ac += 1
    show monika 1 onlayer front at malpha(ac / ad)
    y "Ve birlikte okuyabiliriz."
    $ ac += 1
    show monika 1 onlayer front at malpha(ac / ad)
    y 1m "Birlikte yiyebiliriz."
    $ ac += 1
    show monika 1 onlayer front at malpha(ac / ad)
    y "Birlikte uyuyabiliriz."
    $ ac += 1
    show monika 1 onlayer front at malpha(ac / ad)
    y 1s "Kulağa güzel gelmiyor mu?"
    $ ac += 2
    show monika 1 onlayer front at malpha(ac / ad)
    y "İsteyebileceğimiz her şeye kavuşmuş oluruz."
    $ ac += 2
    show monika 1 onlayer front at malpha(ac / ad)
    y 1a "Kulübe katılmanın sebebi de bu değil miydi zaten?"
    $ ac += 2
    show monika 1 onlayer front at malpha(ac / ad)
    y "Sanki bu kaderimizde vardı."
    $ ac += 2
    show monika 1 onlayer front at malpha(ac / ad)
    y "Birbirimizle buluşmamızı gerektiren bir kader."
    $ ac += 2
    show monika 1 onlayer front at malpha(ac / ad)
    y "Ve böylece benim yıllarca sabırla beklediğim mutlu sonumuza sahip olacağız."
    $ ac += 2
    show monika 1 onlayer front at malpha(ac / ad)
    y "Benimle birlikte olur musun, [player]?"
    $ ac += 2
    show monika 1 onlayer front at malpha(ac / ad)
    $ gtext = glitchtext(200)
    y "Benimle{space=60}[gtext]{nw}"
    hide monika onlayer front
    window hide(None)
    $ poemsread = 0
    $ y_gave = False
    play music t5
    scene bg club_day
    window show(None)
    window auto

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
