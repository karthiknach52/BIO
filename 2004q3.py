morse_map = {"a":".-", "b":"-...",
    "c":"-.-.", "d":"-..", "e":".",
    "f":"..-.", "g":"--.", "h":"....",
    "i":"..", "j":".---", "k":"-.-",
    "l":".-..", "m":"--", "n":"-.",
    "o":"---", "p":".--.", "q":"--.-",
    "r":".-.", "s":"...", "t":"-",
    "u":"..-", "v":"...-", "w":".--",
    "x":"-..-", "y":"-.--", "z":"--.."
}

inv_morse_map = {v: k for k, v in morse_map.items()}

def alphanum_to_morse(input:str):

    output = ""
    for i in input:
        output = output + morse_map[i]

    return output

def count_conversions(input:str, k:int, letters:list=[], count:int=0):

    if len(input) == 0 and len(letters) == k:
        count += 1
        letters = []
        return count

    if len(letters) == k:
        return count

    for i in morse_map.values():
        if input.startswith(i):
            letters.append(inv_morse_map[i])
            count = count_conversions(input.removeprefix(i), k, letters, count)
            letters.pop()

    return count


input = input("Enter a string: ")
morse_input = alphanum_to_morse(input)

print(count_conversions(morse_input, len(input)))