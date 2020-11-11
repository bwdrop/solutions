#!/usr/bin/python3

mappings = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
    100: 'hundred',
    1000: 'thousand'
}

def to_letters(nb):
    if nb == 0:
        return ''
    elif nb <= 20:
        return mappings[nb]
    elif nb < 100:
        return mappings[nb - nb % 10] + to_letters(nb % 10)
    elif nb < 1000:
        modulo = to_letters(nb % 100)
        hundreds = mappings[nb // 100] + mappings[100]
        return hundreds if modulo == '' else hundreds + 'and' + modulo
    return mappings[nb // 1000] + mappings[1000]

print(sum([len(to_letters(i)) for i in range(1001)]))
