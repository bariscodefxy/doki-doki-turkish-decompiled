init python:
    class RectCluster(object):
        def __init__(self, theDisplayable, numRects=12, areaWidth = 30, areaHeight = 30):
            self.sm = SpriteManager(update=self.update)
            self.rects = [ ]
            self.displayable = theDisplayable
            self.numRects = numRects
            self.areaWidth = areaWidth
            self.areaHeight = areaHeight
            
            for i in range(self.numRects):
                self.add(self.displayable)
        
        def add(self, d):
            s = self.sm.create(d)
            s.x = (random.random() - 0.5) * self.areaWidth * 2
            s.y = (random.random() - 0.5) * self.areaHeight * 2
            s.width = random.random() * self.areaWidth / 2
            s.height = random.random() * self.areaHeight / 2
            self.rects.append(s)
        
        def update(self, st):
            for s in self.rects:
                s.x = (random.random() - 0.5) * self.areaWidth * 2
                s.y = (random.random() - 0.5) * self.areaHeight * 2
                s.width = random.random() * self.areaWidth / 2
                s.height = random.random() * self.areaHeight / 2
            return 0

image n_rects_ghost1:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    pos (580, 270)
    size (20, 25)
    alpha 0.0
    8.0
    easeout 12 alpha 1.0

image n_rects_ghost2:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    pos (652, 264)
    size (20, 25)
    alpha 0.0
    8.0
    easeout 12 alpha 1.0

image n_rects_ghost3:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    pos (616, 310)
    size (25, 15)
    alpha 0.0
    8.0
    easeout 12 alpha 1.0

image n_rects_ghost4:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    pos (735, 310)
    size (25, 20)
    0.5
    easeout 0.25 zoom 4.5 xoffset 250 yoffset -250

image n_rects_ghost5:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    pos (740, 376)
    size (25, 20)
    0.5
    easeout 0.25 zoom 4.5 xoffset 250 yoffset -100

