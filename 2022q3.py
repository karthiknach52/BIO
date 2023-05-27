parked = "abcdefghijklmnop"
branch_to_take = 12345678901234

branch_to_take += -1
parked_array = []
recreated = [None] * len(parked)
branch_sizes = []
branch_indexes = []
branch_choices = []
pref_list = []

for char in parked:
    parked_array.append(ord(char)-97)

for i in range(len(parked)):
    pos = parked_array.index(i)
    recreated[pos] = i
    branches = [pos]
    while pos > 0 and recreated[pos-1] != None:
        pos += -1
        branches.append(pos)
    branches.reverse()
    branch_choices.append(branches)
    branch_sizes.append(len(branches))

for i in reversed(range(1, len(branch_sizes) - 1)):
    branch_sizes[i] = branch_sizes[i] * branch_sizes[i + 1]
branch_sizes.pop(0)

for i in range(len(branch_sizes)):
    branch_indexes.append(branch_to_take // branch_sizes[i])
    branch_to_take = branch_to_take % branch_sizes[i]

branch_indexes.append(branch_to_take)

for i in range(len(branch_indexes)):
    pref_list.append(chr(branch_choices[i][branch_indexes[i]] + 65))

print("".join(pref_list))