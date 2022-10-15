label ch10_main:
    $ delete_all_saves()
    $ persistent.deleted_saves = True
    $ gtext = glitchtext(48)
    stop music
    $ config.window_hide_transition = None
    scene bg residential_day
    with dissolve_scene_half
    $ config.window_hide_transition = Dissolve(.2)
    play music t2g
    queue music t2g2

    s "[gtext]"
    $ s_name = glitchtext(12)
    "Bana doğru koşan, üzerine çekebileceği dikkatten bihabermişçesine el sallayan baş belası bir kız görüyorum."
    "O kızın adı [s_name], kendisi komşum ve çocukluğumdan beri yakın arkadaşım."
    "Hani bugün olsa arkadaş olmak istemeyeceğiniz ama uzun zamandır birbirinizi tanıdığınızdan bir şekilde arkadaşlığınızı yürüttüğünüz tipler olur ya, o da öyle işte."
    "Eskiden okula birlikte giderdik, ama liseye başladığımız sıralarda Sayori sürekli uyuyakalmaya başladı, ben de onu beklemekten bıkmıştım."
    "Ama bu şekilde peşimden gelecekse kaçıp gitsem daha iyi sanki."
    "Yine de, sadece iç çekip kaldırımda öylece durup [s_name]’nin bana yetişmesini bekliyorum."

    show sayori glitch zorder 2 at t11
    python:
        currentpos = get_pos()
        startpos = currentpos - 0.3
        if startpos < 0: startpos = 0
        track = "<from " + str(startpos) + " to " + str(currentpos) + ">bgm/2.ogg"
        renpy.music.play(track, loop=True)
    pause 1.0
    $ gtext = glitchtext(48)
    s "{cps=60}[gtext]{/cps}{nw}"
    pause 1.0
    $ gtext = glitchtext(48)
    s "{cps=60}[gtext]{/cps}{nw}"
    show screen tear(8, offtimeMult=1, ontimeMult=10)
    pause 1.5
    hide screen tear
    window hide(None)
    window auto
    scene black with trueblack
    $ delete_all_saves()
    $ persistent.playthrough = 2
    $ persistent.anticheat = renpy.random.randint(100000, 999999)
    $ anticheat = persistent.anticheat

    jump ch20_from_ch10
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
