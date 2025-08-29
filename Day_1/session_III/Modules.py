#!/usr/bin/env python
# coding: utf-8

# In[9]:


def add_num(a,b) -> float:
    '''Returns addition of two numbers. Function takes only two arguments
    
    Usage:
    >>> add_num(1,2)
    3
    '''
    return a+b
def sub_num(a,b) -> float:
    '''Returns subtraction of two numbers. Function takes only two arguments
    
    Usage:
    >>> sub_num(2,1)
    1
    '''
    return a-b
def mul_num(a,b)->  float:
    '''Returns multiplication of two numbers. Function takes only two arguments
    
    Usage:
    >>> mul_num(1,2)
    2
    '''
    return a*b
def div_num(a,b)->  float:
    '''Returns division of two numbers. Function takes only two arguments
    
    Usage:
    >>> add_num(1,2)
    0.5
    '''
    return a/b



if __name__ == '__main__':
    choice = input('A-->addition\nS-->subtraction\nM-->Multiplication\n')
    num = input('Input two numbers seperated by comma').split(',')
    (a,b) = float(num[0]),float(num[1])
    if choice.upper() == 'A':
        print(add_num(a,b))
    elif choice.upper() == 'S':
        print(sub_num(a,b))
    elif choice.upper() == 'M':
        print(mul_num(a,b))
             
     