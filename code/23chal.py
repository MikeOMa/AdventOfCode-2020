input = "784235916"
ex_input = "389125467"
#input = input
import time
start = time.time()
input = [int(i) for i in input]
mil = 1000000
n=len(input)
input = input + [i for i in range(max(input)+1, mil+1)]
current_cup = 3
setup = input.copy()
idx_trans = lambda x : x%len(input)
def find_cup(current_cup, picked_up, n=1000000):
    next_cup = ((current_cup-2)%n)+1
    if next_cup in picked_up:
        next_cup = find_cup(next_cup, picked_up)
    return next_cup

def move_cup(current_cup_idx):
    current_cup = setup[current_cup_idx]
    next_three_idx = [idx_trans(current_cup_idx+i) for i in range(1,4)]
    next_three = [setup[idx] for idx in next_three_idx]
    next_three_idx.sort()
    for k in next_three_idx[::-1]:
        setup.pop(k)
    destination_cup = find_cup(current_cup, next_three)
    destination_idx = setup.index(destination_cup)
    for idx, el in enumerate(next_three):
        setup.insert(destination_idx+idx+1, el)
    next_idx = idx_trans(setup.index(current_cup)+1)
    return next_idx
current_cup_idx=0
n_rounds = 10000000
for i in range(n_rounds):
    next_cup_idx=move_cup(current_cup_idx)
    current_cup_idx=next_cup_idx
    if i%1000==0:
        print(i)
pos1 = setup.index(1)
print(setup[idx_trans(pos1+1)]*setup[idx_trans(pos1+2)])
#print(''.join([str(setup[idx_trans(pos1+i)]) for i in range(1,len(setup))]))
###53472698 too high
print((time.time()-start)/n_rounds*10000000/60/60)