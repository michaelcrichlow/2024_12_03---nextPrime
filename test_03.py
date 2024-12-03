def is_prime(n: int) -> bool:
    if n == 1:
        return False
    for val in range(2, n // 2 + 1):
        if n % val == 0:
            return False

    return True


def nextPrime(n: int) -> int:
    res = n + 1
    while is_prime(res) == False:
        res += 1

    return res


def main() -> None:
    print(nextPrime(3))
    print(nextPrime(12))
    print(nextPrime(8))


if __name__ == '__main__':
    main()

# nextPrime(3) => 5
