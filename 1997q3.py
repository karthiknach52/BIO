# Finds highest possible divisor first time then increments
def egyptian_fraction(n, d):
    denominators = []
    d2 = -(d // -n)
    while n / d != 0:
        if (n*d2 - d) / (d*d2) >= 0:
            n = (n*d2 - d)
            d = (d * d2)
            denominators.append(d2)
        d2 += 1

    return denominators

# Finds highest possible divisor each time
def egyptian_fraction(n, d):
    denominators = []
    while n / d != 0:
        d2 = -(d // -n)
        if (n*d2 - d) / (d*d2) >= 0:
            n = (n*d2 - d)
            d = (d * d2)
            denominators.append(d2)

nu = int(input("Numerator: "))
de = int(input("Denominator: "))
print(egyptian_fraction(nu, de))