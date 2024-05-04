import numpy as np
import matplotlib.pyplot as plt

# draw theoretical solution
def v(x):
    return -0.024 * x**2

def sigma_x(y):
    return 480 * y

def plot_theo():
    x = np.linspace(0, 5, 100)


    v_values = v(x)

    y = np.sqrt(3)/12
    sigma_x_value = sigma_x(y)


    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.plot(x, v_values, label='v(x) = -0.024x^2')
    plt.title('Plot of v(x) = -0.024x^2')
    plt.xlabel('x')
    plt.ylabel('v(x)')
    plt.grid(True)
    plt.legend()


    plt.subplot(1, 2, 2)
    plt.axhline(y=sigma_x_value, color='r', label=f'sigma_x(x) = 480y, y={y}')
    plt.title('Plot of sigma_x(x) = 480y')
    plt.xlabel('x')
    plt.ylabel('sigma_x(x)')
    plt.ylim(0, 500)  
    plt.grid(True)
    plt.legend()

    plt.show()

# draw 1*5 v disp
def plot_5Elem_full():
    x=[0,1,2,3,4,5]
    v=[0.0, -0.008, -0.032, -0.072, -0.128, -0.2]
    x_sxx=[1, 2, 3, 4, 5]
    sxx=[23.0940107351, 23.0940107351, 23.0940107351, 23.0940107351,23.0940107351]
    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.plot(x, v, label='v displacement')
    plt.title('Plot of v displacement')
    plt.xlabel('x')
    plt.ylabel('v')
    plt.grid(True)
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.plot(x_sxx, sxx, 'r-o', label='stress')
    plt.title('Plot of stress at gauss points')
    plt.xlabel('x')
    plt.ylabel('stress')
    plt.grid(True)
    plt.legend()

    plt.show()

def plot_5Elem_reduced():
    x=[0,1,2,3,4,5]
    v=[0.0, -0.008, -0.032, -0.072, -0.128, -0.2]
    x_sxx=[1, 2, 3, 4, 5]
    sxx=[23.0940107351, 23.0940107351, 23.0940107351, 23.0940107351,23.0940107351]
    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.plot(x, v, label='v displacement')
    plt.title('Plot of v displacement')
    plt.xlabel('x')
    plt.ylabel('v')
    plt.grid(True)
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.plot(x_sxx, sxx, 'r-o', label='stress')
    plt.title('Plot of stress at gauss points')
    plt.xlabel('x')
    plt.ylabel('stress')
    plt.grid(True)
    plt.legend()

    plt.show()


# draw 2*5 v disp
def plot_10Elem_full():
    x=[0,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5]
    v=[0.0,-3.33333333e-04, -1.33333333e-03, -3.00000000e-03, -5.33333333e-03, -8.33333333e-03, -1.20000000e-02, -1.63333333e-02, -2.13333333e-02, -2.70000000e-02, -3.33333333e-02]
    x_sxx=[1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
    sxx=[5.25783422965,5.25783422965,5.25783422965,5.25783422965,5.25783422965,5.25783422965,5.25783422965,5.25783422965,5.25783422965]
    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.plot(x, v, label='v displacement')
    plt.title('Plot of v displacement')
    plt.xlabel('x')
    plt.ylabel('v')
    plt.grid(True)
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.plot(x_sxx, sxx, 'r-o', label='stress')
    plt.title('Plot of stress at gauss points')
    plt.xlabel('x')
    plt.ylabel('stress')
    plt.grid(True)
    plt.legend()

    plt.show()


plot_5Elem_reduced()

