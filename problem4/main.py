def ubah_huruf(sentence):
    pattern = ""
    for char in sentence:
        if char.isalpha():
            if char.islower():
                if char == 'a':
                    shifted_char = 'z'
                else:
                    shifted_char = chr(ord(char) - 1)
            else:
                if char == 'A':
                    shifted_char = 'Z'
                else:
                    shifted_char = chr(ord(char) - 1)
            pattern += shifted_char
        else:
            pattern += char
    return pattern

if __name__ == '__main__':
    print(ubah_huruf("SEPULSA OKE")) # COZEVCK YUO
    print(ubah_huruf("ALTERRA ACADEMY")) # KVDOBBK KMKNOWI
    print(ubah_huruf("INDONESIA")) # SXNYXOCSK
    print(ubah_huruf("GOLANG")) # QYVKXQ
    print(ubah_huruf("PROGRAMMER")) # ZBYQBKWWOB