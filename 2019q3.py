def find_limit(prefix, lowestLetter="T", lowestPairLetter="U"):
    for c in prefix:
        if c < lowestLetter:
            lowestLetter = c
        if lowestLetter < c:
            if c < lowestPairLetter:
                lowestPairLetter = c

    return lowestLetter, lowestPairLetter

def block_chains(p, remaining, lowestLetter="T", limitLetter ="U"):

    if len(remaining) == 0:
        return 1

    if ord(limitLetter) - 65 < len(remaining):
        return 0

    count = 0
    for c in remaining:

        if c < limitLetter:
            t_lowestLetter = lowestLetter
            t_limitLetter = limitLetter

            if c < lowestLetter:
                t_lowestLetter = c

            if lowestLetter < c < limitLetter:
                t_limitLetter = c

            count += block_chains(p+c, remaining - set(c), t_lowestLetter, t_limitLetter)
            
    return count



import sys

l = int(sys.argv[1])

try:
    p = sys.argv[2]
except:
    p = ''

remaining = [chr(i+65) for i in range(l)]
remaining = set(remaining) - set(i for i in p)

lowestLetter, limitLetter = find_limit(p)

print(block_chains(p, remaining, lowestLetter, limitLetter))