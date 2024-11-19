import pygad
import numpy as np
import matplotlib.pyplot as plt

# Define the fitness function


def fitness_function(ga_instance, solution, solution_idx):
    temperature, pressure, oxygen_to_biomass, reaction_time = solution
    hydrogen_yield = (temperature * 0.01) + (pressure * 0.02) + \
        (oxygen_to_biomass * 0.03) + (reaction_time * 0.05)

    # Penalize for out-of-range values
    if temperature < 600 or temperature > 1000:
        hydrogen_yield *= 0.8
    if pressure < 1 or pressure > 50:
        hydrogen_yield *= 0.8

    return hydrogen_yield


# Genetic Algorithm parameters
num_generations = 100
num_parents_mating = 10
sol_per_pop = 20
num_genes = 4

# Parameter boundaries
gene_space = [
    {'low': 600, 'high': 1000},  # Temperature (Kelvin)
    {'low': 1, 'high': 50},      # Pressure (atm)
    {'low': 0.1, 'high': 1.0},   # O/B ratio (dimensionless)
    {'low': 1, 'high': 10}       # Reaction time (hours)
]

# Create GA instance
ga_instance = pygad.GA(
    num_generations=num_generations,
    num_parents_mating=num_parents_mating,
    fitness_func=fitness_function,
    sol_per_pop=sol_per_pop,
    num_genes=num_genes,
    gene_space=gene_space,
    mutation_type="random"
)

# Run the GA
ga_instance.run()

# Extract best solution
solution, fitness, _ = ga_instance.best_solution()
print("Optimal Parameters:", solution)
print("Maximum Hydrogen Yield:", fitness)

# Smooth the fitness curve using a moving average
fitness_curve = ga_instance.best_solutions_fitness
window_size = 5
smooth_fitness_curve = np.convolve(
    fitness_curve, np.ones(window_size)/window_size, mode='valid')

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(range(len(smooth_fitness_curve)), smooth_fitness_curve,
         label="Smoothed Fitness Curve", color="blue")
plt.scatter(range(len(fitness_curve)), fitness_curve,
            label="Original Fitness Curve", color="orange", alpha=0.5, s=10)
plt.title("Hydrogen Production Optimization", fontsize=16)
plt.xlabel("Generation (Dimensionless)", fontsize=12)
plt.ylabel("Fitness (Hydrogen Yield, mol/s)", fontsize=12)
plt.legend()
plt.grid(alpha=0.3)
plt.show()
