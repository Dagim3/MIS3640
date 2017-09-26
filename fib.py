n = (input('What number do you select?'))

def fib (n):
    if n==1 or n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

fib (n)