#1. What exactly is []?
'''
empty list
'''

#2. In a list of values stored in a variable called spam, how would you assign the value &#39;hello&#39; as the
#third value? (Assume [2, 4, 6, 8, 10] are in spam.)

l=[2,4,6,8,10]
print(l)
l.insert(2,'hello')
print(l)

#Let&#39;s pretend the spam includes the list [&#39;a&#39;, &#39;b&#39;, &#39;c&#39;, &#39;d&#39;] for the next three queries.

#3. What is the value of spam[int(int(&#39;3&#39; * 2) / 11)]?

spam=['a','b','c','d']
print(spam)
print(int(int('3'*2)/11))
print(spam[3])
'''
d
'''

#4. What is the value of spam[-1]?
print(spam[-1])
'''
d
'''

#5. What is the value of spam[:2]?
print(spam[:2])
'''
['a','b']
'''

#Let&#39;s pretend bacon has the list [3.14, &#39;cat,&#39; 11, &#39;cat,&#39; True] for the next three questions.

#6. What is the value of bacon.index(&#39;cat&#39;)?

bacon=[3.14,'cat',11,'cat','True']

print(bacon.index('cat'))
'''
1
'''

#7. How does bacon.append(99) change the look of the list value in bacon?

bacon.append(99)
print(bacon)

'''
[3.14, 'cat', 11, 'cat', 'True', 99]
'''

#8. How does bacon.remove(&#39;cat&#39;) change the look of the list in bacon?
bacon.remove('cat')
print(bacon)
'''
[3.14, 11, 'cat', 'True', 99]
'''

#9. What are the list concatenation and list replication operators?
'''
concat--> +
replication--> *
'''

#10. What is difference between the list methods append() and insert()?
'''
append--> add element in list at the end
insert--> add element at particular index mentioned
'''

#11. What are the two methods for removing items from a list?
'''
pop
remove
'''

#12. Describe how list values and string values are identical.
'''
both are sequential
'''

#13. What&#39;s the difference between tuples and lists?
'''
list-->mutable
tuple--> immutable
'''

#14. How do you type a tuple value that only contains the integer 42?
a=(42,)
print(a)

#15. How do you get a list value&#39;s tuple form? How do you get a tuple value&#39;s list form?
l=[1,2,3,4]
print(tuple(l))

t=(1,2,3,4)
print(list(t))

#16. Variables that &quot;contain&quot; list values are not necessarily lists themselves. Instead, what do they
#contain?

'''

'''

#17. How do you distinguish between copy.copy() and copy.deepcopy()?
'''
shallow copy -->copy.copy()--> creates copy of an object but store reference of  each element of the object
deep copy -->copy.deepcopy()--> creates copy of object and elements of the object
'''
import copy
ol=[[1,2,3],[4,5,6],[7,8,9]]
nl=copy.copy(ol)
nl[0][1]=100
print(ol)
print(nl)
'''
[[1, 100, 3], [4, 5, 6], [7, 8, 9]]
[[1, 100, 3], [4, 5, 6], [7, 8, 9]]
'''

old=[[1,2,3],[4,5,6],[7,8,9]]
nld=copy.deepcopy(old)
nld[0][1]=100
print(old)
print(nld)
'''
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
[[1, 100, 3], [4, 5, 6], [7, 8, 9]]

'''




