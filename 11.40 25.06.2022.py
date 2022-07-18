# задача 1
def FirstFactorial(num):
  fact = 1
  for n in range(2, num + 1):
     fact *= n
  # code goes here
  return fact

# keep this function call here 
print(FirstFactorial(input()))

#задача 2
def FirstReverse(str): 

    # code goes here 
    return str[::-1]
    
# keep this function call here  
print(FirstReverse(input()))
