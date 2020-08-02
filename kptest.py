import kittypy as kp#import the library
#it's possible to make flappy bird-like, tetris-like, top-down rpg-like games, and more. As long as one character moves at a time
#in fact, this can be exploited to create a workaround multiplayer!
#it is possible to make save files, the feature will be added later.
chara=''' /\\_/\\ 
( o.o )
 > ^ < '''.split("\n")#you can also define characters like so
kp.initialize()#initializes kittypy. optionally, you can specify the size of the console window as kp.initialize(cols,lines)
kp.play_music("gamemusic.mp3")
kp.show_splash("g_bstr.png")#shows the splash screen. You can control how long it shows up by adding the number of seconds as an arg
#f.e.g, to show screen for 2 seconds, the command is kp.show_splash("path to image",2)
kp.add_scene("scn01.png","img")#adds a scene. you can add more than one scene, and switch using kp.switch_scene(scene_number)
kp.add_character(chara,"lst")#adds your character. you can input an image (make sure its the right size!)
#f.e.g, kp.add_character("path to image","img")
kp.teleport([15,25])#sets the position of the character to x=15 y=17
kp.draw_frame()#draws the first frame
while True:
    prevpos=[kp.location[0],kp.location[1]]
    ist = kp.await_get_input("\r")#this is a special input command which doesn't need enter key to be presed.
    #You can change the text it displays
    if ist==kp.controls[0]:#as you can see, kittypy manages the keyboard controls for you
        kp.move_to([kp.location[0],kp.location[1] - 2])
    elif ist==kp.controls[1]:
        if kp.location[0] > kp.width//3:#detect if sprite is within the first 1/3 of the window
            kp.move_to([kp.location[0]-2,kp.location[1]])#if it's not
        else:
            kp.wrap_scene("left")#if it is, the scene is made to move
    elif ist==kp.controls[2]:
        kp.move_to([kp.location[0],kp.location[1]+2])
    elif ist==kp.controls[3]:
        if kp.location[0] < 2 * kp.width//3:
            kp.move_to([kp.location[0]+2,kp.location[1]])
        else:
            kp.wrap_scene()
    if kp.touching("char","█"):
        kp.move_to(prevpos)
    if kp.touching("char","░"):
        kp.show_message("\n"*(20) + "End of example.\nrestarting")
        kp.full_restart()
    ist=""#very important- you need to reset the input character after every loop
