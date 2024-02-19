def arithmetic_arranger(problems,answer=False):

    # Checking the number of problems in 1st argument
    if len(problems) > 5:
        return "Error: Too many problems."
    
    # First instance of function call where 2nd argument is equal to 'False'
    if answer == False:
        top = []
        bottom = []
        dashes = []
        for problem in problems:

            # Splitting each problem
            num1, operator, num2 = problem.split()

            # Checking whether each number is an integer
            if num1.isdigit() is not True or num2.isdigit() is not True:
                return "Error: Numbers must only contain digits."
            
            # Checking whether the length of each number is less than or equal to 4
            if len(num1) > 4 or len(num2) > 4:
                return "Error: Numbers cannot be more than four digits."
            
            # Checking whether the operators of all problems are either '+' or '-'
            if operator != '+' and operator != '-':
                return "Error: Operator must be '+' or '-'."
            
            # Formatting the numbers and operator
            elif len(num1) > len(num2):
                fnum1 = " " * 2 + num1
                fnum2 = operator + " " + " " * (len(num1) - len(num2)) + num2
            elif len(num2) > len(num1):
                fnum1 = " " * ((len(num2)-len(num1)) + 2) + num1
                fnum2 = operator + " " + num2
            elif len(num1) == len(num2):
                fnum1 = " " * 2 + num1
                fnum2 = operator + " " + num2

            # Adding numbers and operator to respective lists
            top.append(fnum1)
            bottom.append(fnum2)

            # Formatting and adding dashes to list of dashes 
            if len(num1) > len(num2):
                dash = "-" * (len(num1) + 2)
                dashes.append(dash)
            elif len(num2) > len(num1):
                dash = "-" * (len(num2) + 2)
                dashes.append(dash)
            elif len(num1) == len(num2):
                dash = "-" * (len(num1) + 2)
                dashes.append(dash)

        # Formatting lists to remove brackets, commas and quotation marks
        formatted_top = ((' ' * 4).join(x for x in top))
        formatted_bottom = ((' ' * 4).join(x for x in bottom))
        formatted_dashes = ((' ' * 4).join(x for x in dashes))

        # Storing formatted lists in variable
        arranged_problems = f"{formatted_top}\n{formatted_bottom}\n{formatted_dashes}"
        return arranged_problems

     # Second instance of function call where 2nd argument is equal to 'True'
    if answer == True:
        top = []
        bottom = []
        dashes = []
        answers = []
        for problem in problems:

            # Splitting each problem
            num1, operator, num2 = problem.split()

            # Checking whether each number is an integer
            if num1.isdigit() is not True or num2.isdigit() is not True:
                return "Error: Numbers must only contain digits."
            
            # Checking whether the length of each number is less than or equal to 4
            if len(num1) > 4 or len(num2) > 4:
                return "Error: Numbers cannot be more than four digits."
            
            # Checking whether the operators of all problems are either '+' or '-'
            if operator != '+' and operator != '-':
                return "Error: Operator must be '+' or '-'."
            
            # Formatting the numbers and operator
            elif len(num1) > len(num2):
                fnum1 = " " * 2 + num1
                fnum2 = operator + " " + " " * (len(num1) - len(num2)) + num2
            elif len(num2) > len(num1):
                fnum1 = " " * ((len(num2)-len(num1)) + 2) + num1
                fnum2 = operator + " " + num2
            elif len(num1) == len(num2):
                fnum1 = " " * 2 + num1
                fnum2 = operator + " " + num2

            # Adding numbers and operator to lists    
            top.append(fnum1)
            bottom.append(fnum2)
           
            # Formatting and adding dashes to list of dashes
            if len(num1) > len(num2):
                dash = "-" * (len(num1) + 2)
                dashes.append(dash)
            elif len(num2) > len(num1):
                dash = "-" * (len(num2) + 2)
                dashes.append(dash)
            elif len(num1) == len(num2):
                dash = "-" * (len(num1) + 2)
                dashes.append(dash)

            # Calculating, formatting and adding answers to list of answers    
            num1 = int(num1)
            num2 = int(num2)
            if operator == "+":
                answer = num1 + num2
                str_answer = str(answer)
                if len(str_answer) < 5:
                    f_answer = "  " + str_answer
                else:
                    f_answer = " " + str_answer
                answers.append(f_answer)
            elif operator == "-":
                answer = num1 - num2
                str_answer = str(answer)
                if len(str_answer) < 5:
                    f_answer = " " * 2 + str_answer
                else:
                    f_answer = " " + str_answer
                answers.append(f_answer)

        # Formatting lists to remove brackets, commas and quotation marks
        formatted_top = ((' ' * 4).join(x for x in top))
        formatted_bottom = ((' ' * 4).join(x for x in bottom))
        formatted_dashes = ((' ' * 4).join(x for x in dashes))
        formatted_answers = ((' ' * 4).join(x for x in answers))

        # Storing formatted lists in variable
        arranged_problems = f"{formatted_top}\n{formatted_bottom}\n{formatted_dashes}\n{formatted_answers}"
        return arranged_problems