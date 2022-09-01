# problem 6 creating a function that calculates the factoral of any given number

def fact(x):
    if x == 1:
        return x
    else:
        return x * fact(x-1)

n = int(input("Enter a postive integer to computer a factoral: "))
print("The factoral of 5 is", fact(n))
