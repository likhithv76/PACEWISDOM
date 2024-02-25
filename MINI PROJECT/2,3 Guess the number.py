import random

print("""Let's play a guess the number game! 
choose among these options:
1. I will guess the number,
2. I need computer to guess the number.
       """)
choose = int(input("Enter either 1 or 2:"))

if choose == 1:
    x = int(input("Enter the range of Guess: "))
    random_number = random.randint(1,x)
    guess = 0

    while guess != random_number:
        guess = int(input("Enter the guess: "))
        if guess <= random_number:
            print("Your guess is lower!")
        elif guess >= random_number:
            print("Your guess is higher!")
    print(f"You got the right answer ;), the guessed number is {random_number}")

elif choose == 2:
    y = int(input("Enter the range of guess: "))
    low = 1
    high = y
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low 
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'Yay! The computer guessed your number, {guess}, correctly!')
else:
    print("Invalid Option")




