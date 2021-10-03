"""
Instruction:
https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload
"""

print('Welcome to Treasure Island\nYour mission is to find the treasure')
road = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()


if road == 'left':
    do = input("""You come to a lake. There is an island in the middle of the lake. 
    Type 'wait', to wait for a boot. type 'swim' to swim across """).lower()
    if do == 'wait':
        colour = input("""You arrive at the island unharmed. There is a house with 3 doors.
        One red, one yellow and one blue. Which colour do you choose?""").lower()

        if colour == 'yellow':
            print('You WIN!')
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
            /______/______/______/______/______/______/______/______/______/______/_____ /
            *******************************************************************************
            ''')
        elif colour == 'blue':
            print('Attacked by trout. GAME OVER')
        elif colour == 'red':
            print('Burned by fire. GAME OVER')
        else:
            print('GAME OVER')
    else:
        print('Attacked by trout. GAME OVER')
else:
    print('Fall into a hole. GAME OVER')