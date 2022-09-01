# solving the Tower of hanoi problem



def creating_tower(n):
    lists = []
    for i in range(n):
        lists.append(i+1)
    print("The tower shows the disk number ascending from the top ( 1 ) to the bottom (", n ,")")
    print("Tower 1:", lists)
    return lists

move = 1
def tower(n, s, d, a, move):
    if n == 1:
        print("Move", move, "- from Disk 1 from Tower", s, "to Tower", d)
        move += 1

        if s == 'A':
            print("A: ", x[n-1])
            if d == 'B':
                y.append(x[n-1])
                x.remove(x[n-1])
            else:
                z.append(x[n-1])
                x.remove(x[n-1])
        elif s == 'B':
            print("B: ", y[n-1])
            if d == 'A':
                x.append(y[n-1])
                y.remove(y[n-1])
            else:
                z.append(y[n-1])
                y.remove(y[n-1])
        else:
            print("C: ", z[n-1])
            if d == 'A':
                x.append(z[n-1])
                z.remove(z[n-1])
            else:
                y.append(z[n-1])
                z.remove(z[n-1])

        print("Tower A: ", x)
        print("Tower B: ", y)
        print("Tower C: ", z)
        print("----------------------------------------------")
        return

    tower(n-1, s, a, d, move)
    move += 1
    print("Move", move, ": From disk", n, "from Tower", s, "to Tower", d, "-")

    k = n-1

    if s == 'A':
        print("A: ", x[k-1])
        if d == 'B':
            y.append(x[k-1])
            x.remove(x[k-1])
        else:
            z.append(x[k-1])
            x.remove(x[k-1])
    elif s == 'B':
        print("B: ", y[k-1])
        if d == 'A':
            x.append(y[k-1])
            y.remove(y[k-1])
        else:
            z.append(y[k-1])
            y.remove(y[k-1])
    else:
        print("C: ", z[k-1])
        if d == 'A':
            x.append(z[k-1])
            z.remove(z[k-1])
        else:
            y.append(z[k-1])
            z.remove(z[k-1])

    print("Tower A: ", x)
    print("Tower B: ", y)
    print("Tower C: ", z)
    print("----------------------------------------------")


    move += 1
    tower(n-1, a, d, s, move)
    move += 1



v = int(input("Enter the number of disks in Tower A: "))
a, b, c = 'A', 'B', 'C'

x = creating_tower(v)
print("++++++++++++++++++++++++++++++++++++++++++++++")
y = []
z = []

tower(v, a, b, c, move)
