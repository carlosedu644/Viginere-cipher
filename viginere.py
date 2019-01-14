# Viginere cipher


def alphabet_map():
    alpha = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10,
             'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20,
             'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25, ' ': 27}
    return alpha


def alphabet(phrase):
    return alphabet_map()[phrase]


def inv_alphabet_map(phrase):
    inv_map = {v: k for k, v in alphabet_map().items()}
    return inv_map[phrase]


def main():
    k = input("Key> ")
    p = input("Phrase> ")

    key = list(k)
    phrase = list(p)

    j = 0

    for i in range(len(phrase)):
        if i < len(key):
            if alphabet(phrase[i]) + alphabet(key[i]) < 26:
                print(inv_alphabet_map(alphabet(phrase[i]) + alphabet(key[i])))
            else:
                print(inv_alphabet_map(alphabet(phrase[i]) + alphabet(key[i]) - 26))
        elif i >= len(key):
            if alphabet(phrase[i]) + alphabet(key[j]) < 26:
                print(inv_alphabet_map(alphabet(phrase[i]) + alphabet(key[j])))
                j += 1
            else:
                print(inv_alphabet_map(alphabet(phrase[i]) + alphabet(key[j]) - 26))


main()
