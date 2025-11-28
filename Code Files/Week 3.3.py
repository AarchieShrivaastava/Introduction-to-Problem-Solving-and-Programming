def is_automorphic(n):
    """
    Return True if n is an automorphic number.
    An automorphic number's square ends with the number itself.
    """
    sq = n * n
    return str(sq).endswith(str(abs(n)))


if __name__ == "__main__":
    num = int(input("Enter a number: "))
    if is_automorphic(num):
        print(f"{num} is an automorphic number.")
    else:
        print(f"{num} is NOT an automorphic number.")
