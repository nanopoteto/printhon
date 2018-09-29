import inspect
import re
import printhon

def print_default(*input):
    if len(input) == 1:
        input = input[0]
    if printhon.color == 'blue':
        print("\033[0;34m" + str(input) + "\033[0;39m")
    elif printhon.color == 'yellow':
        print("\033[0;33m" + str(input) + "\033[0;39m")
    elif printhon.color == 'green':
        print("\033[0;32m" + str(input) + "\033[0;39m")
    elif printhon.color == 'red':
        print("\033[0;31m" + str(input) + "\033[0;39m")
    else:
        print(str(input))

def printnv(input, con=''):
    context = inspect.getframeinfo(inspect.currentframe().f_back).code_context[0]
    text = re.search(r'\(.*\)', context).group()[1:-1].split(',')[0]
    print_default(text+con, input)
    
def nv(input, con=''):
    context = inspect.getframeinfo(inspect.currentframe().f_back).code_context[0]
    text = re.search(r'\(.*\)', context).group()[1:-1].split(',')[0]
    print_default(text+con, input)
    
def p(input):
    print_default(input)
        
def line(input=None, mark='-'):
    if input is not None:
        input = str(input)
        output = mark*(24-len(input)//2) + ' ' + str(input)+ ' ' + mark*(24-len(input)//2)
        print_default(output)
    else:
        print_default(mark*50)
    
    