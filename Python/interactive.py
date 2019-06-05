# Variable 
'''
_abc24 = 10 # protected member
print(_abc24)
'''
'''
val = 24 
print(id(val))
val1 = 25
print(id(val1))
val3 = 24
print(id(val3))
val = "Hello"
print(id(val))
'''

# type detection
'''
val = 356
print(val)
print(type(val))
strg = "this is very easy language"
print(strg)
print(type(strg))
fl = 23456.343434
print(fl)
print(type(fl))
'''

# multiple variable assignment
'''
a=b=c=34
print(a,b,c)
'''

# multiple variable assignment with different object
'''
a,b,c = 10,20,30
print(a,b,c)
str1,str2,str3 = 10,"Hi",12345.1234
print(str1,str2,str3)
'''

# Method to typecast from one type to another type to another type
'''
# 1> integer to float
a=10 
print(a)
print(type(a))
b=float(a)
print(b)
print(type(b))
'''

# 2> integer to string
'''
a= 10 
print(a)
print(type(a))
b=str(a)
print(b)
print(type(b))
'''

# Type casting
'''
# 3> string to integer
val = "234567"   
print(val)
print(type(val))
val2 = int(val)
print(val)
print(type(val2))
# note - we can't typecast from string to integer when string have atleast one alphabet
'''

# 4> String to Float
'''
val = '23425.4748'
print(val)
print(type(val))
val2 = float(val)
print(val2)
print(type(val2))
'''

# 5> Float to Integer
'''
val = 23425.4748
print(val)
print(type(val))
val2 = int(val)
print(val2)
print(type(val2))
# whenever we convert from float to integer then pvm will remove all digits after the point
'''

# 5> Float to String
'''
val = 23425.4748
print(val)
print(type(val))
val2 = str(val)
print(val2)
print(type(val2))
'''

# 6> Integer to Binary
'''
val = 23
print(val)
print(type(val))
val2 = bin(val)
print(val2)
print(type(val2))
'''

# 7> Binary to Integer
'''
val = '0b101'
print(val)
print(type(val))
val2 = int(val,2)
print(val2)
print(type(val2))
'''

# 8> Integer to Octagonal
'''
val = 23
print(val)
print(type(val))
val2 = oct(val)
print(val2)
print(type(val2))
'''

# 9> Octagonal to Integer
'''
val = '0o27'
print(val)
print(type(val))
val2 = int(val,8)
print(val2)
print(type(val2))
'''

# 10> Integer to Hexagonal
'''
val = 234598079
print(val)
print(type(val))
val2 = hex(val)
print(val2)
print(type(val2))
'''

#11> Hexagonal To Integer
'''
val = '0xdfbaebf'
print(val)
print(type(val))
val2 = int(val,16)
print(val2)
print(type(val2))
'''

#12> Hexagonal To Octagonal
'''
val = '0xdfbaebf'
print(val)
val = int(val,16)
val = oct(val)
print(val)
'''

# Method to print in PYTHON
'''
print(245)
print(3425.25)
print("qfhtr")
print('eghh')
a = 10 
b = 20
print ("Sum of",a,"and",b,"is",a+b)
'''
'''
%d ---> integer
%s ---> string
%f ---> float
'''
'''
print("Sum of %d and %d is %d"%(a,b,a+b))
a= 1436475937.78978927398742897
print("%f"%a)
print("%.10f"%a)
print("%.100f"%a)
a = 25.464646464
b = 32.279293030
print("Sum of %f and %f is %f"%(a,b,a+b))
print("Sum of %.2f and %.2f is %.2f"%(a,b,a+b))
print("sum of {} and {} is {}".format(a,b,a+b))
print("sum of {one} and {two} is {three}".format(one=a,two=b,three=a+b))
a = 1
b = 23
print("%2d"%a)
print("%3d"%b) # it will occupy total 3 spaces
'''

# Method to take input by user at runtime
'''
a = input("Enter Value")
print(a)
print(type(a))
'''

# Method to take Integer Input by user
'''
a= int(input("Enter Value -- "))
print(a)
print(type(a))

# Note - if we take any other value than integer then it will show error
'''
# Method to take Float input by user
'''
a = int(float(input("Enter Value")))
print(a)
print(type(a))
'''

# Method to take all type of input by the user
'''
a = eval(input("Enter Value:"))
print(a)
print(type(a))
'''
'''
# Calculator using eval

exp = eval(input("Enter Expression:"))
print(exp)
'''

# operator  30-05-2019
'''
operator is applied between two operands to perform some specific task
ex - a+b 
here a and b are the operands "+" is a operator 
'''

