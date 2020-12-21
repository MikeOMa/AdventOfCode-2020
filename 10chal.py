file = open('10chal.txt')
data = file.readlines()
file.close()
import numpy as np
data = [int(i.replace('\n','')) for i in data]
data = [0]+data+[max(data)+3]
sorted = np.sort(data)
differences  =np.diff(sorted)
num1s = [i for i in differences if i==1]
num3s = [k for k in differences if k==3]
print((differences==1).sum()*(differences==3).sum())
def doesitwork(jolt_low, jolt_high):
    return jolt_low+1<=jolt_high<=(jolt_low+3)

finish_conn_list = sorted[-1]
class adapter:
    def __init__(self, jolts):
        self.jolts = jolts
        possible_connections = [(i, jolt) for i, jolt in enumerate(sorted) if doesitwork(self.jolts,jolt)]
        self.possible_conn_jolts = [i[1] for i in possible_connections]
        self.conn_indx = [i[0] for i in possible_connections]
        self.stored_flag = False
    def get_possibilities(self, list_of_adapters):
        if not self.stored_flag:
            if len(self.conn_indx) > 0:
                sum = 0
                for i in self.conn_indx:
                    sum += list_of_adapters[i].get_possibilities(list_of_adapters)
            else:
                sum = 1
            self.num_poss = sum
            self.stored_flag=True
        return self.num_poss


list_of_adapters = [adapter(i) for i in sorted]


print(list_of_adapters[0].get_possibilities(list_of_adapters))