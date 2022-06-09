
def factorial(num):
    if num <0:
        return 'Factorial does not for negative numbers'
    elif num==0 or num==1:
        return 1 #Because 0!=1 & 1!=1
    else:
        return num*factorial(num-1) #n!=n*(n-1)*(n-2)*(n-3)*.....*1

#lets check some examples
print(factorial(0))
print(factorial(-6))
print(factorial(4))


