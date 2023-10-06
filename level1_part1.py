def solution(s):
    char_to_braille = {
        "a": "100000",
        "b": "110000",
        "c": "100110",
        "d": "100010",
        "e": "100010",
        "f": "110100",
        "g": "110110",
        "h": "110010",
        "i": "010100",
        "j": "010110",
        "k": "101000",
        "l": "111000",
        "m": "101100",
        "n": "101110",
        "o": "101010",
        "p": "111100",
        "q": "111110",
        "r": "111010",
        "s": "011100",
        "t": "011110",
        "u": "101001",
        "v": "111001",
        "w": "010111",
        "x": "101101",
        "y": "101111",
        "z": "101011"
    }
    capital_letter_follows = "000001"
    space = "000000"
    result = []
    for c in s:
        if c == " ":
            result.append(space)
        elif c.islower():
            result.append(char_to_braille[c])
        else:
            result.append(char_to_braille[c.lower()])
    return ''.join(result)
