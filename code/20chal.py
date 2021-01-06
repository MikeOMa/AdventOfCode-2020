import time
t = time.time()
data = open("20chal.txt").readlines()
data = [i.replace('\n','') for i in data if i!='\n']

start_idxs = [i for i,j in enumerate(data) if 'Tile' in j]
arrays_raw = [data[(idx+1):(idx+11)] for idx in start_idxs]
tile_idxs = [int(data[i].replace('Tile ','').replace(":","")) for i in start_idxs]
import numpy as np
def str_list_to_numpy(str_list):
    ret = [[i=='#' for i in _str] for _str in str_list]
    return np.array(ret)
arrays = [str_list_to_numpy(str_list) for str_list in arrays_raw]
from numba import jit
##Includes identity
array_ops = []
array_ops = []
#equiv =[ (0,2),(0,1),(1,2),(1,1)]
#@jit(forceobj=True)
def transforms(array):
    transformed_arrs = []
    combos = []
    array_variants = [array, np.fliplr(array), np.flipud(array)]
    for i in range(4):
        for num, j in enumerate(array_variants):
            transformed_arrs.append(np.rot90(j, k=i))
            combos.append((i,num))
    flips = []
    for arr in transformed_arrs:
        flips = flips+ [np.flipud(arr), np.fliplr(arr)]

    return transformed_arrs+flips


##hflip, = vflip, rot90x2
##vflip = hflip rot 90x1
all_trans = transforms(arrays[0])
##Check rotations are okay
mask_same = [[int((i==j).all()) for i in all_trans] for j in all_trans]
samerow, samecol = np.where(mask_same)
drop = [j for (i,j) in zip(samerow,samecol) if i>j]
def get_transforms(arr):
    k = transforms(arr)
    return [k[i] for i in range(len(k)) if i not in drop]

dirs = ['u','d','l','r']
def check_comp(x,y, dir = 'u'):
    if dir=='u':
        rel_x = x[0,:]
        rel_y = y[-1,:]
        ret = (rel_x==rel_y).all()
    elif dir == 'd':
        ret = check_comp(y,x, dir='u')
    elif dir == 'l':
        rel_x = x[:,0]
        rel_y = y[:,-1]
        ret = (rel_x==rel_y).all()
    elif dir == 'r':
        ret = check_comp(y,x, dir='l')
    return ret

N = int(np.sqrt(len(arrays)))
INIT = np.zeros((N,N), dtype=int)-1




import networkx as nx
all_possible_arrays = [i for array in arrays for i in get_transforms(array)]
num_arr = len(all_possible_arrays)
num_trans = len(get_transforms(arrays[0]))
comp_graph = nx.DiGraph()
for i in range(num_arr):
    comp_graph.add_node(i)
for i in range(num_arr):
    for j in range(num_arr):
        kw_attrs = {_str:check_comp(all_possible_arrays[i], all_possible_arrays[j],_str) for _str in ['u', 'd', 'l','r']}
        comp_graph.add_edge(i,j, **kw_attrs)

idxs = [[i,j] for i in range(N) for j in range(N)]
options = set(range(num_arr))
dirs = {'u': [-1,0], 'd': [1,0], 'l':[0,-1],'r':[0,1]}
def check_valid(new_layout, idx):
    new_val = new_layout[idx[0], idx[1]]
    flag = True
    for dir in dirs.keys():
        idx_to_check = [idx[0]+dirs[dir][0],idx[1]+dirs[dir][1]]
        try:
            val = new_layout[idx_to_check[0], idx_to_check[1]]
        except IndexError:
            val = -1
        if val != -1:
            flag = flag and comp_graph.edges[new_val, val][dir]
    return flag


def eliminate(current_solution):
    current_used = np.floor(current_solution.flatten()/num_trans)
    using = set([i*num_trans+j for i in current_used for j in range(num_trans)])
    return options-using
c=0
def all_solutions(layout, new_entry):
    global c
    c+=1
    vals = [layout[i,j] for i,j in idxs]
    i,j = idxs[vals.index(-1)]
    new_layout = layout.copy()
    new_layout[i,j] = new_entry
    works = check_valid(new_layout, [i,j])
    if works:
        if -1 in new_layout:
            next_trials = eliminate(new_layout)
            ret = [i for new_entry in next_trials for i in all_solutions(new_layout, new_entry)]
        else:
            ret= [new_layout]
    else:
        ret = []
    return ret


soln = [l for i in options for l in all_solutions(INIT,i)]
answer =[1951,    2311,    3079,2729,    1427,    2473,2971,1489, 1171]
print(time.time()-t)
print(len(soln))
configuration = np.floor(soln[1]/num_trans)
corners = [-1,-1,1,1]
answer = [tile_idxs[int(configuration[i,j])] for i,j in [(0,0), (0,-1), (-1,-1), (-1,0)]]
prod = 1
for l in answer:
    prod = prod*l

print('#####################')
print(prod)
print('###############################')
layout_for_soln = soln[1]
def join_tiles(trim=False):
    N_vals = 8
    if not trim:
        N_vals = 10
    full_picture = np.empty((N * N_vals, N * N_vals), dtype=np.bool)
    for i in range(N):
        for j in range(N):
            num=layout_for_soln[i,j]
            arr_soln = all_possible_arrays[num]
            if trim:
                trim_tile = arr_soln[1:-1, 1:-1]
            else:
                trim_tile = arr_soln
            start= [i*N_vals, j*N_vals]
            if num==599:
                print(start)
            full_picture[start[0]:(start[0]+N_vals), start[1]:(start[1]+N_vals)]=trim_tile
    return full_picture
full_pic = join_tiles(trim=False)
picture = join_tiles(trim=True)
np.savetxt('20chal_soln.csv', picture)
import pickle
pickle.dump(picture, open('20chal_soln.p', 'wb'))

sea_monster = [[]]
ex_soln = [1951,2311,3079,2729,1427,2473,2971,1489,1171]
arrs = transforms(arrays[1])
### 11, ,
#for arr in arrs:
#    print(arr)


#print([tile_idxs.index(l) for l in ex_soln])
