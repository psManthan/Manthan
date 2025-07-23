import random
print("Welcome to the gussing number game ")
low =int(input("Enter the lower bound of the game "))
high =int(input("Enter the upper bound of the game"))
print("You have 10 chances of gussing the number between the {low} and {high}")
number = random.randint(low, high)
ch =10
guess = 0
while guess <ch :
    guess +=1
    guess =int(input("Enter your guess :\t"))
    if guess == number :
        print("Congragulation u have gussed")
        break
    elif guess <number :
        print("Your guess is low")
        
    elif guess >number :
        print("YOur guess is high")

    elif guess <number :
        print("tooo low ! try higher number")    