data = open('18chal.txt').readlines()


def line_parser(line):
    line = line.replace('\n', '')
    _list = line.split(' ')
    return _list

problems = [line_parser(line) for line in data]
def plus_first(math):
    ##Messy solution to problem 2
    try:
        idx = math.index('+')
        pl2 = int(math.pop(idx+1))
        op = math.pop(idx)
        pl1 = int(math.pop(idx-1))
        sum_ret = pl1+pl2
        math.insert(idx-1, sum_ret)
        plus_first(math)
    except:
        return math
def solver(math):
    plus_first(math)
    num = int(math.pop())
    if len(math)>=2:
        op = math.pop()
        if op == '+':
            ret = num+solver(math)
        if op == '*':
            ret = num*solver(math)
    else:
        ret = num
    return ret

print(solver(['1', '+', '2','*','4'][::-1]))
### Deal with brackets

def find_brackets(line):
    bracket_idx = [[i for i, operation in enumerate(line) for _ in range(operation.count(search)) if search in operation] for search in ('(', ')')]
    return bracket_idx, len(line)
def match_brackets(line):
    ### Luckily the ordering from this function will be in hierarcial ordering saving future checks
    (opening, closing), n = find_brackets(line)
    pairs = []
    current_opening = []
    for l in range(n):
        for _ in range(opening.count(l)):
            current_opening.append(l)
        for _  in range(closing.count(l)):
            opening_idx = current_opening.pop(-1)
            pairs.append((opening_idx,l))
    return pairs
import re
def get_diget(s):
    num = filter(None, re.split(r'(\d+)', s))
    return num

def reduce_brackets(parsed_line, pair_idx):
    elements = []
    for k in range(pair_idx[1], pair_idx[0]-1,-1):
        elements.append(parsed_line.pop(k))

    elements = elements[::-1]
    num_brackets = [elements[0].count('(')-1,elements[-1].count(')')-1]
    math = [i.replace('(', '') for i in elements]
    math = [i.replace(')', '') for i in math]
    ret = str(solver(math))
    ret = num_brackets[0]*'(' + ret+ num_brackets[1]*')'
    parsed_line.insert(pair_idx[0],ret)
print(data[368])
parsed_line = line_parser(data[368])
print(parsed_line)
brackets = match_brackets(parsed_line)
print(reduce_brackets(parsed_line, brackets[2]))
print(parsed_line)
solutions = []
for problem in problems:
    brackets = match_brackets(problem)
    while len(brackets)>0:
        pair = brackets[0]
        reduce_brackets(problem, pair)
        brackets = match_brackets(problem)
    ret = solver(problem)
    solutions.append(ret)
    
