# Scissors cuts Paper
# Paper covers Rock
# Rock crushes Lizard
# Lizard poisons Spock
# Spock smashes Scissors
# Scissors decapitates Lizard
# Lizard eats Paper
# Paper disproves Spock
# Spock vaporizes Rock
# (and as it always has) Rock crushes Scissors

import random as r

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

lizard = '''
                       )/_
             _.--..---"-,--c_
        \L..'           ._O__)_
,-.     _.+  _  \..--( /         
  `\.-''__.-' \ (     \_      
    `''        `\__   /\
                ')
'''

spock = '''
                     .......................... 
                 ................................... 
              ......................................... 
            ............................................. 
           ................................................ 
          .................................................. 
         .................................................... 
         ......;%;%%%%%%%%%%%%%%%%%%%%%%%%%%%;%%.............. 
         .....;%%%;;;;%%%%%%%%%%%%%%%%%%;;;;%%%%..............% 
         .....%%%%%%%%;;;%%%%%%%%%%%%;;;%%%%%%%%%............%%% 
         /....%%%%%%%%%%%%;%%%%%%%%;%%%%%%%%%%%%%%..........;%%% 
         //...%%%a@@`  '@%%//%%%%%%%%@`  '@@a%%%%%%........;%/%% 
         //...%@@@@@aaa@@@%//%%%%%%@@@@aaa@@@@@%%%%%......%%/%% 
         //...%%%%%%%%%%%%%//%%%%%%%%%%%%%%%%%%%%%%%%....%%/%%% 
          //..%%%%%%%%%%%%//%%%%%%%%%%%%%%%%%%%%%%%%%...%%/%%% 
           //.%%%%%%%%%%%%//%%%%%%%%%%%%%%%%%%%%%%%%%..%%/%%% 
            //%%%%%%%%%%%//%%%%%%%%%%%%%%%%%%%%%%%%%%..%/%%% 
             ;%%%%%%%%%%%//%%%%%%%%%;/%%%%%%%%%%%%%%%.%%% 
               %%%%%%%%%//%%%%%%%%%%%;/%%%%%%%%%%%%%%%% 
                %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%/ 
                 ;%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%// 
                   %%%%%<<<<<<<<<<<<<<<<<%%%%%%%%%%;// 
                    %%%%%<<<<<<<<<<<<<<<%%%%%%%%%%;/// 
                     %%%%%%%%%%%%%%%%%%%%%%%%%%%;///// 
                      %%%%%%%%%%%%%%%%%%%%%%%%;///////. 
                      /;%%%%%%%%%%%%%%%%%%%;////////.... 
                      ///;%%%%%%%%%%%%%%;////////......... 
                    ...///////////////////////.............. 
                  ........////////////////................,;;, 
               ,;............/////////.................,;;;;;;;;, 
           ,;;;;;;,................................,;;;;;;;;;;;;;;, 
       ,;;;;;;;;;;;;;,........................,;;;;;;;;;;;;;;;;;;;; 
   ,;;;;;;;;;;;;;;;;;;;;;,................,;;;;;;;;;;;;;;;;;;;;;;;; 
 ,;;;;;;;;;;;;;;;;;;;;;;;;;;,.........,;;;;;;;;;;;;;;;;;;;;;;;;;;;; 
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;/#\;;;;;;;;;;; 
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;/####\;;;;;;;;; 
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;/#######\;;;;;;;
'''

your_choice = int(input('''
Select your choice from options below!
1 - Rock
2 - Paper
3 - Scissors
4 - Lizard
5 - Spock\n
'''))

computer_choice = r.randint(1, 5)

print("\nComputer chose {} ".format(computer_choice))

the_choices = [rock, paper, scissors, lizard, spock]

if your_choice == computer_choice:
    print("It's a draw")
    print(the_choices[your_choice-1])
    print(the_choices[computer_choice-1])

if your_choice == 1 and computer_choice == 2:
    print("Your choice is: \n{}".format(the_choices[your_choice-1]))
    print("Computers's choice is: \n{}".format(the_choices[computer_choice-1]))
    print("You lost!!\n\nPaper covers Rock! *Evil sheldon voice*")

if your_choice == 1 and computer_choice == 3:
    print("Your choice is: \n{}".format(the_choices[your_choice-1]))
    print("Computers's choice is: \n{}".format(the_choices[computer_choice-1]))
    print("You Won!!\n\n(and as it always has) Rock crushes Scissors *Evil sheldon voice*")

