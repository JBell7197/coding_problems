test_cases = int(input("How many test cases: "))

remainder_list = []
#figure out how to get inputs on the same line. Possible github put up
for i in range(test_cases):
    first_value = int(input("First value: "))
    second_value = int(input("Second value: "))
    formula = first_value % second_value
    remainder_list.append(formula)

for i in remainder_list:
    print(i)