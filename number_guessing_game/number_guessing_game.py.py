import random
num=random.randint(1,100)
print("Number Guessing Game")
play_game=input("Do you want to play game? (y/n) : ")
if(play_game=='n'):
    print("End of program")
    exit()
else:
    while(play_game=='y'):
        # first time
        user_number=int(input("Guess a number between 1 to 100 : "))
        while(user_number>100 or user_number<1):
            user_number=int(input("Please enter a number between a vlid range 1 to 100 : "))
        attempt=1
        
        if(user_number>num):
            print("Guess is too high")
        elif(user_number<num):
            print("Guess is too low")
        #after first time
        while(user_number!=num):
            user_number=int(input("Guess again number between 1 to 100 : "))
            while(user_number>100 or user_number<1):
                user_number=int(input("Please enter a number between a vlid range 1 to 100 : "))
            attempt=attempt+1
            if(user_number>num):
                print("Guess is too high") 
            elif(user_number<num):
                print("Guess is too low")
             
        print("congratullations your guess is correct")
        print(f"you guessed correct number in {attempt} attempts ")
        play_game=input("Do you want to play again? (y/n) : ")