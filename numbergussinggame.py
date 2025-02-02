from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(user_guess, actual_answer):
    if user_guess > actual_answer:
        print("too high")
        return - 1

    elif user_guess < actual_answer:
        print("too low")
        return - 1

    else:
        print("you guess it right 'WELLDONE' ")



def set_difficulty():
    level = input("what is the difficulty level you want: 'easy' or 'hard' ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():


    print("welcome to the number guessing game!")
    print("Think a number between 1 to 100")
    answer = randint(1, 100)

    print(f"psst, the right answer is {answer}")


    turns = set_difficulty()
    guess = 0
    
    while guess != answer:
        print(f"you have {turns} attempt remmaning to guess the number")

        guess = int(input(" make a guess?: "))
        check_answer(guess, answer,)
        if turns == 0:
            print("you run out of chances 'you loose' ")
            return
        elif guess != answer:
            print("guess again")

game()



