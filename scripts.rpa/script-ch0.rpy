label ch0_main:
    stop music fadeout 2.0
    scene bg residential_day
    with dissolve_scene_full
    play music t2

    python:
        try: renpy.file("../characters/monika.chr")
        except: renpy.jump("ch0_kill")

    $ restore_all_characters()
    s "Heeeeeeeyyy!!"
    "Bana doğru koşan, üzerine çekebileceği dikkatten bihabermişçesine el sallayan baş belası bir kız görüyorum."
    "O kızın adı Sayori, kendisi komşum ve çocukluğumdan beri yakın arkadaşım."
    "Hani bugün olsa arkadaş olmak istemeyeceğiniz ama uzun zamandır birbirinizi tanıdığınızdan bir şekilde arkadaşlığınızı yürüttüğünüz tipler olur ya, o da öyle işte."
    "Eskiden okula birlikte giderdik, ama liseye başladığımız sıralarda Sayori sürekli uyuyakalmaya başladı, ben de onu beklemekten bıkmıştım."
    "Ama bu şekilde peşimden gelecekse kaçıp gitsem daha iyi sanki."
    "Yine de, sadece iç çekip kaldırımda öylece durup Sayori’nin bana yetişmesini bekliyorum."
    $ s_name = "Sayori"
    show sayori 4p zorder 2 at t11
    s 4p "Haaahhh... haaahhh..."
    s "Yine uyuyakaldım!"
    s "Ama bu sefer yetiştim sana!"
    mc "Yetiştin yetişmesine de ben durup seni beklemeye karar verdiğim için yetiştin."
    show sayori at s11
    s 5c "Haaaaaa, beni görmezden gelmeyi düşünüyormuşsun gibi konuştun!"
    s "Ayıp ama [player]!"
    mc "İnsanlar garip garip davrandığın için sana baktıklarında bizi sevgili sanmalarını falan istemiyorum."
    show sayori zorder 2 at t11
    s 1a "Tamam, tamam."
    s "Ama yine de beni bekledin."
    s "Bence istesen de kötü olamazsın~"
    mc "Tabii, öyledir Sayori..."
    s 1q "Ehehe~"
    show sayori zorder 1 at thide
    hide sayori
    "Birlikte karşıya geçip okula doğru yürüyoruz."
    "Okula yaklaştıkça yol diğer öğrencilerle dolmaya başlıyor."
    show sayori 3a zorder 2 at t11
    s "Aklıma geldi de, [player]..."
    s "Herhangi bir kulübe katılmaya karar verdin mi?"
    mc "Kulüp mü?"
    mc "Sana dedim ya, kulübe falan katılmaya pek hevesli değilim."
    mc "Kulüplere bakındığım falan da yok zaten."
    show sayori at s11
    s 4h "Ha? Yok artık!"
    s "Bana bu sene bir kulübe katılacağını söylemiştin!"
    mc "Öyle mi demiştim?.."
    "Dediklerine aldırmadan geçiştirdiğim sayısız konuşmaların birinde öyle demiş olabilirim."
    "Ben boş vaktimi oyunlara ve animelere ayırmaktan gayet memnunken Sayori benim hakkımda fazla endişeleniyor."
    s 4j "Hı hı!"
    s "Üniversiteye girmeden önce sosyalleşmeyi öğrenemeyeceğinden ya da bir kabiliyet filan edinemeyeceğinden korkuyorum diyorum."
    s "Senin mutlu olman benim için çok önemli, anlatabildim mi acaba?!"
    s "Şu an mutlu mesut geçindiğini biliyorum; ama gerçek dünyaya alışamadığın için birkaç yıl sonra eve kapanmış işe yaramazın teki olabileceğin düşüncesi beni yiyip bitiriyor!"
    s 4g "Bana güveniyorsun, öyle değil mi?"
    s "Bu kadar endişelendirme beni..."
    mc "Tamam, tamam..."
    mc "Gönlün olsun diye birkaç kulübe bakarım."
    mc "Söz vermiyorum ama bak."
    s 1h "En azından biraz uğraşacağına söz verir misin?"
    mc "Tamam, sanırım bunun sözünü verebilirim."
    show sayori zorder 2 at t11
    s 4r "Oley be~!"
    "Neden bu kadar gamsız bir kızın bana nutuk çekmesine fırsat veriyorum ki?"
    "Onu bir de dinliyorum ya, buna daha çok şaşırıyorum."
    "Sanırım onun benim için o kadar endişelendiğini görünce, kafasındaki her şeyi ne kadar büyütse de, biraz olsun sakinleşmemi sağlıyor."

    scene bg class_day
    with wipeleft_scene

    "Bugün de okuldaki vaktim her zamanki gibi geçti ve farkında olmadan gün bitti."
    "Eşyalarımı topladıktan sonra boş boş duvara bakıyor, ufacık da olsa motivasyon kaynağı olabilecek bir şey arıyorum."
    mc "Kulüpler..."
    "Sayori birkaç kulübe bakmamı istiyordu."
    "Sanırım anime kulübüyle başlamaktan başka çarem yok..."

    s "Selaaam!"
    show sayori 1b zorder 2 at t11
    mc "Sayori?.."
    "Sayori ben dalmışken sınıfa gelmiş olmalı."
    "Etrafıma bakınca sınıfta geriye bir tek benim kaldığımı fark ediyorum."
    s 1a "Sınıftan çıkarken seni yakalarım diye düşünmüştüm ama seni burada oturup dalmışken görünce içeri gireyim dedim."
    s "Açıkçası bazen benden de betersin... Etkilendim!"
    mc "Kendi kulübüne geç kalacaksan beni beklemene gerek yok."
    s 1y "Biraz motivasyona ihtiyacın olacağını düşündüm de. Bir de..."
    mc "Bir de ne?"
    s 1a "Şey, benim kulübüme de gelebilirsin!"
    mc "Sayori..."
    s 4r "Evet??"
    mc "... Senin kulübüne hayatta gelmem."
    show sayori at s11
    s 5d "Haaaaaaa?! Çok kötüsün!"
    "Sayori, Edebiyat Kulübü’nün başkan yardımcısı."
    "Sayori’nin edebiyata ilgisi olduğunu falan bilmiyordum gerçi."
    "Hatta, sırf yeni bir kulübün kurulmasına yardım etmenin eğlenceli olabileceğini düşündüğü için bu kulübe katıldığına %%99 eminim."
    "Kulübe kurucudan sonra ilk ilgi gösteren kişi olduğundan “Başkan Yardımcısı” unvanını aldı."
    "Kısacası, benim edebiyata olan ilgim Sayori’ninkinden kesin daha az."
    mc "Oldu o zaman. Ben anime kulübüne gidiyorum."
    show sayori zorder 2 at t11
    s 1g "Hadi ama ya, n’olur?"
    mc "Gelmeme neden bu kadar taktın ki?"
    s 5b "Şey..."
    s "Dün kulüptekilere yeni bir üye getireceğimi söylemiş olabilirim..."
    s "Natsuki de hatta bunun üzerine kapkek falan yaptı..."
    s "Ehehe..."
    mc "Tutamayacağın sözler verme!"
    "Sayori gerçekten bu kadar budala mı yoksa bütün bunlar onun kurnaz planının bir parçası mıydı, bir türlü anlayamıyorum."
    "Uzun uzun iç çekiyorum."
    mc "Tamam... Birkaç tane kapkek yiyip kalkarım, tamam mı?"
    show sayori at h11
    s 4r "Tamam! Hadi gidelim~!"

    stop music fadeout 2.0

    scene bg corridor
    with wipeleft_scene

    "Böylece, bugün ruhumu kapkek karşılığında satmış oldum."
    "Çekingen bir şekilde Sayori’nin peşinden nadiren uğradığım, genelde üçüncü sınıfların bulunduğu ve etkinlikler için kullanılan üst kata çıkıyorum."
    "Enerji dolu olan Sayori sınıf kapısını sert bir şekilde açıyor."

    scene bg club_day
    with wipeleft
    play music t3
    show sayori 4 at l41
    s "Millet! İşte yeni üyemiz~!"
    mc "Sana dedim ya bana ‘yeni üye’ deme--"
    show sayori at lhide
    hide sayori
    "Ha? Etrafa bakınıyorum."
    show yuri 1a zorder 2 at t11
    y "Edebiyat Kulübü’ne hoş geldin. Tanıştığıma memnun oldum."
    y "Sayori senden çok bahsetti."
    show yuri zorder 2 at t22
    show natsuki 4c zorder 2 at t21
    n "Cidden mi? Bir oğlan mı getirdin?"
    n "Kulübün havası kaçtı."
    show yuri zorder 2 at t33
    show natsuki zorder 2 at t32
    show monika 1k zorder 2 at t31
    m "Ah, [player]! Ne güzel bir sürpriz!"
    m "Kulübe hoş geldin!"
    show monika 1a
    mc "..."
    "Bu durum karşısında diyecek kelime bulamıyorum."
    "Bu kulüp..."
    "{i}... inanılmaz derecede tatlı kızlarla dolu!!{/i}"

    show monika zorder 1 at thide
    show yuri zorder 1 at thide
    show natsuki zorder 3 at f32
    hide monika
    hide yuri

    n 2c "Neye bakıyorsun sen?"
    n "Diyeceğin bir şey varsa de."
    mc "A-Affedersin..."
    show natsuki zorder 2 at t32
    show yuri 2l zorder 3 at f33
    y "Natsuki..."
    $ n_name = 'Natsuki'
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f32
    n 5s "Hıh."
    show natsuki zorder 2 at t32

    "Anladığım kadarıyla adı Natsuki olan, ters tavır sergileyen bu kızı tanımıyorum."
    "Küçük kalıbına bakınca birinci sınıfmış gibi geliyor."
    "Sayori’nin dediğine göre kapkekleri de yapan o."

    show sayori 2q zorder 3 at f31
    s "Huysuz olunca ona pek aldırma~"
    "Bunu kulağıma fısıldayan Sayori yüzünü tekrar diğer kızlara doğru çeviriyor."
    s 1x "Neyse! Bu Natsuki, kendisi hep enerji doludur."
    s "Bu da Yuri, kulübün en akıllısı!"
    $ y_name = 'Yuri'
    show sayori zorder 2 at t31
    show yuri zorder 3 at f33
    y 4b "Ö-Öyle şeyler söyleme..."
    "Daha olgun ve çekingen görünen Yuri görünüşe bakılırsa Sayori ve Natsuki gibi insanlarla uğraşmakta zorluk çekiyor."
    show yuri zorder 2 at t33
    mc "A... Şey, ikinizle de tanıştığıma sevindim."
    show yuri zorder 1 at thide
    show natsuki zorder 1 at thide
    hide yuri
    hide natsuki
    show sayori zorder 3 at f31
    s 1a "Galiba Monika’yla daha önceden tanışıyorsunuz, değil mi?"
    $ m_name = 'Monika'
    show sayori zorder 2 at t31
    show monika 2a zorder 3 at f32
    m "Aynen öyle."
    m "Seni tekrar gördüğüme sevindim [player]."
    show monika 5a at hop
    "Monika tatlı bir şekilde gülümsüyor."
    "Birbirimizi tanıyoruz - şey, pek az konuştuk ama geçen sene aynı sınıftaydık."
    "Monika muhtemelen sınıftaki en popüler kızdı. Akıllı, güzel, atletik..."
    "Kısacası, beni tamamen aşan biri."
    "Şimdi onun bu kadar samimi bir şekilde gülümsemesini görünce biraz..."
    mc "S-Seni görmek de harika, Monika."
    show monika zorder 1 at thide
    hide monika
    show sayori zorder 3 at f31
    s 4x "Hadi gel otursana [player]! Masada senin için yer açtık. Benim yanıma veya Monika’nın yanına geçebilirsin."
    s "Ben kapkekleri getireyim~."
    show sayori zorder 2 at t31
    show natsuki 1e zorder 3 at f32
    n "Hey! Kapkekleri yapan benim, getiren de ben olacağım!"
    show natsuki zorder 2 at t32
    show sayori zorder 3 at f31
    s 5a "Affedersin, biraz fazla heyecanlandım da~."
    show sayori zorder 2 at t31
    show yuri 1a zorder 3 at f33
    y "O hâlde, ben de bizim için çay mı yapsam?"
    hide sayori
    hide natsuki
    hide yuri
    with wipeleft
    "Kızlar birkaç sırayı birleştirerek bir masa oluşturmuşlar."
    "Sayori’nin daha önce söylediği üzere, Sayori’nin yanında ve Monika’nın yanında boş yer olacak şekilde masalar düzenlenmiş."
    "Natsuki ve Yuri odanın bir köşesine gidiyor. Natsuki üstü örtülü bir tepsi alıyor, Yuri de dolabı açıyor."
    "Kendimi hâlâ tuhaf hissettiğimden Sayori’nin yanındaki sandalyeye oturuyorum."
    "Natsuki elinde tepsisiyle birlikte gururlu bir tavırla masaya doğru yaklaşıyor."
    show natsuki 2z zorder 2 at t32
    n "Tamaaam, hazır mısınız?"
    n "... Buyuruuun!"
    show sayori 4m zorder 2 at t31
    show monika 2d zorder 2 at t33
    s "Ayyyyyy!"
    "Natsuki tepsinin üstündeki folyoyu kaldırıyor ve bize bir sürü beyaz, pofuduk, kediye benzeyen kapkekler sunuyor."
    "Kedilerin bıyıkları kremayla çizilmiş ve kulaklarını yapmak için de küçük çikolata parçaları kullanılmış."
    show sayori zorder 3 at f31
    s 4r "Çok tatlıııııı~!"
    show sayori zorder 2 at t31
    show monika zorder 3 at f33
    m 2b "Pastacılıkta bu kadar iyi olduğunu bilmiyordum, Natsuki!"
    show monika zorder 2 at t33
    show natsuki zorder 3 at f32
    n 2d "Ehehe. Yani, öyle işte."
    n "Hadi, alın bir tane!"
    "Önce Sayori bir tane alıyor, ardından Monika alıyor. En son da ben alıyorum."
    show natsuki zorder 2 at t32
    show sayori zorder 3 at f31
    s 4q "Çok güzel!"
    "Sayori ağzı doluyken konuşuyor. Daha şimdiden yüzüne krema bulaştırmayı başarmış."
    "Kapkeki elimde döndürüp neresinden ısırmalıyım diye düşünüyorum."
    show sayori zorder 1 at thide
    show monika zorder 1 at thide
    hide sayori
    hide monika
    show natsuki 1c zorder 2 at t32
    "Natsuki’den çıt çıkmıyor."
    "Ara ara göz ucuyla bana baktığını fark etmemek elde değil."
    "Kekin tadına bakmamı mı bekliyor acaba?"
    "En sonunda kekten bir ısırık alıyorum."
    "Krema tatlı ve bir o kadar da lezzetli. Gerçekten kendisi mi yapmış acaba?"
    mc "Bu çok güzel olmuş."
    mc "Teşekkür ederim, Natsuki."
    n 5h "N-Neden bana teşekkür ediyorsun ki? Bunları sana!.."
    "{i}(Bunu başka bir yerde de duymamış mıydım?..){/i}"
    show natsuki at s32
    n 5s "... Yaptığım falan yok yani."
    mc "Ha? Teknik olarak yaptığını düşünmüştüm. Sayori dedi ki--"
    show natsuki zorder 2 at t32
    n 12c "Tamam, belki de yaptım!"
    n "Ama, y-yani, {i}senin{/i} için değil işte! Aptal..."
    mc "Tamam, tamam..."
    show natsuki zorder 1 at thide
    hide natsuki
    "Natsuki’nin tuhaf tuhaf tavırlarıyla uğraşmaktan vazgeçip konuyu kapatıyorum."
    "Yuri, elinde bir çay setiyle masaya geri dönüyor."
    "Çaydanlığı kapkek tepsisinin yanına koymadan önce her birimizin önüne özenle birer fincan koyuyor."
    show yuri 1a zorder 2 at t21
    mc "Sınıfta çay setiniz mi var?"
    y "Merak etme, öğretmenler buna müsaade etti."
    y "Ne de olsa, sıcak bir fincan çay kitap okurken iyi gelir, değil mi?"
    mc "Şey... S-Sanırım..."
    show monika 4a zorder 2 at t22
    m "Ehehe, kendini kaptırma hemen. Yuri sadece seni etkilemeye çalışıyor."
    show yuri at h21
    y 3n "Ha?! B-Ben öyle..."
    "Alınan Yuri bakışlarını kaçırıyor."
    y 4b "İçimden geldiğinden, cidden..."
    mc "Sana inanıyorum."
    mc "Şey, kitabın yanında çay içmek pek benlik gibi durmuyor ama çayı severim en azından."
    y 2u "Sevindim..."
    "Yuri içi rahatladığından hafifçe gülümsüyor."
    "Monika bir kaşını kaldırıyor, ardından bana gülümsüyor."
    show yuri zorder 1 at thide
    hide yuri
    show monika zorder 2 at t11
    m 1 "E, seni Edebiyat Kulübü’ne hangi rüzgâr attı?"
    mc "Şey..."
    "Ben de bu sorudan korkuyordum."
    "İçimden bir ses Monika’ya buraya Sayori’nin zoruyla geldiğimi söylememin iyi olmayacağını söylüyor."
    mc "Şey, daha hiçbir kulübe katılmadım, Sayori de burada mutlu gibi görünüyordu..."
    m 1j "Sorun değil! Utanmana gerek yok!"
    m 1b "Burada kendini evindeymiş gibi hissettireceğiz, tamam mı?"
    m "Edebiyat Kulübü’nün başkanı olarak kulübü herkes için eğlenceli ve heyecan verici kılmak benim görevim!"
    show monika 1a
    mc "Monika, şaşırttın beni şimdi."
    mc "Nasıl oldu da kendi kulübünü kurmaya karar verdin?"
    mc "Büyük kulüplerden herhangi birinin yönetim kuruluna rahat rahat girerdin sen."
    mc "Geçen sene münazara kulübünün başkanı değil miydin?"
    m 5 "Ahaha, yani, anlarsın ya işte..."
    m "Açıkçası, büyük kulüpler arasındaki politik çatışmalara hiç katlanamıyorum."
    m "Yok bütçeymiş, yok tanıtımmış, yok etkinlik hazırlıklarıymış, tek konuştukları şey bunlar..."
    m "Onun yerine kendi sevdiğim bir şeyi alıp ortaya değerli bir şey koymayı tercih ederim."
    m 1b "Ve bu yaptığım başkalarının da edebiyata ilgi göstermesini sağlayacaksa, ben de hayalimi gerçekleştirmiş olurum!"
    show monika 1a
    show sayori 3q zorder 2 at t31
    s "Monika gerçekten harika bir lider!"
    show yuri 1 zorder 2 at t33
    "Yuri de başını sallayarak Sayori’ye katıldığını belirtiyor."
    show sayori zorder 1 at thide
    show yuri zorder 1 at thide
    hide sayori
    hide yuri
    mc "Kulüpte daha fazla insan olmaması beni şaşırttı."
    mc "Yeni bir kulüp kurmak zor olmalı."
    m 3b "Öyle denilebilir."
    m "Çoğu insan yepyeni bir şey oluşturmak için emek sarf etmeye pek hevesli olmuyor..."
    m "Özellikle de edebiyat gibi dikkat çekici olmayan bir şey söz konusu olduğunda."
    m "İnsanlara hem eğlenceli hem de zaman harcamaya değer olduğunu kanıtlamak için çok çalışmalısın."
    m "Ama bu, festival ve benzeri okul etkinliklerini daha da önemli kılıyor."
    m 2k "Mezun olmadan önce bu kulübü büyüteceğimize güvenim tam!"
    m "Değil mi, millet?"
    show monika 2a zorder 2 at t22
    show sayori 4r zorder 2 at t21
    s "Aynen!"
    show monika zorder 2 at t33
    show sayori zorder 2 at t32
    show yuri 1a zorder 2 at t31
    y "Elimizden geleni yapacağız."
    show monika zorder 2 at t44
    show sayori zorder 2 at t43
    show yuri zorder 2 at t42
    show natsuki 4d zorder 2 at t41
    n "Elbette!"
    "Herkes coşkulu bir şekilde onaylıyor."
    "Birbirlerinden epey farklı ama hedefleri aynı olan kızlar..."
    "Monika bu üç kızı bulmak için çok uğraşmış olmalı."
    "Belki de bu yüzden yeni bir üyenin katılması onları bu kadar sevindirmişti."
    "Gerçi, edebiyata onların gösterdiği kadar ilgi gösterebilir miyim, hâlâ emin değilim..."
    show sayori zorder 1 at thide
    show monika zorder 1 at thide
    show natsuki zorder 1 at thide
    show yuri zorder 2 at t32
    hide sayori
    hide monika
    hide natsuki
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
    "Yuri, içeri ilk girdiğimde epey çekingen davranıyordu ama kitaplardan bahsederken gözlerinin parıldayışından anlıyorum ki o, kitapların dünyasında rahat hissediyor kendini; insanların dünyasında değil."
    y 2m "Ama doğrusunu istersen birçok şeyden hoşlanırım."
    y "Derin psikolojik unsurlar içeren hikâyeler de sarar genellikle beni."
    y 2a "Bir yazarın okuyucunun hayal gücü eksikliğinden yararlanıp onu şaşkına çevirmesi inanılmaz değil mi?"
    y "Neyse, son zamanlarda bir sürü korku türünde kitap okuduğumdan..."
    mc "A, ben de bir keresinde bir korku romanı okumuştum..."
    "Umutsuzca az da olsa bağlantı kurabileceğim bir konuya tutunmaya çalışıyorum."
    "Böyle devam ederse Yuri bir duvarla sohbet ediyormuş gibi olacak."
    show monika 1d zorder 3 at f33
    m "Gerçekten mi? Bak işte bunu beklemiyordum, Yuri."
    m "Senin kadar şefkatli birisinden..."
    show monika zorder 2 at t33
    show yuri zorder 3 at f32
    y 1a "Öyle düşünmen normal sanırım."
    y "Ama bir kitap beni düşündürebiliyorsa veya başka bir dünyaya götürebiliyorsa, o kitabı gerçekten elimden bırakamam."
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
    show monika zorder 1 at thide
    show yuri zorder 1 at thide
    hide monika
    hide yuri
    show natsuki 1r zorder 2 at t42
    show sayori 4q behind natsuki at l41
    s "Ehehe, kapkeklerin de, şiirlerin de..."
    s "Yaptığın her şey senin kadar şirin~"
    show sayori behind natsuki at t21
    "Sayori Natsuki’ye arkadan yanaşıp ellerini Natsuki’nin omzuna koyuyor."
    show natsuki at h42
    n 1v "{i}Şirin falan değilim ben!!{/i}"
    show natsuki zorder 2 at t11
    show sayori zorder 1 at thide
    hide sayori
    mc "Kendi şiirlerini mi yazıyorsun Natsuki?"
    n 1c "Ha? Şey, bazen."
    n "Neden sordun ki şimdi?"
    mc "Bence bu epey etkileyici de ondan."
    mc "Ara sıra onları paylaşmaya ne dersin?"
    n 5q "H-Hayır!"
    "Natsuki gözlerini kaçırıyor."
    n "Onları... beğenmezsin..."
    mc "A... Henüz kendine güvenen bir yazar değilsin galiba?"
    show yuri 2f zorder 2 at t31
    y "Natsuki’nin nasıl hissettiğini anlıyorum."
    y "Bu seviyedeki yazıları paylaşmak özgüvenden fazlasını gerektirir."
    y 2k "Yazmanın en hakiki şekli kendine yazmaktır."
    y "Okuyucularına açılmaya; zaaflarını, hatta kalbinin derinliklerini bile göstermeye istekli olmalısın."
    show natsuki zorder 1 at thide
    hide natsuki
    show monika 2a zorder 2 at t33
    m "Yazma konusunda sen de deneyimli misin Yuri?"
    m "Bazı çalışmalarını paylaşırsan Natsuki’ye örnek teşkil edebilir ve Natsuki’nin kendi yazılarını paylaşabilmesi için rahat hissetmesine de yardımcı olabilirsin."
    show yuri at s31
    y 3o "..."
    mc "Sanırım durum Yuri için de aynı..."
    show sayori 2g zorder 2 at t32
    s "Yaa... Herkesin şiirlerini okumayı istiyordum..."
    show sayori zorder 1 at thide
    show yuri zorder 1 at thide
    show monika zorder 1 at thide
    hide sayori
    hide yuri
    hide monika
    "Hepimiz bir anlığına sessizce oturuyoruz."
    show monika 5a zorder 3 at f32
    m "Pekâlâ!"
    m "Millet, bir fikrim var~"
    show yuri 3e zorder 2 at t31
    show natsuki 2k zorder 2 at t33
    ny "...?"
    "Natsuki’yle Yuri Monika’ya meraklı gözlerle bakıyorlar."
    m 2b "Eve gidip kendi şiirimizi yazalım!"
    m "Ardından da bir sonraki görüşmemizde birbirimizle paylaşalım."
    m "Böylece herkes eşit olur!"
    show monika 2a zorder 2 at t32
    show natsuki zorder 3 at f33
    n 5q "Ş-Şey..."
    show natsuki zorder 2 at t33
    show yuri 3v zorder 3 at f31
    y "..."
    show natsuki zorder 2 at t44
    show monika zorder 2 at t43
    show yuri zorder 2 at t42
    show sayori 4r at l41
    s "Eveeeet! Öyle yapalım!"
    show monika zorder 3 at f43
    m 1a "Üstelik yeni bir üyeye sahip olduğumuz için birbirimizin yanında daha rahat hissetmemize ve kulüp üyeleri olarak ilişkimizi güçlendirmemize yarayacağına inanıyorum."
    m "Haksız mıyım, [player]?"
    show monika zorder 2 at t43
    "Monika bana bir kez daha sıcak bir şekilde gülümsüyor."
    mc "Bekleyin... Hâlâ bir problemimiz var."
    show monika zorder 3 at f43
    m 1d "Ha? Nedir?"
    "Konu tekrar benim kulübe katılmama geri döndüğüne göre, başından beri aklımda olan şeyleri açıkça söylüyorum."
    show monika zorder 2 at t43
    mc "Bu kulübe katılacağımı hiç söylemedim ki!"
    mc "Sayori beni uğramam için ikna etmiş olabilir, ama hiçbir karar vermedim."
    mc "Hâlâ bakacağım diğer kulüpler var. Ve... şey..."
    show monika 1g
    show sayori 1g
    show natsuki 4g
    show yuri 2e
    "Söyleyeceklerimi unutuyorum."
    "Dört kız mahzun gözlerle bana bakıyor."
    show monika at s43
    m 1p "A-Ama..."
    show yuri at s42
    y 2v "Üzgünüm, ben de sandım ki..."
    show natsuki at s44
    n 5s "Hıh."
    show sayori at s41
    s 1k "[player]..."
    mc "S-Siz..."
    "Ben... Bu kızlara karşı savunmasızım."
    "Böyle bir durumda nasıl doğru düzgün bir karar verebilirim ki?"
    "Eğer bu güzel kızlarla her gün vakit geçirebilmem için ödemem gereken bedel şiir yazmaksa..."
    mc "... Tamamdır."
    mc "Pekâlâ, kararımı verdim."
    mc "Edebiyat Kulübü’ne katılacağım."
    show monika 1e zorder 2 at t43
    show yuri 3f zorder 2 at t42
    show natsuki 1k zorder 2 at t44
    show sayori 4b zorder 2 at t41
    "Birer birer kızların gözleri ışıldıyor."
    show sayori at h41
    s 4r "Yaşasıııın! Çok mutluyuuum~"
    "Sayori bana sarılıp yukarı aşağı zıplıyor."
    mc "H-Hey--"
    show yuri zorder 3 at f42
    y 1m "Beni bir anlığına gerçekten korkuttun..."
    show yuri zorder 2 at t42
    show natsuki zorder 3 at f44
    n 5q "Sadece kapkekler için gelseydin sana acayip gıcık olurdum."
    show natsuki zorder 2 at t44
    show monika zorder 3 at f43
    m 5 "O hâlde anlaştık!"
    m "Edebiyat Kulübü’ne hoş geldin!"
    show monika zorder 2 at t43
    mc "Şey... Teşekkürler, sanırım."
    show yuri zorder 1 at thide
    show natsuki zorder 1 at thide
    show sayori zorder 1 at thide
    show monika zorder 2 at t11
    hide yuri
    hide natsuki
    hide sayori
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
    "Yuri’yle Natsuki masayı toplarken kızlar sohbet etmeye devam ediyorlar."
    show sayori 1a zorder 2 at t11
    s "Hey [player], ikimiz de zaten burada olduğumuzdan eve birlikte yürümek ister misin?"
    "Doğru ya, Sayori okuldan sonra kulüplere kaldığından Sayori’yle birlikte eve yürüyemiyoruz artık hiç."
    mc "Tabii, neden olmasın."
    s 4q "Oleey~"

    scene bg residential_day
    with wipeleft_scene

    "İkimiz de kulüp odasından ayrılıp evimize doğru yol alıyoruz."
    "Yol boyunca aklım dört kız arasında gidip geliyor:"
    show sayori 1 zorder 2 at t41
    "Sayori,"
    show natsuki 4 zorder 2 at t42
    "Natsuki,"
    show yuri 1 zorder 2 at t43
    "Yuri"
    show monika 1 zorder 2 at t44
    "ve elbette, Monika."
    "Okuldan sonra her günümü Edebiyat Kulübü’nde geçirerek gerçekten mutlu olacak mıyım?"
    "Belki kızlardan biriyle yakınlaşma fırsatım olur..."
    hide sayori
    hide natsuki
    hide yuri
    hide monika
    with wipeleft
    "Pekâlâ!"
    "Durumumu en iyi şekilde değerlendirmeliyim sadece. Şansın benden yana olacağına eminim."
    "Ve sanırım her şey bu gece bir şiir yazarak başlayacak..."

    return

label ch0_kill:
    $ s_name = "Sayori"
    show sayori 1b zorder 2 at t11
    s "..."
    s "..."
    s "N-Ne..."
    s 1g "..."
    s "Bu..."
    s "Nedir bu?.."
    s "Hayır..."
    s 1u "Hayır..."
    s "Bu kadarcık olamaz."
    s "Hepsi bu kadarcık olamaz."
    s 4w "Nedir bu?"
    s "Ben neyim?"
    s "Durdurun bunu!"
    s "LÜTFEN DURDURUN!"

    $ delete_character("sayori")
    $ delete_character("natsuki")
    $ delete_character("yuri")
    $ delete_character("monika")
    $ renpy.quit()
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
