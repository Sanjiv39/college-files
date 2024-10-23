from constraint import Problem

# Define the problem
problem = Problem()

# Define variables (regions) and their domains (colors)
colors = ["Red", "Green", "Blue"]
regions = ["Western Australia", "Northern Territory", "South Australia",
"Queensland", "New South Wales", "Victoria", "Tasmania"]

# Add variables to the problem, all regions can take any color
for region in regions:
    problem.addVariable(region, colors)

# Add constraints - adjacent regions should not have the same color
# Australia map constraints:
# Western Australia is adjacent to Northern Territory, South Australia
problem.addConstraint(lambda a, b: a != b, ("Western Australia", "Northern Territory"))
problem.addConstraint(lambda a, b: a != b, ("Western Australia", "South Australia"))

# Northern Territory is adjacent to Western Australia, South Australia, Queensland
problem.addConstraint(lambda a, b: a != b, ("Northern Territory", "South Australia"))
problem.addConstraint(lambda a, b: a != b, ("Northern Territory", "Queensland"))

# South Australia is adjacent to Western Australia, Northern Territory, Queensland, New South Wales, Victoria
problem.addConstraint(lambda a, b: a != b, ("South Australia", "Queensland"))
problem.addConstraint(lambda a, b: a != b, ("South Australia", "New South Wales"))
problem.addConstraint(lambda a, b: a != b, ("South Australia", "Victoria"))

# Queensland is adjacent to Northern Territory, South Australia, New South Wales
problem.addConstraint(lambda a, b: a != b, ("Queensland", "New South Wales"))

# New South Wales is adjacent to Queensland, South Australia, Victoria
problem.addConstraint(lambda a, b: a != b, ("New South Wales", "Victoria"))

# Tasmania has no neighbors, no constraints needed for it.
# Solve the problem
solution = problem.getSolutions()

# Display the results
print("Possible colorings of the map of Australia:")
for sol in solution:
    print(sol)
