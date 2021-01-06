file = open("fourth_chal.txt", 'r')
data = file.readlines()
file.close()
#print(data[-1])
splits = [i for i, line in enumerate(data) if line=='\n']
#print(splits)
splits = [-1]+splits+[len(data)]
person_dicts = []
for indx in range(len(splits)-1):
    lower = splits[indx]+1
    upper = splits[indx+1]
    id_lines = data[lower:upper]
    data_groups = [split_part for txt in id_lines for split_part in txt.replace('\n', '').split(' ')]
    d = {}
    for line in data_groups:
        key, value = line.split(':')
        d[key]=value
    person_dicts.append(d)


required_keys = ['byr', 'iyr','eyr','hgt', 'hcl', 'ecl','pid']
all_keys = required_keys+['cid']
def is_subset(l1, l2):
    flag = set(l1).issubset(set(l2))
    return(flag)

def checker(person):
    flags =[]
    flag1 = is_subset(required_keys, person.keys())
    if flag1:
        flag2 = int(person['byr'])>=1920 and int(person['byr'])<=2002
        flags.append(flag2)
        issue_yr = int(person['iyr'])
        flags.append(issue_yr >= 2010 and issue_yr<=2020)
        ex_year = int(person['eyr'])
        flags.append(ex_year>=2020 and ex_year<=2030)
        if len(person['hgt'])>2:
            height = int(person['hgt'][:-2])
            unit = person['hgt'][-2:]
            if unit == 'cm':
                height_flag = height>=150 and height<=193
            elif unit == 'in':
                height_flag=height>=59 and height <= 96
            else:
                height_flag=False
        else:
            height_flag= False

        flags.append(height_flag)
        flags.append(person['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])
        flags.append(len(person['pid'])==9)
        hcl = person['hcl']

        if len(hcl)<7:
            hcl_flag = False
        elif hcl[0]!='#':
            hcl_flag=False
        elif not hcl[1:].isalnum():
            hcl_flag=False
            print(hcl[1:].isupper())
        else:
            hcl_flag=True
        flags.append(hcl_flag)
    else:
        flags.append(False)
    return flags
print(len([i for i in person_dicts if is_subset(required_keys, i.keys())]))
data = [i for i in person_dicts if all(checker(i))]
for l in data:
    if is_subset(required_keys, l.keys()):
        print("#"*10)
        print(l)
        print(checker(l))
#print(splits)
print(person_dicts[-1])
#print(data[0:6])

print(len(data))
