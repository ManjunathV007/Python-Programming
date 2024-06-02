def countLetters(s):
    lowerCount = upperCount = 0

    for x in s:
        if x.islower():
            lowerCount += 1
        elif x.isupper():
            upperCount += 1
        else:
            print('invalid character')

    print('lower characters : ', lowerCount)
    print('upper characters : ', upperCount)

s = input('enter any string : ')
countLetters(s)
