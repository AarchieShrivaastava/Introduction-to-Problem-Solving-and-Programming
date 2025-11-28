def is_harshad(n):
    """
    Return True if n is a Harshad number.
    A Harshad number is divisible by the sum of its digits.
    """
    if n == 0:
        return False  # by convention, we don't consider 0 as Harshad

    digit_sum = sum(int(d) for d in str(abs(n)))
    return n % digit_sum == 0


if __name__ == "__main__":
    num = int(input("Enter a number: "))
    if is_harshad(num):
        print(f"{num} is a Harshad number.")
    else:
        print(f"{num} is NOT a Harshad number.")
