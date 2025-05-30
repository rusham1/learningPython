import random
print("Guessing Game")
print("You get 3 attempts to guess the number between 1 and 10")
n=random.randint(1, 10)
for i in range(3):
    num=int(input("Enter your guess: "))
    if num==n:
        print("You guessed it right!")
    elif num<n:
        print("Your guess is too low")
    elif num>n:
        print("Your guess is too high")  

print("The number was", n) 
    