import numpy as np
import matplotlib.pyplot as plt

# Gauss quadrature
def gauss(ngp):
    # This function now ensures that 'gp' and 'w' are NumPy arrays
    if ngp == 1:
        gp = np.array([0])
        w = np.array([2])
    elif ngp == 2:
        gp = np.array([-np.sqrt(1/3), np.sqrt(1/3)])
        w = np.array([1, 1])
    elif ngp == 3:
        gp = np.array([-np.sqrt(3/5), 0, np.sqrt(3/5)])
        w = np.array([5/9, 8/9, 5/9])
    elif ngp == 4:
        gp = np.array([-np.sqrt((3+2*np.sqrt(6/5))/7), -np.sqrt((3-2*np.sqrt(6/5))/7), 
                        np.sqrt((3-2*np.sqrt(6/5))/7), np.sqrt((3+2*np.sqrt(6/5))/7)])
        w = np.array([(18-np.sqrt(30))/36, (18+np.sqrt(30))/36, 
                      (18+np.sqrt(30))/36, (18-np.sqrt(30))/36])
    else:
        print("Invalid number of Gauss points specified. Only supports 1 to 4 Gauss points.")
        return None, None
    
    return w, gp



def calculate_error(number_of_elements, x_element_steps=1000):
    element_length = 1 / number_of_elements
    x_global_coordinate = np.linspace(0, 1, x_element_steps * number_of_elements)
    
    # Get Gauss points and weights
    w, gp = gauss(4)
    
    total_error = 0
    
    for i in range(number_of_elements):
        # Transform Gauss points to the current element's domain
        x_gp = 0.5 * (1 + gp) * element_length + i * element_length
        
        # Calculate the estimated and real displacements at Gauss points
        ue1 = np.power(x_gp[0], 3)
        ue2 = np.power(x_gp[-1], 3)
        estimated_disp = ((x_gp[-1] - x_gp) * ue1 + (x_gp - x_gp[0]) * ue2) / element_length
        real_disp = np.power(x_gp, 3)
        
        # Calculate error for the current element using Gauss quadrature
        error = np.sum(w * np.power(estimated_disp - real_disp, 2)) * element_length / 2
        total_error += error
    
    return total_error

# Plot function
def plot_log_error(number_of_elements):
    # Initialize arrays for errors and log lengths
    errors = np.zeros(len(number_of_elements))
    log_lengths = np.zeros(len(number_of_elements))
    
    # Calculate errors for each number of elements
    for i, n in enumerate(number_of_elements):
        error = calculate_error(number_of_elements = n) 
        element_length = 1 / n
        errors[i] = error
        log_lengths[i] = np.log(element_length)
    
    log_errors = np.log(errors)

    # Plot
    plt.figure(figsize=(10, 6))
    plt.plot(log_lengths, log_errors, marker='o', linestyle='-')
    plt.xlabel('Log of Element Length')
    plt.ylabel('Log of L2-norm Error')
    plt.title('Log-Log Plot of L2-norm Error vs Element Length')
    plt.grid(True)
    plt.show()


# Calculate and plot error
plot_log_error(np.array([2, 4, 8]))



