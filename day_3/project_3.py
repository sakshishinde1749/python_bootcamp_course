#treasure hunt game

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

print("welcome to the treasure Island\n\nYour mission is to find the treasure\n")

choice1 = input('You\'re at the crossroad, where do you want to go? Type "Right" or "Left"\n').lower()

if choice1 == "right": 
    choice2 = input('\nYou have come to a lake, there is an island in the middle of the lake,'
                    ' type "Wait" to wait for a boat, type "Swim" to swim across\n').lower()
        
    if choice2 == "wait":
        choice3 = input('\nYou have arrive at the island unharmed'
                        ' There is house with 3 doors. One red, one blue and one yellow.'
                        'Which one do you choose??\n').lower()
        
        if choice3 == "yellow":
            print("\nYou found the treasure. You Win!")
        elif choice3 == "blue":
            print("\nYou enter the room of beasts. Game Over!")
        elif choice3 == "red":
            print("\nIt\'s the room full of fire. Game Over!")
        else:
            print("\nYou chose the room that doesn\'t exists. Game Over!")

    else:
        print("\nYou got attacked by angry trout. Game over!")

else:
    print("\nYou fell in the hole. Game Over!")



