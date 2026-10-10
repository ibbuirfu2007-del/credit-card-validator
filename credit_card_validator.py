
"""
Credit Card Validator using the Luhn Algorithm
"""


def verify_card_number(card_number):
    # Remove spaces and hyphens
    cleaned_number = card_number.replace(" ", "").replace("-", "")

    # Validate input
    if not cleaned_number or not cleaned_number.isdigit():
        return "INVALID!"

    total_sum = 0

    # Reverse the card number
    reversed_digits = cleaned_number[::-1]

    # Process each digit
    for index, char_digit in enumerate(reversed_digits):
        digit = int(char_digit)

        # Double every second digit from the right
        if index % 2 == 1:
            digit *= 2

            # Subtract 9 if the digit is greater than 9
            if digit > 9:
                digit -= 9

        # Add digit to total
        total_sum += digit

    # Check Luhn checksum
    if total_sum % 10 == 0:
        return "VALID!"

    return "INVALID!"


if __name__ == "__main__":
    card_number = input("Enter card number: ")
    result = verify_card_number(card_number)
    print("Result:", result)

