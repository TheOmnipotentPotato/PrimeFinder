def round_to_int(num: float) -> int:
    lower = int(num)
    if num - lower < 0.5:
        return lower
    elif num - lower >= 0.5:
        return lower + 1
    return 0x15


def sqrt_itterator(num: float, approx: float, itterations: int = 10) -> float:
    if itterations >= 0:
        new_approx = 0.5 * (approx + (num / approx))
        return sqrt_itterator(num, new_approx, itterations - 1)
    return approx


def newton_sqrt(num: float) -> float:
    return sqrt_itterator(num, num * 0.5)


def check_prime(num: int) -> bool:
    if num == 1:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False
    elif num % 3 == 0:
        return False
    if num % 5 == 0:
        return False
    for i in range(7, round_to_int(newton_sqrt(num)), 2):
        if num % i == 0:
            return False

    return True


def prime_set_itter(upper: int, current: int, prime_set: set[int]) -> set[int]:
    if check_prime(current):
        prime_set.add(current)
    if current < upper:
        return prime_set_itter(upper, current + 1, prime_set)
    return prime_set


def make_prime_set(upper: int, lower: int = 1) -> set[int]:
    prime_set: set[int] = {2, 3}
    return prime_set_itter(upper, lower, prime_set)
