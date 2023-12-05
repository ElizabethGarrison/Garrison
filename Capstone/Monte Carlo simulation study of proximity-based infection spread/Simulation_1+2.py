import numpy as np
import matplotlib.pyplot as plt

# Constants
num_centers = 5  # Number of population centers
population_density = 10000  # walkers per km^2
area = 1  # km^2
N = population_density * area  # total population

# Generate random population centers
np.random.seed(42)
centers = np.random.rand(num_centers, 2) * np.sqrt(area)

# Function to simulate random walk around population centers
def random_walk(steps, step_length):
    # Initialize positions randomly around population centers
    positions = np.random.rand(N, 2) * np.sqrt(area)
    
    # Infection starts at the center of the area
    center_infection = np.linalg.norm(positions - np.sqrt(area) / 2, axis=1) <= 0.1
    
    # Simulation loop
    for step in range(steps):
        # Random step direction and length
        angles = 2 * np.pi * np.random.rand(N)
        dx = np.cos(angles) * step_length
        dy = np.sin(angles) * step_length
        
        # Update positions
        positions[:, 0] += dx
        positions[:, 1] += dy
        
        # Reflect boundary conditions
        positions[positions < 0] *= -1
        positions[positions > np.sqrt(area)] = 2 * np.sqrt(area) - positions[positions > np.sqrt(area)]
        
        # Calculate distances to population centers
        for center in centers:
            distances = np.linalg.norm(positions - center, axis=1)
            infections = distances <= 0.2  # Assuming 0.2 km as touching distance
            center_infection = np.logical_or(center_infection, infections)
        
        # Check simulation termination condition for SI model (95% infected)
        if np.sum(center_infection) >= 0.95 * N:
            return positions, center_infection, step  # Return positions, infection status, and termination step
    
    return positions, center_infection, steps  # Return positions, infection status, and final step if termination condition not met

# Simulation parameters
steps = 1000  # Number of steps in the simulation

# Run simulations for Case 1: Varying step lengths (r/2, r/4, r/5)
step_lengths = [0.5, 0.25, 0.2]  # step lengths as fractions of r
results_case1 = []

for step_length_factor in step_lengths:
    step_length = step_length_factor * np.sqrt(area)  # Length of random walk steps
    walker_positions, infections_over_time, termination_step = random_walk(steps=steps, step_length=step_length)
    results_case1.append((walker_positions, infections_over_time, termination_step, step_length))

# Plotting for Case 1
plt.figure(figsize=(12, 8))
plt.subplot(2, 2, 1)

for center in centers:
    plt.scatter(center[0], center[1], color='red', marker='o', label='Population Center')

for result in results_case1:
    walker_positions, infections_over_time, _, step_length = result
    plt.scatter(walker_positions[:, 0], walker_positions[:, 1], c=infections_over_time, cmap='cool', alpha=0.5, label=f'Infected Walkers, Step Length={step_length:.2f}')

plt.xlabel('X')
plt.ylabel('Y')
plt.title('2D Random Walk - Infection Spread around Population Centers (Case 1)')
plt.legend()
plt.grid(True)

# Print results for Case 1
print("Results for Case 1:")
for idx, result in enumerate(results_case1):
    _, _, termination_step, step_length = result
    print(f"Step Length {idx + 1} ({step_length:.2f} km): Infection termination at step {termination_step}")

# Run simulations for Case 2: SIRS infection model with different recovery rates
recovery_rates = [0.0002, 0.001, 0.005]  # Recovery rates
results_case2 = []

for recovery_rate in recovery_rates:
    center_infection = np.zeros(N, dtype=bool)  # Define center_infection here
    
    # Assume a portion of the recovered population is susceptible to reinfection
    susceptible_reinfected = int(0.05 * N)
    recovered_pop = np.zeros(N, dtype=bool)
    recovered_pop[:susceptible_reinfected] = True
    
    for _ in range(steps):
        # Randomly select recovered individuals susceptible to reinfection
        np.random.shuffle(recovered_pop)
        reinfect_indices = np.where(recovered_pop)[0][:susceptible_reinfected]
        
        # Recover and reinfect susceptible individuals
        recovered_pop[reinfect_indices] = False
        recovered_pop = np.logical_or(recovered_pop, np.random.rand(N) < recovery_rate)
        
        # Calculate distances to population centers
        for center in centers:
            distances = np.linalg.norm(walker_positions - center, axis=1)
            infections = distances <= 0.2  # Assuming 0.2 km as touching distance
            infections = np.logical_and(infections, np.logical_not(recovered_pop))
            center_infection = np.logical_or(center_infection, infections)
        
        # Check simulation termination condition for SIRS model (95% infected)
        if np.sum(center_infection) >= 0.95 * N:
            results_case2.append((walker_positions, center_infection, recovery_rate))
            break

# Plotting for Case 2
plt.subplot(2, 2, 2)

for center in centers:
    plt.scatter(center[0], center[1], color='red', marker='o', label='Population Center')

for result in results_case2:
    walker_positions, infections_over_time, recovery_rate = result
    plt.scatter(walker_positions[:, 0], walker_positions[:, 1], c=infections_over_time, cmap='cool', alpha=0.5, label=f'Infected Walkers, Recovery Rate={recovery_rate:.4f}')

plt.xlabel('X')
plt.ylabel('Y')
plt.title('2D Random Walk - Infection Spread around Population Centers (Case 2)')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
