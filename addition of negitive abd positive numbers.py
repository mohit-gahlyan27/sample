num = int(input("enter numbers: "))

pos = 0
neg = 0

for i in range(num,4):
    num = int(input("enter number: "))
    
    if num > 0:
        pos += num
    if num < 0:
        neg += num

print("Sum of positive  =", pos)
print("Sum of negative = ", neg)
 