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