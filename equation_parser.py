# def split(string):
#     return [char for char in equation]

# equation = split(equation)
number_digits = ['1','2','3','4','5','6','7','8','9','0']
operation_chars = ['+','-','*','/']
while True:
    equation = input("Enter the equation:")
    parsed_equation = list(equation)
    for i in parsed_equation:
        if (i in number_digits):
            print(i)
        elif (i in operation_chars):
            print(i)