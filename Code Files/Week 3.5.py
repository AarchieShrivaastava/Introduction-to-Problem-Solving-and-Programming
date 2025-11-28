def prime_factors(n):
    """
    Return the list of prime factors of n.
    Example: 36 -> [2, 2, 3, 3]
    """
    factors = []
    if n == 0 or n == 1 or n == -1:
        return factors

    # work with positive value, keep sign separate if needed
    num = abs(n)

    # factor 2
    while num % 2 == 0:
        factors.append(2)
        num //= 2

    # factor odd numbers from 3 upwards
    i = 3
    while i * i <= num:
        while num % i == 0:
            factors.append(i)
            num //= i
        i += 2

    # if remaining num is a prime > 2
    if num > 2:
        factors.append(num)

    return factors


if __name__ == "__main__":
    num = int(input("Enter a number: "))
    factors = prime_factors(num)
    if not factors:
        print(f"{num} has no prime factors in the usual sense (0, 1, -1).")
    else:
        print(f"Prime factors of {num} are: {factors}")
