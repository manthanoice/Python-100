num = int(input("Enter till which number you want to find sum: "))
answer = 0
for i in range(0, num+1):
    if i%2==0:
        answer+=i
print("Sum from 1 to {} is {}".format(num, answer))