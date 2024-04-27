import numpy as np

# Define the matrices B^1 and B^2
B1 = 0.5 * np.array([
    [-0.5, 0, 1, 0, -0.5, 0],
    [0, -2, 0, 0, 0, 2],
    [-2, -0.5, 0, 1, 2, -0.5]
])

B2 = 1.0 * np.array([
    [-0.5, 0, 0, 0, 0.5, 0],
    [0, 0, 0, -2, 0, 2],
    [0, -0.5, -2, 0, 2, 0.5]
])

# Define the matrix D
D = 3.3e7 * np.array([
    [1, 0.3, 0],
    [0.3, 1, 0],
    [0, 0, 0.35]
])

# Areas and thickness (assuming t^e = 1 for both elements)
A1, t1 = 1, 1
A2, t2 = 0.5, 1

# Calculate K^1 and K^2
K1 = A1 * t1 * B1.T @ D @ B1
K2 = A2 * t2 * B2.T @ D @ B2

# Define L^1 and L^2 matrices
L1 = np.array([
    [1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0]
])

L2 = np.array([
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 1]
])

# Create an empty global stiffness matrix K of appropriate size (8x8 given L1 and L2)
K = np.zeros((8, 8))

# Compute contributions from K1 and K2
K += L1.T @ K1 @ L1
K += L2.T @ K2 @ L2

print("Global Stiffness Matrix K:")
print(K)


# Define matrices and vectors
K_F = 10**6 * np.array([
    [31.35, 0, -23.1, -5.775],
    [0, 68.8875, -4.95, -66],
    [-23.1, -4.95, 27.225, 10.725],
    [-5.775, -66, 10.725, 67.44375]
])

K_FE = 10**6 * np.array([
    [-4.125, -4.95, -4.125, 10.725],
    [-5.775, -1.44375, 10.725, -1.44375],
    [0, 0, -4.125, -5.775],
    [0, 0, -4.95, -1.44375]
])

f_F = np.array([0, 0, 0, -20])

d_E = np.array([0, 0, 0, 0])

# Compute d_F
d_F = np.linalg.solve(K_F, f_F - np.dot(K_FE, d_E))

# Define additional matrices and vectors for r_E calculation
K_E = 10**6 * np.array([
    [13.6125, 5.3625, -9.4875, 0.4125],
    [5.3625, 33.721875, -0.4125, -32.278125],
    [-9.4875, -0.4125, 17.7375, -5.3625],
    [0.4125, -32.278125, -5.3625, 35.165625]
])

K_EF = 10**6 * np.array([
    [-4.125, -5.775, 0, 0],
    [-4.95, -1.44375, 0, 0],
    [-4.125, 10.725, -4.125, -4.95],
    [10.725, -1.44375, -5.775, -1.44375]
])

f_E = np.array([0, 0, 0, -20])

# Compute r_E
r_E = np.dot(K_E, d_E) + np.dot(K_EF, d_F) - f_E

# Output the results
print("Displacements d_F:", d_F)
print("Reactions r_E:", r_E)

# Define the material properties matrix D^e
D_e = 3.3e7 * np.array([
    [1, 0.3, 0],
    [0.3, 1, 0],
    [0, 0, 0.35]
])

# Define the deformation matrices B^1 and B^2
B1 = 0.5 * np.array([
    [-0.5, 0, 1, 0, -0.5, 0],
    [0, -2, 0, 0, 0, 2],
    [-2, -0.5, 0, 1, 2, -0.5]
])

B2 = 1.0 * np.array([
    [-0.5, 0, 0, 0, 0.5, 0],
    [0, 0, 0, -2, 0, 2],
    [0, -0.5, -2, 0, 2, 0.5]
])

# Define the displacement vectors d^1 and d^2
d1 = 1e-6 * np.array([0, 0, 0, 0, -0.386714096, -6.65018257])
d2 = 1e-6 * np.array([0, 0, -0.386714096, -6.65018257, 1.23358547, -7.03364697])

# Calculate sigma^1 and sigma^2
sigma1 = D_e @ B1 @ d1
sigma2 = D_e @ B2 @ d2

# Print the results
print("Stress vector sigma^1:", sigma1)
print("Stress vector sigma^2:", sigma2)


# Define the displacement vectors d^h_F and d^F
d_h_F = np.array([-3.87100810e-07, -6.65683275e-06, 1.23481905e-06, -7.04068062e-06])
d_F = np.array([-3.86714096e-07, -6.65018257e-06, 1.23358547e-06, -7.03364697e-06])

# Calculate the absolute difference
difference = np.abs(d_h_F - d_F)

# Calculate the absolute values of d_F to avoid division by zero issues
absolute_d_F = np.abs(d_F)

# Calculate the error
error = difference / absolute_d_F

# Print the error
print("Error:", error)

