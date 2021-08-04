#number of test cases
test_cases = input("How many test cases: ")
test_cases = int(test_cases)

for i in range(test_cases):
    cupcake_count = input("Number of cupcakes: ")
    cupcake_count = int(cupcake_count)
    highest = 0
    highest_count = None
    for count in range(1, cupcake_count+1):
        formula = cupcake_count % count
        if formula > highest:
            highest = formula
            highest_count = count

    if highest_count is None:
        highest_count = cupcake_count
    print(highest_count)
