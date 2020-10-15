length = 531441
iterations = 9
perimeter = 4 * length
bases = 4

for i in range(iterations):
    length = length / 3
    perimeter -= bases * length
    perimeter += bases * length * 3

    bases = bases * 5

print("Länge: ", perimeter)