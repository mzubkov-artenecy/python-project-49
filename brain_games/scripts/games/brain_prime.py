from random import randint

import prompt
from brain_games.scripts.games.config import TRIES_COUNT
from brain_games.scripts.games.functions import welcome_user, is_prime


def main():
    print("Welcome to the Brain Games! (Progression)")
    name = welcome_user()
    print(f"Hello, {name}!")
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    correct_count: int = 0
    while correct_count < TRIES_COUNT:
        prime_or_not = randint(0, 1)
        while True:
            number = randint(4, 100)
            is_number_prime = is_prime(number)
            if is_number_prime == prime_or_not:
                break
        result = "yes" if is_number_prime else "no"
        print(f"Question: {number} ({result})")
        answer: str = prompt.string("Your answer: ", empty=True) or ""
        answer = answer.lower()
        if answer == result:
            print("Correct!")
            correct_count += 1
        else:
            print(
                f"'{answer}' is wrong answer ;(.",
                f"Correct answer is '{result}'.",
            )
            print(f"Let's try again, {name}!")
            break
    if correct_count == TRIES_COUNT:
        print(f"Congratulation, {name}!")


if __name__ == "__main__":
    main()
