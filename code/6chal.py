f = open('6_chal.txt')
data=f.readlines()
f.close()

splits = [i for i, line in enumerate(data) if line=='\n']
#print(splits)
splits = [-1]+splits+[len(data)]
group_answers = []

for indx in range(len(splits)-1):
    lower = splits[indx]+1
    upper = splits[indx+1]
    id_lines = data[lower:upper]
    data_groups = [split_part for txt in id_lines for split_part in txt.replace('\n', '').split(' ')]
    group_answers.append(data_groups)
all_sets = []
for k in group_answers:
    group_qs = k[0]
    for person_answers in k[1:]:
        group_qs = set(person_answers).intersection(group_qs)
    all_sets.append(group_qs)
print(sum([len(_set) for _set in all_sets]))