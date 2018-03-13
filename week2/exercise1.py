"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

# I think this will write a string of words
some_words = ['what', 'does', 'this', 'line', 'do', '?'] # It listed each item in a string

# I think this will search for the function word
for word in some_words:
    print(word) # it did nothing

# I think this will search for the function x in some_words
for x in some_words:
    print(x) # this did nothing

# I think this will search for the function some_words
print(some_words) # this did nothing

# I think this will print 'some_words contains more than 3 words' if there are more than 3 words
if len(some_words) > 3:
    print('some_words contains more than 3 words') # this printed some_words contains more than 3 words

# this will return a certain set of information 
def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname())

usefulFunction() # this returns information about my computer
