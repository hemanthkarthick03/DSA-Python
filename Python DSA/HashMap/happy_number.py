"""
HAPPY NUMBER - Easy
Determine if number is happy (sum of squares of digits eventually equals 1).

Logical Thinking:
1. Use set to detect cycles
2. Calculate sum of squares
3. Stop when reach 1 or cycle detected

Logical Thinking:
def is_happy(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(d)**2 for d in str(n))
    return n == 1
"""

# TODO: Implement solution


# Test cases
if __name__ == "__main__":
    print(f"Testing Happy Number...")
    print("Add your test cases here")
