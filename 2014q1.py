k = int(input())

lucky_numbers = []
for i in range(k):
    lucky_numbers.append(2*i + 1)

i = 1   
while lucky_numbers[i] < k:
    del lucky_numbers[lucky_numbers[i]-1::lucky_numbers[i]]
    i += 1

if lucky_numbers[i] == k:
    print(lucky_numbers[i-1], lucky_numbers[i+1])
else:
    print(lucky_numbers[i-1], lucky_numbers[i])

# for a list of lucky numbers:
# print(lucky_numbers) 