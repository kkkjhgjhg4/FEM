import numpy as np
import matplotlib.pyplot as plt



def calculate_displacements(number_of_elements, x_element_steps=1000, plot = False):
    # Calculate the element length and coordinate steps
    element_length = 1 / number_of_elements
    x_element_coordinate = np.linspace(0, element_length, x_element_steps)
    
    # Global coordinates
    x_global_coordinate = np.linspace(0, 1, x_element_steps * number_of_elements)

    # Estimated displacement for one element
    def estimated_displacement_element(x_element_coordinate):
        displacement = np.zeros_like(x_element_coordinate)
        xe2 = x_element_coordinate[-1]
        xe1 = x_element_coordinate[0]
        ue1 = np.power(xe1, 3)
        ue2 = np.power(xe2, 3)
        
        for i, x in enumerate(x_element_coordinate):
            displacement[i] = ((xe2 - x) * ue1 + (x - xe1) * ue2) / element_length
        return displacement
    
    # Real displacement for global coordinates
    def real_displacement_global(x_global_coordinate):
        return np.power(x_global_coordinate, 3)

    # Calculate and concatenate estimated displacement for each element
    estimated_disp_global = np.concatenate([
        estimated_displacement_element(x_element_coordinate + i * element_length) 
        for i in range(number_of_elements)
    ])

    # Real displacement for the entire domain
    real_disp_global = real_displacement_global(x_global_coordinate)
    
    # Plotting
    if plot:
        plot_displacement(estimated_disp_global, real_disp_global, x_global_coordinate)

    #return estimated_disp_global, real_disp_global 


def calculate_strains(number_of_elements, x_element_steps=1000, plot = False):
    # Calculate the element length and coordinate steps
    element_length = 1 / number_of_elements
    x_element_coordinate = np.linspace(0, element_length, x_element_steps)
    
    # Global coordinates
    x_global_coordinate = np.linspace(0, 1, x_element_steps * number_of_elements)

    # Estimated strain for one element
    def estimated_strain_element(x_element_coordinate):
        xe1 = x_element_coordinate[0]
        xe2 = x_element_coordinate[-1]
        ue1 = np.power(xe1, 3)
        ue2 = np.power(xe2, 3)
        strain = (ue2 - ue1) / element_length
        return np.full_like(x_element_coordinate, strain)
    
    # Real strain for global coordinates
    def real_strain_global(x_global_coordinate):
        return 3 * np.power(x_global_coordinate, 2)

    # Calculate and concatenate estimated strain for each element
    estimated_strain_global = np.concatenate([
        estimated_strain_element(x_element_coordinate + i * element_length) 
        for i in range(number_of_elements)
    ])

    # Real strain for the entire domain
    real_strain_global = real_strain_global(x_global_coordinate)
    
    # Plotting
    if plot:
        plot_strain(estimated_strain_global, real_strain_global, x_global_coordinate)

    #return estimated_strain_global, real_strain_global


# Plot functions
def plot_displacement(estimated_disp_global, real_disp_global, x_global_coordinate):
    plt.figure(figsize=(10, 6))
    plt.plot(x_global_coordinate, real_disp_global, label='Real Displacement')
    plt.plot(x_global_coordinate, estimated_disp_global, '--', label='Estimated Displacement')
    plt.legend()
    plt.xlabel('X Coordinate')
    plt.ylabel('Displacement Value')
    plt.title('Real vs Estimated Displacement')
    plt.show()

def plot_strain(estimated_strain_global, real_strain_global, x_global_coordinate):
    plt.figure(figsize=(10, 6))
    plt.plot(x_global_coordinate, real_strain_global, label='Real Strain')
    plt.plot(x_global_coordinate, estimated_strain_global, '--', label='Estimated Strain')
    plt.legend()
    plt.xlabel('X Coordinate')
    plt.ylabel('Strain Value')
    plt.title('Real vs Estimated Strain')
    plt.show()





# Calculate displacements for a unit length bar divided into any number of elements
calculate_displacements(2, plot=True)  
# calculate_displacements(4)  
#calculate_displacements(number_of_elements=8, plot=True)  

# Calculate strains for a unit length bar divided into any number of elements
calculate_strains(2)
# calculate_strains(4)
# calculate_strains(number_of_elements=8 , plot=True)

