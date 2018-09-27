import inspect
import re

def printnv(input, con=''):
    # print inspect.currentframe().f_back.f_restricted
    context = inspect.getframeinfo(inspect.currentframe().f_back).code_context[0]
    # text = context.split('(')[1].split(')')[0]
    text = re.search(r'\(.*\)', context).group()[1:-1].split(',')[0]
    print(text+con, input)