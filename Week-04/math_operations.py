
""" Django  Week 4 Tasks

Create a Python module (math_operations.py) with the following functionalities:

a. Basic Operations Function:

Create a function basic_operations that takes two numbers and performs basic arithmetic operations (addition, subtraction, multiplication, division). This function should return a dictionary with the results for each operation. """

def basic_operations(a, b):
    # Perform basic arithmetic operations
    # Return results in a dictionary
    try:
        result = {}
        result["Sum"] = a + b
        result["Difference"] = a - b
        result["Product"] = a * b
        result["Quotient"] = a / b
    except TypeError:
        return "Pass only a number!" 
    except ZeroDivisionError:
        return "Can't divide with Zero"  
    else:
        return result 
""" b. Power Operation Function:
Create a function power_operation that takes a base and an exponent and calculates the result of the power operation. Use the **kwargs feature to allow the user to specify an optional modulo value. If the modulo value is provided, calculate the result modulo the specified value.
"""
def power_operation(base, exponent, **kwargs):
    # Calculate power operation
    # If 'modulo' is provided in kwargs, calculate modulo
    try:
        result = base ** exponent
        if 'modulo' in kwargs:
            result %= kwargs['modulo']
    except TypeError:
        return "Pass only a number!" 
    except ZeroDivisionError:
        return "Can't divide with Zero"
    else:
        return result

""" c. Exception Handling:
Add appropriate exception handling in both functions to handle cases such as division by zero and invalid inputs.
In the same module, create a higher-order function apply_operations that takes a list of tuples, where each tuple contains a function and its corresponding arguments. Use map to apply each function to its arguments and return a list of results."""

def apply_operations(operation_list):
    # Use map to apply each function to its arguments
    # Return a list of results
    result = list(map(lambda op: op[0](*op[1]), operation_list))
    return result

