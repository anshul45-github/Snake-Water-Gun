import random

'''
1 for snake
-1 for water
0 for gun
'''

computer = random.choice([1, -1, 0])  # Randomly choose between snake, water, and gun
youstr = input("Enter your choice (snake/water/gun): ").lower()
youDict = {"snake": 1, "water": -1, "gun": 0}
reverseDict = {1: "snake", -1: "water", 0: "gun"}

you = youDict.get(youstr, None)

print(f"You chose: {youstr}\nComputer chose: {reverseDict[computer]}")

if computer == -1 and you == 1:
    print("You win! Snake drinks water.")
elif computer == 1 and you == -1:
    print("You lose! Snake drinks water.")
elif computer == 0 and you == 1:
    print("You lose! Gun shoots snake.")
elif computer == 1 and you == 0:
    print("You win! Gun shoots snake.")
elif computer == -1 and you == 0:
    print("You lose! Water douses gun.")
elif computer == 0 and you == -1:
    print("You win! Water douses gun.")
elif computer == you:
    print("It's a tie! Both chose the same.")
elif you is None:
    print("Invalid input! Please enter snake, water, or gun.")
else:
    print("Unexpected error occurred.")