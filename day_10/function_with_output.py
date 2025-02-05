"""It is a function with some return value"""  #docstrings

def function1(text):
    return text + text

def function2(text):
    return text.title()    # .title() makes first letter capitalise and rest keeps small

function1_output = function1("Hello")
print(function1_output)

function2_output = function2(function1("hello"))
print(function2_output)