# Types of operator 
'''
1> Arithmetic operator
'''
# +,-,*,/,//(floor division),**(exponent),%(modulus)
'''
print(34+54)
print(20-10)
print(35*4)
print(45/4)    # return always float 
print(24//5)   # return always integer
print(3**2)    # return power of any number 
print(23%2)    # return remainder
print(2%23)    # return remainder as dividend whenever dividend< divisor
print(-24%6)   # -6*5 + 6    HAMESHA MULTIPLY VALI DIGIT EK ZYDA LETE HA 
print(-23%6)   # -6*4 + 1
print(27%6)    # -6*5 + 3
'''

'''
2> assignment operator
'''
# =,+=,-=,*=,/=,**=,%=
'''
a=10
print(a)
a+=1     # a = a+1
print(a)
a-=1     # a = a-1
print(a)
a*=2
print(a)
a/=2
print(a)
a//=2
print(a)
a**=2   # a = a**2
print(a)
a%=2    # a = a%2
print(a)
'''

'''
3> comparison operator
'''
# <,>,<=,>=,==,!=
# Task of Comparison Operator --- ALWAYS RETURN BOOLEAN VALUE 
# boolean --- True , False 
'''
print(3==3)
print('Hii' == 'Hello')
print(34>2)
print(34>=34)
print(66<=45)
print(24!=35)   # not equal to 
'''

'''
4> logcal operator
'''
# and,or,not
# AND 
'''
T and T = T 
F and T = T
T and F = F 
F AND F = F 
'''
'''
print(3>5 and 35<55)
print(56==56 and 'hii' == 'Hii')
print(4==4 and 5>2)
'''

# OR 
'''
T or T = T 
F or T = T 
T or F = T 
F or F = F 
'''
'''
print(3>5 or 35<55)
print(56==56 or 'hii' == 'Hii')
print(4==4 or 5>2)
'''
# NOT 
'''
not T = F 
not F = T 
'''
'''
print(not 3>2)
print(not 3<2)
'''
# NAND 
'''
T and T = F 
T and F = T
F and T = T 
F AND F = T 
'''
'''
print(3>5 NAND 35<55)
print(56==56 NAND 'hii' == 'Hii')
print(4==4 NAND 5>2)
'''
#Multiple logical operator in an expression
'''
print(345>7 or 'fvvg'!='dgbtr' and 6<1)
print(345>7 and 'fvvg'!='dgbtr' and 6<1)
print(345>7 or 'fvvg'!='dgbtr' or 6<1)
'''

'''
5> Membership operator
'''
'''
# in , not in
print('a' in 'raman')
print('z' in 'shyam')
print('z' not in 'shyam')
'''

'''
6> Identity operator
'''
# is , is not 
'''
a = 12
b = 13
print(a is b)
print(a == b)
a = [34,4,7,2]
b = a.copy()
#b = a
print(a,id(a))
print(b,id(b))
print(a is b)
print(a==b)
print(a is not b)
'''

'''
7> bitwise operator
'''
# bitwise and (&) , bitwise or (|) , bitwise xor(^)
# bitwise left shift (<<) , bitwise right shift (>>)

# bitwise and (&)
'''
1 & 1 = 1
0 & 1 = 0 
1 & 0 = 0 
0 & 0 = 0 
'''
'''
a = 34 
b = 45 
print (a, bin(a))
print(b,bin(b))
print(a&b,bin(a&b))
'''


# bitwise or (|)
'''
1 | 1 = 1
0 | 1 = 1 
1 | 0 = 1
0 | 0 = 0
'''
'''
a = 34 
b = 45 
print (a, bin(a))
print(b,bin(b))
print(a|b,bin(a|b))
'''

# bitwise xor 
'''
1 ^ 1 = 0 
0 ^ 1 = 1
1 ^ 0 = 1 
0 ^ 0 = 0
'''
'''
a = 34 
b = 45 
print (a, bin(a))
print(b,bin(b))
print(a^b,bin(a^b))
'''

# bitwise left shift (<<)
'''
a=12 print(a,bin(a))
print(a<<2,bin(a<<2))
'''

# bitwise right shift (>>)
'''
a=12 print(a,bin(a))
print(a>>2,bin(a>>2))
'''

#8> Ternary operator

'''
num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))
val = "%d is greater" %num1 if(num1>num2)\
else "both number is same" if(num1==num2)\
else "%d is greater"%num2
print(val)
''' 

