def roman_numerals(number):

    numerals = {1:"I", 4:"IV", 5:"V", 9:"IX", 10:"X", 40:"XL", 50:"L", 90:"XC", 100:"C", 400:"CD", 500:"D", 900:"CM", 1000:"M"}
    output = []

    for n in reversed(numerals.keys()):
        while number - n >= 0:
            number -= n
            output.append(n)

    for n in enumerate(output):
        output[n[0]] = str(numerals[n[1]])

    return "".join(output)

def part_c():
    less = 0
    more = 0
    for i in range(1, 4000):
        if len(roman_numerals(i)) < len(str(i)):
            less += 1
        elif len(roman_numerals(i)) > len(str(i)):
            more += 1

    return less, more

number = int(input("Enter a number: "))
print(roman_numerals(number))
print(part_c())