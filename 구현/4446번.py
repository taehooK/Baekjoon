def solution():
    chars_one = list('aiyeou')
    chars_other = list('bkxznhdcwgpvjqtsrlmf')

    while True:
        try:
            string = input()
            ret = []
            for i in range(len(string)):
                char = string[i]
                asc = ord(char)

                if 65 <= asc <= 90 or 97 <= asc <= 122:
                    offset = 0
                    if 65 <= asc <= 90: #대문자이면
                        offset = -32
                        asc += 32
                    char = chr(asc)
                    if char in chars_one:
                        index = chars_one.index(char) + 3
                        if index >= len(chars_one):
                            index -= len(chars_one)
                        char = chars_one[index]
                    else:
                        index = chars_other.index(char) + 10
                        if index >= len(chars_other):
                            index -= len(chars_other)
                        char = chars_other[index]
                    char = chr(ord(char) + offset)
                ret.append(char)
            print(''.join(ret))
        except:
            break
solution()
        #대문자도 아니고 소문자도 아니면 pass

        #대문자이면

        #소문자이면




