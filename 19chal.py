data = open('19chal.txt').readlines()
n_lines = data.index('\n')
rule_data = [i.replace('\n','') for i in data[:n_lines] if i!='\n']
str_to_check = [i.replace('\n','') for i in data[(n_lines+1):] if i!='\n']

def line_parser(line):
    key, remainder = line.split(': ')
    chars = remainder.split(' ')
    return key, chars
class rule:
    def __init__(self, remainder):
        self.ran_before=False
        self.chars = remainder
        nquot = self.chars[0].count('"')
        self.multirule=False
        if nquot==2:
            self.final_type = True
            self.char_desired = self.chars[0].replace('\"','')
        else:
            self.final_type=False
        if '|' in self.chars:
            i = self.chars.index('|')
            self.multirule = True
            self.rules = [rule(self.chars[:i]), rule(self.chars[(i+1):])]
    def checkrule(self, list_of_char, rules_dict):
        ### Returns a number from 0 to N where N is the length of the str
        n = len(list_of_char)
        if self.multirule:
            idxs = [rule.checkrule(list_of_char, rules_dict) for rule in self.rules]
            ret = min(idxs)
        elif self.final_type:
            if self.char_desired in list_of_char:
                ret = list_of_char.index(self.char_desired)+1
            else:
                ret = n+1
        else:
            min_idx = 0
            for k in range(len(self.chars)):
                sub_string_occurance = rules_dict[self.chars[k]].checkrule(list_of_char[(min_idx):], rules_dict)
                if (min_idx+sub_string_occurance)>len(list_of_char):
                    min_idx = len(list_of_char)+1
                    break
                else:
                    min_idx = min_idx+sub_string_occurance
            ret = min_idx
        return(ret)




parsed_lines = [line_parser(i) for i in rule_data]

def solution(parsed_lines):
    rules = {key: rule(remainder) for key, remainder in parsed_lines}
    lens_of_strings = [len(l) for l in str_to_check]
    res = [rules['0'].checkrule(_str, rules) for _str in str_to_check]
    matched = [last_idx==n for n,last_idx in zip(lens_of_strings, res)]
    return matched
matched = solution(parsed_lines)
def remap(key, remainder,rep = [0,0]):
    if key == '8':
        remainder = ['42']+['42']*rep[0]
    if key == '11':
        remainder = ['42'] +['42']*rep[1]+ ['31']*rep[1]+ ['31']
    return key, remainder
all_masks = []
for k in range(20):
    for k2 in range(20):
        remapped_lines = [remap(key, remainder, rep=[k,k2]) for key, remainder in parsed_lines]
        maskie = solution(remapped_lines)
        all_masks.append(maskie)

n = len(all_masks[0])
nrow = len(all_masks)
ans = sum([any([all_masks[i][j] for i in range(nrow)]) for j in range(n)])
print(ans)
###>230
### >303
### 357
### Not 325
### <416