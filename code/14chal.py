data = open("14chal.txt").readlines()
data = [i.replace("\n","") for i in data if i!='\n']
import re
def parse_line(line):

    line= line.replace(" ", "")
    part1,part2 = line.split("=")
    if "mask"==part1:
        command= 'mask'
        indx='na'
        numeric = part2
    elif "mem" in part1:
        command="mem"
        start_indx = part1.index("[")
        end_indx = part1.index("]")
        indx = int(part1[start_indx+1:end_indx])
        numeric = int(part2)
    return command,indx, numeric
_,_, ex_mask = parse_line(data[0])
_,_,_ex_num = parse_line(data[1])
n = len(ex_mask)
def get_binary_string(num):
    bin_num = bin(num)[2:]
    return "0"*(n-len(bin_num))+bin_num

def add_strings(mask_str, bin_str):
    char_list = [mask_str[i] if mask_str[i]!='X' else bin_str[i]
        for i in range(n)]
    return ''.join(char_list)

mem = {}
mem_int = {}
mem_original  = {}
current_mask = ex_mask
for line in data:
    cmd, indx, numeric = parse_line(line)
    if cmd == 'mask':
        current_mask = numeric
    elif cmd == 'mem':
        mem_original[indx] = numeric
        binary_rep = get_binary_string(numeric)
        mem[indx] = add_strings(current_mask,binary_rep)
        mem_int[indx] = int(mem[indx],2)
print(sum(mem_int.values()))

def add_strings(mask_str, bin_str):
    char_list = []
    for i in range(n):
        if mask_str[i]=='0':
            char_list.append(bin_str[i])
        elif mask_str[i]=='1':
            char_list.append('1')
        else:
            char_list.append('X')
    return "".join(char_list)
def expand_mask(mask_str):
    if "X" in mask_str:
        ##Get first X
        X_indx = mask_str.index('X')
        new_strs = []
        list_of_chars = list(mask_str)
        list_of_chars[X_indx] = '0'
        new_strs.append("".join(list_of_chars))
        list_of_chars[X_indx] = '1'
        new_strs.append("".join(list_of_chars))
        list_of_poss = [i for new_str in new_strs for i in expand_mask((new_str))]
    else:
        list_of_poss = [mask_str]
    return list_of_poss


mem = {}
mem_int = {}
current_mask = ex_mask
for line in data:
    cmd, indx, numeric = parse_line(line)
    if cmd == 'mask':
        current_mask = numeric
    elif cmd == 'mem':
        binary_rep = get_binary_string(indx)
        memmask = add_strings(current_mask, binary_rep)
        list_of_binary_mems = expand_mask(memmask)
        for binary_num in list_of_binary_mems:
            k = int(binary_num,2)
            mem_int[k] = numeric
print(sum(mem_int.values()))

ex_num  = 42
bin_rep_num = get_binary_string(42)
print(bin_rep_num)
ex_string = add_strings("000000000000000000000000000000X1001X", "000000000000000000000000000000101010")
print(ex_string)
## is not 3776654071760
## is not 3776283666474