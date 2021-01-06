import numpy as np
input = np.loadtxt("20chal_soln.csv")


sample_input = open('20p2sample.txt').readlines()
sample_input = [list(i.replace('\n', "")) for i in sample_input if i!='\n']
sample_input = np.array([[i=='#'for i in line] for line in sample_input])
monster = open("20chal_seamons.txt").readlines()
monster = [list(_str.replace("\n",'')) for _str in monster]
monster = [i + [' ']*(20-len(i)) for i in monster]
monster = [[i=='O' for i in _list] for _list in monster]
monster_arr = np.array(monster)
input = input.astype(np.bool)
import pickle
#input = pickle.load(open("20chal_soln.p", 'rb'))
len_of_monster = monster_arr.shape[1]
height_of_monster= monster_arr.shape[0]
monster_weight = monster_arr.sum()
def find_the_monster(picture):
    N = picture.shape[0]
    inp_copy = picture.copy()
    for i in range(N-height_of_monster):
        for j in range(N-len_of_monster):
            sub_arr = picture[i:(i+height_of_monster), j:(j+len_of_monster)]
            sub_arr_copy = inp_copy[i:(i+height_of_monster), j:(j+len_of_monster)]
            k = np.logical_and(monster_arr,sub_arr)
            if np.sum(k) == monster_weight:
                print('hi')
                sub_arr_copy[monster_arr] = False

    return inp_copy
final = input.copy()#np.zeros((N,N), dtype=np.bool)
print(final.sum())

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
all_trans = transforms(input)
##Check rotations are okay
mask_same = [[int((i==j).all()) for i in all_trans] for j in all_trans]
samerow, samecol = np.where(mask_same)
drop = [j for (i,j) in zip(samerow,samecol) if i>j]
def get_transforms(arr):
    k = transforms(arr)
    return [k[i] for i in range(len(k)) if i not in drop]
arrs = get_transforms(input)
for arr in arrs:
    res = find_the_monster(arr)
    print(res.sum())
for k in range(4):
    for i, arr in enumerate([np.fliplr(input), input]):
        res = find_the_monster(np.rot90(arr,k=k))
        print(res.sum())
        res = np.rot90(res,k=4-k)
        if i==0:
            res = np.fliplr(res)
        final = np.logical_and(final, res)
###2109 too low
### 2589 max
### 2349 too high
### not 2289
### not 2274
print(final.sum())