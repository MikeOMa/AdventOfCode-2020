data = open("16chal.txt").readlines()

field_dict = {}
your_ticket = []
nearby_tickets = []

current_section = ''
class inrange:
    def __init__(self, min_val, max_val):
        self.min_val = int(min_val)
        self.max_val = int(max_val)
    def __call__(self, new_val):
        return self.min_val<=new_val<= self.max_val
def strlist_to_intlist(strlist):
    return [int(i) for i in strlist.split(",")]
for line in data:
    line = line.replace("\n", "")
    if line in ["your ticket:", 'nearby tickets:']:
        current_section = line
    elif line=="":
        continue
    elif current_section == '':
        line=line.replace(" ", "")
        key, val = line.split(":")
        ranges = val.split("or")
        field_dict[key] = []
        for l in ranges:
            nums = l.split("-")
            field_dict[key].append(inrange(nums[0],nums[1]))
    else:
        if "your" in current_section:
            your_ticket = strlist_to_intlist(line)
        else:
            nearby_tickets.append(strlist_to_intlist(line))

N = len(your_ticket)
keys = list(field_dict.keys())
import numpy as np
def check_ranges(num, range_list):
    return any([check(num) for check in range_list])

def ticket_checker(ticket):
    ret = np.empty((N,N), dtype=np.bool)
    for i, key in enumerate(keys):
        field_ranges = field_dict[key]
        for j, val in enumerate(ticket):
            ret[i,j] = check_ranges(val,field_ranges)
    return ret

ret = ticket_checker(nearby_tickets[0])
invalids = []
first_pass_good = []
bool_arrays = []
for ind, ticket in enumerate(nearby_tickets):
    bool_array = ticket_checker(ticket)
    scan = bool_array.any(axis=0)
    bad_values = [val for val, _bool in zip(ticket,scan) if not _bool]
    invalids = invalids+bad_values
    if len(bad_values)==0:
        first_pass_good.append(ind)
        bool_arrays.append(bool_array)


print(sum(invalids))

valid_tickets = [nearby_tickets[i] for i in first_pass_good]
collapsed = np.array(bool_arrays).all(axis=0)
possible_sets = []
for l in range(N):
    possible_sets.append(set(np.where(collapsed[:,l])[0]))
lens_of_sets = [len(possible_set) for possible_set in possible_sets]
lens_order = np.argsort(lens_of_sets)
combination = [-1 for i in range(N)]
for l in lens_order:
    possible_set = possible_sets[l]-set(combination)
    combination[l] = list(possible_set)[0]

key_interest = [combination.index(k) for k,value in enumerate(keys) if 'departure' in value]

vals = [your_ticket[i] for i in key_interest]
prod =1
for val in vals:
    prod=prod*val
## too low 204376594109
print(prod)