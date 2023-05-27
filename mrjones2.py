# https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/count-permutations-2-b1453c05/

input = [5, 6, 7, 7, 7, 8]

input_set = set(input)

numbers = set(range(1, len(input)+1))

missing = numbers - input_set
missing = list(missing)
missing.sort()

seen = set()
duplicate = []
for i in range(len(input)):
    if input[i] in seen:
        duplicate.append(input[i])
        input[i] = None

    seen.add(input[i])


def recurse(input:list, missing:list, duplicate:list, count:int):

    j = 0
    while j < len(input) and input[j] != None:
        j += 1

    if j == len(input):
        return missing, duplicate, (count + 1)

    i = 0
    while i < len(input) and input[i] != duplicate[0]:
        i += 1

    t_duplicate = duplicate.copy()
    t_duplicate.pop(0)
    
    k = 0
    while k < len(missing) and missing[k] < input[i]:
        input[j] = missing[k]
        t_missing = missing.copy()
        t_missing.pop(k)
        a_missing, a_duplicate, count = recurse(input, t_missing, t_duplicate, count)
        input[j] = None
        k += 1

    return missing, duplicate, count

missing, duplicate, count = recurse(input, missing, duplicate, 0)

print(count)