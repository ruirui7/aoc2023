#1) Find the index range of all numbers
#2) Check, for each number, whether any number within the index range is
#   adjacent to any number

#*map size is 140x140
import sys

with open('aoc3.txt') as f:
    map_ = [list(f.readline().strip()) for _ in range(140)]

##for i in range(20):
##    for j in range(140):
##        sys.stdout.write(map_[i][j])
##    print()

no_index = []
skip = 0
for i in range(140):
    for j in range(140):
        if skip > 0:
            skip -= 1
            continue

        if map_[i][j].isdigit() == True:
            end = j
            for k in range(j+1, 140):
                if map_[i][k].isdigit() == True:
                    end = k
                else:
                    break

            no_index.append((i, j, end))
            skip += (end-j)

temp_index = []

for index in no_index:
    i = index[0]
    j = index[1]
    end = index[2]
    no = ''.join(map_[i][j:end+1])
    temp_index.append((index, int(no)))

no_index = temp_index

for index in no_index:
    i = no_index[0]
    j = no_index[1]
    end = no_index[2]
    for k in range(j, end+1):
        if i != 0:
            if k != 0:
                if map_[i][k-1].isdigit() == False and map_[i][k-1].isdigit() != '.':
                    
                
