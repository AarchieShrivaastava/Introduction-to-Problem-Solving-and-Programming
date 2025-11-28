def is_deficient(n):
    """
    Return True if n is a deficient number.
    A number is deficient if the sum of its proper divisors is less than the number itself.
    """
    if n <= 0:
        return False  # not defined for non-positive integers

    if n == 1:
        # proper divisors of 1 = {} -> sum = 0 < 1 -> deficient
        return True

    s = 1  # 1 is a proper divisor of every n > 1
    i = 2
    while i * i <= n:
        if n % i == 0:
            s += i
            if i != n // i:
                s += n // i
        i += 1

    return s < n


if __name__ == "__main__":
    num = int(input("Enter a number: "))
    if is_deficient(num):
        print(f"{num} is a deficient number.")
    else:
        print(f"{num} is NOT a deficient number.")
