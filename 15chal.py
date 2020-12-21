from collections import Counter
sample_input = [0,3,6]
input = [0,13,1,8,6,15]
#input = sample_input
class turns:
    def __init__(self, turn_options):
        self.spoken =[]
        self.counter = Counter()
        self.n = 0
        self.turns = turn_options
        self.turn_tracker = {}
    def update(self, turn):
        self.spoken.append(turn)

        self.counter[turn]+=1
        self.n+=1
        if turn not in self.turn_tracker.keys():
            self.turn_tracker[turn] = []
        self.turn_tracker[turn].append(self.n)
    def next_turn(self):

        if self.n<len(self.turns):
            next_turn = self.turns[self.n]
        else:
            last = self.spoken[-1]
            counter_val = self.counter[last]
            if counter_val==1:
                next_turn = self.turns[0]
            else:
                lturns = self.turn_tracker[last][-2:]
                next_turn = lturns[1]-lturns[0]

        return next_turn

record = turns(input)
for turn in range(30000000):
    turn = record.next_turn()
    record.update(turn)

print(turn)
