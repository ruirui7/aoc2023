INSTRUCTION = 'LRRLRRLLRRRLRRLRLRRRLRRLRRRLRLLRRRLRRRLRLRRRLRRLRRLRLRLLLRRRLRRRLRRLRRLRLRRRLRRLLRRLRRLRLLRLRLRRLRLLRLRLRRRLRRLRLLRLRLLRRLRLRRLLLRLRRLRRRLLLRRLRLRRRLLRRLLLRRRLRRRLLLRRLLRLRRLRLRRLLLRLRRLLLLRRLLRRRLRRLRRLRLRLLRLRRRLLRRLLRRLRRLRRLRRLRLLRRLRRRLRLRLLLRRRLLRRRLRRLRRLLLLRRRR'
with open('aoc8.txt') as f:
    nodes = {}
    for line in f:
        node_name = line[0:3]
        node_left = line[7:10]
        node_right = line[12:15]
        nodes[node_name] = (node_left, node_right)

##cur_node = 'AAA'
##steps = 0
##while cur_node != 'ZZZ':
##    for char in INSTRUCTION:
##        steps += 1
##        if char == 'L':
##            cur_node = nodes[cur_node][0]
##        else:
##            cur_node = nodes[cur_node][1]
##
##print(steps)

cur_nodes = []
for n in nodes:
    if n[2] == 'A':
        cur_nodes.append(n)

steps = []

for n_ in cur_nodes:
    step = 0
    while n_[2] != 'Z':
        for char in INSTRUCTION:
            step += 1
            if char == 'L':
                n_ = nodes[n_][0]
            else:
                n_ = nodes[n_][1]
    steps.append(step)

print(steps)
    




