""" 
Develop a program that checks if a user-inputted word is a palindrome. A palindrome is a word that reads the same backward as forward (e.g., "radar"). """

text = input("Enter the word: ")
revtext = ""
for char in range(len(text) - 1, -1, -1):
    revtext = revtext + text[char]
if (text == revtext):
    print ("The word "+ text +" is Palindrome")
else: print ("The word "+ text +" is Not Palindrome")