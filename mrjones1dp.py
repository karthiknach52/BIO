memo = {}

def recurse(n, x):
    count = 0

    if n in memo:
        return memo[n]

    if n == 0:
        return 1
    
    for a in x:
        if n - a >= 0:
            count += recurse(n - a, x)
            memo[n] = count

    return count


x = [1, 2]
n = 4

print(recurse(n, x))