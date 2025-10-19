#THIS CODE IS THE SOLUTION FOR A HACKERRANK PROBLEM CALLED "VALIDATING CREDIT CARD NUMBERS"
#The problem is the following:
"""A valid credit card has the following characteristics:

1. It must start with a 4, 5 or 6.
2. It must contain exactly 16 digits.
3. It must only consist of digits (0-9).
4. It may have digits in groups of 4, separated by one hyphen "-".
5. It must NOT use any other separator like ' ' , '_', etc.
6. It must NOT have 4 or more consecutive repeated digits.
EXAMPLE:
4123456789123456 : Valid
5123-4567-8912-3456 : Valid
61234-567-8912-3456 : Invalid, because the card number is not divided into equal groups of 4.
4123356789123456 : Valid
51-67-8912-3456 : Invalid, consecutive digit 3 is repeating 4 times.
5123 -- 4567 -- 8912 -- 3456 : Invalid, because space '  ' and - are used as separators.
"""
import re

CARD_PATTERN = r"^[4-6]{1}([0-9]{15}|[0-9]{3}\-([0-9]{4}\-){2}[0-9]{4})$"

def validateCardNumber(card_number:str) -> bool:
    if re.search(CARD_PATTERN, card_number):
        card_number = card_number.replace("-", "")
        for indx in range(0, len(card_number) - 3):
            if card_number[indx:indx+4].count(card_number[indx]) > 3:
                return "Invalid"
        return "Valid"
    return "Invalid"

if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        print(validateCardNumber(input()))
