""" Write a program that prints the following pattern.
The program should accept the input for character
The pattern consists of a series of lines
The characters in each line should follow a specific pattern based on the line number.
Use conditional statements to determine the pattern for each line.
Use a loop to iterate through the lines and print the characters accordingly.
You are not allowed to use functions in your code.
Do not store the pattern or any intermediate results in variables. """

value = input ("Enter a character: ")
count = 0
for i in value:
    count += 1

if value in ['a' , 'e', 'i', 'o', 'u']:
    print("Vowels are not allowed!")
elif count > 1:
    print("Length of character should be 1.")
else:
    for num in range(1,10,2):
        print(num * value)
