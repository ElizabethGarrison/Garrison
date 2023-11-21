import math
import random
import statistics
import matplotlib.pyplot as plt

# Function for a single step in a random direction
def walk():
    direction = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])  # North, South, East, West movements
    return direction

# Function to perform a random walk for n steps
def random_walk(steps):
    x, y = 0, 0  # Starting coordinates
    for _ in range(steps):
        direction = walk()
        x += direction[0]
        y += direction[1]
    # Calculate the distance from the original location after n steps
    distance = math.sqrt(x**2 + y**2)
    return distance

# Function to run the simulation multiple times (50 times in this case)
def run_simulation(runs, steps):
    distances = []
    for _ in range(runs):
        distance = random_walk(steps)
        distances.append(distance)
    return distances

# Perform 50 simulations with 10,000 steps each
simulations = run_simulation(50, 10000)

# Calculate required statistics
mean_distance = statistics.mean(simulations)
longest_distance = max(simulations)
shortest_distance = min(simulations)
confidence_interval = statistics.stdev(simulations) * 1.96 / math.sqrt(len(simulations))

# Plotting a histogram of distances in pink color
plt.hist(simulations, bins=20, alpha=0.7, color='pink')
plt.xlabel('Distance')
plt.ylabel('Frequency')
plt.title('Distribution of Distances after 10,000 Steps')
plt.grid(True)
plt.show()

# Displaying results
print(f"Mean distance after 10,000 steps: {mean_distance:.2f}")
print(f"Longest distance after 10,000 steps: {longest_distance:.2f}")
print(f"Shortest distance after 10,000 steps: {shortest_distance:.2f}")
print(f"Confidence interval for mean distance (95%): +/- {confidence_interval:.2f}")
