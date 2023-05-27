def is_pat(word):

    if len(word) == 1:
        return True

    for i in range(1,len(word)):
        half1 = word[:i]
        half2 = word[i:]

        if is_pat(half1[::-1]) and is_pat(half2[::-1]):
            
            lowest_half1 = half1[0]
            for letter in half1:
                if letter < lowest_half1:
                    lowest_half1 = letter

            highest_half2 = half2[0]
            for letter in half2:
                if letter > highest_half2:
                    highest_half2 = letter

            if highest_half2 < lowest_half1:
                return True

    return False

input = input("Enter the two strings: ")
s1, s2 = input.split()
s1s2 = s1 + s2

for s in [s1, s2, s1s2]:
    if is_pat(s):
        print("YES")
    else:
        print("NO")