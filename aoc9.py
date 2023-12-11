import sys

with open('aoc9.txt') as f:
    seq = []
    for line in f:
        cur_line = line.strip().split(' ')
        for i in range(len(cur_line)):
            cur_line[i] = int(cur_line[i])
        seq.append(cur_line)

def check_seq(seq):
    for i in range(len(seq)):
        if seq[i] != 0:
            return False

    return True

total = 0

for s in seq:
    seq_list = []
    cur_seq = s
    while not check_seq(cur_seq):
        seq_list.append(cur_seq)
        new_seq = []
        for i in range(len(cur_seq)-1):
            new_seq.append(cur_seq[i+1]-cur_seq[i])
        cur_seq = new_seq

    res = 0
    for e in seq_list[::-1]:
        res = e[0]-res

    total += res

print(total)

    
