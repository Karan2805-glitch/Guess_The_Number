import random
num=random.randint(1,100)
check=1
guesses=0
while(check):
        a=int(input("Guess any integer between 1 to 100:"))
        if(a==num):
            print("Yes ! you have guessed the correct number")
            check=0
            guesses+=1
        elif(a<num):
             print("No! You have to go higher")
             guesses+=1
        else:
              print("No! you a have to go lower")
              guesses+=1

print(f"You have guessed {num} number in {guesses} guesses.\n Congratulations ")