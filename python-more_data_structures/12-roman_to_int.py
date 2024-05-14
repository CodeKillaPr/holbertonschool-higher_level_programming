#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0

    roman_dict = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    result = 0
    prev = 0

    for i in roman_string[::-1]:
        if roman_dict[i] >= prev:
            result += roman_dict[i]
        else:
            result -= roman_dict[i]
        prev = roman_dict[i]

    return result
