import math
def add(x, y):
    return x + y
def sub(x, y):
    return x - y
def div(x, y):
    return x / y
def mul(x, y):
    return x*y
def sqr(x):
    return math.sqrt(x)
def pwr(x, y):
    return math.pow(x, y)
def grt(x, y):
    if x < y:
        print (y, ' is greater than ', x)
    elif x > y:
        print (x, ' is greater than ', y)
    elif x == y:
        print (y, ' is equal to  ', x)
    else:
        print ("Invalid")
def fac(x):
    return math.factorial(x)
def hcfnaive(x, y):
    while(y):
        x, y = y, x % y
        
        return x
print ("Select Operation: \n 1. Add \n 2. Subtract \n 3. Divide \n 4. Multiply \n 5. Squareroot \n 6. Square \n 7. Exponential Function ")
print(' 8. Compare two numbers \n 9. Factorial of a number \n 10. Greatest common Divisor of two numbers \n 0. Exit \n')
while True:
    use = input("Enter your choice: ")
    #2 number functions#
    if use in  ('1', '2', '3', '4', '7', '8', '10'):
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
    if use == '1':
        print (num1, "+", num2, "=", add(num1, num2))
    elif use == '2':
        print (num1, '-', num2, '=', sub(num1, num2))
    elif use == '3':
        print (num1, '/', num2, '=', div(num1, num2))
    elif use == '4':
        print (num1, '*', num2, '=', mul(num1, num2))
    elif use == '7':
        print (num1, ' to the power of ', num2, ' = ', pwr(num1, num2))
    elif use == '8':
        print (grt(num1, num2))
    elif use == '10':
        print ('Greatest common Divisor of ', num1, ' and ', num2, ' = ', hcfnaive(num1, num2))
    
    #1 number functions#
    
    elif use in ('5', '6', '9'):
        num1 = float(input('Enter the number: '))
    if use == '5':
            print ('Squareroot of ', num1, ' is ', sqr(num1))
    elif use == '6':
        print ('Square of ', num1, ' is ', num1*num1)
    elif use == '9':
        print ('Factorial of ' , num1, ' is ', fac(num1))
            
    
    elif use in ('0'):
        print("Thank you")
        exit()
    else:
        print ('Invalid Input')
    