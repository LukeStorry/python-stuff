###################################################
# Luke Storry
#
# User: LS14172
# Candidate Number: 14609
#
# COMS30127 - Coursework 1 - auto-associative networks
# Hopfield network, using seven_segment_p3.py
###################################################


from math import *


def seven_segment(pattern):

    def to_bool(a):
        if a == 1:
            return True
        return False

    def hor(d):
        if d:
            print(" _ ")
        else:
            print("   ")

    def vert(d1, d2, d3):
        word = ""

        if d1:
            word = "|"
        else:
            word = " "

        if d3:
            word += "_"
        else:
            word += " "

        if d2:
            word += "|"
        else:
            word += " "

        print(word)

    pattern_b = list(map(to_bool, pattern))

    hor(pattern_b[0])
    vert(pattern_b[1], pattern_b[2], pattern_b[3])
    vert(pattern_b[4], pattern_b[5], pattern_b[6])

    number = 0
    for i in range(0, 4):
        if pattern_b[7 + i]:
            number += pow(2, i)
    print(int(number))


def hopfield(pattern_list, nodes):
    n = len(nodes)

    weight_matrix = [[0.0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                for a in pattern_list:
                    weight_matrix[i][j] += a[i] * a[j]
                weight_matrix[i][j] /= len(pattern_list)

    def update(nodes):
        out = [0 for _ in range(n)]
        for i in range(n):
            for j in range(n):
                out[i] += weight_matrix[i][j] * nodes[j]
            out[i] = 1 if out[i] >= 0 else -1
        return out

    while True:
        new_nodes = update(nodes)
        if nodes == new_nodes:
            break
        seven_segment(new_nodes)
        nodes = new_nodes


six = [1, 1, -1, 1, 1, 1, 1, -1, 1, 1, -1]
three = [1, -1, 1, 1, -1, 1, 1, 1, 1, -1, -1]
one = [-1, -1, 1, -1, -1, 1, -1, 1, -1, -1, -1]

seven_segment(three)
seven_segment(six)
seven_segment(one)


print("test1")

test = [1, -1, 1, 1, -1, 1, 1, -1, -1, -1, -1]

seven_segment(test)

# here the network should run printing at each step
hopfield([three, six, one], test)

print("test2")

test = [1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1]

seven_segment(test)

# here the network should run printing at each step
hopfield([three, six, one], test)
