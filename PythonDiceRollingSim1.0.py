
def dicerollsim(dice_sides, dice_rolls):
    import random
    for x in range(dice_rolls):
        print(random.randint(1, dice_sides))


def userinput():
    global user_sides
    global user_rolls
    user_sides = int(
        input("How many sides should the dice you want to roll have?"))
    user_rolls = int(input("How many times should I roll that dice?"))

userinput()
dicerollsim(user_sides, user_rolls)


role_again = input("Do you want to role again?")
while role_again == "yes":
    same_values = input("Should I use the same values?")
    if same_values == "no":
        userinput()
    dicerollsim(user_sides, user_rolls)
    role_again = input("Do you want to role again?")
else:
    print("Have a great day.")
