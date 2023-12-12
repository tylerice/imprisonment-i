name = input ('Please enter your name to start playing IMPRISONMENT I! ')
print(f'Greetings! Welcome your adventure {name}!')
print ("This is a text-based game called IMPRISONMENT I created by Tyler Le. You may use similar concepts in your own games as the ones in this story, but please do give proper credit if necessary.")
start = input ('Would you like to start the game? (y/n)')
if start == 'y':
    print("Great! Let's start your adventure!")
    setting = input("Your plane has just crashed in a field just a few miles north from a prison.. not just any prison, a Social Justice Prison. This is a prison based off of the ideas of Charles Dickens. The pilot of the plane died of a heart attack and you are left stranded with nothing but a pocket-knife, one MRE packet, and a glock in your backpack. You look further to your north, and all you see is a barren and dry desert stretching further than the eye can see. You automatically rule out going north so you decide to go [south] towards the prison.")

else:
    print("Lame.. you are now dead! 💀💀💀")
    quit ()
#start of the game
if setting == 'south':
    print ("You've been walking south in the direction of the prison for two hours now and the sun has completely set.")
    response = input ("Eventually, you arrive outside of the prison's huge iron gates.. Would you like to [bang] on the gates or [wait] until the morning when a guard comes out to patrol in the morning?")
    #choice #1
    if response == 'bang':
        print ("You bang on the gate lightly, no response.. Then you start to get desperate for water and thirsty, so you now you start rapping on the gates with much greater force. After a few moments, a cyclops comes outside and opens the gates, welcoming you inside!")
        response = input ("[follow] the cyclops")
        if response == 'follow':
          print ("It was a trap, you fell for it and now you've fallen victim to it")
          print ("You fell around 300 stories in the air and minecraft fall damage came into reality! 💀💀💀")
    #choice #2
    if response == 'wait':
        print ("You wait outside the gates for the next few hours and nobody comes outside. You become desperate and now you have to make a decesion.")
        response = input ("Would you like to [turn] away or be [patient] and wait for someone to come outside?")
        if response == 'patient':
            print ("You wait longer outside of the gates and nobody comes outside. You've died of dehydration and even though, you were patient, this might not have been the greatest choice ever.. 💀💀💀")
        if response == 'turn':
            print ("You leave the gates and you begin to wander back in the barren desert.")
            print ("You wander around for fifteen minutes before spotting a nearly dried-up lake.")
            response = input ("Would you like to [go] to the lake or [sleep]?")
            if response == 'go':
                 print ("You are very dehydrated and start stumbling your way towards the lake. Once you arrive, you take big gulps of the remaining water of what was a lake.")
                 print ("You use your hands as a scoop, and you take three handfuls of water before the 'lake' magically dries up and becomes a barren, dry desert like the things around it.")
                 response = input ("You make your way back to the prison but you trip over an invisible watermelon and die.. *Hint: Try the other choice..* 💀💀💀")
            if response == 'sleep':
                 print ("You take a short nap before being awakened in the early morning by a cyclops.")
                 print ("He is startled to see a traveler coming around his land. ***WHAT BRINGS YOU HERE?***")
                 response = input ("Would you like to [lie] or be [truthful] to him?")
                 if response == 'lie':
                      print ("Uh.. Fishing.")
                      print ("***FISHING IN THE DESERT?? QUITE BELIEVABLE. FOR THAT LIE, YOU DESERVE TO BECOME MY DINNER.***")
                      print ("Welp, I guess that's what you get for lying.. moral of the story: don't lie kids!! You lost! 💀💀💀")
                 if response == 'truthful':
                      print ("Uh.. I was just wandering and got a bit lost.. *hehe*")
                      response = input ("***OH.. TRAVELER.. I SEE, WHY DON'T YOU FOLLOW ME INSIDE AND I'LL BE SURE TO MAKE YOU FEEL WELCOMED [follow] the cyclops***")
                      if response == 'follow':
                           print ("You follow the cyclops down a dark hall and the next thing you know.. you're knocked out.")
                           print ("You have a dream.. One where you are being hung upside down and many things are racing through your head. Specifically.. social injustice. You hear voices tormenting you about racism in our world, sexism, and poverty. You see into the past-- slavery and you are horrified by the image of it. You also see women being treated unfairly, and disrespected.. not being allowed to work. Finally, your last vision goes into the future when you see poverty on the streets. You are faced with the image of people sleeping on sidewalks and suffering from sicknesses without any help.")
                           print ("Eventually you wake up and find that you are being hung upside down in a chamber with nothing inside besides the chain that's hooked onto the celling which is dangling you by the legs above a pit of fire.")
                           response = input ("Would you like to [scream] for help or stay [quiet] and wait for someone to come find you?")
                           if response == 'scream':
                                print ("You were dropped into the pit of fire and you lost.. It turns out that the room is noise activated and any little sound will release the chain. 💀💀💀")
                           if response == 'quiet':
                                print ("You made the correct choice! The cyclops did in fact eventually come in. He gave you a long lecture you about social injustice and why it needs the be stopped.")
                                print ("You keep your eyes peeled for any possible escape methods while he is speaking to you. You look around to get a better glance of what's around you. You spot a lever in the far side of the room which is flicked downwards, which might be what's holding he chain in place. You remember that you still have your backpack with a pocket knife and a glock inside of it.")
                                print ("Eventually, the cyclops leaves the room and now you can start trying to escape.")
                                response = input ("Would you like to [squeeze] your hands through the chains hopefully grabbing the pocket-knife and glock out of your backpack or do [nothing] and just sit a wait.")
                                if response == 'nothing':
                                     print ("Well.. That's was a dumb choice. You just sit there helplessly. After a few hours, the chains release and you are released into the pit of fire. You were burned alive. 💀💀💀")
                                if response == 'squeeze':
                                     print ("You manage to successfully slip only one hand through the chains and you reach for the pocket-knife in your backpack.")
                                     response = input ("You grab the pocket-knife. What would you like to do next.. [throw] it at the lever or attempt at cutting the chains off.")
                                     if response == 'throw':
                                          print ("You hit the lever bulls-eye de-activating the chain mechanism. Then a clear floor appears beneath you and you are dropped safely onto it. Well.. somewhat safely, just with a few bruises and scars.")
                                          response = input ("Next to the lever, a door slides open. On the other side of it, you can see blue sky. Would you like to start [walking] towards it or [check] around for any additional traps.")
                                          if response == 'walking':
                                               print ("You walk towards the door but accidentally step on an active land mine. I bet you can guess what happens next.. you died 💀💀💀")
                                          if response == 'check':
                                               print ("You check your surroundings and spot a few landmines blended in with the floor. They are somewhat invisible.")
                                               print ("You manage to sneakily walk quietly around them and nice work.. you didn't get blown to pieces!")
                                               print ("As you get closer and closer to the exit, the blue sky starts to fade away and instead you are faced with a void of darkness.")
                                               print ("You fall asleep again.. but this time you see the problems of world hunger")
                                               print ("You see adults and even small children who look no older than seven lying hungry all across the streets of America. Some of them are alone.. without their mother or father. You realize how extremely lucky you are to not have to worry about these problems back at home and you make a promise to yourself to make a difference in society.")
                                               print ("Before your vision comes to an end, you start coming back to reality and in front of you, the door is no longer filled with darkness. You see your home.. back in San Francisco. Your wife.. your daughter. You are filled with tears as you take a step forward. All of a sudden you wake up in a cold sweat and you are safe and sound on your bed.")
                                               print ("You think of what you just saw and everyday from that point on, you strive to become a better man and do great things.")
                                               print ("You become a Social Justice activist and you are honored all across the world as a hero!")
                                               print ("Congratulations, you have finished the game-- IMPRISONMENT I.")
        if response == 'follow':
            print ("You follow the cyclops down a dark corridor leading to a hidden stairwell lit up with nothing but a hanging chandelier.")
            response = input ("He suddenly turns around and strikes you once with his fist. *HAR HAR HAR HAR*.. He laughs evily and you don't remember anything past that moment. When you wake up you are in a dark room, but you feel as if something's missing. You try to think about how you ended up here but you cannot remember. Your head aches and you suddenly remember that you no longer have your backpack. What would you like to do? [Look] around the cell or go back to [sleep].")
            if response == 'sleep':
                print ("Do something more productive, restart the game! You lost! 💀💀💀")
            if response == 'look':
                print ("You look around and see a metal toilet, the bunk bed you're currently cuffed to and a wooden stick lying on the ground. You also notice a set of keys outside of the cell which are just out of hands reach.")
                response = input ("Do you want to [grab] the stick on the floor?")
                if response == 'grab':
                    print ("You stuggle a bit to pick up the stick with one hand cuffed to the bunk bed. Eventually, you manage to kick it towards your direction and you get a hold of it.")
                    response = input ("Would you try and attempt to [pick] the lock on your handcuffs? If you fail, the stick will crack and the cyclops will be alerted by the sound.")
                    if response == 'pick':
                        print ("You successfully pick the lock and you are freed from the cuffs. You are not careful and the cuffs drop to the floor making a loud band. From the other corridor, the cyclops yells ***WHAT WAS THAT???***")
                        response = input ("Do you want to [respond] or [ignore] his question?")
                        if response == 'respond':
                            print ("You yell back 'Uh.. nothing. Don't worry about it.'")
                        if response == 'ignore':
                            print ("You hear footsteps approaching quickly and you only see two possible options.")
                            response = input ("Would you like to [hide] under the bunkbed or [recuff] yourself to the bunkbed pretending as if nothing happened at all.")
                        if response == 'hide':
                                    print ("You've managed to squeeze under the bunkbed as the footsteps become louder and closer to you.")
                                    print ("***WHAT??? IMPOSSIBLE, THE PUNY CREATURE DID NOT ESCAPE ME***")
                                    response = input ("The cyclops left the cell leaving the door wide open. Would you like to make a [dash] for it or [stay] in your cell afraid that he will catch you.")
                                    if response == 'dash':
                                            print ("You dash through the empty corridors and the sound of your footsteps echo loudly.")
                                            print ("All of a sudden, out of nowhere, the cyclops appears before you and grabs you by the collar of your shirt.")
                                            response = input ("***DO YOU UNDERSTAND WHY YOU ARE HERE IN THE FIRST PLACE?*** [yes] or [no]")
                                            if response == 'yes':
                                                 print ("Um.. yes, well... I have literally no clue.")
                                                 response = input ("***WELL, LET ME EXPLAIN SOME THINGS TO YOU. FIRST OF ALL, YOU ARE HERE BECAUSE OF SOCIAL CRIMES YOU HAVE COMMITTED. SECONDLY, BECAUSE.. I SAID SO!!! BACK IN THE CELL YOU GO*** You [go] back into the cell grudgingly..")
                                                 if response == 'go':
                                                    print ("You are now tossed back in the cell and this time, the cyclops melts the key in a cauldron of lava right in front of your very own eyes. There you are faced with many of the social crimes humanity has commited such as racism, sexism, and poverty. You are faced with endless flashbacks to when Black people were treated unfairly and the Chinese people were not allowed to immigrate to the United States. You also see the times when women were not allowed equal voting rights and weren't allowed to work. Finally, you see into the future and the streets all across America are littered with poverty.")
                                                    print ("The cyclops slaps you back into reality and you are lying on the ground terrified and absolutely scarred for life.")
                                                 response = input ("***NOW.. DO YOU SEE WHY I HAVE DECIDED TO CAPTURE YOU???*** [yes] or [no]")
                                                 if response == 'no':
                                                      print ("***AH.. THAT'S TOO BAD. LOOK'S LIKE REHABILITATION IS NOT POSSIBLE FOR EVERYONE AFTER ALL***")
                                                      print ("***YOU'LL MAKE A DECLIOUS TOE NAIL-FLESH SOUP FOR SUPPER TONIGHT!!")
                                                      print ("*HAR HAR HAR HAR HAR* ***YUMMY YUMMY IN MY TUMMY***, roars the cyclops as he marches out of the corridor.")
                                                      print ("You realize that you are screwed and fate does end up catching up with you. Long story short, you end up being toe nail-flesh soup.")
                                                      print ("You did in fact become a delicous soup-supper but you lost! 💀💀💀")
                                                      print ("***IF I RELEASE YOU BACK INTO THE WILDERNESS, DO YOU PROMISE TO TAKE EVERYTHING THAT YOU JUST SAW AND HELP CHANGE THE WORLD FOR THE GREATER GOOD?*** [yes] or [no]")
                                                      if response == 'no':
                                                           print ("Delicous toe-nail supper, coming right up! The cyclops has had enough with you and has ran out of patience. You became quite a delcious dinner for him. You were cooked alive! 💀💀💀")
                                                 if response == 'yes':
                                                      print ("***FANTASTIC, I'M GOING TO HAVE YOU STAY HERE FOR TWO MORE NIGHTS TO LET THAT SINK IN***")
                                                      response = input ("You have forty-eight hours to wait out. Would you like to [sleep] or [stay] awake?")
                                                      if response == 'stay':
                                                           print ("You try your best to stay away but eventually you start dozing off and you fall asleep.")
                                                           if response == 'sleep':
                                                                print ("You lie on the very uncomfortable bunk bed starring at the ceiling of your cell. You find yourself unable to fall asleep for the next few hours, but you eventually fall into the darkness abyss of sleep.")
                                                                response = input ("When you open your eyes in the morning, you feel a presence hovering over you. Would you like to [wake] up or [ignore] your senses and go back to sleep.")
                                                                if response == 'ignore':
                                                                     print ("Mr tough guy cyclops here doesn't like being ignored and you get slapped a few times and lose the game!! 💀💀💀")
                                                                if response == 'wake':
                                                                     print ("You are awaken by a shook and when you look up, you see the cyclops starring straight at you.")
                                                                     print ("***WAKE UP KID, IT'S BEEN TWO DAYS.. DO YOU WANT TO LEAVE OR NOT?")
                                                                     response = input ("You are completely shocked, confused as to how you managed to sleep 48 hours on the most uncomfortable bed you've ever slept on.. But you realize that all that doesn't matter right now. Would you like to [leave] or [stay]?")
                                                                     if response == 'stay':
                                                                          print ("Guess what buddy, I don't want you to stay. So I'm going to make you leave!")
                                                                          print ("The cyclops shows you the exit of the Social Justice Prison, but before letting you free. He decides to traumatize you once again.")
                                                                          print ("This time, you are sent back in time to the days of slavery during the 1800s. You see African Americans stripped of their rights and you can visually see the sweat and tears rolling and dripping down their faces as they are forced to work on huge plantations and farms. Worst of all, you see their masters trading them to other slave owners like they are just fruits and vegetables.")
                                                                          print ("You all of a sudden snap back into reality with sweat pouring down your face which is bright red.")
                                                                          print ("***THIS IS ALL PART OF THE REHABILITATION PROCESS, IT'S TOUGH, BUT YOU GOT TO PUSH THROUGH IT***")
                                                                          response = input ("***KID, ARE YOU READY TO GO BACK INTO THE REAL WORLD AND MAKE A DIFFERENCE?*** [yes] or welp.. [yes]")
                                                                          if response == 'yes':
                                                                             print ("You wake up in a cold sweat back home in your bedroom. All of it, everything seemed so real.. You think about all that just happened and went on.")
                                                                             print ("You go on to become a great social justice activist. You influenced the movement of civil rights and are praised for being a hero!")
                                                                             print ("Congratulations! You have completed IMPRISONMENT I!")
                                                                     if response == 'leave':
                                                                        print ("The cyclops shows you the exit of the Social Justice Prison, but before letting you free. He decides to traumatize you once again.")
                                                                        print ("This time, you are sent back in time to the days of slavery during the 1800s. You see African Americans stripped of their rights and you can visually see the sweat and tears rolling and dripping down their faces as they are forced to work on huge plantations and farms. Worst of all, you see their masters trading them to other slave owners like they are just fruits and vegetables.")
                                                                        print ("You all of a sudden snap back into reality with sweat pouring down your face which is bright red.")
                                                                        print ("***THIS IS ALL PART OF THE REHABILITATION PROCESS, IT'S TOUGH, BUT YOU GOT TO PUSH THROUGH IT***")
                                                                        response = input ("***KID, ARE YOU READY TO GO BACK INTO THE REAL WORLD AND MAKE A DIFFERENCE?*** [yes] or welp.. [yes]")
                                                                        if response == 'yes':
                                                                             print ("You wake up in a cold sweat back home in your bedroom. All of it, everything seemed so real.. You think about all that just happened and went on.")
                                                                             print ("You go on to become a great social justice activist. You influenced the movement of civil rights and are praised for being a hero!")
                                                                             print ("Congratulations! You have completed IMPRISONMENT I!")
   
                                                 if response == 'no':
                                                      print ("***AH.. THAT'S TOO BAD. LOOK'S LIKE REHABILITATION IS NOT POSSIBLE FOR EVERYONE AFTER ALL***")
                                                      print ("***YOU'LL MAKE A DECLIOUS TOE NAIL-FLESH SOUP FOR SUPPER TONIGHT!!")
                                                      print ("*HAR HAR HAR HAR HAR* ***YUMMY YUMMY IN MY TUMMY***, roars the cyclops as he marches out of the corridor.")
                                                      print ("You realize that you are screwed and fate does end up catching up with you. Long story short, you end up being toe nail-flesh soup.")
                                                      print ("You did in fact become a delicous soup-supper but you lost! 💀💀💀")