"""
EXCEL SHEET COLUMN NUMBER - Easy
Convert Excel column title to number (A=1, Z=26, AA=27).

Logical Thinking:
1. Base 26 number system
2. Process from left to right
3. Multiply by 26 and add digit value

Logical Thinking:
def title_to_number(column_title):
    result = 0
    for char in column_title:
        result = result * 26 + (ord(char) - ord('A') + 1)
    return result
"""

# TODO: Implement solution


# Test cases
if __name__ == "__main__":
    print(f"Testing Excel Sheet Column Number...")
    print("Add your test cases here")
