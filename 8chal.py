file = open('8chal.txt', 'r')
data=file.readlines()
file.close()

instructions = []
numbers = []
print(data[-1])

for line in data:
    line.replace('\n','')
    inst, num = line.split(' ')
    instructions.append(inst)
    numbers.append(int(num))
acc=0
pos = 0
jmps = [i for i, inst in enumerate(instructions) if inst=='jmp']
nops = [i for i, inst in enumerate(instructions) if inst=='nop']
result = []
for k in jmps:
    visited = [0 for i in range(len(numbers))]
    acc=0
    pos=0
    for i in range(100000):
        if visited[pos]==1:
            break
        else:
            visited[pos]=visited[pos]+1
        instruction = instructions[pos]
        if pos==k:
            instruction='nop'
        number = numbers[pos]

        if instruction=='jmp':
            pos = pos+number
        elif instruction=='acc':
            acc=acc+number
        if instruction in ['acc', 'nop']:
            pos=pos+1
        if pos>=len(instructions):
            print(k)
            print('hi')
            print(acc)
            break

