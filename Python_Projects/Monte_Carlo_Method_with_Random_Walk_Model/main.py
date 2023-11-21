import numpy as np
import matplotlib.pyplot as plt
import statistics

def random_walk_diffusion(steps):
    particle_positions = np.zeros((steps + 1, 10000, 2))

    for i in range(1, steps + 1):
        steps_x = np.random.normal(0, 1, 10000)
        steps_y = np.random.normal(0, 1, 10000)

        particle_positions[i, :, 0] = particle_positions[i - 1, :, 0] + steps_x
        particle_positions[i, :, 1] = particle_positions[i - 1, :, 1] + steps_y

    return particle_positions

def random_walk_advection_diffusion(steps, velocity):
    particle_positions = np.zeros((steps + 1, 10000, 2))

    for i in range(1, steps + 1):
        steps_x = np.random.normal(0, 1, 10000)
        steps_y = np.random.normal(0, 1, 10000)

        particle_positions[i, :, 0] = particle_positions[i - 1, :, 0] + steps_x + velocity[0]
        particle_positions[i, :, 1] = particle_positions[i - 1, :, 1] + steps_y + velocity[1]

    return particle_positions

def calculate_statistics(particle_positions):
    distances = []
    for i in range(1, len(particle_positions)):
        distance = np.linalg.norm(particle_positions[i], axis=1)
        distances.append(distance)

    mean_distance = np.mean(distances[-1])
    longest_distance = np.max(distances[-1])
    shortest_distance = np.min(distances[-1])
    confidence_interval = 1.96 * np.std(distances[-1]) / np.sqrt(len(distances[-1]))
    
    return mean_distance, longest_distance, shortest_distance, confidence_interval

def plot_distribution(particle_positions, step, advection=False):
    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    plt.scatter(particle_positions[step][:, 0], particle_positions[step][:, 1], s=5, color='pink')
    if advection:
        plt.title(f'Particle Distribution with Velocity after {step} steps')
    else:
        plt.title(f'Particle Distribution after {step} steps')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.grid(True)

    plt.subplot(1, 2, 2)
    plt.hist2d(particle_positions[step][:, 0], particle_positions[step][:, 1], bins=50, cmap='RdGy')
    plt.colorbar(label='Number of Particles')
    if advection:
        plt.title(f'2D Histogram with Velocity after {step} steps')
    else:
        plt.title(f'2D Histogram after {step} steps')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')

    plt.tight_layout()
    plt.show()

diffusion_positions = random_walk_diffusion(200)
plot_distribution(diffusion_positions, 50)
plot_distribution(diffusion_positions, 100)
plot_distribution(diffusion_positions, 150)
plot_distribution(diffusion_positions, 200)

velocity = (0.1, 0.1)
advection_positions = random_walk_advection_diffusion(200, velocity)
plot_distribution(advection_positions, 50, advection=True)
plot_distribution(advection_positions, 100, advection=True)
plot_distribution(advection_positions, 150, advection=True)
plot_distribution(advection_positions, 200, advection=True)

# Calculate and print results for diffusion process
diffusion_results = calculate_statistics(diffusion_positions)
print("Results for Diffusion Process:")
print(f"Mean distance after 200 steps: {diffusion_results[0]:.2f}")
print(f"Longest distance after 200 steps: {diffusion_results[1]:.2f}")
print(f"Shortest distance after 200 steps: {diffusion_results[2]:.2f}")
print(f"Confidence interval for mean distance after 200 steps (95%): +/- {diffusion_results[3]:.2f}")

# Calculate and print results for advection-diffusion process
advection_results = calculate_statistics(advection_positions)
print("\nResults for Advection-Diffusion Process:")
print(f"Mean distance after 200 steps with velocity: {advection_results[0]:.2f}")
print(f"Longest distance after 200 steps with velocity: {advection_results[1]:.2f}")
print(f"Shortest distance after 200 steps with velocity: {advection_results[2]:.2f}")
print(f"Confidence interval for mean distance after 200 steps with velocity (95%): +/- {advection_results[3]:.2f}")
