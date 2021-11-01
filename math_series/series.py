# n=int(input())
def fibonacci(n):
    #Base Case
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


#print(fibonacci(3))


def lucas(n):
 if n < 1:
     return 2
 elif n == 1:
  return 1
 else :
     return lucas(n-1)+ lucas(n-2)
  
#print(lucas(2))


def sum_series (n, b= 0 , c = 1):

    if n == 0:
        return b
    elif n == 1:
        return c
    else:
        return  sum_series((n-1),b,c) + sum_series(n-2)


    
print(sum_series(3,0,1))