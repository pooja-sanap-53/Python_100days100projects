# Day 03
# Date: 17 Nov 2021
# Treasure Hunting


'''
Instructions
Make your own "Choose Your Own Adventure" game. Use conditionals such as if, else, and elif statements to lay out the logic and the story's path in your program.



🧞‍♂️ 🐊 🧙‍♂️ 🧟 🧚‍♂️ 🧝‍♂️ 🥷 🤖 👽 🙀

That said if you'd like to continue with my example, feel free to use the text snippets below...

Text Snippets from my example
'You\'re at a crossroad. Where do you want to go? Type "left" or "right"'
'You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.'
"You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?"
"It's a room full of fire. Game Over."
"You found the treasure! You Win!"
"You enter a room of beasts. Game Over."
"You chose a door that doesn't exist. Game Over."
"You get attacked by an angry trout. Game Over."
"You fell into a hole. Game Over."
'''

print("Welcome to the treasure Hunting!!!\n Hope this journey becomes super adventurous journey and you find the TREASURE!")

print("Your are in a Maze. \nWhere do you want to go now?\nPress 'L' for going left\nPress 'R' for going right")
maze = input()

if maze =='L':
    print("You have choosen left.")
    print('''Oh, wait..
Can you see that! 
It\'s a Lake!!

What would you like to do now?
Press 'B' to wait for a boat 
Press 'S' to swim across ''')

    lake= input()
    if lake == 'B':
        print('''You have choosen to wait for a boat.
So, let\'s wait until a boat arrives.
Waiting..
Still waiting..
Oh! Look a boat has arrived. Let's take a ride.

Travelling through boat...
''')
    elif lake == 'S':
        print('''Great choice!!
Let\'s start swimming then!
        ''')
    else:
        print("Invalid input.")

    print("Looks like we have reached an island!\nThere is a building over there which has three doors of three different colours.\nWhich one do you choose?\nPress 'G' gor Green door\nPress 'Y' for Yellow door \nPress 'O' for Orange door")
    island_door = input()
    if island_door =='G':
        print("You have choosen Green door.\n Alas! It is full of fire!\n OMG!! RUN !\n You did not escape. \n GAME OVER!!")
    elif island_door == 'Y':
        print("You have choosen Yellow door.\n Alas! It is full of beasts!\n OMG!! RUN !\n You did not escape. \n GAME OVER!!")
    elif island_door == 'O':
        print("You have choosen Orange door.\n Congrats, it\'s full of treasure.\n You won!! ")
    else:
        print("Invalid input")


elif maze =='R':
    print("You have choosen right.")
    print('''Oh, wait..
Can you see that! 
It\'s a Big Mountain!!

What would you like to do now?
Press 'C' to climb the mountain
Press 'P' to go in plains ''')

    lake= input()
    if lake == 'C':
        print('''You have choosen to climb the mountain.
So, let\'s start climbing the mountain.

''')
    elif lake == 'P':
        print('''Great choice!!
Let\'s start walking then!
        ''')
    else:
        print("Invalid input.")

    print("Looks like we have reached an Forest!\nThere is a building over there which has three doors of three different colours.\nWhich one do you choose?\nPress 'G' gor Green door\nPress 'Y' for Yellow door \nPress 'O' for Orange door")
    forest_door = input()
    if forest_door =='G':
        print("You have choosen Green door.\n Alas! It is full of fire!\n OMG!! RUN !\n You did not escape. \n GAME OVER!!")
    elif forest_door == 'Y':
        print("You have choosen Yellow door.\n Alas! It is full of beasts!\n OMG!! RUN !\n You did not escape. \n GAME OVER!!")
    elif forest_door == 'O':
        print("You have choosen Orange door.\n Congrats, it\'s full of treasure.\n You won!! ")
    else:
        print("Invalid input")


else:
    print("Invalid input.")
