x = int(input("Enter any number: "))
answer = int(0)
while x!=0:
    o = int(x%10)
    answer+=o
    x/=10
print(answer)