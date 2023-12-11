import sys
with open('aoc2.txt') as f:
    games = []
    for line in f:
        cur_line = line.strip()

        #Isolate data
        i = cur_line.index(':')
        cube_sets = cur_line[i+2:]
        cube_sets = cube_sets.split(';')
        
        for i in range(len(cube_sets)):
            cube_sets[i] = cube_sets[i].split(',')
            for j in range(len(cube_sets[i])):
                cube_sets[i][j] = cube_sets[i][j].strip()
            
            dic = {}
            for j in range(len(cube_sets[i])):
                if 'red' in cube_sets[i][j]:
                    dic['red'] = int(cube_sets[i][j][:cube_sets[i][j].index(' ')])
                elif 'blue' in cube_sets[i][j]:
                    dic['blue'] = int(cube_sets[i][j][:cube_sets[i][j].index(' ')])
                if 'green' in cube_sets[i][j]:
                    dic['green'] = int(cube_sets[i][j][:cube_sets[i][j].index(' ')])

            cube_sets[i] = dic
##            print(cube_sets)

        games.append(cube_sets)

colours = ('red', 'green', 'blue')
max_dic = {'red':12, 'green':13, 'blue':14}

id_sum = 0
counter = 1
for game in games:
    inv = False
    for cube_set in game:
        for colour in colours:
            if colour in cube_set:
                if cube_set[colour] > max_dic[colour]:
                    inv = True
                    break

        if inv == True:
            break

    if inv == True:
        counter += 1
        continue

    id_sum += counter
    counter += 1

print(f'Sum of ID: {id_sum}')
sum_power = 0

for game in games:
    min_red = -1
    min_green = -1
    min_blue = -1
    
    for cube_set in game:
        if min_red == -1:
            if 'red' in cube_set:
                min_red = cube_set['red']
        else:
            if 'red' in cube_set:
                if cube_set['red'] > min_red:
                    min_red = cube_set['red']
                    
        if min_green == -1:
            if 'green' in cube_set:
                min_green = cube_set['green']
        else:
            if 'green' in cube_set:
                if cube_set['green'] > min_green:
                    min_green = cube_set['green']
                    
        if min_blue == -1:
            if 'blue' in cube_set:
                min_blue = cube_set['blue']
        else:
            if 'blue' in cube_set:
                if cube_set['blue'] > min_blue:
                    min_blue = cube_set['blue']
    sys.stdout.write(f'Red:{min_red} | Green:{min_green} | Blue:{min_blue}\n')
    sum_power += (min_red*min_green*min_blue)

print(sum_power)
        

        
                
        
                
        























        
