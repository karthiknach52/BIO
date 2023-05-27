def palindrome(txt):

    middle = txt[(len(txt)-1)//2:(len(txt)+1)//2]
    middle2 = txt[(len(txt)+1)//2:(len(txt)+3)//2]

    first_half  = txt[:(len(txt)//2)]
    second_half = txt[(len(txt)//2) + 1:]

    if (middle2 > middle) or (second_half == first_half[::-1]):
        middle =  str(int(middle) + 1)

    if len(txt) % 2 == 0:
        first_half = first_half[:-1] + middle
        out = first_half + first_half[::-1]

    if len(txt) % 2 == 1:
        out = first_half + middle + first_half[::-1]

    return out

input = input("Enter a number: ")
print(palindrome(input))