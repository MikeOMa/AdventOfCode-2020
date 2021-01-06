import numpy as np
data = open("17chal.txt").readlines()
init_layout = np.empty((len(data), len(data[0])-1,1,1), dtype=np.unicode)
for row, line in enumerate(data):
    line = line.replace('\n',"")
    if line != "\n":
        init_layout[row,:,0,0] = [i for i in line]
print(init_layout[:,:,0])dd
lower = lambda x: (max(0,x-1))
def get_els(layout, indx):
    current_el = layout[indx]
    idx1 = layout[lower(indx[0]):(indx[0]+2),lower(indx[1]):(indx[1] + 2), lower(indx[2]):(indx[2] + 2), lower(indx[3]):(indx[3] + 2)]
    ret = list(idx1.flatten())
    ret.remove(current_el)
    return ret
def iterate(layout):
    next_layout = np.pad(layout.copy(),1,constant_values='.')
    old_padded = np.pad(layout,1, constant_values='.')
    for indx in np.ndindex(next_layout.shape):
        value = old_padded[indx]
        neighbors = get_els(old_padded,indx)
        active = len([i for i in neighbors if i=='#'])
        inactive = len([i for i in neighbors if i =='.'])
        if value == '#':
            if active in [2, 3]:
                next_layout[indx] = '#'
            else:
                next_layout[indx] = '.'
        if value =='.':
            if active ==3:
                next_layout[indx] = '#'
    return(next_layout)
current = init_layout
for i in range(6):
    next = iterate(current)
    print(np.sum(next=='#'))
    current=next
