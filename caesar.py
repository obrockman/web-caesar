def encrypt(text, rot):
    new_str = "" 
    for i in text:
        new_char = rotate_character(i, rot)
        new_str = new_str + new_char
    return new_str

def alphabet_position(letter):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    alpha2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if letter.isalpha():
        if letter.isupper():
            for i in alpha2:
                if i == letter:
                    returnletter = alpha2.index(i)
            return returnletter
        else:
            for x in alpha:
                if x == letter:
                    rl = alpha.index(x)
            return rl
    else:
        return letter
    

def rotate_character(char, rot):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    alpha2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if char.isalpha():
        if char.isupper():
            position = alphabet_position(char)
            new_pos = (position + rot) % 26 
            new_char = alpha2[new_pos]
            return new_char
        else:
            position = alphabet_position(char)
            new_pos = (position + rot) % 26 
            new_char = alpha[new_pos]
            return new_char
    else:
        return char