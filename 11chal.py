data = open("11chal.txt").readlines()
import numpy as np
from math import copysign
data = [[_char for _char in _str.replace("\n","")] for _str in data]
data = np.array(data)
nrow = len(data)
ncol = len(data[0])
def get_element(layout, indx, increment):
    # L for empty, # for taken, . for floor, -1 for off the plane
    new_indx = [indx[l]+increment[l] for l in range(2)]
    flag1 = 0 <= new_indx[0] < nrow
    flag2 = 0 <= new_indx[1] < ncol
    if flag1 and flag2:
        found = layout[new_indx[0], new_indx[1]]
        if found == '.':
            increment = list(increment)
            for sub_indx in range(2):
                if increment[sub_indx]!=0:
                    next_in_line = int(copysign(1,increment[sub_indx]))
                    increment[sub_indx]= increment[sub_indx] + next_in_line
            element = get_element(layout, indx, increment)
        else:
            element = found
    else:
        element = -1
    return element

def get_els(layout, current_pos,list_of_indx):
    surrounding_elements = []
    for increment in list_of_indx:
        surrounding_elements.append(get_element(layout, current_pos, increment))
    return surrounding_elements
class seat:
    def __init__(self, position, layout):
        self.indx = position
        self.status = layout[position[0], position[1]]
    def update_surroundings(self,layout):
        diag_rule = [(-1,-1), (-1,1), (1,-1),(1,1)]
        self.diags = get_els(layout, self.indx, diag_rule)
        plus_rule = [(0,1),(0,-1),(1,0),(-1,0)]
        self.plus = get_els(layout, self.indx, plus_rule)
    def update(self, new_layout):
        if self.status == '#':
            num_occupied = len([i for i in self.diags+self.plus if i=='#'])
            if num_occupied>=5:
                self.status = 'L'
        elif self.status == 'L':
            num_occupied = len([i for i in self.diags + self.plus if i == '#'])
            if num_occupied == 0:
                self.status = '#'
        new_layout[self.indx[0], self.indx[1]] = self.status
        return self.status
layout=data
seats = [seat([i,j], layout) for i in range(nrow) for j in range(ncol)]
for k in range(100):
    new_layout = layout.copy()
    for seat in seats:
        seat.update_surroundings(layout)
        seat.update(new_layout)
    if (new_layout==layout).all():
        print('finished at '+str(k))
        break
    layout=new_layout.copy()

print(sum(sum(new_layout=='#')))
