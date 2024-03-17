import numpy as np


def function_value(excersice, x, *argv):
    match excersice:
        case 3.1 :
            index = 0
            a = np.zeros(1)
            for arg in argv:
                a[index] = arg
                index = index + 1
            real_solution = 3 - 2.19595 * np.sin(2 * x)
            trail_solution = 3 - 2 * x + a[0] * (x**2 - x)
        case 3.2 :
            index = 0
            a = np.zeros(2)
            for arg in argv:
                a[index] = arg
                index = index + 1
            real_solution = 4 * (np.exp(-2 * x) - 1) + 8 * x
            trail_solution = a[0] * x + a[1] * x**2
    return real_solution, trail_solution
        
def error(real_solution, trail_solution):
    error = np.abs(real_solution - trail_solution) / real_solution
    return error

print('-----------Error of exercise 3.1-----------')

real, trail = function_value(3.1, 0.5, 4)
print("Collocation Method: Error(x=0.5) = ", error(real, trail))
real, trail = function_value(3.1, 0.7, 4)
print("Collocation Method: Error(x=0.7) = ", error(real, trail))

real, trail = function_value(3.1, 0.5, 48/13)
print("Subdomain Method: Error(x=0.5) = ", error(real, trail))
real, trail = function_value(3.1, 0.7, 48/13)
print("Subdomain Method: Error(x=0.7) = ", error(real, trail))


real, trail = function_value(3.1, 0.5, 20/7)
print("Galerkin Method: Error(x=0.5) = ", error(real, trail))
real, trail = function_value(3.1, 0.7, 20/7)
print("Galerkin Method: Error(x=0.7) = ", error(real, trail))

real, trail = function_value(3.1, 0.5, 90/37)
print("Least Squares Method: Error(x=0.5) = ", error(real, trail))
real, trail = function_value(3.1, 0.7, 90/37)
print("Least Squares Method: Error(x=0.7) = ", error(real, trail))

real, trail = function_value(3.1, 0.5, 32/9)
print("Least Squares Collation Method: Error(x=0.5) = ", error(real, trail))
real, trail = function_value(3.1, 0.7, 32/9)
print("Least Squares Collation Method: Error(x=0.7) = ", error(real, trail))

print('-----------Error of exercise 3.2-----------')

real, trail = function_value(3.2, 0.5, 808/569, 1856/569)
print("Least Squares Collation Method: Error(x=0.5) = ", error(real, trail))
real, trail = function_value(3.2, 0.7, 808/569, 1856/569)
print("Least Squares Collation Method: Error(x=0.7) = ", error(real, trail))

real, trail = function_value(3.2, 0.5, 12/7, 20/7)
print("Galerkin Method: Error(x=0.5) = ", error(real, trail))
real, trail = function_value(3.2, 0.7, 12/7, 20/7)
print("Galerkin Method: Error(x=0.7) = ", error(real, trail))


