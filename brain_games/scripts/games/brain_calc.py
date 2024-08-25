import enum
from random import randint

import prompt

from brain_games.scripts.games.config import TRIES_COUNT
from brain_games.scripts.games.functions import welcome_user


OPER_SIGN: list = ["+", "-", "*"]


class Oper(enum.IntEnum):
    Add = 0
    Sub = 1
    Mul = 2


def main():
    print("Welcome to the Brain Games! (CALC)")
    name = welcome_user()
    print(f"Hello, {name}!")
    print("What is the result of the expression?")
    correct_count: int = 0
    while correct_count < TRIES_COUNT:
        oper = randint(Oper.Add, Oper.Mul)
        if oper == Oper.Add:
            num1 = randint(0, 50)
            num2 = randint(0, 50)
            result = num1 + num2
        elif oper == Oper.Sub:
            result = randint(0, 50)
            num1 = randint(result, result + 50)
            num2 = num1 - result
        else:
            num1 = randint(1, 10)
            num2 = randint(1, 20)
            result = num1 * num2
        print(f"Question: {num1} {OPER_SIGN[oper]} {num2}")
        answer = prompt.integer("Your answer: ")
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
