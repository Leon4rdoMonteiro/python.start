operator = input('Provide the operator: ')
first_number = int(input('Provide the first number: '))
second_number = int(input('Provide the second number: '))

def calculator(operator, x=0, y=0):
    if operator == '+':
        return x + y
    elif operator == '-':
        return x - y
    elif operator == '*':
        return x * y
    else:
        return x / y
        

result = calculator(
    operator, 
    x=first_number, 
    y=second_number
)

print('The result is:', result) 