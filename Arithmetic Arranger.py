# Arithmetic Arranger Practice
# Instructions found at:
# https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/arithmetic-formatter


# - Define a function arithmetic_arranger() that takes a list
#   of arithmetic problems as a string and formats them vertically.
#   If second argument is set to True, then show answers as well.


#   - Situations that will return an error:
#        - If there are too many problems supplied to the function. 
#          - The limit is five, anything more will return: 
#            Error: Too many problems.
#        - The appropriate operators the function will accept are addition 
#          and subtraction. 
#          - Multiplication and division will return an error. Other operators 
#            not mentioned in this bullet point will not need to be tested. 
#            The error returned will be: 
#            Error: Operator must be '+' or '-'.
#        - Each number (operand) should only contain digits. 
#          - Otherwise, the function will return: 
#            Error: Numbers must only contain digits.
#        - Each operand (aka number on each side of the operator) has a max 
#          of four digits in width.
#          - Otherwise, the error string returned will be: 
#            Error: Numbers cannot be more than four digits.

#   - If the user supplied the correct format of problems, the conversion you 
#     return will follow these rules:
#        - There should be a single space between the operator and the longest 
#          of the two operands, the operator will be on the same line as the 
#          second operand, both operands will be in the same order as provided 
#          (the first will be the top one and the second will be the bottom).
#        - Numbers should be right-aligned.
#        - There should be four spaces between each problem.
#        - There should be dashes at the bottom of each problem. The dashes 
#          should run along the entire length of each problem individually. 

# Example call
# arithmetic_arranger(["1 + -2000", "24 + 8515", "3801 - 2", "45 + 43", "123 + 49"], True)
# 
#       1        24      3801      45      123
# + -2000    + 8515    -    2    + 43    +  49
# -------    ------    ------    ----    -----
#   -1999      8539      3799      88      172


def arithmetic_arranger(problems, answers=False):

    # Check number of problems
    if len(problems) > 5:
        error = "Error: Too many problems."
        print(error)
        return error

    # Start list of formatted problems
    # Format will be [[num1, op, num2], [...], ...]
    split_problems = []

    # Check formatting
    for problem in problems:
        # problem = ['1 + 2']
        problem = problem.split()
        # problem = ['1', '+', '2']
        first = problem[0]
        op = problem[1]
        second = problem[2]

        # Check for digits only
        try:
            int(first)
            int(second)
        except: 
            error = "Error: Numbers must only contain digits."
            print(error)
            return error
        
        # Check number length
        if int(first) > 9999 or int(first) < -9999 or int(second) > 9999 or int(second) < -9999:
            error = "Error: Numbers cannot be more than four digits."
            print(error)
            return error
        
        # Check operator
        if op != '+' and op != '-':
            error = "Error: Operator must be '+' or '-'."
            print(error)
            return error
        
        # Add to formatted problems list
        split_problems.append(problem)

    # Print problems

    # Initialize lines
    final_line1 = ''
    final_line2 = ''
    final_line3 = ''
    final_line4 = ''

    counter = 0

    for prob in split_problems:

        num1 = prob[0]
        num2 = prob[2]
        op = prob[1]

        if op == '+':
            ans = str(int(num1) + int(num2))
        else:
            ans = str(int(num1) - int(num2))

        if len(num1) >= len(num2):
            line1 = '  ' + ' ' * (len(num1) - len(num2) - (len(num1) - 1)) + num1
            line2 = op + ' ' + ' ' * (len(num1) - len(num2)) + num2
            line3 = '-' * len(line2)
            line4 = ' ' * (len(line2) - len(ans)) + ans
            
            final_line1 += line1
            final_line2 += line2
            final_line3 += line3
            final_line4 += line4

        elif len(num2) > len(num1):
            line1 = '  ' + ' ' * (len(num2) - len(num1)) + num1
            line2 = op + ' ' + ' ' * (len(num2) - len(num1) - (len(num2) - 1)) + num2
            line3 = '-' * len(line2)
            line4 = ' ' * (len(line2) - len(ans)) + ans

            final_line1 += line1
            final_line2 += line2
            final_line3 += line3
            final_line4 += line4

        counter += 1

        if counter != len(problems):
            final_line1 += '    '
            final_line2 += '    '
            final_line3 += '    '
            final_line4 += '    '
        elif counter == len(problems):
            final_line1 += '\n'
            final_line2 += '\n'
            final_line3 += '\n'
    
    if answers == True:
        output = final_line1 + final_line2 + final_line3 + final_line4
    else:
        output = final_line1 + final_line2 + final_line3[:-1]

    print(output + '\n')
    return output
        
arithmetic_arranger(["1 + -2000", "24 + 8515", "3801 - 2", "45 + 43", "123 + 49"], True)
