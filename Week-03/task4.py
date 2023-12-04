""" 
Write a Python program to find and print the sum of all the even numbers from 1 to 50 (inclusive). Additionally, for each even number, if it is a multiple of 3, print "Three" instead of the number; if it is a multiple of 5, print "Five" instead of the number. Finally, print the total sum and the count of numbers replaced with "Three" or "Five."
 """
sum = 0
count = 0
for num in range(2 , 51, 2):
    sum += num
    if num % 3 == 0:
        print("Three" , end=", ")
        count +=1
    elif num % 5 == 0:
        print("Five", end=", ")
        count += 1
    else: print (num , end=", ")
print (f"\n\nTotal Sum: {sum} \nReplaced Numbers: {count}")