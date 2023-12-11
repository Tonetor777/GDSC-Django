
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
"""
Create a Python script that identifies and collects files (both created and modified) in the last 24 hours from the current directory. Update these files in some way and move them to a folder named "last_24hours."

Requirements:

Listing Files:
Use the os module to list all files in the current directory.
Identification of Files:
Implement a function to determine whether a file has been created or modified in the last 24 hours.
Consider both the modification time (st_mtime) and creation time (st_ctime) of the file.

Update Files:
Create a function to update the identified files. For example, append a timestamp to the content of each file.

Create "last_24hours" Folder:
Check if a folder named "last_24hours" exists. If not, create it using the os module.

Move Files:
Move the identified and updated files to the "last_24hours" folder using different method
Combine the functions to achieve the main objective.

Feel free to seek clarification on any part of the task. The primary goal is to enhance your understanding of file handling, time-based operations, and module usage in Python.

 """
