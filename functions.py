'''
def func():
    print('I am the function')

func()
'''
'''
#if number of arguments is unknown,,use a asterisk
def function(*names):
  print("The topic is " + names[1])

function("python", "iot", "ml")
'''
'''
# arguments with key-value
def function(k1, k2, k3):
  print("The topic is " + k3)

function(k1 = "python", k2 = "iot", k3 = "web")

def function(**k):
  print("the topic is " + k["k1"])

function(k1 = "python", k2 = "iot")
'''
'''
def sum(x,y):
    return x+y

add = sum(5,5)
print(add)'''
'''
#passing list in arguments
def list(l):
    for i in l:
        print(i)

list([1,2,3])'''

#global vs local

#local
def func():
  k = 10
  print(k)
func()
print(k)

#global
'''
k=10
def func():
  print("func : ",k)
func()
print('outside : ',k)
'''
'''
def func():
  global k 
  k=10
  print(k)
func()
print(k)
'''