import prompt


def welcome_user() -> str:
    return prompt.string("May I have your name? ")


def get_greater_common_divisor(n1: int, n2: int) -> int:
    if n1 == n2:
        return n1
    n1, n2 = min(n1, n2), max(n1, n2)
    while n1 != n2:
        n = n2 % n1
        if not n:
            return n1
        n1, n2 = min(n1, n), max(n1, n)
    return n1
