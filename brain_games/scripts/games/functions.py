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


def is_prime(value: int) -> int:
    if abs(value) < 4:
        return True
    for i in range(2, abs(value) // 2 + 1):
        if not value % i:
            return False
    return True
