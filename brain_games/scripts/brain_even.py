from random import randint

import prompt


def welcome_user() -> str:
    return prompt.string("May I have your name? ")


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
        answer: str = prompt.string("Your answer: ")
        answer_low: str = answer.lower()
        if answer_low in answers and answers.index(answer_low) == number % 2:
            print("Correct!")
            correct_count += 1
        else:
            correct_answer = answers[number % 2]
            print(
                f"'{answer}' is wrong answer ;(.",
                f"Correct answer was '{correct_answer}'.)",
            )
            print(f"Let's tey again, {name}!")
            break
    if correct_count == 3:
        print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