label natsuki_exclusive2_1:
    scene bg club_day
    with wipeleft_scene
    n "Of!.."
    "Natsuki’nin deponun içinden öfkeli bir şekilde ofladığını duyuyorum."
    "Bir şey canını sıkmış gibi görünüyor."
    "Belki yardıma ihtiyacı vardır diye yanına yaklaşıyorum."
    play music t6 fadeout 1
    scene bg closet
    show natsuki 4r zorder 2 at t11
    with wipeleft_scene
    $ style.say_dialogue = style.normal
    mc "Bir şey mi arıyorsun?"
    $ style.say_dialogue = style.edited
    n 4x "siktiğimin monikasığğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğğ"
    $ style.say_dialogue = style.normal
    $ _history_list[-1].what = "Kahrolası Monika..."
    n "Eşyalarımı olmaları gerektiği yere geri koymuyor hiç!"
    n "Birisi gelip dağıtacaksa koleksiyonunu düzenli tutmanın ne anlamı kalıyor ki?"
    "Natsuki üst üste dizilmiş birkaç kitabı ve kutuyu rafın bir kenarına itiyor."
    mc "Manga..."
    n 2c "Sen manga okuyorsun, değil mi?"
    mc "Şey--"
    mc "... Bazen..."
    "Manga, karşındaki kişinin bu konudaki duruşunun ne olduğunu bilmeden gerçekten sevdiğini itiraf edemeyeceğin şeylerden biri."
    mc "... Nereden anladın ki?"
    n 2k "Bir ara bahsetmiştin."
    n "Ayrıca, yüzünden okunuyor zaten."
    "Ne demek oluyor bu?.."
    mc "A-Anladım..."
    "Raflardan birinin yanında, üst üste dizili envaiçeşit kitabın arasında bir cilt manga yalnız başına duruyor."
    "Meraktan mangayı kitapların arasından çıkarıyorum."
    n 1b "Demek {i}buradaydı{/i}!"
    "Natsuki mangayı elimden kapıyor."
    "Sonra bir kutu mangaya doğru dönüyor ve cildi diğerlerinin tam ortasına yerleştiriyor."
    n 4d "Aah, böylesi çok daha iyi!"
    n "Bir kutulu setin içinde bir cildin eksik olduğunu görmek muhtemelen bu dünyadaki en sinir bozucu manzara."
    mc "O hissi bilirim..."
    "Natsuki’nin hayranlıkla seyrettiği kutulu manga setine yakından bakıyorum."
    mc "Parfe Kızlar?.."
    "Bu, hayatımda hiç duymadığım bir seri."
    "Bu muhtemelen ya bu serinin berbat olduğununun ya da hedef kitlesinin benden çok farklı olduğunun göstergesi."
    n 5g "Yargılayacaksan gidip şuradaki kapının camının arkasından yargılayabilirsin."
    "Natsuki sınıf kapısını işaret ediyor."
    mc "H-Hey, bir şeyi yargıladığım falan yok!.."
    mc "Bir şey demedim bile."
    n 5c "Ses tonundan anladım."
    $ style.say_dialogue = style.normal
    n "Ama sana bir şey diyeceğim, [player]."
    n 4l "Bunu doğrudan Edebiyat Kulübü’nden bir ders olarak gör:{nw}"
    $ _history_list[-1].what = "Bunu doğrudan Edebiyat Kulübü’nden bir ders olarak gör: Bir kitabı kapağına göre yargılama!"
    $ style.say_dialogue = style.edited
    n "bir kitabı kapağına göreeeeeeeeeeeeeeeee eeeee ee{space=20}e{space=40}e{space=120}e{space=160}e{space=200}e"
    $ style.say_dialogue = style.normal
    $ _history_list.pop()
    n "Hatta--"
    "Natsuki, kutudan Parfe Kızlar’ın ilk cildini çıkarıyor."
    n "Sana tam olarak neden böyle dediğimi göstereceğim!"
    "Natsuki kitabı ellerime tutuşturuyor."
    mc "A..."
    "Kapağına bakıyorum."
    "Kapağında, renkli kıyafetler içinde hayat dolu feminen pozlar veren dört kız var."
    "Bu... aşırı “moe”."
    n 4b "Öylece durma orada!"
    mc "Ha--"
    show natsuki zorder 1 at thide
    hide natsuki
    "Natsuki kolumdan tutup beni depodan çıkarıyor."
    "Daha sonrasında ise pencere denizliğinin altına duvara yaslanarak oturuyor."
    "Oturduğu yerin yakınına hafifçe vurarak oraya oturmamı işaret ediyor."
    show bg club_day
    show natsuki 2a zorder 2 at t11
    with wipeleft
    mc "Sandalye daha rahat olmaz mıydı?.."
    "Yere oturuyorum."
    n 2k "Sandalyeler işimizi görmez."
    n "Öyle aynı anda okuyamayız."
    mc "Ha? Niye ki?"
    mc "Şey... Sanırım yakın olmak böyle daha kolay..."
    n 2o "--!"
    n 5r "Ö-Öyle şeyler söyleme!"
    n "Kendimi garip hissettireceksin bana!"
    "Natsuki kollarını kavuşturuyor ve benden biraz uzaklaşıyor."
    mc "Özür dilerim..."
    show natsuki 5g
    "Ben de ona bu kadar yakın oturmayı pek beklemiyordum..."
    "Bunun tam olarak kötü bir şey olduğunu söyleyemem tabii."
    "Kitabı açıyorum."
    "Birkaç saniye sonra Natsuki, fark etmeyeceğimi umarak, santim santim tekrar yanıma geliyor."
    "Kolumun üzerinden kitaba baktığını, okumaya başlamaya benden daha hevesli olduğunu görebiliyorum."
    n 1k "Vay be, bunun başlangıcını okuyalı ne kadar zaman olmuştur acaba?.."
    mc "Ha?"
    mc "Ara sıra eski ciltlere dönüp göz gezdirmiyor musun?"
    n 2k "Pek değil."
    n "Belki bir seriyi bitirdikten bir süre sonra."
    n 2c "Hey, dikkatini veriyor musun?"
    mc "Şey..."
    "Veriyorum ama henüz önemli bir şey olmadı o yüzden aynı zamanda konuşabiliyorum da."
    "Görünüşe bakılırsa hikâye liseye giden bir grup arkadaşla alakalı."
    "Tipik “hayattan kesitler” muhabbeti."
    "Bu tarz hikâyeler artık benim pek ilgimi çekmiyor çünkü hikâyelerin pek azı ilgi çekici bir konunun olmayışının eksikliğini eğlenceli bir yazım tarzı ile kapatabiliyor."
    $ persistent.clear[0] = True
    scene n_cg1_bg
    show n_cg1_base
    with dissolve_cg
    mc "... Bunun senin için sıkıcı olmadığına emin misin?"
    n "Değil!"
    mc "Sadece benim okumamı izlemene rağmen mi?"
    n "Şey!.."
    n "Ben... böyle iyiyim."
    mc "Sen öyle diyorsan..."
    mc "Sanırım sevdiğin bir şeyi bir başkasıyla paylaşmak epey eğlenceli bir şey."
    mc "Herhangi bir arkadaşımı sevdiğim bir seriye başlaması için ikna ettiğimde hep heyecanlanırım."
    mc "Bu hissi bilir misin?"
    n "?.."
    mc "Ha?"
    mc "Bilmiyor musun?"
    show n_cg1_exp2 at cgfade
    n "Şey..."
    n "Onu..."
    n "Eh, pek bilmiyorum."
    mc "... Nasıl yani?"
    mc "Mangalarını arkadaşlarınla paylaşmıyor musun?"
    hide n_cg1_exp2
    show n_cg1_exp3 at cgfade
    n "Bunu yüzüme vurmasan olmaz mıydı?"
    n "Of..."
    mc "Şey... Özür dilerim..."
    n "Hıh."
    n "Sanki arkadaşlarımın bunu okumasını sağlayabilirim de..."
    n "Arkadaşlarım mangaların çocuklar için olduğunu düşünüyorlar."
    n "Onlar şöyle şeyler söylemeden mangalardan bahsedemiyorum bile..."
    n "‘Ha? Kaç yaşına geldin, hâlâ bunlarla mı ilgileniyorsun?’"
    n "Suratlarına yumruğu geçiresim geliyor..."
    mc "Of, öylelerini iyi bilirim..."
    mc "Açıkçası buna ön yargıyla yaklaşmayacak bir arkadaş bulmak zor, bunlardan hoşlanan bir arkadaş bulmak ise daha da zor..."
    mc "Ben zaten eziğin teki sayılırım o yüzden zamanla diğer eziklere bir şekilde çekildim sanırım."
    mc "Ama bu muhtemelen senin gibi biri için çok daha zordur..."
    hide n_cg1_exp3
    n "Hmm."
    n "Evet, oldukça haklısın."
    "{i}... Dur biraz, hangi kısım için dedi bunu??{/i}"
    $ style.say_dialogue = style.normal
    n "Ya, bunları kendi odamda bile tutamam gibi geliyor..."

    $ style.say_dialogue = style.edited
    n "Babam bunları bulsaydı ağzımı yüzümü dağıtırdı."
    $ style.say_dialogue = style.normal
    $ _history_list[-1].what = "Babam bunları bulsaydı ne yapardı bilmiyorum bile."
    n "En azından burada, kulüp odasında, güvendeler."
    show n_cg1_exp3 at cgfade
    n "Monika bu konuda biraz gıcıklık yapmıştı gerçi..."
    n "Of! Hiç kazanamayacağım, değil mi?"
    mc "Eh, nihayetinde buna değdi ama, değil mi?"
    mc "Yani, ben buradayım, bu mangayı okuyorum."
    n "Ama bu benim hiçbir sorunumu çözüyor değil."
    mc "Belki de çözmüyor..."
    mc "Ama en azından eğleniyorsun, öyle değil mi?"
    hide n_cg1_exp3
    show n_cg1_exp2 at cgfade
    n "--"
    n "..."
    n "... Yani?"
    mc "Ahaha."
    hide n_cg1_exp2
    show n_cg1_exp3 at cgfade
    n "Of, yeter bu kadar!"
    n "Okumaya devam edecek misin etmeyecek misin?"
    mc "Tamam, tamam..."
    "Sayfayı çeviriyorum."
    show black with dissolve_cg
    "..."
    "..."
    "....."
    "......."
    "........."
    "Zaman geçiyor."
    hide n_cg1_exp3
    show n_cg1_exp4 behind black at cgfade
    "Natsuki şu an garip bir şekilde sessiz."
    "Natsuki’ye doğru kaçamak bir bakış atıyorum."
    hide black with dissolve_cg
    "Uykuya dalmak üzereymiş gibi görünüyor."
    mc "Hey, Natsuki..."
    hide n_cg1_exp4
    show n_cg1_exp5 at cgfade
    n "E-Evet?"
    "Natsuki birden üstüme yığılıyor."
    play sound fall
    $ style.say_dialogue = style.normal
    mc "H-Hey--"
    show n_cg1_exp5
    hide n_cg1_exp5

    show n_cg1b
    hide n_cg1_base

    $ currentpos = get_pos()
    $ audio.t6g = "<from " + str(currentpos) + " loop 10.893>bgm/6g.ogg"
    play music t6g
    $ ntext = glitchtext(96)
    $ style.say_dialogue = style.edited
    n "{color=#000}[ntext]{/color}"
    $ ntext = glitchtext(96)
    n "{color=#000}[ntext]{/color}"
    $ style.say_dialogue = style.normal

    stop music
    window hide(None)
    window auto
    scene bg club_day
    show monika 1r zorder 2 at t11
    m "Of of..."
    m 1d "Natsuki, iyi misin?"
    show monika zorder 2 at t21
    show natsuki 12b zorder 3 at f22
    n "..."
    show natsuki zorder 2 at t22
    show monika zorder 3 at f21
    m 1a "Al bakalım..."
    show monika zorder 2 at t21
    "Monika çantasına uzanıp içinden bir tür protein barı çıkarıyor."
    "Natsuki’ye doğru fırlatıyor."
    "Natsuki’nin gözleri bir anda yeniden parlıyor."
    "Protein barını yerden kapıp hızlı bir şekilde paketini açıyor."
    show natsuki zorder 3 at f22
    n 1s "Sana demedim mi bana nağm..."
    show natsuki zorder 2 at t22
    "Natsuki cümlesini bile tamamlamadan protein barını ağzına tıkıştırıyor."
    show natsuki zorder 1 at thide
    hide natsuki
    show monika 3b zorder 2 at t11
    m "Endişelenme [player]."
    m "Natsuki’nin bir şeyi yok."
    m "Arada sırada oluyor bu."
    m 1a "Bu yüzden çantamda onun için atıştırmalık bir şey tutuyorum hep."
    m 5a "Her neyse!.."
    m "Şiirlerimizi paylaşalım mı artık?"

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
