def length_is_valid(some_string):
    if 6 <= len(some_string) <= 10:
        return True
    print("Password must be between 6 and 10 characters")
    return False


def symbols_are_valid(some_string):
    if some_string.isalnum():
        return True
    print("Password must consist only of letters and digits")
    return False


def have_at_least_two_digits(some_string):
    digits_counter = 0
    for char in some_string:
        if char.isdigit():
            digits_counter += 1
    if digits_counter >= 2:
        return True
    print("Password must have at least 2 digits")
    return False


password = input()
validated = [length_is_valid(password), \
             symbols_are_valid(password), have_at_least_two_digits(password)]
if all(validated):
    print("Password is valid")
