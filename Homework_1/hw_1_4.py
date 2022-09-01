# problem 4 - creating a list that is greater than a specified number

n = int(input("How many elements do you want in your list? "))
listn = []
choice = input("Do you want to create a custom list or a random list? Enter \"custom\" or \"random\" ")
if choice == "random":
    import random
    for i in range(n):
        listn.append(random.randint(0,100))
        
elif choice == "custom":
    for i in range(n):
        k = int(input("Enter a number: "))
        listn.append(k)
else:
    print("Nope")
print("Current list: ", listn)
 
q = int(input("Enter a number that you want to filter to the numbers greater than that number: "))
for i in listn:
    if(q >= i):
        listn.remove(i)

print("Current list: ", listn)