# Function example
import random

def my_func(param1 = 'default'):
    """_summary_
    Args:
        param (str, optional): _description_. Defaults to 'default'.
    """
    print("my first python function {}".format(param1))
    
my_func()


#Filter
mylist = [1,2,3,4,5,6,7,8]

def even_bool(num):
    return num%2 == 0

evens = filter(even_bool, mylist)
print(list(evens))

# Lambda Expression
print('---Lambda Exp---')
evens = filter(lambda num:num%2 == 0, mylist)
print(list(evens))

#Game ------

#GET GUESS
def get_guess():
    return list(input("What is your guess"))

#GENERATE COMPUTER CODE 123
def generate_code():
    digits = [str(num) for num in range(10)]
    
    #Shuffle the digits
    random.shuffle(digits)
    # Then grab the first three
    return digits[:3]

#GENERATE THE CLUES
def genetate_clues(code, user_guess):
    if user_guess == code:
        return "CODE CRACKED!"
    
    clues = []
    for ind, num in enumerate(user_guess):
        if num == code[ind]:
            clues.append("match")
        elif num in code:
            clues.append("Close")
    
    if clues == []:
        return ["Nope"]
    else:
        return clues
# RUN GAME LOGIC
print("Welcome Code Breaker")

secret_code = generate_code()
print(secret_code)
clue_report = []

while clue_report != "CODE CRACKED":
    guess = get_guess()
    
    clue_report = genetate_clues(guess, secret_code)
    print("here is the result of your guess: ")
    for clue in clue_report:
        print(clue)
#x = get_guess()
#print(x)