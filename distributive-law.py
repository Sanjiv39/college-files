# Function to demonstrate the distributive law
def distributive_law(a, b, c):
    # Calculate both sides of the distributive law
    left_side = a * (b + c)
    right_side = (a * b) + (a * c)
    # Display the results
    print(f"Using a = {a}, b = {b}, c = {c}:")
    print(f"Left Side: a * (b + c) = {a} * ({b} + {c}) = {left_side}")
    print(f"Right Side: (a * b) + (a * c) = ({a} * {b}) + ({a} * {c}) = {right_side}")
    # Check if the law holds
    if left_side == right_side:
        print("The Distributive Law holds: a * (b + c) = (a * b) + (a * c)")
    else:
        print("The Distributive Law does not hold.")
        
# Input values
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))
# Call the function to demonstrate the distributive law
distributive_law(a, b, c)