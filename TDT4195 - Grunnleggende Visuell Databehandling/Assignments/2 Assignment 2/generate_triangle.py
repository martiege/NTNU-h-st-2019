
def coordinate_shift(x, y):
    return (
        (x, 0, 0, 0), 
        (x, y, 0, 0), 
        (0, y, 0, 0)
    )

def generate_triangles(n_triangles, n_coordinates):
    from math import sqrt
    side_division = (int(sqrt(n_triangles)) + 1)

    triangles = []
    if n_coordinates < 1:
        return
    elif n_coordinates == 1:
        base = [1.0]
    elif n_coordinates == 2:
        base = [1.0, 1.0]
    elif n_coordinates == 3:
        base = [1.0, 1.0, 0.0]
    else:
        base = [1.0, 1.0] + [0.0 for i in range(n_coordinates - 3)] + [1.0]

    for t in range(n_triangles):
        #if t % 2 == 0:
        x_shift = - (float(t % side_division) + 1.0) / side_division
        y_shift = - (float(t // side_division) + 1.0) / side_division
        print("X:", x_shift)
        print("Y:", y_shift)
        shift = coordinate_shift(x_shift, y_shift)
        triangles.append(generate_triangle(base, shift))

    return triangles

def gen_xy(num, size):
    from math import sqrt
    
    x = 2 * (float(num % size)) / size - 0.9
    y = 2 * (float(num // size)) / size - 0.9

    return x, y

def generate_triangle(base, shift):
    coordinates = []
    for c in range(len(shift)):
        coordinate = []
        for i in range(len(base)):
            coordinate.append(base[i] + shift[c][i])
        coordinates.append(coordinate)

    return coordinates

def generate_indices(triangles):
    indices = []
    index = 0
    for triangle in triangles: 
        for coordinates in triangle:
            indices.append(index)
            index += 1
    
    return indices

def format_triangles(triangles):
    result = "{\n\t"

    l_triangles = len(triangles)
    for ts in range(l_triangles):
        
        l_triangle = len(triangles[ts])
        for t in range(l_triangle):
            
            l_coordinates = len(triangles[ts][t])
            for c in range(l_coordinates):

                result += str(triangles[ts][t][c])
                if not ((c + 1) == l_coordinates and (t + 1) == l_triangle and (ts + 1) == l_triangles):
                    result += ", "
                    
            if (t + 1) == l_triangle and (ts + 1) == l_triangles:
                result += "\n"
            else:
                result += "\n\t"
            
    return result + "}"

def format_indices(indices, n_coordinates):
    result = "{"

    l_indices = len(indices)
    for i in range(l_indices):
        if (i + 1) == l_indices:
            result += str(indices[i]) + "\n}"
        elif (i % n_coordinates) == 0:
            result += "\n\t" + str(indices[i]) + ", "
        else: 
            result += str(indices[i]) + ", "
    
    return result

def generate_data(n_triangles, n_coordinates):
    triangles = generate_triangles(n_triangles, n_coordinates)
    indices = generate_indices(triangles)
    return format_triangles(triangles), format_indices(indices, n_coordinates)
    

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--triangles')
    parser.add_argument('-c', '--coordinates')
    args = parser.parse_args()

    if not args.triangles:
        print("No number of triangles given, default 3")
        args.triangles = 3

    if not args.coordinates:
        print("No number of coordinates given, default 3")
        args.coordinates = 3

    print("Generating triangles...")
    # for t in generate_triangles(3, 3):
    #     print(t)
    for i in range(25):
        print(gen_xy(i, 5))
    # triangles = generate_triangles(int(args.triangles), int(args.coordinates))
    # print(format_triangles(triangles))

    # print("-"*50)
    # a, b = generate_data(int(args.triangles), int(args.coordinates))
    # print(a)
    # print(b)