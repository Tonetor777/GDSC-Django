""" 
Develop a program that checks if a user-inputted word is a palindrome. A palindrome is a word that reads the same backward as forward (e.g., "radar"). """

text = input("Enter the word: ")
revtext = "".join(reversed(text))
print ("The word "+ text , "is Palindrome" if text == revtext else "is Not Palindrome" )
