import numba

file = open('9chal.txt')
data = file.readlines()
file.close()

for line_num in range(len(data)):
    line = data[line_num]
    line = int(line.replace('\n', ''))
    data[line_num] = line

nums_25 = data[:25]

def get_all_sums(list_of_nums):
    """
    Hackiest thing I will have done in this competition,
    There is a much smarter way to do this
    """
    return [i+j for i in list_of_nums for j in list_of_nums]
for i in range(25,len(data)):
    next_num = data[i]
    all_sums = get_all_sums(nums_25)
    if next_num in all_sums:
        nums_25.append(next_num)
        nums_25.pop(0)
    else:
        break

goal = next_num
max_indx = i
for start in range(0, max_indx):
    for end in range(start+1, max_indx):
        list_interest = data[start:end]
        if sum(list_interest)==goal:
            print(start, end)
            print(min(list_interest)+max(list_interest))
            break