'''
num1 = int(input("Enter first number")) #23  #13
num2 = int(input("Enter second number")) #12  #22
num3 = int(input("Enter third number")) #21  #50
val = num1 if(num1>=num2 and num1>=num3) else num2 if(num2>=num3) else num3
print(val,"is greatest")
'''
# Ternary operator using tuple 
'''
num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))
val((num2,num1) [num1>=num2])
print(val,"is greatest")              # True me right side ....... False me left side 
'''

# Ternary operator using lambda expression
'''
num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))
val =((lambda:num2,lambda:num1) [num1>=num2] ())
print(val,"is greatest")
'''

# Ternary operator using dictionary
'''
num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))
val =({True:num1,False:num2} [num1>=num2])
print(val,"is greatest")
'''

# CONTROL STATEMENT    03-06-2019
'''
1> if else statement 
2> if elif else statement 
3> nested if else statement 
'''
# 1> if else statement 
'''
syntax

if (condition):
	block of if 
else:
	block of else
'''
# detect either person is eligible for vote in india or not
'''
age = int(input("Enter an age:"))
if(age>=18):
	print("you are eligible for voting in india.")
else:
	print("you are not eligible to vote in india.")
'''

# Detect either number is odd or even 
'''
num = int(input("Enter a number"))
if(num%2==0):
	print(num,"is even number.")
else:
	print(num,"is an odd number.")
'''
# 2> if elif else statement
'''
syntax:

if(condition):
	block of if
elif(condition):
	block of first elif
elif(statement):
	block of second elif:
---------------------------
---------------------------
---------------------------
if(condition):
	block of n elif
	else:
	block of else
'''

# Detect greatest number among three numbers
'''
num = int(input("Enter first number"))
num1 = int(input("Enter second number"))
num2 = int(input("Enter third number"))
if(num>=num1 and num>=num2):
	print(num,"is the greatest number.")
elif(num1>=num2 and num1>=num2):
	print(num1,"is the greatest number.")
else:
	print(num2,"is the greatestnumber.")
'''	

#isinstance
'''
val = 2000.9
print(isinstance(val,str))
print(isinstance(val,int))
print(isinstance(val,float))
'''

#NOTested if else statement
'''
syntax 
if (condition):
	if(condition):
		block of if
	else:
		block of else
else:
	if(condition):
		block of if
	else:
		block of else
'''
'''
age = int(input("Enter an age:"))
if(age<=0 or age>=100):
	print("invalid input")
else:
	if(age>=18):
		print("you are eligible for voting in india")
	else:
		print("you are not eligible to vote in india")
'''

# LEAP YEAR
'''
num = int(input("Enter the year"))
if(num%4==0):
	if(num%100==0):
		if(num%400==0):
			print(num,"year is leap year")
		else:
			print(num,"not a leap year")
	else:
		print(num, "is a leap year")
else:
	print(num,"is not a leap year")
'''

'''
num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))
num3 = int(input("Enter third number"))
if(num1==num2==num3):
	print("All elements are equal")
elif(num1==num2):
	print(num1,num2,"The two elements are equal")
	if(num1>num2 and num1>num3):
			print(num1,"is the greatest")
	elif(num2>num1 and num2>num3):	
			print(num2,"is the greatest")
	else:	
			print(num3,"is the greatest")
elif(num2==num3):
	print(num2,num3,"The two elements are equal")
	if(num2>num3 and num2>num1):
			print(num2,"is the greatest")
	elif(num3>num2 and num3>num2):	
			print(num3,"is the greatest")
	else:	
			print(num1,"is the greatest")
elif(num3==num1):
	print(num3,num1,"The two elements are equal")
	if(num3>num1 and num3>num2):
			print(num3,"is the greatest")
	elif(num1>num2 and num1>num3):	
			print(num1,"is the greatest")
	else:	
			print(num2,"is the greatest")
elif(num1!=num2!=num3):
	if(num1>num2 and num1>num3):
			print(num1,"is greatest")
	elif(num2>num1 and num2>num3):
			print(num2,"is greatest")
	elif(num3>num1 and num3>num2):
			print(num3,"is greatest")
'''
# SWAPPING	
# 1> Swapping using Temporary variable
'''
num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))
print("First number before swapping is",num1)
print("Second number before swapping is",num2)
temp = num1
num1 = num2
num2 = temp
print("First number after swapping is",num1)
print("Second number after swapping is",num2)
'''

# 2> Swapping using multiple variable assignment
'''
num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))
print("First number before swapping is",num1)
print("Second number before swapping is",num2)
num1,num2=num2,num1
print("First number after swapping is",num1)
print("Second number after swapping is",num2)
'''

