def is_pronic(n):
    """
    Return True if n is a pronic number.
    A pronic number is of the form k * (k + 1) for some integer k.
    """
    if n < 0:
        return False

    k = 0
    while k * (k + 1) <= n:
        if k * (k + 1) == n:
            return True
        k += 1
    return False


if __name__ == "__main__":
    num = int(input("Enter a number: "))
    if is_pronic(num):
        print(f"{num} is a pronic number.")
    else:
        print(f"{num} is NOT a pronic number.")
