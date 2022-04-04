'''
def recursion(k):
  if(k>0):
    result = k+recursion(k-1)
    print(result)
  else:
    result = 0
  return result

recursion(4)
'''
'''
#factorial without recursion
def fact(n):
  f=1
  for i in range(1,n+1):
    f=f*i
  return f

print(fact(5))
'''
'''
#factorial

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

fact = factorial(6)
print(fact)
'''

#fibonacci with recursion
def fibo(n):
   if n <= 1:
       return n
   else:
       return(fibo(n-1) + fibo(n-2))
for i in range(5):
  print(fibo(i))