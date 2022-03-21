# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 2: MULTIPLICATION TABLE
#
# NAME:         Michael Usher
# ASSIGNMENT:   Project 3: Arrays & Maps

# Write a function called multiplication_table that
# takes a width, height, & scaling factor as parameters
# and returns a two-dimensional array multiplication
# table scaled by the scaling factor.
# You should not be using any functions other than range.
def multiplication_table(w, h, s): #multiplication table
    result = []
    for i in range(1, h + 1):
        tmp = []
        for j in range(1, w + 1):
            tmp.append(i * j * s)
        result.append(tmp)
    return result

def print_2D(b): #prints it
    for i in range(len(b)):
        print(b[i])

def main(): #tests it
    print("5 3 1:")
    print_2D(multiplication_table(5, 3, 1))
    print("5 3 2:")
    print_2D(multiplication_table(5, 3, 2))
    print("25 3 10:")
    print_2D(multiplication_table(25, 3, 10))
    print("10 10 1:")
    print_2D(multiplication_table(10, 10, 1))
    print("0 1 4:")
    print_2D(multiplication_table(0, 1, 4))
    print("1 0 4:")
    print_2D(multiplication_table(1, 0, 4))
    print("0 0 4:")
    print_2D(multiplication_table(0, 0, 4))
    print("1 1 4:")
    print_2D(multiplication_table(1, 1, 4))
    print("1 1 0:")
    print_2D(multiplication_table(1, 1, 0))
    print("1 1 -1:")
    print_2D(multiplication_table(1, 1, -1))
    print("5 3 -2:")
    print_2D(multiplication_table(5, 3, -2))
    print("10 10 -3:")
    print_2D(multiplication_table(10, 10, -3))

if __name__ == '__main__':
    main()