"""
LETTER COMBINATIONS PHONE - Medium
Generate letter combinations from phone number.

Logical Thinking:
1. Map digits to letters
2. Backtrack through each digit
3. Add each letter and recurse

Logical Thinking:
def letter_combinations(digits):
    if not digits:
        return []
    mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    result = []
    def backtrack(index, path):
        if index == len(digits):
            result.append(''.join(path))
            return
        for letter in mapping[digits[index]]:
            path.append(letter)
            backtrack(index + 1, path)
            path.pop()
    backtrack(0, [])
    return result
"""

# TODO: Implement solution


# Test cases
if __name__ == "__main__":
    print(f"Testing Letter Combinations Phone...")
    print("Add your test cases here")
