label ch20_from_ch10:
    scene bg residential_day
    with dissolve_scene_half
    play music t2
    jump ch20_main2

label ch20_main:
    stop music fadeout 2.0
    scene bg residential_day
    with dissolve_scene_full
    play music t2

label ch20_main2:
    "Her zamanki gibi sıradan bir okul günü."
    "Sabahları genelde berbat oluyor; etrafım okula birlikte giden arkadaş grupları ve çiftlerle sarılı oluyor."
    "Ben okula hep yalnız gittim."
    "Kendime hep birkaç kızla falan tanışmanın zamanının geldiğini söylüyorum..."
    "Ama herhangi bir kulübe katılmam için beni motive eden bir şey yok."
    "Boş zamanımı oyun ve animelerle geçirip kıt kanaat geçinmek bana epey yetiyor."
    "Anime kulübü var elbette ama içinde kız falan yoktur zaten..."

    scene bg class_day
    with wipeleft_scene

    "Bugün de okuldaki vaktim her zamanki gibi geçti ve farkında olmadan gün bitti."
    "Eşyalarımı topladıktan sonra boş boş duvara bakıyor, ufacık da olsa motivasyon kaynağı olabilecek bir şey arıyorum."
    mc "Kulüpler..."
    "İlgimi çeken hiçbir kulüp yok."
    "Hem, hepsi de zaten uğraşamayacağım kadar zahmetlidir."
    "Sanırım anime kulübüyle başlamaktan başka çarem yok..."

    $ m_name = "???"

    m "... [player]?"
    window hide(None)
    show monika g2 zorder 2 at t11
    pause 0.75
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.25
    stop sound
    hide screen tear
    window show(None)
    show monika 1 zorder 2 at t11
    mc "... Monika?"
    $ m_name = "Monika"
    m 1b "Ay, seni burada görmeyi hiç beklemiyordum!"
    m 5 "Uzun zaman oldu, değil mi?"
    mc "Şey..."
    mc "Evet, öyle."
    "Monika tatlı bir şekilde gülümsüyor."
    "Birbirimizi tanıyoruz - şey, pek az konuştuk ama geçen sene aynı sınıftaydık."
    "Monika muhtemelen sınıftaki en popüler kızdı. Akıllı, güzel, atletik..."
    "Kısacası, beni tamamen aşan biri."
    "Şimdi onun bu kadar samimi bir şekilde gülümsemesini görünce biraz..."
    mc "Buraya neden gelmiştin?"
    m 1a "Ha, kulübümde kullanmak için birkaç araç gereç arıyordum da."
    m 1d "Burada hiç elişi kâğıdı var mı, biliyor musun?"
    m "Veya keçeli kalem?"
    mc "Dolaba bir bak istersen."
    mc "... Sen münazara kulübündeydin, değil mi?"
    m 5 "Ahaha, şey..."
    m "Aslında münazara kulübünü bıraktım."
    mc "Gerçekten mi? Bıraktın mı?"
    m "Evet..."
    m 2e "Açıkçası, büyük kulüpler arasındaki politik çatışmalara hiç katlanamıyorum."
    m "Yok bütçeymiş, yok tanıtımmış, yok etkinlik hazırlıklarıymış, tek konuştukları şey bunlar..."
    m "Onun yerine kendi sevdiğim bir şeyi alıp ortaya değerli bir şey koymayı tercih ederim."
    mc "Öyleyse, hangi kulübe katılmaya karar verdin?"
    m 1b "Aslında yeni bir kulüp başlatacağım!"
    m "Bir edebiyat kulübü!{nw}"
    show screen tear(20, 0.1, 0.1, 0, 40)
    window hide(None)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.25
    stop sound
    hide screen tear
    window show(None)
    m "Bir edebiyat kulübü!{fast}"
    window auto
    mc "Edebiyat mı?.."
    "Bu sanki biraz... yavan?"
    mc "Şu an kaç üye var?"
    m 5 "Hm..."
    m "Ahaha..."
    m "Bunu söylemek biraz utanç verici ama şu an üç kişiyiz."
    m "Kulağa sıkıcı gelen bir şey için yeni üye bulmak gerçekten zor..."
    mc "Anlıyorum..."
    m 3d "Ama aslında hiç de öyle sıkıcı bir şey değil ya!"
    m "Edebiyat herhangi bir şey olabilir. Okuma, yazma, şiir..."
    m 3e "Hatta var ya, üyelerimden biri manga koleksiyonunu kulüp odasında saklıyor..."
    mc "Dur biraz... Cidden mi?"
    m 2k "Evet. Komik, değil mi?"
    m 2e "Manganın edebiyat olduğu konusunda da ısrarcı."
    m "Şey, kız yanılmıyor sanırım..."
    m "Hem, üye üyedir, değil mi?"
    "... Monika “kız” mı dedi?"
    "Hmm..."
    m 1a "Hey, [player]..."
    m "Bu arada... Hâlâ katılacak yeni bir kulüp arıyor musun?"
    mc "A--"
    mc "Şey, sanırım evet ama..."
    m "Öyleyse..."
    m 5 "Bana büyük bir iyilik yapman mümkün müdür acaba?"
    m "Katılmanı istemeyeceğim ama..."
    m "En azından kulübümü ziyaret edersen çok mutlu olurum."
    m "Lütfen?"
    mc "Şey..."
    "Şey, sanırım reddetmem için hiçbir gerekçe yok..."
    "Ayrıca, Monika gibi birini nasıl reddedebilirim ki?"
    mc "Olur, bi’ bakabilirim sanırım."
    m 1k "Ay, harika!"
    m 1b "Çok tatlısın, [player]. Bunu biliyor muydun?"
    mc "Ö-Önemli bir şey değil, cidden..."
    m 1a "Gidelim mi o hâlde?"
    m "Araç gereçlere sonra bakarım, sen daha önemlisin."

    stop music fadeout 2.0

    scene bg corridor
    with wipeleft_scene

    "Böylece, bugün ruhumu Monika ve karşı konulmaz gülümsemesine satmış oldum."
    "Çekingen bir şekilde Monika’nın peşinden nadiren uğradığım, genelde üçüncü sınıfların bulunduğu ve etkinlikler için kullanılan üst kata çıkıyorum."
    "Enerji dolu olan Monika sınıf kapısını sert bir şekilde açıyor."

    scene bg club_day2
    with wipeleft
    play music t3

    if renpy.random.randint(0, 2) == 0:
        show monika g1 at l31
    else:
        show monika 3b at l31
    m "Ben geldim~!"
    m "Yanımda bir de bir konuk getirdim!"
    show yuri 2t zorder 2 at t33
    if not config.skipping:
        show screen invert(0.15, 0.3)
    y "Ha?"
    y "Bir... Bir konuk mu?"
    show natsuki 4c zorder 2 at t32
    n "Cidden mi? Bir oğlan mı getirdin?"
    n "Kulübün havası kaçtı."
    show monika 3m zorder 3 at f31
    m "Kaba davranma, Natsuki..."
    m 3b "... Her neyse, kulübe hoş geldin, [player]!"
    show monika 3a zorder 2 at t31
    mc "..."
    "Bu durum karşısında diyecek kelime bulamıyorum."
    "Bu kulüp..."
    "{i}... inanılmaz derecede tatlı kızlarla dolu!!{/i}"

    show natsuki zorder 3 at f32
    n 5c "Bi’ düşüneyim..."
    n "Sen Monika’nın erkek arkadaşısın, değil mi?"
    show natsuki zorder 2 at t32
    mc "Ne--"
    mc "Hayır, değilim!"
    show yuri zorder 3 at f33
    y 2l "Natsuki..."
    $ n_name = 'Natsuki'
    "Anladığım kadarıyla adı Natsuki olan, ters tavır sergileyen bu kızı tanımıyorum."
    "Küçük kalıbına bakınca birinci sınıfmış gibi geliyor."

    show yuri zorder 2 at t33
    show monika zorder 3 at f31
    m 2l "H-Her neyse, bu Natsuki, her zamanki gibi enerjik..."
    m 2b "Bu da Yuri, Başkan Yardımcısı!"
    $ y_name = 'Yuri'
    show monika 2a zorder 2 at t31
    show yuri zorder 3 at f33
    y 4 "T-Tanıştığımıza memnun oldum..."
    "Daha olgun ve çekingen görünen Yuri görünüşe bakılırsa Natsuki gibi biriyle uğraşmakta zorluk çekiyor."
    show yuri zorder 2 at t33
    mc "A... Şey, ikinizle de tanıştığıma sevindim."
    show monika zorder 3 at f31
    m 1a "[player] ile bir sınıfta karşılaştım ve o da kulübe bir göz atmaya karar verdi."
    m "Ne harika, değil mi?"
    show monika zorder 2 at t31
    show natsuki zorder 3 at f32
    n 4e "Dur biraz! Monika!"
    n "Sana yeni birini getirmeden önce bana haber vermeni söylememiş miydim?"
    n 4q "Ben de şey yapacaktım... E, bilirsin..."
    show natsuki zorder 2 at t32
    show monika zorder 3 at f31
    m 1e "Üzgünüm, üzgünüm!"
    m "Bunu unutmadım, ama ona rast geldim."
    show monika zorder 2 at t31
    show yuri zorder 3 at f33
    y 1a "Öyleyse, en azından çay yapmalıyım, değil mi?"
    show yuri zorder 2 at t33
    show monika zorder 3 at f31
    m 1b "Evet, bu harika olur!"
    m "Neden gelip oturmuyorsun, [player]?"
    hide monika
    hide natsuki
    hide yuri
    with wipeleft
    "Kızlar birkaç sırayı birleştirerek bir masa oluşturmuşlar."
    "Yuri odanın bir köşesine gidiyor ve dolabı açıyor."
    "O sırada, Monika ve Natsuki karşı karşıya oturuyorlar."
    "Kendimi hâlâ tuhaf hissettiğimden Monika’nın yanındaki sandalyeye oturuyorum."
    show monika 1a zorder 2 at t11
    m "Şimdi, normalde buraya gelmeyi planlamadığını biliyorum..."
    m "Ama burada kendini evinde hissetmeni sağlayacağız, tamam mı?"
    m 1j "Edebiyat Kulübü’nün başkanı olarak kulübü herkes için eğlenceli ve heyecan verici kılmak benim görevim!"
    mc "Bu kulüpte daha fazla insan olmaması şaşırtıcı."
    mc "Yeni bir kulüp kurmak zor olmalı."
    m 3b "Öyle denilebilir."
    m "Çoğu insan yepyeni bir şey oluşturmak için emek sarf etmeye pek hevesli olmuyor..."
    m "Özellikle de edebiyat gibi dikkat çekici olmayan bir şey söz konusu olduğunda."
    m "İnsanlara hem eğlenceli hem de zaman harcamaya değer olduğunu kanıtlamak için çok çalışmalısın."
    m "Ama bu, festival ve benzeri okul etkinliklerini daha da önemli kılıyor."
    m 2k "Mezun olmadan önce bu kulübü büyüteceğimize güvenim tam!"
    m "Değil mi, Natsuki?"
    show monika zorder 2 at t22
    show natsuki 4q zorder 2 at t21
    n "Şey..."
    n "... Sanırım."
    "Natsuki isteksizce onaylıyor."
    "Birbirlerinden epey farklı ama hedefleri aynı olan kızlar..."
    "Monika bu iki kızı bulmak için çok uğraşmış olmalı."
    "Yuri, elinde bir çay setiyle masaya geri dönüyor."
    "Çaydanlığı kapkek tepsisinin yanına koymadan önce her birimizin önüne özenle birer fincan koyuyor."
    show natsuki zorder 1 at thide
    show monika zorder 1 at thide
    hide natsuki
    hide monika
    show yuri 1a zorder 2 at t21
    mc "Sınıfta çay setiniz mi var?"
    y "Merak etme, öğretmenler buna müsaade etti."
    y "Ne de olsa, sıcak bir fincan çay kitap okurken iyi gelir, değil mi?"
    mc "Şey... S-Sanırım..."
    show monika 4a zorder 3 at f22
    m "Ehehe, kendini kaptırma hemen. Yuri sadece seni etkilemeye çalışıyor."
    show monika zorder 2 at t22
    show yuri at hf21
    y 3n "Ha?! B-Ben öyle..."
    "Alınan Yuri bakışlarını kaçırıyor."
    y 4b "İçimden geldiğinden, cidden..."
    show yuri zorder 2 at t21
    mc "Sana inanıyorum."
    mc "Şey, kitabın yanında çay içmek pek benlik gibi durmuyor ama çayı severim en azından."
    show yuri zorder 3 at f21
    y 2u "Sevindim..."
    show yuri zorder 2 at t21
    "Yuri içi rahatladığından hafifçe gülümsüyor."
    show monika zorder 1 at thide
    hide monika
    show yuri 1a zorder 2 at t32
    y "E [player], ne gibi şeyler okumayı seversin?"
    mc "A... Şey..."
    "Son yıllarda ne kadar az şey okuduğumu hesaba katarsak, bu soruya verebileceğim çok iyi bir yanıt yok."
    mc "... Manga..."
    "Diyorum kısık bir sesle, şakayla karışık."
    show natsuki 1c zorder 2 at t41
    "Natsuki birden başını kaldırıyor."
    "Sanki bir şey söylemek istiyormuş gibi bakıyor ama sessizliğini koruyor."
    show natsuki zorder 1 at thide
    hide natsuki
    y 3u "P-Pek kitap okuyan birisi değilsin galiba..."
    mc "... Yani, öyle ama bu değişebilir..."
    "Ne diyorum ben?"
    "Yuri’nin üzgün gülümsemesini gördükten sonra düşünmeden konuştum."
    mc "Her neyse, ya sen, Yuri?"
    y 1l "Düşüneyim..."
    "Yuri parmaklarını fincanın ağzında gezdiriyor."
    y 1a "Ben en çok derin ve karmaşık fantastik dünyalar yaratan romanları seviyorum."
    y "Onların ardında yatan yaratıcılığın ve hünerin seviyesi bana gerçekten büyüleyici geliyor."
    y 1f "Ve böylesine yabancı bir dünyada geçen güzel bir hikâyeyi aktarabilmek de eşit derecede inanılmaz geliyor."
    "Yuri tutkulu bir şekilde kitaplarla ilgili düşüncelerinden bahsetmeye devam ediyor."
    "Yuri, içeri ilk girdiğimde epey çekingen davranıyordu ama kitaplardan bahsederken gözlerinin parıldayışından anlıyorum ki o, kitapların dünyasında rahat hissediyor kendini, insanların dünyasında değil."
    y 2m "Ama doğrusunu istersen birçok şeyden hoşlanırım."
    y "Derin psikolojik unsurlar içeren hikâyeler de sarar genellikle beni."
    y 2a "Bir yazarın okuyucunun hayal gücü eksikliğinden yararlanıp onu şaşkına çevirmesi inanılmaz değil mi?"
    y "Neyse, son zamanlarda bir sürü korku türünde kitap okuduğumdan..."
    mc "A, ben de bir keresinde bir korku romanı okumuştum..."
    "Umutsuzca az da olsa bağlantı kurabileceğim bir konuya tutunmaya çalışıyorum."
    "Böyle devam ederse Yuri bir duvarla sohbet ediyormuş gibi olacak."
    show monika 1j zorder 3 at f33
    m "Ahaha. Tam da senden bekleyeceğim bir şey, Yuri."
    m 1a "Kişiliğine uyuyor."
    show monika zorder 2 at t33
    show yuri zorder 3 at f32
    y 1a "A, öyle mi?"
    y "Cidden, bir kitap beni düşündürebiliyorsa veya başka bir dünyaya götürebiliyorsa, o kitabı gerçekten elimden bırakamam."
    y "Sürreal korku türü kısa bir süreliğine bile olsa dünyaya bakış açını değiştirmeyi başarır genelde."
    show yuri zorder 2 at t32
    show natsuki 5q zorder 3 at f31
    n "Ay, korku türünden nefret ederim..."
    show natsuki zorder 2 at t31
    show yuri zorder 3 at f32
    y 1f "Öyle mi? Neden ki?"
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f31
    n 5c "Şey, ben..."
    "Natsuki bir anlığına bakışlarını bana çeviriyor."
    n 5q "Boş ver."
    show natsuki zorder 2 at t31
    show monika zorder 3 at f33
    m 1a "Doğru, genelde şirin şeyler hakkında yazmayı seversin, değil mi Natsuki?"
    show monika zorder 2 at t33
    show natsuki 1o zorder 3 at f31
    n "N-Ne?"
    n "Sana bunu düşündüren ne?"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f33
    m 3b "Son kulüp buluşmamızda müsvedde bir kâğıt bırakmıştın."
    m "Bir şiir üzerinde çalışıyordun galiba. Hatta, yanılmıyorsam şiirin adı--"
    show monika zorder 2 at t33
    show natsuki 1p zorder 3 at f31
    n "Sakın söyleme!!"
    n "Ve şiirimi geri ver!"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f33
    m 1j "Peki, peki~"
    show monika 1a zorder 2 at t33
    mc "Kendi şiirlerini mi yazıyorsun Natsuki?"
    show natsuki zorder 3 at f31
    n 1c "Ha? Şey, bazen."
    n "Neden sordun ki şimdi?"
    show natsuki zorder 2 at t31
    mc "Bence bu epey etkileyici de ondan."
    mc "Ara sıra onları paylaşmaya ne dersin?"
    show natsuki zorder 3 at f31
    n 5q "H-Hayır!"
    "Natsuki gözlerini kaçırıyor."
    n "Onları... beğenmezsin..."
    show natsuki zorder 2 at t31
    mc "A... Henüz kendine güvenen bir yazar değilsin galiba?"
    show yuri zorder 3 at f32
    y 2f "Natsuki’nin nasıl hissettiğini anlıyorum."
    y "Bu seviyedeki yazıları paylaşmak özgüvenden fazlasını gerektirir."
    y 2k "Yazmanın en hakiki şekli kendine yazmaktır."
    y "Okuyucularına açılmaya; zaaflarını, hatta kalbinin derinliklerini bile göstermeye istekli olmalısın."
    show yuri zorder 2 at t32
    show monika 2a zorder 3 at f33
    m "Yazma konusunda sen de deneyimli misin Yuri?"
    m "Bazı çalışmalarını paylaşırsan Natsuki’ye örnek teşkil edebilir ve Natsuki’nin kendi yazılarını paylaşabilmesi için rahat hissetmesine de yardımcı olabilirsin."
    show yuri at s32
    y 3o "..."
    mc "Sanırım durum Yuri için de aynı..."
    "Hepimiz bir anlığına sessizce oturuyoruz."
    show monika zorder 3 at f33
    m 5a "Hey, aklıma bir fikir geldi!"
    m "Buna ne dersiniz?"
    show monika zorder 2 at t33
    show natsuki 2k zorder 3 at f31
    show yuri 3e zorder 3 at f32
    ny "...?"
    "Natsuki’yle Yuri Monika’ya meraklı gözlerle bakıyorlar."
    show natsuki zorder 2 at t31
    show yuri zorder 2 at t32
    show monika zorder 3 at f33
    m 2b "Eve gidip kendi şiirimizi yazalım!"
    m "Ardından da bir sonraki görüşmemizde birbirimizle paylaşalım."
    m "Böylece herkes eşit olur!"
    show monika 2a zorder 2 at t33
    show natsuki zorder 3 at f31
    n 5q "Ş-Şey..."
    show natsuki zorder 2 at t31
    show yuri 3v zorder 3 at f32
    y "..."
    show yuri zorder 2 at t32
    show monika 2m zorder 3 at f33
    m "A..."
    m "Şey, bunun iyi bir fikir olduğunu düşünmüştüm..."
    show monika zorder 2 at t33
    show yuri zorder 3 at f32
    y 2l "Yani..."
    y "... Haklısın bence, Monika."
    y 2f "Muhtemelen hepimizin birlikte katılacağı aktiviteler bulmaya başlamalıyız."
    y 2h "Ben, Başkan Yardımcısı olmanın sorumluluğunu almayı kabul ettim ne de olsa..."
    y "O yüzden kulübü ve üyelerini yetiştirmek için elimden geleni yapmalıyım."
    y 2a "Ayrıca, artık yeni bir üyemiz var..."
    y "Atılacak iyi bir adım gibi görünüyor."
    y "Sen de katılıyor musun, [player]?"
    show yuri zorder 2 at t32
    mc "Bekleyin... Hâlâ bir problemimiz var."
    show monika zorder 3 at f33
    m 1d "Ha? Nedir?"
    "En önemli konuya geri döndüğümüze göre, başından beri aklımda olan şeyleri açıkça söylüyorum."
    show monika zorder 2 at t33
    mc "Bu kulübe katılacağımı hiç söylemedim ki!"
    mc "Monika beni uğramam için ikna etmiş olabilir, ama hiçbir karar vermedim."
    mc "Hâlâ bakacağım diğer kulüpler var. Ve... şey..."
    show monika 1g
    show natsuki 4g
    show yuri 2e
    "Söyleyeceklerimi unutuyorum."
    "Üç kız mahzun gözlerle bana bakıyor."
    show monika at s33
    m 1p "A-Ama..."
    show yuri at s32
    y 2v "Üzgünüm, ben de sandım ki..."
    show natsuki at s31
    n 5s "Hıh."
    mc "Ha?.."
    "Kızlar birbirine bakıyor ve ardından Monika bana dönüyor."
    show monika zorder 3 at f33
    m 1m "Sanırım... sana doğruyu söylemeliyim, [player]."
    m "Gerçek şu ki..."
    m 1p "... Resmî bir kulüp oluşturabilmek için yeterli üye sayısına sahip değiliz."
    m "Dört üyeye ihtiyacımız var..."
    m "Ve yeni üye bulmak için o kadar, o kadar çok uğraşıyorum ki."
    m "Eğer festivalden önce bir üye daha bulmazsak..."
    show monika zorder 2 at t33
    mc "..."
    "Ben... Bu kızlara karşı savunmasızım."
    "Böyle bir durumda nasıl doğru düzgün bir karar verebilirim ki?"
    "Onları yüzüstü bırakırsam kendimi kötü hissederim..."
    "Hem, burası oldukça rahat bir kulübe benziyor..."
    "Yani, eğer bu güzel kızlarla her gün vakit geçirebilmem için ödemem gereken bedel şiir yazmaksa..."
    mc "... Tamamdır."
    mc "Pekâlâ, kararımı verdim."
    mc "Edebiyat Kulübü’ne katılacağım."
    show monika 1e zorder 2 at t33
    show yuri 3f zorder 2 at t32
    show natsuki 1k zorder 2 at t31
    "Birer birer kızların gözleri ışıldıyor."
    show monika zorder 3 at f33
    m "Tanrım, gerçekten mi?"
    m "Gerçekten ciddi misin, [player]?"
    show monika zorder 2 at t33
    mc "Evet..."
    mc "Eğlenceli olabilir, değil mi?"
    show yuri zorder 3 at f32
    y 1m "Beni bir anlığına gerçekten korkuttun..."
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f31
    n 5q "O kadar olandan sonra çekip gitseydin sana acayip gıcık olurdum."
    show natsuki zorder 2 at t31
    show monika zorder 3 at f33
    m "[player], çok mutluyum.."
    m 1k "Artık resmî bir kulüp olabiliriz!"
    m 1e "Bunun için çok teşekkür ederim. Sen gerçekten inanılmazsın."
    m "İyi bir zaman geçirmen için her şeyi yapacağım, tamam mı?"
    show monika zorder 2 at t33
    mc "Şey... Teşekkürler, sanırım."
    show yuri zorder 1 at thide
    show natsuki zorder 1 at thide
    show monika zorder 2 at t11
    hide yuri
    hide natsuki
    m 3b "Pekâlâ, millet!"
    m "Sanırım böylelikle bugünün toplantısını güzel bir sonla bitirebiliriz."
    m "Bugünkü ödevinizi unutmayın:"
    m "Herkes bir şiir yazıp bir sonraki toplantıya getirecek ve birbirimizle şiirlerimizi paylaşacağız!"
    "Monika bir kez daha bana bakıyor."
    m 1a "[player], kendini nasıl ifade edeceğini görmeyi dört gözle bekliyorum."
    show monika 5 at hop
    m "Ehehe~"
    mc "T-Tamam..."
    show monika zorder 1 at thide
    hide monika
    "Olmayan yazma becerimle sınıfın yıldızı Monika’yı etkileyebilir miyim gerçekten?"
    "Endişeyle dolmaya başladım bile."
    "Yuri çay setini toplarken kızlar sohbet etmeye devam ediyorlar."
    mc "O hâlde ben yavaştan gideyim..."
    show monika 5a zorder 2 at t11
    m "Tamam!"
    m "Yarın görüşürüz."
    m "Sabırsızlanıyorum!"

    scene bg residential_day
    with wipeleft_scene

    "Böylece kulüp odasından çıkıp eve doğru yol alıyorum."
    "Yol boyunca aklım üç kız arasında gidip geliyor:"
    show natsuki 4a zorder 2 at t31
    "Natsuki,"
    show yuri 1a zorder 2 at t32
    "Yuri"
    show monika 1a zorder 2 at t33
    "ve elbette, Monika."
    "Okuldan sonra her günümü Edebiyat Kulübü’nde geçirerek gerçekten mutlu olacak mıyım?"
    "Belki kızlardan biriyle yakınlaşma fırsatım olur..."
    hide natsuki
    hide yuri
    hide monika
    with wipeleft
    "Pekâlâ!"
    "Durumumu en iyi şekilde değerlendirmeliyim sadece. Şansın benden yana olacağına eminim."
    "Ve sanırım her şey bu gece bir şiir yazarak başlayacak..."

    stop music fadeout 2.0
    scene black with dissolve_scene_full
    $ config.skipping = False
    $ config.allow_skipping = False
    $ allow_skipping = False

    call screen confirm("Özel bir şiir açtınız.\nOkumak ister misiniz?", Return(True), Return(False))
    if _return:
        call expression "poem_special_" + str(persistent.special_poems[0])
    else:
        pass

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
