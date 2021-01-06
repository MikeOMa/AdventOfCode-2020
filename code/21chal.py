data = open("21chal.txt").readlines()
data = [i.replace("\n","") for i in data if i != '\n']

def line_parser(line):
    ingredients, contains = line.split('(contains')
    ingredients = ingredients.split(" ")
    ingredients = [i for i in ingredients if i != '']
    contains = contains.replace(")", '')
    contains = contains.split(" ")
    contains = [i.replace(",","") for i in contains if i != '']
    return ingredients, contains
parsed_data = [line_parser(line) for line in data]
print(parsed_data[0])
all_contents = set([l for i in parsed_data for l in i[1]])
all_ingredients_list = [l for i in parsed_data for l in i[0]]
all_ingredients = set(all_ingredients_list)
dict_all_options = {content:[] for content in all_contents}
for ingredients, contents in parsed_data:
    ing_set = set(ingredients)
    for content in contents:
        dict_all_options[content].append(ing_set)
feasible_set = {content: set.intersection(*dict_all_options[content]) for content in dict_all_options.keys()}
def drop_from_sets(element, set_dict):
    print(set_dict)
    print(element)
    for key in set_dict:
        set_dict[key] = set_dict[key]-set([element])
    return set_dict
def find_first_unique(set_dict):
    found = -1
    for key in set_dict:
        if len(set_dict[key])==1:
            found = key
            break
    return found
known = {}
change_flag = True
while change_flag:
    key = find_first_unique(feasible_set)
    if key!=-1:
        known[key] = list(feasible_set[key])[0]
        del feasible_set[key]
        feasible_set = drop_from_sets(known[key], feasible_set)
    else:
        change_flag = False
unaccounted_ing = all_ingredients
for key in known:
    unaccounted_ing = unaccounted_ing-set([known[key]])
for key in feasible_set:
    unaccounted_ing = unaccounted_ing-feasible_set[key]
counter = 0
for ing in unaccounted_ing:
    counter+=all_ingredients_list.count(ing)
print(counter)

all_keys = list(known.keys())
all_keys.sort()
res_str = ""
for key in all_keys:
    res_str = res_str+known[key]+','
print(res_str[:-1])
