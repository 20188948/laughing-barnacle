restart = True
found_endings = set()
endings = 0
while restart == True:
    print("You are Alex Carter, a curious teen who discorvers a strange silver key buried in")
    print("the woods near the town of Ravenshirt. A message is scrated into its surface:")
    print("'Only those who seek the truth may unlock it'")
    print("That night, you dream of a hidden foor and a voice wispering:")
    print("“The key must be used before the full moon.”")
    print("Tonight is the full moon.")
    print("You pack a flashlight and head out.")
    print("After 20 minutes of walking, you reach a fork in the path.")
    print("Left — toward the abandoned Ravenshire Manor")
    print("Right — toward the old stone bridge by the river")
    scene1=input("Would you like to go Left or Right?(enter left or right)")
    if scene1=='left':
        print("The manor is silent and cold. In the main hall you find:")
        print("A locked basement door and A dusty library")
        fork1=input("which would you like to enter?(Enter basement or libary)")
        if fork1=='basement':
            print("The key fits. You enter a room glowing with symbols and a stone pedestal.")
            print("On it rests a crystal orb.")
            ending1=input("Do you touch it or leave it alone(Enter touch or leave)")
            if ending1=='touch':
                print("The orb flashes — your body fills with power.")
                print("You become the new guardian of ancient magic.")
                print("Ravenshire will never be the same again.")
                print("You have found an ending")
                if 'basement_touch' in found_endings:
                    print("Already found ending")
                else:
                    endings = endings + 1
                    found_endings.add('basement_touch')
                restart=input("Do you wish to play again?(Enter yes or no)")
                if restart == 'no':
                    restart = False
                else:
                    restart = True
                

            else:
                print("A whisper says, “Truth ignored is truth erased.”")
                print("You turn to leave… and vanish.")
                print("You were never seen again — not even remembered.")
                print("You have found an ending")
                if 'basement_leave' in found_endings:
                    print("Already found ending")
                else:
                    endings = endings + 1
                    found_endings.add('basement_leave')
                restart=input("Do you wish to play again?(Enter yes or no)")
                if restart == 'no':
                    restart = False
                else:
                    restart = True

    
        else:
            print("You discover a hidden cupboard. Inside is a leather journal describing the key.")
            print("The last page reads:")
            print("“The curse ends only when the cursed one remembers.”")
            print("Suddenly you hear footsteps.")
            ending2 = input("Do you hide and listen or Confront the footsteps(Enter hide or confront)")
            if ending2 == 'hide':
                print("You overhear that you were cursed at birth to forget who you were.")
                print("By learning the truth, the curse lifts — you remember your real family.")
                print("You leave Ravenshire to start a new life.")
                print("You have found an ending")
                if 'library_hide' in found_endings:
                    print("Already found ending")
                else:
                    endings = endings + 1
                    found_endings.add('library_hide')
                restart=input("Do you wish to play again?(Enter yes or no)")
                if restart == 'no':
                    restart = False
                else:
                    restart = True
            else:
                print("A shadowy man attacks and steals the key.")
                print("You survive, but spend your life trying to get it back.")
                print("The mystery becomes an obsession that never ends.")
                print("You have found an ending")
                if 'library_confront' in found_endings:
                    print("Already found ending")
                else:
                    endings = endings + 1
                    found_endings.add('library_confront')
                restart=input("Do you wish to play again?(Enter yes or no)")
                if restart == 'no':
                    restart = False
                else:
                    restart = True



    else:
        print("The river glows with moonlight. Under the bridge you see:")
        print("A wooden chest")
        print("A ladder going down to a tunnel")
        fork2=input("what do you do?(Enter chest or ladder)")
        if fork2=='chest':
            print("The key unlocks the chest. Inside is an old music box, already winding itself.")
            ending3=input("Do you Let the music play or Smash the music box(Enter smash or play)")
            if ending3=='play':
                print("The music plays — memories flood back of a happy childhood.")
                print("You realize the key belonged to your parents, lost long ago.")
                print("You find them again, and the family is reunited.")
                print("You have found an ending")
                if 'chest_play' in found_endings:
                    print("Already found ending")
                else:
                    endings = endings + 1
                    found_endings.add('chest_play')
                restart=input("Do you wish to play again?(Enter yes or no)")
                if restart == 'no':
                    restart = False
                else:
                    restart = True
            else:
                print("When you smash the music box, black mist pours out.")
                print("The river turns dark and the forest rots.")
                print("The curse spreads, and you become its unwilling guardian.")
                print("You have found an ending")
                if 'chest_smash' in found_endings:
                    print("Already found ending")
                else:
                    endings = endings + 1
                    found_endings.add('chest_smash')
                restart=input("Do you wish to play again?(Enter yes or no)")
                if restart == 'no':
                    restart = False
                else:
                    restart = True
        else:
            print("The tunnel leads to an underground lake. At the center is an ancient door.")
            print("You put the key in. It unlocks.")
            print("Inside is a glowing portal.")
            print("You step though")
            print("You enter a peaceful kingdom beyond Earth.")
            print("You are welcomed as the Seeker of Truth.")
            print("You never return home — and never wish to")
            print("You have found an ending")
            if 'tunnel_portal' in found_endings:
                print("Already found ending")
            else:
                endings = endings + 1
                found_endings.add('tunnel_portal')
            restart=input("Do you wish to play again?(Enter yes or no)")
            if restart == 'no':
                restart = False
            else:
                restart = True
    print("You have found",endings,"ending")