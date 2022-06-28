'''
1. What are escape characters, and how do you use them?

use to insert special characters with \ in strings 
eg. if you want string from next line we use \n 

'''
txt=' please enter this in next \n line'
print(txt)

'''
2. What do the escape characters n and t stand for?

n--> next line
t--> tab

'''

'''
3. What is the way to include backslash characters in a string?

using \\'
'''

'''
4. The string "Howl's Moving Castle" is a correct value. Why isn't the single quote character in the word Howl's not escaped a problem?

here "" and '' both are used for strings but if there is ' then we use "" to make it start and end of string

'''

'''
5. How do you write a string of newlines if you don't want to use the n character?

using ''' '''

'''

'''
6. What are the values of the given expressions?
'Hello, world!'[1]-->e
'Hello, world!'[0:5]-->Hello
'Hello, world!'[:5]-->Hello
'Hello, world!'[3:]-->lo, world!

'''
print('Hello, world!'[1])
print('Hello, world!'[0:5])
print('Hello, world!'[:5])
print('Hello, world!'[3:])

'''
7. What are the values of the following expressions?
'Hello'.upper()-->HELLO
'Hello'.upper().isupper()-->True
'Hello'.upper().lower()-->hello

'''
print('Hello'.upper())
print('Hello'.upper().isupper())
print('Hello'.upper().lower())

'''
8. What are the values of the following expressions?
'Remember, remember, the fifth of July.'.split()--> ['Remember,', 'remember,', 'the', 'fifth', 'of', 'July.']
'-'.join('There can only one.'.split())--> first split and then join-->There-can-only-one.

'''

print('Remember, remember, the fifth of July.'.split())
print('-'.join('There can only one.'.split()))

'''
 9. What are the methods for right-justifying, left-justifying, and centering a string?
 
 right justify--> rjust
 left jystify--> ljust
 center-->center
 
'''

'''
10. What is the best way to remove whitespace characters from the start or end?
-->lstrip and rstrip
'''