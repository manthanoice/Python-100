def prime(n):
    if n<2:
        print("{} is not Prime!".format(n))
    else:
        the_prime = True
        for i in range(2, n):
            if n%i==0:
                the_prime = False
        if the_prime:
            print("{} is Prime!".format(n))
        else:
            print("{} is not Prime!".format(n))

num = int(input("Enter the number which you want to check if it's prime or not: "))
prime(num)