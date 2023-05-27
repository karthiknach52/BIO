def triangle(input):
    input = [*input]

    numbers = [ord(letter) for letter in input]
    char_sum = {153:66, 137:82, 148:71}

    while len(numbers) > 1:
        for i in range(len(numbers)-1):
            if numbers[i] == numbers[i+1]:
                numbers[i] = numbers[i]
            else:
                numbers[i] = char_sum[numbers[i] + numbers[i+1]]
        numbers.pop(-1)


    return [chr(number) for number in numbers]

input = input("Enter a string: ")
print(triangle(input))