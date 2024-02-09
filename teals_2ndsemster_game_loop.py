#import random module
import random

print('The Loop Game: Rock Paper Scissors:\n')
print("Rock vs Paper then Paper wins \n")
print ("Rock vs Scissors then Rock wins \n")
print( "Paper vs Scissors then Scissor wins \n")
 
 #the above print statement you can even concatenate the strings and write it as one print statement 

#The while statement simply loops until a condition is False.
while True:
     
    print("Enter one choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")
    players_choice=int(input("Enter one choice :"))
     
    # loop will go on, until user enters an invalid input
    while players_choice > 3 or players_choice <1:
      players_choice=int(input('Enter a valid number please '))
         
    if players_choice == 1:
        choice_name= 'Rock'
    elif players_choice == 2:
        choice_name= 'Paper'
    else:
        choice_name= 'Scissors'
         
    print('The players choice is \n',choice_name)
    print('Computers choice :')
  
  #players choice vs computer's random choice
     
    computer_choice = random.randint(1,3)
     #it will pick up a random number between 1,3
    while computer_choice == players_choice:
        computer_choice = random.randint(1,3)
         
    if computer_choice == 1:
        computer_choice_name = 'rocK'
    #elif stands for 'else if' and is used in Python it is used to test multiple conditions. 
    elif computer_choice == 2:
        computer_choice_name = 'paper'
    else:
        computer_choice_name = 'scissor'
    print("Computer choice is \n", computer_choice_name)
    print(choice_name,'Vs',computer_choice_name)
    # draw 
    if players_choice == computer_choice:
        print('Its a Draw',end="")
        result="DRAW"
    # winning condition      
    if (players_choice==1 and computer_choice==2):
        print('paper wins ',end="")
        result='paper'
    elif (players_choice==2 and computer_choice==1):
        print('paper wins ',end="")
        result='paper'
         
    if (players_choice==1 and computer_choice==3):
        print('Rock wins \n',end= "")
        result='Rock'
    elif (players_choice==3 and computer_choice==1):
        print('Rock wins \n',end= "")
        result='rocK'
         
    if (players_choice==2 and computer_choice==3):
        print('Scissors wins ',end="")
        result='scissoR'
    elif (players_choice==3 and computer_choice==2):
        print('Scissors wins ',end="")
        result='Rock'
    if result == 'DRAW':
        print(" TIE ")
    if result == choice_name:
        print("Player wins")
    else:
        print("Wohoo!!! Computer wins!")
    print("Do you want to play again? (Y/N)")
    # strip () is used to remove leading (spaces at the start) and trailing (spaces at the end) whitespace from a string
    out = input().lower().strip()
    #lower converts each uppercase character to lowercase.no uppercase characters in string then it returns the original str
    if out == 'n':
        break
# break: allows you to exit a loop when an external condition is met. Break - controls the script. 
print("Thanks for playing")
