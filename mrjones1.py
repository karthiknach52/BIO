def recurse(n, x):
    count = 0

    if n == 0:
        return 1
    
    for a in x:
        if n - a >= 0:
            count += recurse(n - a, x)

    return count

memo = {0:1}

def recurse_dp(n, x):
    global memo
    count = 0

    if n in memo:
        return memo[n]
    
    for a in x:
        if n - a >= 0:
            count += recurse_dp(n - a, x)
            memo[n] = count

    return count


x = [1, 2]
n = 998

print(recurse_dp(n, x))