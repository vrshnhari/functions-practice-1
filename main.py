# Write a function that takes in three numbers and returns the product of the numbers
def prod(x,y,z):
  return x*y*z 
print("product (2,3,5) = "+str(prod(2,3,5)))


# Write a function that takes in two numbers and returns their average
def aver(x,y):
  return (x+y)/2
print("average(2,3) = "+str(aver(2,3)))


# Write a function that takes in a word and a letter as input, and returns how many times that letter occurs in the word
def letter(x,y):
  n=0
  for i in x:
    if i==y:
      n+=1
  return n 
print("countLetter('bookkeeper', 'e') ="+str(letter("bookkeeper", "e")))


# Write a function that takes in an integer as input, and return show many digits are 7
def seven(x,y):
  f=0
  for i in str(x):
    if i==str(y):
      f+=1 
  return f 
print("countSeven(177877)= "+str(seven(177877,8)))

# Write a function that takes in two numbers, a and b, and returns a to the power of b
def exponent(a,b):
  r=a*1
  for i in range(b-1):
    r*=a
  return r 
print("exponent(2,10)= "+str(exponent(2,10)))
  

# Challenge: Write a function that takes in a number and returns its factorial
def fac(x):
  b=1
  for i in range(x):
    b*=x
    x-=1
  return b 
print("factorial(5)= "+str(fac(5)))

# Create a list of the numbers 1 through 20 (without hard-coding the list)
list1=[1,2,3,4,5,6,7,8,9,10]

# Create a list of the first 20 even numbers (without hard-coding the list)
list2=[]
for i in range(2,21):
  if i%2==0:
    list2.append(i)

# Create a list of the first 10 perfect squares (without hard-coding the list)
squares=[]
for i in range(1,11):
  squares.append(i*i)
print(squares)

# Write a function that takes in two lists and returns the sum of both lists
addition=[]
def n(x,y):
  for i in range(len(y)):
    a=0
    a=x[i]+y[i]
    addition.append(a)
  return addition 
print(n(list1,list2))
    
# Write a function that takes in a list and returns the minimum value in that list
random=[3,2,7,8,5] #creates input list
def minimum(x): #starts and establishes function
  b=x[0]  #creates variable b which is the first number in the random list
  for i in range(len(x)-1):  #creates a for loop which goes through values in random 
    if x[i+1]<b:  #creates a if loop for whether the next value is less than the og one
      b=x[i+1]  #if it is changes variable v
  return b   #return's variable b
print("The smallest number in this list is "+str((minimum(random)))) #prints minimum

# Write a function that takes in a list and returns the maximum value in that list
def maximum(x):
  b=x[0]
  for i in range(len(x)-1):
    if x[i+1]>b:
      b=x[i+1]
  return b 
print("The largest number in this list is "+str((maximum(random))))

# Write a function that takes in a list of lists, and returns the sum of all those lists
v=[]
q=[[2,5,4,6],[8,4,2],[9,2,4]]
def r(x,y,z):
  for i in range(len(y)):
    a=0
    a=x[i]+y[i]+z[i]
    v.append(a)
  return v 
print(r(q[0],q[1],q[2]))

# Write a function that takes in a list of lists, and returns a new list made from “flattening” the lists (putting every element from each list into a single list)
def flat(x):
  newlist=[]
  for j in x:
    for i in range(len(j)):
     newlist.append(j[i])
  return newlist
print("The new list with all the values is "+str(flat(q)))  
  
# Write a function that takes in a list of lists that returns a new list of all the individual maxes from each list. Can you find a way to use the function that you already made that returns the maximum of a list?
ran=[]
def lmax(x):
  for i in x:
    ran.append(maximum(i))
  return ran 
print("The maximum values of the lists are: "+str(lmax(q)))