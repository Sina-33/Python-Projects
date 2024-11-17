import pygad
import numpy as np
import matplotlib.pyplot as plt

# Objective function for optimization (with 3 parameters)
def fitness_function(ga_instance, solution, solution_idx):
    # Energy production from different sources (W)
    solar_power, wind_power, battery_power, hydrogen_power = solution
    
    # Assume a fixed load demand (W)
    load_demand = 1000  # Watts
    
    # Energy cost for each source ($/kWh)
    cost_solar = 0.05
    cost_wind = 0.06
    cost_battery = 0.08
    cost_hydrogen = 0.10
    
    # Calculate total power produced by all sources
    total_power = solar_power + wind_power + battery_power + hydrogen_power
    
    # Calculate the total cost of energy production
    total_cost = (solar_power * cost_solar + 
                  wind_power * cost_wind + 
                  battery_power * cost_battery + 
                  hydrogen_power * cost_hydrogen)
    
    # Calculate energy losses (if any)
    energy_loss = max(0, total_power - load_demand)
    
    # Calculate system efficiency
    efficiency = load_demand / (total_power + 1e-6)  # Avoid division by zero
    
    # Objective: Minimize cost and energy loss, maximize efficiency
    fitness = (1 / (total_cost + energy_loss + 1e-6)) * efficiency
    return fitness

# Genetic Algorithm parameters
num_generations = 100
num_parents_mating = 10
sol_per_pop = 20
num_genes = 4  # Solar, wind, battery, and hydrogen power (W)

# Power ranges for each source (W)
gene_space = [{'low': 0, 'high': 500}, {'low': 0, 'high': 500},
              {'low': 0, 'high': 300}, {'low': 0, 'high': 300}]

# Create Genetic Algorithm instance
ga_instance = pygad.GA(
    num_generations=num_generations,
    num_parents_mating=num_parents_mating,
    fitness_func=fitness_function,
    sol_per_pop=sol_per_pop,
    num_genes=num_genes,
    gene_space=gene_space,
    mutation_type="random"
)

# Run the Genetic Algorithm
ga_instance.run()

# Display the best solution found
solution, fitness, _ = ga_instance.best_solution()
print("Optimal power allocation for each energy source:")
print(f"Solar Power: {solution[0]} W")
print(f"Wind Power: {solution[1]} W")
print(f"Battery Power: {solution[2]} W")
print(f"Hydrogen Power: {solution[3]} W")
print("Highest objective function value (efficiency):", fitness)

# Visualize the optimal power allocation
energy_sources = ['Solar', 'Wind', 'Battery', 'Hydrogen']
plt.figure(figsize=(8, 6))
plt.bar(energy_sources, solution, color=['yellow', 'blue', 'green', 'purple'])

# Adding title and labels
plt.title("Optimal Power Allocation in Hybrid Energy System", fontsize=14)
plt.xlabel("Energy Sources", fontsize=12)
plt.ylabel("Power Allocated (W)", fontsize=12)

# Display the chart
plt.show()
