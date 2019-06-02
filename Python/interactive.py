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
a=12 print(a,bin(a))
print(a>>2,bin(a>>2))

'''
8> ternary operator
'''