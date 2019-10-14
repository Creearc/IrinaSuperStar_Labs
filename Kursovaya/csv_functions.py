def save_coords(ind, position): 
    f = open('paths/' + str(ind) + '.csv', 'a')
    f.write(str(position)[1:-1].replace(", ", ";"))
    f.write('\n')
    f.close()

def load_coords(ind):
    coords = []
    f = open('paths/' + str(ind) + '.csv', 'r')
    for c in f:
        x, y, z = c[:-1].split(';')
        x, y, z = float(x[1:-1]), float(y[1:-1]), float(z)
        coords.append((x, y, z))
    f.close()

    return coords

def clear_paths():
    import os
    for f in os.listdir("paths"):
        os.remove("paths/" + f)
