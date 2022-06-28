'''
1. What does an empty dictionary&#39;s code look like?
'''
dictionary={}
print(dictionary)
print(type(dictionary))

'''
2. What is the value of a dictionary value with the key 'foo' and the value 42?

{'foo':42}
'''

'''
3. What is the most significant distinction between a dictionary and a list?

dict--> key value pair, {}
dict--> values, []
'''

'''
4. What happens if you try to access spam['foo'] if spam is {'bar': 100}?

it will show you key error as foo key not found
'''
# spam={'bar':100}
# spam['foo']

'''
5. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys()?

cat in spam check in dict and cat in spam.keys() will check cat in keys defined in the dict
no difference
as both show True
'''
# spam={'cat':'animal'}

# print('cat' in spam)
# print('cat' in spam.keys())

'''
6. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.values()?

cat in spam  check cat in dict and cat in spam.values() will check cat in value against the key defined

'''

'''
7. What is a shortcut for the following code?
if 'color' not in spam:
spam['color'] = 'black'

'''
spam={}
spam['color']='black'
print(spam)

'''
8. How do you &quot;pretty print&quot; dictionary values using which module and function?

no idea
'''
