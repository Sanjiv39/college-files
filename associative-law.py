def associative_law():
    # Define three numbers
    a = 5
    b = 10
    c = 15
    # Verify the associative law for addition
    addition_left = (a + b) + c
    addition_right = a + (b + c)
    # Verify the associative law for multiplication
    multiplication_left = (a * b) * c
    multiplication_right = a * (b * c)
    # Print results
    print("Associative Law of Addition:")
    print(f"({a} + {b}) + {c} = {addition_left}")
    print(f"{a} + ({b} + {c}) = {addition_right}")
    print("Result of Addition: ", addition_left == addition_right)
    print("\nAssociative Law of Multiplication:")
    print(f"({a} * {b}) * {c} = {multiplication_left}")
    print(f"{a} * ({b} * {c}) = {multiplication_right}")
    print("Result of Multiplication: ", multiplication_left == multiplication_right)

# Call the function to verify associative law
associative_law()