input = open("chal24.txt", 'r').readlines()

parts = ["e", "w", "se", "sw", "ne", "nw"]
def line_parser(line, valid = parts):
    line = line.replace("\n", "")
    l = []
    _str_pos = 0
    while _str_pos< len(line):
        current = line[_str_pos:(_str_pos+2)]
        if current in valid:
            l.append(current)
            _str_pos+=2
        else:
            l.append(current[0])
            _str_pos+=1
    return l

data = [line_parser(line) for line in input]
### figure at https://www.redblobgames.com/grids/hexagons/
walk_dict = {"e" : [1,-1,0],
             "w" : [-1,1,0],
             "ne" : [1,0,-1],
             "se" : [0,-1,1],
             "sw" : [-1,0,1],
             "nw" : [0,1,-1]}
white_dict = {}
current_keys = []

def flip_tile(pos, flip_dict):
    pos = tuple(pos)
    current_keys = flip_dict.keys()
    if pos not in current_keys:
        flip_dict[pos] = 1
    else:
        flip_dict[tuple(pos)] += 1
    return flip_dict
def get_value(pos, _dict):
    try:
        ret = _dict[pos]
    except:
        ret=0
    return ret


def p2_flip(pos, current_dict, flip_dict):
    neighbors = get_neighbors(pos, current_dict)
    current_flip = get_value(pos, current_dict)%2
    num_black = sum([neighbor%2==1 for neighbor in neighbors])
    if num_black == 2 and current_flip==0:
        flip_dict = flip_tile(pos, flip_dict)
    if  current_flip==1 and (num_black>2 or num_black==0):
        flip_dict = flip_tile(pos,flip_dict)
    return flip_dict

def get_neighbors(pos, current_dict):
    coords = [tuple([pos[i]+val[i] for i in range(3)]) for val in walk_dict.values()]
    neighbors = []
    for coord in coords:
        neighbors.append(get_value(coord, current_dict))
    return neighbors

def get_all_neighboor_pos(_dict):
    all_positions = set()
    for pos in _dict.keys():
        coords = [tuple([pos[i] + val[i] for i in range(3)]) for val in walk_dict.values()]
        coords.append(pos)
        all_positions  = all_positions.union(set(coords))
    return all_positions



for steps in data:
    pos = [0,0,0]
    for instruction in steps:
        this_step = walk_dict[instruction]
        pos = [pos[i]+this_step[i] for i in range(3)]
    white_dict = flip_tile(pos, white_dict)
def count_black(_dict):
    flips = _dict.values()
    return len(flips), len([i for i in flips if i%2 !=0])
print(count_black(white_dict))
current_dict = white_dict.copy()
for i in range(100):
    next_dict = current_dict.copy()
    all_pos = get_all_neighboor_pos(current_dict)
    for pos in all_pos:
        next_dict = p2_flip(pos, current_dict, next_dict)
    if (i+1)%10==0:
        print(count_black(next_dict))
    current_dict = next_dict.copy()
