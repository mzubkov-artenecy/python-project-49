from random import randint

import prompt
from brain_games.scripts.games.config import TRIES_COUNT
from brain_games.scripts.games.functions import (
    answer_message,
    get_greater_common_divisor,
    welcome_user,
)


def main():
    print("Welcome to the Brain Games! (GCD)")
    name = welcome_user()
    print(f"Hello, {name}!")
    print("Find the greatest common divisor of given numbers.")
    correct_count: int = 0
    while correct_count < TRIES_COUNT:
        while True:
            num1, num2 = randint(3, 30), randint(2, 20)
            result = get_greater_common_divisor(num1, num2)
            if result > 1:
                break
        print(f"Question: {num1} {num2}")  # ({result})")
        answer = prompt.integer("Your answer: ", empty=True)
        answer_message(name, answer, result)
        if answer == result:
            correct_count += 1
        else:
            break
    if correct_count == TRIES_COUNT:
        print(f"Congratulation, {name}!")


if __name__ == "__main__":
    main()
