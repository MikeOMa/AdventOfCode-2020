f = open("7chal.txt")
data = f.readlines()
f.close()

def parse_line(line):
    line = line.replace('\n', '')
    line = line.replace('.', '')
    lsplit = line.split(' ')
    bag_base = (' ').join(lsplit[:2])
    res = []
    total_chars = len(lsplit)

    for start in range(4,total_chars,4):
        num1 = lsplit[start+0]
        bag1 = lsplit[(start+1):(start+3)]
        bag1 = " ".join(bag1)
        if num1 == 'no':
            num1=0
        else:
            num1=int(num1)
        res.append((bag1,num1))
    return bag_base, res

dict_bag = {}
for line in data:
    bag_base , contains = parse_line(line)
    dict_bag[bag_base] =  {i[0]:i[1] for i in contains}
def join_dict(dict1 , dict2):
    final_dict = dict2
    for key in dict1.keys():
        if key not in dict2:
            final_dict[key]=int(dict1[key])
        else:
            final_dict[key] = int(dict1[key])+int(dict2[key])
    return final_dict

def get_num_bags(color='dark indigo'):
    if 'other bags' not in dict_bag[color].keys():
        _sum=dict_bag[color].copy()
    else:
        _sum={color:0}
        return _sum
    for i in dict_bag[color].keys():
        contains = get_num_bags(i)
        print(contains)
        contains2 = {key: int(dict_bag[color][i])*contains[key] for key in contains.keys()}
        print(contains2)
        print(_sum)
        _sum = join_dict(contains2, _sum)
    return(_sum)

dict_bag2 = {
    'shiny gold' : {'dark_red':2},
  'dark_red': {'orange':2},
    'orange': {'yellow': 2},
    'yellow': {'green': 2},
    'green': {'blue': 2},
    'blue': {'violet': 2},
    'violet': {'other bags': 0}
}
all_colors = dict_bag.keys()
how_many_eventually = {key: get_num_bags(key) for key in dict_bag.keys()}

answer1 = [i for i in all_colors if 'shiny gold' in how_many_eventually[i].keys()]
_dict = how_many_eventually['shiny gold']
print(sum([_dict[i] for i in _dict.keys()]))
###1219667 too high
### 721802 too high


