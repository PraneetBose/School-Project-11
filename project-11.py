# Python program to print the table of a number input by the user.

#storing the number in the variable 'num'
num = int(input("Enter the number: "))
i = 1
for i in range(1, 11):
    print(num, "×", i, "=", num * i)
    i += 1
