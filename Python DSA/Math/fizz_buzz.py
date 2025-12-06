"""
FIZZ BUZZ - Easy
Return array where i: 'Fizz' (div by 3), 'Buzz' (div by 5), 'FizzBuzz' (both), or number.

Logical Thinking:
1. Check divisibility by 15, then 3, then 5
2. Order matters for FizzBuzz
3. Convert to string if not divisible

Logical Thinking:
def fizz_buzz(n):
    result = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append('FizzBuzz')
        elif i % 3 == 0:
            result.append('Fizz')
        elif i % 5 == 0:
            result.append('Buzz')
        else:
            result.append(str(i))
    return result
"""

# TODO: Implement solution


# Test cases
if __name__ == "__main__":
    print(f"Testing Fizz Buzz...")
    print("Add your test cases here")
