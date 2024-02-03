import string
import sys

def is_panagram(text, alp =string.ascii_lowercase):
    return set(alp) <= set(text.lower())


print(is_panagram('The quick brown fox jumps over the lazy dog'))
