import random
target, tries = random.randint(1,100), 0
print("===This is a NUMBER guessing Game ====\n --- The number is within 0 to 100 ---")
while True:
    guess = int(input("Enter your guess:"))
    tries +=1

    if guess == target:
        print(f"the number is {target}, you got it in {tries} tries!")
        break
    elif guess > target:
        print("your guess is too higher")
    else:
        print("your guess is too lower")