# 3> Swappingusing arithmetic operation
'''
num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))
print("First number before swapping is",num1)
print("Second number before swapping is",num2)
num1 = num1 + num2    # 3 + 6 = 9
num2 = num1 - num2    # 9 - 6 = 3
num1 = num1 - num2    # 9 - 3 = 6
print("First number after swapping is",num1)
print("Second number after swapping is",num2)
'''

# LOOP
'''
1. Pretested Loop
	a> While Loop
	b> For Loop
2. Post Tested Loop
	a> Do While Loop
# Note - post tested loop has been removed from pyhton .
'''

# A> While Loop
'''
--> while is a keyword which is used to create loop.
--. while loop are responsible for executing a block of statement more than one time.

 Syntax:
 
 while(condition):
	block of while	
	increment or decrement or pass or continue or break
--> block of while statment will execute till condition will be true.
'''

# INFINITE LOOP 
'''
while(True):
	print("infinite")
'''

# MAKE FINITE LOOP FROM INFINITE LOOP
'''
rang = int(input("Enter a range"))
ctr = 0
while(True):
	print("finite")
	ctr=ctr+1
	if(ctr==rang):
		break
'''

# FINITE LOOP USING VARIABILITY IN CONDITION

# detect first 10 natural number
'''
ctr = 1
while(ctr<=10):
	print(ctr)
	ctr = ctr + 1
'''	
	
# detect first 10 natural number and print sum of 10 natural numbers
'''
ctr = 1
sum = 0
while(ctr<=10):
	print(ctr)
	sum = sum + ctr
	ctr = ctr + 1
print("Sum of first %d natural number is %d"%(ctr-1,sum))
'''

'''
ctr = 1
sum = 0
while(ctr<=10):
	print(ctr,end=" ")
	sum = sum + ctr
	ctr = ctr + 1
print("Sum of first %d natural number is %d"%(ctr-1,sum))
'''

# Detect even or odd in range
'''
rang = int(input("Enter a range"))
ctr = 0 
while(ctr<=rang):
	if(ctr%2==0):
		print(ctr,"is an even number")
	else:
		print(ctr,"is an odd number")
	ctr = ctr +1
'''

# Detect even or odd between two range
'''
range1 = int(input("Enter first range"))
range2 = int(input("Enter second range"))
if(range1>range2):
	range1,range2 = range2,range1
while(range1<=range2):
	if(range1&2==0):
		print(range1,"is and even number")
	else:
		print(range1,"is an odd number")
	range1 = range1 +1
'''

# Detect Prime Number
'''
num = int(input("Enter a number"))
flag = 0 
ctr = 2 
while(ctr<num):
	if(num%ctr==0):
		flag = 1 
		break 
	ctr = ctr + 1
if(flag == 0 and num >= 2):
	print(num,"is a prime number")
else:
	print(num,"is not a prime number")
'''

# First N prime numbers
'''
rang = int(input("Enter a range"))
num = 1
count = 0
while(True):
	flag = 0 
	ctr = 2 
	while(ctr<num):
		if(num%ctr==0):
			flag = 1 
			break 
		ctr = ctr + 1
	if(flag == 0 and num >= 2):
		print(num,end = " ")
		count = count +1      #(count+=1)
	num = num + 1
	if(count == rang):
		break
'''


# Factorial Program
'''
num = int(input("Enter a number whose factorial is to be calculated"))
n=num
factorial=1
while(num>0):
	factorial = factorial * num
	num = num - 1
print("Factorial of %d is %d"%(n,factorial))
'''


# To print Factorial with number
'''
num = int(input("enter the number"))
n=num
factorial=1
print(n,"!=",end=" ")
while(num>0):
	factorial=factorial*num
	if(num == 1):
		print(num,end=" ")
	else:
		print(num,end="*")
	num = num-1
print("=",factorial)
'''
# REVERSE A NUMBER
'''
n=int(input("enter the number"))
rev=0
while(n>0):
	dig=n%10
	rev=rev*10+dig
	n=n//10
print("reverse of digit ",rev)
'''

# PALINDROME NUMBER
# 69696 = 69696
'''
num=int(input("enter the number"))
n=num
rev=0
while(num>0):
	rem=num%10
	rev=rev*10+rem
	num=num//10
if(n==rev):
	print(n,"is a palindrom")
else:
	print(n,"is not a palindrom")
'''


# ARMSTRONG NUMBER
# 153 = 1**3+5**3+3**3=153
num = int(input("enter a number"))
n = num
count = 0
while (num>0):	
	count = count + 1
	num = num // 10
print(count)
num = n
sum = 0 
while(num>0):
	rem = num % 10
	sum = sum + rem**count
	num = num // 10
print(sum)
if(n==sum):
	print(n,"is an armstorng number")
else:
	print(n,"is not an armstrong number")
