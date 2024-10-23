import random

# Objective function we are trying to maximize
def objective_function(x):
    return -x**2 + 10*x + 12

# Get neighboring solutions (small changes in x)
def get_neighbors(x):
    return [x - 1, x + 1]

# Hill Climbing algorithm
def hill_climbing(initial_solution, max_iterations=1000):
    current_solution = initial_solution
    current_value = objective_function(current_solution)
    
    for iteration in range(max_iterations):
        neighbors = get_neighbors(current_solution)
        
        # Evaluate all neighbors and select the best one
        next_solution = max(neighbors, key=objective_function)
        next_value = objective_function(next_solution)
        
        # If the neighbor is better, move to that solution
        if next_value > current_value:
            current_solution = next_solution
            current_value = next_value
        else:
            # If no better neighbor is found, return the current solution
            print(f"Reached local maximum after {iteration} iterations.")
            break
    
    return current_solution, current_value

# Driver code
# We start with a random solution in the range of [-10, 10]
initial_solution = random.randint(-10, 10)
best_solution, best_value = hill_climbing(initial_solution)

print(f"Best solution found: x = {best_solution}, value = {best_value}")
