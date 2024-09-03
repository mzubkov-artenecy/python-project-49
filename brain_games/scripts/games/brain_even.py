from random import randint

import prompt
from brain_games.scripts.games.functions import answer_message, welcome_user


def main():
    print("Welcome to the Brain Games!")
    name = welcome_user()
    print(f"Hello, {name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')
    correct_count: int = 0
    answers: list = ["yes", "no"]
    while correct_count < 3:
        number: int = randint(1, 100)
        print("Question:", number)
        answer: str = prompt.string("Your answer: ", empty=True) or ""
        answer: str = answer.lower()
        result = answers[number % 2]
        # is_true = answer in answers and answer == result
        answer_message(name, answer, result)
        if answer == result:
            correct_count += 1
        else:
            break
    if correct_count == 3:
        print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
