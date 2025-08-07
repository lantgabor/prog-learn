def caesar(text, shift):
    abc = "abcdefghijklmnopqrstuvwxyz"
    result = ""

    for c in text:
        if c in abc:
            i = abc.index(c)
            result += abc[(i + shift) % 26]
        else:
            result += c
    return result


# Example usage
print(caesar("hello world", 3))  # khoor zruog
print(caesar("khoor zruog", -3))  # hello world
