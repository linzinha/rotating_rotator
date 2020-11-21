from string import ascii_lowercase  # imports strings of aphabet
import random

def return_alpha_index(a):
    """ returns the index of an alphabet """
    alphabets = ascii_lowercase
    for i, j in enumerate(alphabets):
        if j == a:
            return (i)
    return (a)


def return_index_alpha(n):
    """ returns an alphabet given the index"""
    alphabets = ascii_lowercase
    for i, j in enumerate(alphabets):
        if i == n:
            return (j)
    return (n)


def encryption(text):
    encryption, result = [], []
    # get the index of the alphabets in text and add the key to them
    for i in text:
        key = random.randint(1, 26)
        keystring.append(key)
        try:
            encryption.append(return_alpha_index(i) + key)
        except:
            encryption.append(return_alpha_index(i))
    # check if a number value is greater than six then subtracts 26 from it
    for i in encryption:
        try:
            if i >= 26:
                result.append(i - 26)
            else:
                result.append(i)
        except:
            result.append(i)
    # get the new number values which is our cipher text
    encryption = "".join([return_index_alpha(n) for n in result])
    return (encryption)

keystring = []

