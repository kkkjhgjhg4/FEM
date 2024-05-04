import numpy as np
import matplotlib.pyplot as plt
from Elasticity2D import FERun
from Exact import ErrorNorm_4_12

# Json data files for meshes
files = ("./Convergence/exercise_4_12_5Elem.json", 
         "./Convergence/exercise_4_12_20Elem.json", 
         "./Convergence/exercise_4_12_80Elem.json", 
         "./Convergence/exercise_4_12_320Elem.json")    

  

# Run FE analysis for all files using meshed
n = len(files)
h = np.zeros(n)
L2Norm = np.zeros(n)
EnergyNorm = np.zeros(n)
for i in range(n):
    FERun(files[i])

    # Calculate error norms for convergence study
    h[i], L2Norm[i], EnergyNorm[i] = ErrorNorm_4_12()


fig, axs = plt.subplots(2, 1, figsize=(8, 8)) 

# L2-Norm error and h figure
axs[0].set_title('L2 error in logarithmic scale', fontsize=10)
axs[0].set_ylabel('L2 Error', fontsize=9)
axs[0].set_xscale('log') 
axs[0].set_yscale('log') 
axs[0].plot(h, L2Norm, marker='o') 
axs[0].grid(True, which="both", ls="--") 
slope_L2, intercept_L2 = np.polyfit(np.log(h), np.log(L2Norm), 1)
print(f"L2 Error Linear Regression (log-log scale): Slope = {slope_L2}, Intercept = {np.exp(intercept_L2)}")

# Energy Norm error and h figure
axs[1].set_title('Energy Norm error logarithmic scale', fontsize=10)
axs[1].set_ylabel('Energy Norm Error', fontsize=9)
axs[1].set_xscale('log') 
axs[1].set_yscale('log') 
axs[1].plot(h, EnergyNorm, marker='o', color='red') 
axs[1].grid(True) 
slope_Energy, intercept_Energy = np.polyfit(np.log(h), np.log(EnergyNorm), 1)
print(f"Energy Norm Error Linear Regression: Slope = {slope_Energy}, Intercept = {intercept_Energy}")

plt.tight_layout() 
plt.show() 