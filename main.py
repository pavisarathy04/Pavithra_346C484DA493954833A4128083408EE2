#Recursive function to find factorial of a number
def factorial(n):

 # base code: if 'n' is 0 or 1
  if n<1:
    return 1

 #use the recursive relation
  return n * factorial(n - 1)


if __name__=='__main__':

  n = 5
  print(f'The factorial of{n} is', factorial(n))
  