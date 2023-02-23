#!/usr/bin/python3
""" FizzBuzz
    Change of logic if (i % 3) == 0 and (i % 5) == 0:
"""
#!/usr/bin/python3

import sys


def fizzbuzz(n: int) -> str:
    """
    FizzBuzz function prints numbers from 1 to n separated by a space.
    - For multiples of three print "Fizz" instead of the number and for
      multiples of five print "Buzz".
    - For numbers which are multiples of both three and five print "FizzBuzz".
    """
    if n < 1:
        return ""

    result = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return " ".join(result)


def get_user_input() -> int:
    """
    Function to get user input.
    """
    if len(sys.argv) <= 1:
        print("Missing number")
        print("Usage: ./fizzbuzz.py <number>")
        print("Example: ./fizzbuzz.py 89")
        sys.exit(1)

    return int(sys.argv[1])


if __name__ == '__main__':
    number = get_user_input()
    print(fizzbuzz(number))
