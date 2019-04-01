import random

# GET GUESS
def get_guess():
    return list(input ("What is your guess?"))

# GET GENERATE COMPUTER CODE
def generate_code():
    digits = [str(num) for num in range(10)]

    # shuffle the digits
    random.shuffle(digits)

    # then grab the first three
    return digits[:3]

# GENERATE THE CLUES

def generate_clues(code,user_guess):

    if user_guess == code:
        return "CODE CRACKED !"

    clues = []

    count = 0

    for ind,num in enumerate(user_guess):
        if num == code[ind]:
            clues.append("match")
        elif num in code:
            clues.append("Close")

    if clues == []:
        return ["Nope"]
    else:
        return clues

# RUN GAME LOGIC

print("Welcome Code Breaker !!!")

secret_code = generate_code()

clue_report = []

while clue_report != "CODE CRACKED !":

    guess = get_guess()

    clue_report = generate_clues(guess,secret_code)

    print("Here is the result of your guess: ")

    for clue in clue_report:
        print(clue)