if your_choice == 1 and computer_choice == 4:
    print("Your choice is: \n{}".format(the_choices[your_choice-1]))
    print("Computers's choice is: \n{}".format(the_choices[computer_choice-1]))
    print("You Won!!\n\nRock crushes Lizard *Evil sheldon voice*")

if your_choice == 1 and computer_choice == 5:
    print("Your choice is: \n{}".format(the_choices[your_choice-1]))
    print("Computers's choice is: \n{}".format(the_choices[computer_choice-1]))
    print("You lost!!\n\nSpock vaporizes Rock! *Evil sheldon voice*")
    
if your_choice == 2 and computer_choice == 1:
    print("Your choice is: \n{}".format(the_choices[your_choice-1]))
    print("Computers's choice is: \n{}".format(the_choices[computer_choice-1]))
    print("You Won!!\n\nPaper covers Rock! *Evil sheldon voice*")

if your_choice == 2 and computer_choice == 3:
    print("Your choice is: \n{}".format(the_choices[your_choice-1]))
    print("Computers's choice is: \n{}".format(the_choices[computer_choice-1]))
    print("You Lost!!\n\nScissors cuts Paper! *Evil sheldon voice*")

if your_choice == 2 and computer_choice == 4:
    print("Your choice is: \n{}".format(the_choices[your_choice-1]))
    print("Computers's choice is: \n{}".format(the_choices[computer_choice-1]))
    print("You Lost!!\n\nLizard eats Paper! *Evil sheldon voice*")

if your_choice == 2 and computer_choice == 5:
    print("Your choice is: \n{}".format(the_choices[your_choice-1]))
    print("Computers's choice is: \n{}".format(the_choices[computer_choice-1]))
    print("You Won!!\n\nPaper disproves Spock! *Evil sheldon voice*")

if your_choice == 3 and computer_choice == 1:
    print("Your choice is: \n{}".format(the_choices[your_choice-1]))
    print("Computers's choice is: \n{}".format(the_choices[computer_choice-1]))
    print("You Lost!!\n\n(and as it always has) Rock crushes Scissors *Evil sheldon voice*")

if your_choice == 3 and computer_choice == 2:
    print("Your choice is: \n{}".format(the_choices[your_choice-1]))
    print("Computers's choice is: \n{}".format(the_choices[computer_choice-1]))
    print("You Won!!\n\nScissors cuts Paper *Evil sheldon voice*")

if your_choice == 3 and computer_choice == 4:
    print("Your choice is: \n{}".format(the_choices[your_choice-1]))
    print("Computers's choice is: \n{}".format(the_choices[computer_choice-1]))
    print("You Won!!\n\nScissors decapitates Lizard *Evil sheldon voice*")

if your_choice == 3 and computer_choice == 5:
    print("Your choice is: \n{}".format(the_choices[your_choice-1]))
    print("Computers's choice is: \n{}".format(the_choices[computer_choice-1]))
    print("You Lost!!\n\nSpock smashes Scissors *Evil sheldon voice*")

if your_choice == 4 and computer_choice == 1:
    print("Your choice is: \n{}".format(the_choices[your_choice-1]))
    print("Computers's choice is: \n{}".format(the_choices[computer_choice-1]))
    print("You Lost!!\n\Rock crushes Lizard *Evil sheldon voice*")

if your_choice == 4 and computer_choice == 2:
    print("Your choice is: \n{}".format(the_choices[your_choice-1]))
    print("Computers's choice is: \n{}".format(the_choices[computer_choice-1]))
    print("You Won!!\n\Lizard eats Paper *Evil sheldon voice*")

if your_choice == 4 and computer_choice == 3:
    print("Your choice is: \n{}".format(the_choices[your_choice-1]))
    print("Computers's choice is: \n{}".format(the_choices[computer_choice-1]))
    print("You Lost!!\n\Scissors decapitates Lizard *Evil sheldon voice*")

if your_choice == 4 and computer_choice == 1:
    print("Your choice is: \n{}".format(the_choices[your_choice-1]))
    print("Computers's choice is: \n{}".format(the_choices[computer_choice-1]))
    print("You Lost!!\n\Rock crushes Lizard *Evil sheldon voice*")