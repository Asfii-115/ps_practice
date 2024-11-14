def solve(s):
    max_value = 0

    for x in s:
        if x not in "aeiou" and (ord(x) - 96) > max_value:
            max_value += ord(x) - 96
    return max_value


def solve(s):
    max_value = 0
    current_sum = 0

    for x in s:
        if x not in "aeiou":  # Check if it's a consonant
            current_sum += ord(x) - 96  # Add its value to the current sum
        else:
            max_value = max(
                max_value, current_sum
            )  # Update max_value if current_sum is higher
            current_sum = 0  # Reset current sum when encountering a vowel

    # After the loop, check once more in case the longest sequence is at the end
    max_value = max(max_value, current_sum)

    return max_value


# Test the function
print(solve("cozy"))  # Expected output: 51

print(solve("zodiac"))
