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

#factorial

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

fact = factorial(6)
print(fact)