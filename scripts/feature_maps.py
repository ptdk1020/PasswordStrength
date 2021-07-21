"""This file contains feature extracting and data enrichment functions"""

import string


# def length(password):
#     return len(password)


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


def num_digit(password):
    """Count the number of digits"""
    digits = ['0', '1', '2', '4', '5', '6', '7', '8', '9']
    count = 0
    for letter in password:
        if letter in digits:
            count += 1
    return count


def num_special(password):
    """Count the number of special characters"""
    return len(password)-num_lowercase(password)-num_uppercase(password)-num_digit(password)


def jarowinkler(password):
    return
