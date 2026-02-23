#1
def square(n):
    for i in range(1, n+1):
        yield i ** 2
a=int(input())
print(*square(a),sep=",")

#2
def even_numbers(n):
    for i in range(1, n+1):
        if i % 2 == 0:
            yield i
a=int(input())
print(*even_numbers(a),sep=",")

#3
def divisible(n):
    for i in range(0, n+1):
        if i % 3==0 and i % 5==0:
            yield i
a=int(input())
print(*divisible(a),sep=",")

#4
def squares(a,b):
    for i in range(a, b+1):
        yield i ** 2
a=int(input())
b=int(input())
print(*squares(a,b),sep=",")

#5
def countdown(n):
    for i in range(n, -1, -1):
        yield i
a=int(input())
print(*countdown(a),sep=",")