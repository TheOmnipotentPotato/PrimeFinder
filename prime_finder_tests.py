import prime_finder


def main() -> None:
    assert prime_finder.check_prime(7) == True
    assert prime_finder.check_prime(8) == False

    return None


if __name__ == "__main__":
    main()
