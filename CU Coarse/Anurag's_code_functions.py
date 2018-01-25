from math import *
import sys
from time import *
from random import*
import hangmanlib

def triangle(n):
    """Gives triangular number"""
    return(n*(n+1)/ 2)

def sum_of_squares(n):
    """Takes the sum of all squares from "1" to "n"""
    return(n*(n+1)*(2*n+1))/6

def sum_of_cubes(n):
    """Takes the sum of all cubes from "1" to "n"""
    return(((n)*(n+1))/2)**2

def binomial(n,r):
    """Gives binomial co-efficieant """
    return(factorial(n))/((factorial(r))*(factorial(n-r)))

def tens_digit(n):
    """Gives the tens digit of any input"""
    return (n-((n//100)*100))//10 

def tens_digit(n):
    """Gives the tens digit of any input"""
    return int ((n//10)%10)

def print_sum2(a, b):
    """Print the sum of two numbers."""
    numsum = a + b
    print (a, '+', b, '=', numsum)

def hypotenuse_func (x,y):
    """Gives the hypotenuse"""
    return (sqrt(x**2 + y**2))

def print_sum(a, b):
 """Print the sum of two numbers."""
 print (a, '+', b, '=', a+b) 

 def print_sum_input():
    """Print the sum of two numbers entered from the terminal"""
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print (num1, '+', num2, '=', num1 + num2)

def chg_val(n):
    """Changes the value of the input"""
    num=3
    return(num)

def is_even (n):
    """Returns true if "n" is even"""
    return(n % 2 == 0)

def hello(): 
    """Returns Hello "Input" """
    name = input("Enter name: ")
    print ("Hello,",name )


def pos_or_neg(x):
    """Print "positive","negative,or"zero" """
    if x > 0:
        print ("positive")
    elif x < 0:
        print ("negative")
    else:
        print ("zero")

def is_pos(n):
    """ Returns true if n is positive"""
    return (n > 0)

def almost_equal(a,b,epsilon):
    """ Shows true if they are almost equal"""
    return (abs(a-b) < epsilon)


def sign(n):
    """Sign of return matches sign of "n" """
    if n>0:
        return (1)
    elif n<0:
        return (-1)
    else:
        return (0)


def heron(a,b,c):
    """ Area of a triangle given three sides"""
    s = (a+b+c)/2
    if a > 0 and b>0 and c > 0 :
        return ( sqrt((s)*(s-a)*(s-b)*(s-c)))
    else:
        return (0.0)

def collatz_func(n):
    if n%2==0:
        return (n/2)
    else:
        return (3*n+1)

def day_of_week(month,day,year):
    if month is 1:
        return (((day)+(26)+(8)+(year-1)+(floor((year-1)/4))-(floor((year-1)/100))+(floor((year-1)/400))+(2))%7)
    elif month is 2:
        return (((day)+(28)+(9)+(year-1)+(floor((year-1)/4))-(floor((year-1)/100))+(floor((year-1)/400))+(2))%7)
    else:
        return (((day)+(2*month)+(floor((3*(month+1))/5))+(year)+(floor(year/4))-(floor(year/100))+(floor(year/400))+(2))%7)

def fibonacci_sequence():
    a,b = 0,1
    while b<10000000:
        return (b)
        a,b = b,a+b

def is_odd(n):
    if n% 2 == 1:
        return ('true')
    else:
        return ('false')

def print_odd_even(n):
    if is_odd(n):
        return ('odd')
    else:
        return ('even')

assert sum_of_squares(25) == 5525

assert sum_of_cubes(30) == 216225

assert almost_equal(2.3*3,6.9,1e-6)
assert not almost_equal(2.3*3,6.9,1e-30)

assert binomial(25,8) == 1081575

assert tens_digit(7) == 0
assert tens_digit(37) == 3
assert tens_digit(1025) == 2

assert sign(3.5) == 1
assert sign(-6.7) == -1
assert sign(0) == 0

assert heron(-3,-2,6) == 0
assert heron(3,0,3) == 0
assert heron(13,14,15) == 84
assert abs(heron(13,13,15) - 79.638) < 0.01

assert collatz_func(3882) == 1941
assert collatz_func(3883) == 11650

##assert day_of_week(6, 2, 2014) == 2
##assert day_of_week(2, 22, 1732) == 6







def fact(n):
    """Returns n factorial"""
    if n<=1:
        return (1)
    else:
        return (n* fact(n-1))

def phi():
    """Returns the value of the golden ration"""
    return (1+(sqrt(5)))/2

def binet(n):
    """Returns the nth fibonacci number"""
    b = (phi())
    return ((b**n)-((-b)**(-n)))//(sqrt(5))

def lucas(n):
    """Returns nth Lucas number"""
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return (lucas(n-2)+lucas(n-1))

def div_11_13(n):
    """Returns true if n is divisable by 11 or 13"""
    return n%11 ==0 or n%13 ==0

def find_div_11_13(start):
    """Finds the first integer greater than start that is divisible by 11 or 13"""
    if start % 11 == 0 or start %13 == 0:
        return start
    else:
        return find_div_11_13(start + 1)

def digit_sum(n):
    """Returns the sum of the digits of n"""
    if n==0:
        return 0
    else:
        return n%10 + digit_sum(n//10)

def find_digit_sum(dsum, start):
    """Returns the number greater than start that the sum of its digits is of dsum"""
    if digit_sum(start) == dsum:
        return start
    else:
        return find_digit_sum(dsum, start+1)
    
def gcd(m,n):
    """Returns GCD of m and n"""
    if n==0:
        return m
    else:
        return gcd(n,(m%n))

def fib_time(n):
    """Returns nth fibonnacci number and time elapsed"""
    start = time()
    result = fib(n)
    end = time()
    print ("Time elapsed:", end - start, 'sec')
    return result

assert binet(30) == 832040

assert lucas(25) == 167761

assert not div_11_13(254)
assert div_11_13(253)
assert div_11_13(481)
assert div_11_13(572)

assert find_div_11_13(5) == 11
assert find_div_11_13(408) == 416

assert digit_sum(7) == 7
assert digit_sum(9876) == 30

assert find_digit_sum(21,1) == 399
assert find_digit_sum(5,290) == 302

##assert gcd(6409, 29203) == 29
##assert gcd(14356,1295) == 375
    
def sum_even_squares(n):
    """returns sum of all even squares """
    sum=0
    for i in range(2, 2**n+1,2):
        sum += i**2
        return(sum)

def print_pairs(list1,list2):
    """Prints each element in list with each element in list2"""
    for elt1 in list1:
        for elt2 in list2:
            print (elt1,elt2)

list1 = list(range (21,101))
list2 = list(range (7, 701, 7))
list3 = list(range (150, 9, -2))

def sum_factorials(n):
    """Returns the sum of all the factorials up to n"""
    sum = 0
    for i in range(1, n+1):
        sum += fact(i)
    return sum

def sum_div_3_5(n):
    """Returns the sum of all integers that are divisible by 3 or five less than n"""
    sum = 0
    for i in range(1, n+1):
        if i % 3 == 0 or i%5 == 0:
            sum += i
    return sum

def product (alist):
    """product of all terms in the list"""
    product = 1
    for i in alist:
        product = product * i
    return product

def num_divisors(n):
    """Returns the number of divisors of n"""
    sum = 0
    for i in range(1, n+1):
        if n % i == 0:
            sum += 1
    return sum

def print_square(n):
    """prints a square of numbers with lenght n"""
    start = 1
    for row in range(1, n+1):
        for column in range (1, n+1):
            print (start, end=" ")
            start += 1
        print ()

def print_triangle(n):
    """prints a trianlge of numbers"""
    start = 1
    for row in range(1, n+1):
        for column in range (1, row+1):
            print (start, end=" ")
            start += 1
        print ()
    
def prime_or_composite():
    for n in range(2,10):
	for x in range (2,n):
            if n % x ==0:
		print (n,'equals',x, '*', n//x)
		break
	else:
	    print (n, 'is a prime number')

def is_prime(n):
    """Returns if the n is prime or not"""
    if n == 1:
        return False
    for i in range(2, n):
        if n%i ==0:
            return False
    return True

def count_primes(numlist):
    """Counts the primes in numlist"""
    counter = 0
    for elt in numlist:
        if is_prime(elt)==True:
            counter += 1
    return counter

def series1(n):
    sum = 0
    for i in range (0, n):
        sum += (1/factorial (i))
    return sum

def series2(n):
    sum = 0
    for i in range (1, n+1):
        sum += (1/(i**2))
    return sum
    
def series3(n):
    sum = 0
    for i in range (1, n+1):
        sum += (1/(2*i-1))*(-1)**(i+1)
    return sum

assert list1 == list(range(21,101))
assert list2 == list(range(7,701,7))
assert list3 == list(range(150,9,-2))

assert sum_div_3_5(90) == 1935

assert sum_factorials(15) == 1401602636313

assert product(list(range(60,82,3))) == 587297574864000

assert num_divisors(60**4) == 225

assert not is_prime(1)
assert not is_prime(4)
assert is_prime(3)
assert not is_prime(91)
assert is_prime(7919)

assert count_primes(list(range(1,701))) == 125

##def almost_equal(a, b, eps):
##    return(abs(a-b) < eps)
##
##assert almost_equal(series1(8), 2.71825, 1e-4)
##assert almost_equal(series2(20), 1.59616, 1e-4)
##assert almost_equal(series3(30), 0.777067, 1e-4)

def cubes(n):
    alist = []
    for i in range(1, n+1):
        alist.append(i**3)
    return alist

list1 = [2**i for i in range(0, 10)]
list2 = [i**2 for i in range(2, 21, 2)]
list3 = [i for i in range (1, 10) if i%3 != 0 ]

listgryfindor = ['Harry', 'Ron', 'Hermione']
listslytherine = ['Malfoy','Crabbe', 'Goyle']

list4 = [[elt1, elt2] for elt1 in listgryfindor for elt2 in listslytherine]

lista = ['H','T']
list5 = [[i, j, k] for i in lista for j in lista for k in lista]

def divisors(n):
    alist = []
    for i in range(1, n+1):
        if n%i == 0:
            alist.append(i)
    return alist

def sum_divisors(n):
    return sum (divisors(n))
    
def primes(maxval):
    blist = []
    for i in range(1, maxval+1):
        if is_prime(i):
            blist.append(i)
    return blist

def extract_primes(alist):
    return [i for i in alist if is_prime(i)]

def divisors2(n):
    return[i for i in range(1, n+1) if n%i == 0]


assert list1 == [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]

assert list2 == [4, 16, 36, 64, 100, 144, 196, 256, 324, 400]

assert list3 == [1, 2, 4, 5, 7, 8]

assert sorted(list4) == sorted([['Harry', 'Malfoy'], ['Harry', 'Crabbe'], ['Harry', 'Goyle'], ['Ron', 'Malfoy'], ['Ron', 'Crabbe'], ['Ron', 'Goyle'], ['Hermione', 'Malfoy'], ['Hermione', 'Crabbe'], ['Hermione', 'Goyle']])

assert sorted(list5) == sorted([ ['H', 'H', 'H'], ['H', 'H', 'T'], ['H', 'T', 'H'], ['H', 'T', 'T'], ['T', 'H', 'H'], ['T', 'H', 'T'], ['T', 'T', 'H'], ['T', 'T', 'T'] ])
assert divisors(2015) == [1, 5, 13, 31, 65, 155, 403, 2015]
assert divisors2(2015) == [1, 5, 13, 31, 65, 155, 403, 2015]

assert sum_divisors(2015) == 2688

assert primes(2) == [2]
assert primes(71) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]

assert extract_primes(list(range(101,110))) == [101, 103, 107, 109]


def squares_suffix(two_digits, n):
    dlist = []
    num  = 1
    while len(dlist)<n:
        if (num**2) % 100 == two_digits:
            dlist.append (num**2)
        num +=1
    return dlist

def first_num_divisors(ndiv):
    counter = 1
    while True:
        if num_divisors(counter) == ndiv:
            return counter
        counter +=1

def digit_sum(n):
    sum = 0
    lists = []
    while True:
        if n != 0:
            b = n % 10
            lists.append(b)
        n = floor(n/10)
    print (sum (lists))


def problem1(n):
    return sum( i**3 for i in range(1, 2*n, 2))

def problem2():
    return sum (i - 1/2 for i in range(1, 51))

def problem3(n):
    xlist = []
    counter = 1
    while len(xlist)<n:
        if counter%5 != 0 and counter%7 != 0:
            xlist.append(counter)
        counter +=1
    return xlist[n-1]

def problem4():
    product = 1
    for i in range (11, 110, 2):
        product = product * i
    return product % 10

def problem6():
    for i in range (0, 10):
        for y in range(0, 10):
            if 2014 - (1900 +10*i +y) == 20*i +2*y:
                return 1900 + 10*i +y
def problem5():
    sum = 0
    for i in range (4, 177, 4):
        sum = sum + sin(i *(pi/180))**2
    return sum

def problem8():
    num = 1000
    while True:
        sqrt(num) != 3*digit_sum(num)
        num += 1
    return num

def digit_sum(n):
    sum = 0
    while n != 0:
        sum += n % 10
        n = (n//10)
    return (sum)
    
def guess(n):
    x = randint(1, n+1)
    print("I'm thinking of a number  from 1 to ", str(n))
    guess = (input) ("Can you guess my number?")
    while int(guess) != x:
        if int(guess) > x:
            print ("Your guess is too high." )
            guess = input("Guess again")
        else:
            print ("Your guess is too low.")
            guess = input("Guess again")
    print("Correct!")

def random_word():
    return choice(hangmanlib.words)

def hangman_dashed(word, letters):
    dashed = []
    for i in range (len(word)):
        dashed += ["__"]
    chg_list(dashed)

def hangman():
    print("Let's play Hangman!")
    print (hangmanlib.pics[0])
    word = random_word()
    print (word)
    letter = input ("Guess a letter:")
    counter = 0
    dashed = []
    while counter < 7:
        if not letter in word:
            print ("Sorry, the letter",letter,"is not in the word")
            counter+=1
            letter = input ("Guess a letter:")
            print (hangmanlib.pics[counter])
            if counter == 7:
                print ("You Lose!")
        elif dashed[i] != "__":
            print (hangmanlib.pics[counter])
            print ("You Win!")
        else:
            print ("Good guess!")
            print (hangmanlib.pics[counter])
            print (chg_list(dashed))

def chg_list(dashed):
    word = random_word()
    x = [i for i in range(len(word)) if word[i]]
    n = len(x)
    counter =0
    while counter < n:
        dashed[x[counter]] = letter

