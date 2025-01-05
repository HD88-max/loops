n = int(input("Enter a number you want the sum till: "))
sum = 0
for i in range(1,n+1):
    sum = sum+i

print("The sum is {0}".format(sum))