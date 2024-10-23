print ("Water Jug Problem")
x=int (input("Enter X:"))
y=int (input("Enter Y:"))
# Initial capacities
capacity_a = 4
capacity_b = 3
# Current water in jugs
jug_a = 0
jug_b = 0

while True:
    rno=int (input ("Enter the Rule No"))
    if rno==1:
        # Step 1: Fill Jug A
        jug_a = capacity_a
        print(f"Filled Jug A: [A: {jug_a}, B: {jug_b}]")
    if rno==2:
        # Step 2: Fill Jug B
        jug_b = capacity_b
        print(f"Filled Jug B: [A: {jug_a}, B: {jug_b}]")
    if rno==3:
        # Step 3: Empty Jug A
        jug_a = 0
        print(f"Emptied Jug A: [A: {jug_a}, B: {jug_b}]")
    if rno==4:
        # Step 4: Empty Jug B
        jug_b = 0
        print(f"Emptied Jug B: [A: {jug_a}, B: {jug_b}]")
    if rno==5:
        # Step 5: Transfer from B to A
        transfer_b_to_a = min(jug_b, capacity_a - jug_a)
        jug_a += transfer_b_to_a
        jug_b -= transfer_b_to_a
        print(f"Transferred from B to A: [A: {jug_a}, B: {jug_b}]")
    if rno==6:
        # Step 6: Transfer from A to B
        transfer_a_to_b = min(jug_a, capacity_b - jug_b)
        jug_b += transfer_a_to_b
        jug_a -= transfer_a_to_b
        print(f"Transferred from A to B: [A: {jug_a}, B: {jug_b}]")
    if rno==7:
        # Step 7: Transfer from B to A until A is full
        transfer_b_to_a = min(jug_b, capacity_a - jug_a)
        jug_a += transfer_b_to_a
        jug_b -= transfer_b_to_a
        print(f"Transferred from B to A until A is full: [A: {jug_a}, B: {jug_b}]")
    if rno==8:
        # Step 8: Transfer from A to B until B is full
        transfer_a_to_b = min(jug_a, capacity_b - jug_b)
        jug_b += transfer_a_to_b
        jug_a -= transfer_a_to_b
        print(f"Transferred from A to B until B is full: [A: {jug_a}, B: {jug_b}]")
    if jug_a==2:
        print(" The result is a Goal state")
        break