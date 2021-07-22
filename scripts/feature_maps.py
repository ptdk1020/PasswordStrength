"""This file contains feature extracting and data enrichment functions"""

import string


def length(password):
    return len(password)


def num_lowercase(password):
    """Count the number of lower case letter"""
    lower_alphabet = string.ascii_lowercase
    count = 0
    for letter in password:
        if letter in lower_alphabet:
            count += 1
    return count


def num_uppercase(password):
    """Count the number of upper case letter"""
    upper_alphabet = string.ascii_uppercase
    count = 0
    for letter in password:
        if letter in upper_alphabet:
            count += 1
    return count


def num_digits(password):
    """Count the number of digits"""
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    count = 0
    for letter in password:
        if letter in digits:
            count += 1
    return count


def num_specials(password):
    """Count the number of special characters"""
    return len(password)-num_lowercase(password)-num_uppercase(password)-num_digits(password)


def first_lower(password):
    """returns 1 first letter is a lowercase letter, 0 otherwise"""
    lower_alphabet = string.ascii_lowercase
    if password[0] in lower_alphabet:
        return 1
    else:
        return 0


def first_upper(password):
    """returns 1 first letter is an uppercase letter, 0 otherwise"""
    upper_alphabet = string.ascii_uppercase
    if password[0] in upper_alphabet:
        return 1
    else:
        return 0


def first_digit(password):
    """returns 1 first letter is a digit, 0 otherwise"""
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    if password[0] in digits:
        return 1
    else:
        return 0


def first_special(password):
    """returns 1 first letter is a special character, 0 otherwise"""
    if first_lower(password) == 0 and first_upper(password) == 0 and first_digit(password) == 0:
        return 1
    else:
        return 0


def last_lower(password):
    """returns 1 last letter is a lowercase letter, 0 otherwise"""
    lower_alphabet = string.ascii_lowercase
    if password[-1] in lower_alphabet:
        return 1
    else:
        return 0


def last_upper(password):
    """returns 1 last letter is an uppercase letter, 0 otherwise"""
    upper_alphabet = string.ascii_uppercase
    if password[-1] in upper_alphabet:
        return 1
    else:
        return 0


def last_digit(password):
    """returns 1 last letter is a digit, 0 otherwise"""
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    if password[-1] in digits:
        return 1
    else:
        return 0


def last_special(password):
    """returns 1 last letter is a special character, 0 otherwise"""
    if last_lower(password) == 0 and last_upper(password) == 0 and last_digit(password) == 0:
        return 1
    else:
        return 0

