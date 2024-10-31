import numpy as np
import matplotlib.pyplot as plt

# Define the system of differential equations
def dBdt(B, F):
    return 0.05 * B * ((B - 3000) / (B + 3000)) * (1 - B / 150000) - 1e-8 * B * F

def dFdt(B, F):
    return 0.08 * F * ((F - 15000) / (F + 15000)) * (1 - F / 400000) - 1e-8 * B * F

# Implement Euler's method
def euler_method(B0, F0, T, num_steps):
    h = T / num_steps  # Step size
    t_values = np.linspace(0, T, num_steps + 1)
    B_values = np.zeros(num_steps + 1)
    F_values = np.zeros(num_steps + 1)
    
    # Initial conditions
    B_values[0] = B0
    F_values[0] = F0
    
    # Euler method loop
    for i in range(num_steps):
        dB = dBdt(B_values[i], F_values[i])
        dF = dFdt(B_values[i], F_values[i])
        B_values[i + 1] = B_values[i] + h * dB
        F_values[i + 1] = F_values[i] + h * dF
    
    return t_values, B_values, F_values

# Initial conditions
B0 = 5000  # Initial blue whale population
F0 = 70000  # Initial fin whale population

# Parameters for simulations
params = [(1000, 50), (1000, 100), (2000, 50)]

# Perform simulations and plot results
for num_steps, T in params:
    t_values, B_values, F_values = euler_method(B0, F0, T, num_steps)
    
    plt.figure(figsize=(10, 6))
    plt.plot(t_values, B_values, label="Blue Whales (B)", color="blue")
    plt.plot(t_values, F_values, label="Fin Whales (F)", color="green")
    plt.title(f"Population Dynamics of Whales (N = {num_steps}, T = {T})")
    plt.xlabel("Time (years)")
    plt.ylabel("Population")
    plt.legend()
    plt.grid(True)
    plt.show()

################################################

# Define parameters for simulations
params = [
    [(4000, 16000), (3000, 16000), (4000, 15000), (3000, 15000)],  # Initial conditions
    (1000, 50)  # (numSteps, T)
]

# Specify colors for plotting
colors = ['red', 'green', 'blue', 'orange']

# Perform simulations and collect results for multiple initial conditions
data = []
for j, initial_conditions in enumerate(params[0]):
    B0, F0 = initial_conditions
    num_steps, T = params[1]
    t_values, B_values, F_values = euler_method(B0, F0, T, num_steps)
    data.append(np.column_stack((B_values, F_values)))

# Plot combined results
for j in range(len(data)):
    plt.plot(data[j][:, 0], data[j][:, 1], label=f"B0 = {params[0][j][0]}, F0 = {params[0][j][1]}", color=colors[j])

plt.title("Population Dynamics of Whales")
plt.xlabel("Blue Whales (B)")
plt.ylabel("Fin Whales (F)")
plt.legend()
plt.grid(True)
plt.show()
