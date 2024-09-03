import prompt


def welcome_user() -> str:
    return prompt.string("May I have your name? ")


def get_greater_common_divisor(number1: int, number2: int) -> int:
    if number1 == number2:
        return number1
    number1, number2 = min(number1, number2), max(number1, number2)
    while number1 != number2:
        n = number2 % number1
        if not n:
            return number1
        number1, number2 = min(number1, n), max(number1, n)
    return number1


def is_prime(value: int) -> int:
    if abs(value) < 4:
        return True
    for i in range(2, abs(value) // 2 + 1):
        if not value % i:
            return False
    return True


def answer_message(name, is_true, answer, result) -> str:
    if is_true:
        print("Correct!")
    else:
        print(
            f"'{answer}' is wrong answer ;(.",
            f"Correct answer is '{result}'.",
        )
        print(f"Let's try again, {name}!")
