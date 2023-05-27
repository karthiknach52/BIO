def encrypt(input):
    input_array = []
    output_array = []

    for char in input:
        input_array.append(ord(char) - 64)
    
    for i in reversed(range(1, len(input_array))):
        input_array[i] = input_array[i] - input_array[i-1]
        if input_array[i] < 1:
            input_array[i] += 26

    for num in input_array:
        output_array.append(chr(num + 64))

    return "".join(output_array)

def part_c():
    input = "OLYMPIAD"
    output = encrypt(input)
    counter = 1
    while output != input:
        output = encrypt(output)
        counter += 1

    print(counter)

input = input("Enter input string: ")
print(encrypt(input))