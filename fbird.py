import kittypy as kp
from threading import Thread
kp.initialize()
dchara='''  , ___
`\/{X,X}
 / /)  )
/,--"-"-'''.split("\n")
achara='''  , ___
`\/{o,o}
 / /)  )
/,--"-"-'''.split("\n")
kp.backfore=kp.Fore.WHITE
kp.chcolor=kp.Fore.BLACK + kp.Back.CYAN
kp.backback=kp.Back.CYAN
kp.play_music("start.mp3")
kp.show_splash("fbird_splash.png",2,kp.Image.BOX)
kp.add_scene("fbird_back.png","img",kp.Image.NONE)
kp.add_character(achara,"lst")
kp.add_character(dchara,"lst")
kp.cursp=0
kp.teleport([15,24])
kp.draw_frame()
kp.gravity(7)
def pt():
    score=0
    while True:
        kp.wrap_scene()
        score+=1
        kp.wait(0.1)
        if kp.touching("char","█"):
            break
    kp.cursp=1
    kp.play_music("lose.mp3")
    kp.chcolor=kp.Fore.RED + kp.Back.CYAN
    kp.move_to([kp.location[0],kp.location[1]-10])
    kp.show_message("\n"*(20) + "SCORE "+str(score)+"\nrestarting...")
    kp.full_restart()
t = Thread(target=pt, args=())
t.start()
while True:
    prevpos=[kp.location[0],kp.location[1]]
    ist = kp.await_get_input("\r")
    if ist==kp.controls[0]:
        kp.teleport([kp.location[0],kp.location[1]-3])
        kp.play_music("fly.wav")
    elif ist==kp.controls[2]:
        kp.teleport([kp.location[0],kp.location[1]+3])
    ist=""
