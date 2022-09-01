# problem 5 - Fibonacci series between 0-50

first_val = 0
second_val = 1
sum = 0
fib = [first_val, second_val]
while sum < 50:
    sum = first_val + second_val
    if sum > 50:
        break
    fib.append(sum)
    first_val = second_val
    second_val = sum
print("Fibonacci series between 0-50 ", fib)