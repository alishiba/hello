Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
name="python programming"
len(name)
18
max(name)
'y'
min(name)
' '
name.count(" ")
1
name.split()
['python', 'programming']
#hello
name.split()#chopping
['python', 'programming']
name="Diksha Rana"
print(name)
Diksha Rana
name="Diksha\nRana"
print(name)
Diksha
Rana
m="key\t name\t age"
m.count(" ")
2
m.count("\t
        
SyntaxError: unterminated string literal (detected at line 1)
'm.count("\t")
        
SyntaxError: unterminated string literal (detected at line 1)
m.count("\t")
...         
2
>>> name="age\lie"
...         
>>> print(name)
...         
age\lie
>>> letter="""name hello"""
...         
>>> print(letter)
...         
name hello
>>> """name hello"""
...         
'name hello'
>>> age=20
...         
>>> if age<30:
...         print("ok")
... else:
...     print("not ok")
... 
...     
ok
>>> a==10
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    a==10
NameError: name 'a' is not defined
>>> a==10\a<=4
SyntaxError: unexpected character after line continuation character
>>> if a==10 and a<=8:
...     print("yes")
... else:
...     print("okey")
... 
...     
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    if a==10 and a<=8:
NameError: name 'a' is not defined
