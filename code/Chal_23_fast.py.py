# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time

from numba import jit

start = time.time()
input = "784235916"
# input = "389125467" # < example given
###Read in data
mil = 1000000
input_list = [int(i) - 1 for i in input]
n_input = len(input_list)
p2_input_list = input_list + [i for i in range(n_input, mil)]


def get_circular(x, n=n_input):
    return (x + 1) % n


def classic_to_linked_list(_list):
    n = len(_list)
    ll = [0] * len(_list)
    for i, j in enumerate(_list):
        ll[j] = _list[(i + 1) % n]
    return ll


@jit
def get_next(current_num, elim_list, n=10):
    pos = (current_num - 1) % n
    if pos in elim_list:
        pos = get_next(pos, elim_list=elim_list, n=n)
    return pos


def ll_to_classic(ll):
    classic = [0] * len(ll)
    pos = 0
    for k in range(len(ll)):
        classic[(k + 1) % len(ll)] = ll[pos]
        pos = ll[pos]
    return classic


@jit
def play_game(ll, start, num_plays):
    N = len(ll)
    current_position = start
    next_three = [0, 0, 0]
    for i in range(num_plays):
        pos = current_position
        # print('#'*5)
        # print(ll)
        # print('#'*5)
        for k in range(3):
            next_three[k] = ll[pos]
            pos = ll[pos]
        # print('pos', ll[pos])
        # print('current_pos', current_position)
        ll[current_position] = ll[pos]
        destination_position = get_next(current_position, elim_list=next_three, n=N)
        # print(destination_position)
        ll[destination_position], ll[next_three[-1]] = next_three[0], ll[destination_position]
        current_position = ll[current_position]


print(53248976)
p1_input_ll = classic_to_linked_list(input_list)
output = p1_input_ll.copy()
play_game(output, input_list[0], 100)

ans1 = [str(i + 1) for i in ll_to_classic(output)]
print("Q1", ans1)

p2_input_ll = classic_to_linked_list(p2_input_list)
ans2 = 1
pos = 0
p2_output_ll = p2_input_ll.copy()
play_game(p2_output_ll, p2_input_list[0], mil * 10)
for k in range(2):
    pos = p2_output_ll[pos]
    ans2 *= pos + 1
print(ans2)
print(time.time() - start)

