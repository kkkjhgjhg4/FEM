#! usr/bin/env/python3
import numpy as np

def calculate_constraining_force(node_index, node_elem_number, *forces): # node_elem_numer is the number of elements of the node you want to calculate the constraining force\
                                                             # forces must in order of global degree of freedom
    node_force = np.zeros(node_elem_number * 2)
    index = 0
    for force in forces:
        node_force[index] = force
        index = index + 1
    cos = 20 / np.sqrt(20**2 + 10**2)
    sin = 10 / np.sqrt(20**2 + 10**2)
    match int(node_index):
        case 1:
            constraining_force_x = -(node_force[0] * 0 + node_force[1] * cos + node_force[2] * 1)
            constraining_force_y = -(node_force[0] * 1 + node_force[1] * sin + node_force[2] * 0)
        case 3:
            constraining_force_x = 0.0
            constraining_force_y = -(node_force[0] * sin + node_force[1] * 0 + node_force[2] * 1)
    return constraining_force_x, constraining_force_y

def calculate_resultant(load_x, load_y, constraining_forces):
    resultant_x = 0.0
    resultant_y = 0.0
    for x_index in range(0, constraining_forces.size, 2):
        resultant_x = constraining_forces[x_index] + resultant_x
    resultant_x = resultant_x + load_x
    for y_index in range(1, constraining_forces.size, 2):
        resultant_y = constraining_forces[y_index] + resultant_y
    resultant_y = resultant_y + load_y

    return resultant_x, resultant_y



constraining_x_1, constraining_y_1 = calculate_constraining_force(1, 3, -2.31867e-01, -5.99564e-01, 5.36266e-01)
constraining_x_3, constraining_y_3 = calculate_constraining_force(3, 3, -5.99564e-01, 5.36266e-01, -2.31867e-01)

constraining_forces = np.array([constraining_x_1, constraining_y_1, constraining_x_3, constraining_y_3])

resultant_x, resultant_y = calculate_resultant(0, -1, constraining_forces)

print('resultant_x = ', resultant_x, 'resultant_y = ', resultant_y)

if resultant_x < 10**(-5) and resultant_y < 10 ** (-5):
    print('Resultant forces are below e-5, can be regarded as balanced!')