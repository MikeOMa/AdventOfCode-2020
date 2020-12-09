f = open('5_chal.txt')
data = f.readlines()
f.close()

data = [i.replace("\n", "") for i in data]
options = list(range(128))
class airplane_seat:
    def __init__(self, _string):
        self.original = _string
        self.row_str = _string[:7]
        self.row = self.get_num(self.row_str)
        self.col_str = _string[7:]
        self.col = self.get_num(self.col_str)
        self.seat_id = self.row*8+self.col

    def get_num(self, strl):
        l = list(range(2**len(strl)))
        for k in strl:
            n=len(l)
            if k in "LF":
                l = l[:int(n/2)]
            elif k in "BR":
                l= l[int(n/2):]
        assert len(l)==1, ValueError(f"{strl} is invalid")
        return l[0]

objs = [airplane_seat(i) for i in data]
seat_ids = [obj.seat_id for obj in objs]
row_ids = [obj.row for obj in objs]
col_ids = [obj.col for obj in objs]
def get_row_col(id):
    col = id % 8
    row = int((id - col) / 8)
    return row, col

def is_free(id):
    row, col = get_row_col(id)
    flags = []
    for k in [-1,1]:
        id_new = id+k
        flags.append(id_new in seat_ids)
    flags.append(row not in [0,127])
    flags.append(id not in seat_ids)
    return flags
all_possible_ids = [i*8+k for i in range(128) for k in range(8)]
free_ids = [id for id in all_possible_ids if all(is_free(id))]
print(free_ids)
print(len(free_ids))
print(len(all_possible_ids))

