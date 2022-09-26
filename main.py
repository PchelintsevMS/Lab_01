import math
'''class Zad1():
    print("Введите до какого числа выводить ")
    k = int(input())
    n = k
    while n > 1:
        m = k
        while m > 1:
            a = m*m-n*n
            b = 2*m*n
            c = m*m+n*n
            if c*c == a*a+b*b:
                print(f"{m} {n} {a} {b} {c}")
            m = m-1
        n = n-1

class Zad2():
    print("Введите N ")
    n = int(input())
    i=1
    Sum=0
    s=0
    while i <= n:
       s+=math.sin(i)
       Sum+=1/s
       i+=1
    print(Sum)
'''

class Zad3():
    print("Введите N ")
    n = int(input())
    i = 1
    p = 1
    while i <= n:
        p *= 2*n/(2*n+1)
        i+=1
    print(p)

