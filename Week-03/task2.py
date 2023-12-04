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
