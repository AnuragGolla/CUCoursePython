from math import *
import sys

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






