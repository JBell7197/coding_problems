#display right decimal points
test_cases = int(input("How many test cases: "))

list_of_salaries = []
for i in range(test_cases):
    basic_salary = int(input("What is the basic salary: "))
    if basic_salary < 1500:
        HRA = basic_salary * .1
        DA = basic_salary * .9
        gross_salary = basic_salary + HRA + DA
    else:
        HRA = 500
        DA = basic_salary * .98
        gross_salary = basic_salary + HRA + DA
    list_of_salaries.append(gross_salary)
    
for numbers in list_of_salaries:
    print(numbers)
