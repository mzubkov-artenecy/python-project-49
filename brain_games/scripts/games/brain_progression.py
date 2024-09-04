from random import randint

import prompt
from brain_games.scripts.games.config import TRIES_COUNT
from brain_games.scripts.games.functions import answer_message, welcome_user


def main():
    print("Welcome to the Brain Games! (Progression)")
    name = welcome_user()
    print(f"Hello, {name}!")
    print("What number is missing in the progression?")
    correct_count: int = 0
    while correct_count < TRIES_COUNT:
        arr: list = [0] * randint(5, 15)
        arr[0] = randint(1, 10)
        step = randint(1, 5)
        arr = [arr[0] + step * x for x in range(0, len(arr))]
        idx = randint(1, len(arr)) - 1
        result = arr[idx]
        print("Question: ", end="")
        print(*arr[:idx], "..", *arr[idx + 1:])  # fmt:skip
        answer = prompt.integer("Your answer: ", empty=True)
        answer_message(name, answer, result)
        if answer == result:
            correct_count += 1
        else:
            break
    if correct_count == TRIES_COUNT:
        print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
