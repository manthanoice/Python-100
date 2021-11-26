import random as r

print('''
TBBT Gang Raise up!
Today we're gonna play
Rock, Paper, Scissors, Lizard, Spock!
Let's GO!!
''')

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
    `''        `\__   /
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
5 - Spock

Enter your choice: \n
'''))

s1 = "Scissors cuts Paper"
s2 = "Paper covers Rock"
s3 = "Rock crushes Lizard"
s4 = "Lizard poisons Spock"
s5 = "Spock smashes Scissors"
s6 = "Scissors decapitates Lizard"
s7 = "Lizard eats Paper"
s8 = "Paper disproves Spock"
s9 = "Spock vaporizes Rock"
s10 = "(and as it always has) Rock crushes Scissors"

sheldon = "*Evil Sheldon Voice*"

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
    print("You lost!!\n\n{} {}".format(s2, sheldon))

if your_choice == 1 and computer_choice == 3:
    print("Your choice is: \n{}".format(the_choices[your_choice-1]))
    print("Computers's choice is: \n{}".format(the_choices[computer_choice-1]))
    print("You Won!!\n\n{} {}".format(s10, sheldon))

if your_choice == 1 and computer_choice == 4:
    print("Your choice is: \n{}".format(the_choices[your_choice-1]))
    print("Computers's choice is: \n{}".format(the_choices[computer_choice-1]))
    print("You Won!!\n\n{} {}".format(s3, sheldon))

if your_choice == 1 and computer_choice == 5:
    print("Your choice is: \n{}".format(the_choices[your_choice-1]))
    print("Computers's choice is: \n{}".format(the_choices[computer_choice-1]))
    print("You lost!!\n\n{} {}".format(s9, sheldon))
    
if your_choice == 2 and computer_choice == 1:
    print("Your choice is: \n{}".format(the_choices[your_choice-1]))
    print("Computers's choice is: \n{}".format(the_choices[computer_choice-1]))
    print("You Won!!\n\n{} {}".format(s2, sheldon))

if your_choice == 2 and computer_choice == 3:
    print("Your choice is: \n{}".format(the_choices[your_choice-1]))
    print("Computers's choice is: \n{}".format(the_choices[computer_choice-1]))
    print("You Lost!!\n\n{} {}".format(s1, sheldon))

if your_choice == 2 and computer_choice == 4:
    print("Your choice is: \n{}".format(the_choices[your_choice-1]))
    print("Computers's choice is: \n{}".format(the_choices[computer_choice-1]))
    print("You Lost!!\n\n{} {}".format(s7, sheldon))

if your_choice == 2 and computer_choice == 5:
    print("Your choice is: \n{}".format(the_choices[your_choice-1]))
    print("Computers's choice is: \n{}".format(the_choices[computer_choice-1]))
    print("You Won!!\n\n{} {}".format(s8, sheldon))

if your_choice == 3 and computer_choice == 1:
    print("Your choice is: \n{}".format(the_choices[your_choice-1]))
    print("Computers's choice is: \n{}".format(the_choices[computer_choice-1]))
    print("You Lost!!\n\n{} {}".format(s10, sheldon))

if your_choice == 3 and computer_choice == 2:
    print("Your choice is: \n{}".format(the_choices[your_choice-1]))
    print("Computers's choice is: \n{}".format(the_choices[computer_choice-1]))
    print("You Won!!\n\n{} {}".format(s1, sheldon))

if your_choice == 3 and computer_choice == 4:
    print("Your choice is: \n{}".format(the_choices[your_choice-1]))
    print("Computers's choice is: \n{}".format(the_choices[computer_choice-1]))
    print("You Won!!\n\n{} {}".format(s6, sheldon))

if your_choice == 3 and computer_choice == 5:
    print("Your choice is: \n{}".format(the_choices[your_choice-1]))
    print("Computers's choice is: \n{}".format(the_choices[computer_choice-1]))
    print("You Lost!!\n\n{} {}".format(s5, sheldon))

if your_choice == 4 and computer_choice == 1:
    print("Your choice is: \n{}".format(the_choices[your_choice-1]))
    print("Computers's choice is: \n{}".format(the_choices[computer_choice-1]))
    print("You Lost!!\n\n{} {}".format(s3, sheldon))

if your_choice == 4 and computer_choice == 2:
    print("Your choice is: \n{}".format(the_choices[your_choice-1]))
    print("Computers's choice is: \n{}".format(the_choices[computer_choice-1]))
    print("You Won!!\n\n{} {}".format(s7, sheldon))

if your_choice == 4 and computer_choice == 3:
    print("Your choice is: \n{}".format(the_choices[your_choice-1]))
    print("Computers's choice is: \n{}".format(the_choices[computer_choice-1]))
    print("You Lost!!\n\n{} {}".format(s6, sheldon))

if your_choice == 4 and computer_choice == 5:
    print("Your choice is: \n{}".format(the_choices[your_choice-1]))
    print("Computers's choice is: \n{}".format(the_choices[computer_choice-1]))
    print("You Won!!\n\n{} {}".format(s4, sheldon))

if your_choice == 5 and computer_choice == 1:
    print("Your choice is: \n{}".format(the_choices[your_choice-1]))
    print("Computers's choice is: \n{}".format(the_choices[computer_choice-1]))
    print("You Won!!\n\n{} {}".format(s9, sheldon))

if your_choice == 5 and computer_choice == 2:
    print("Your choice is: \n{}".format(the_choices[your_choice-1]))
    print("Computers's choice is: \n{}".format(the_choices[computer_choice-1]))
    print("You Lost!!\n\n{} {}".format(s8, sheldon))

if your_choice == 5 and computer_choice == 3:
    print("Your choice is: \n{}".format(the_choices[your_choice-1]))
    print("Computers's choice is: \n{}".format(the_choices[computer_choice-1]))
    print("You Lost!!\n\n{} {}".format(s5, sheldon))

if your_choice == 5 and computer_choice == 4:
    print("Your choice is: \n{}".format(the_choices[your_choice-1]))
    print("Computers's choice is: \n{}".format(the_choices[computer_choice-1]))
    print("You Lost!!\n\n{} {}".format(s4, sheldon))


print("\n\nThanks for playing amigos!")