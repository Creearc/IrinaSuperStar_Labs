name = '1'

def get_ind(cp, old_positions):
    print(cp)
    l = -1
    ind = 0
    i = 0
    for p in old_positions:
        ln = ((cp[0] - p[0]) ** 2 + (cp[1] - p[1]) ** 2) ** (1.0/2)
        if (l > ln) or (l == -1):
            ind = i
            l = ln
        i += 1

    return ind, l

def save_coords(ind, position): 
    f = open(str(ind) + '.csv', 'a')
    f.write(str(position)[1:-1].replace(", ", ";"))
    f.write('\n')
    f.close()


coords = [(2, 2, 0), (23, 23, 0), (5, 5, 0)]

coords_new = [(3, 2, 0), (23, 30, 0), (5, 2, 0)]

print(get_ind(coords_new[0], coords))
save_coords(1, coords[1])
