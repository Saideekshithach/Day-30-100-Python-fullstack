#Anonymous functions are nameless functions we use a keyword called as lambda to create anonymous functions.

'''def cal(x):
    res=2*x+5
    return res
print(cal(5))'''
'''def f(x):
    print(2*x+5)
f(5)

def f(x):
    return (2*x+5)
print(f(5))

def f():
    x=int(input("enter the value:"))
    print(2*x+5)
f()'''

#syntax
#a-lambda arg:expr
'''
a=lambda x:2*x+5
print(a(5))

a=int(input("a value"))
b=lambda x:2*x+5
print(b(a))

print((lambda x,y:x+y)(3,5))

a=lambda x,y:x+y
print(a(3,5))'''

'''a=lambda x:x.upper()
x=input()
print(a('codegnan'))
print(a(x))'''

'''a="codegnan"
b=lambda a:a.upper()
print(b(a))'''

a=[1,2,3,4,5]
b=lambda a:a**2 for i in a
print(b(a))


'''#python course
#Python Course
a="python course"
b=lambda a:a.title()
print(b(a))'''

'''a=lambda a:a.title()
print(a("python course")'''

'''a,b=[str(x) for x in input("enter the names").split(",")]
c=lambda a,b:(a+" "+b).title()
print(c(a,b))

fname,lname=input("enter the names").split(",")
fullname=lambda fname,lname:(fname+" "+lname).title()
print(fullname(fname,lname))'''

'''a=input("fname")
b=input("lname")
c=lambda a,b:(a+" "+b).title()
print(c(a,b))'''

#filter
'''a=[10,20,17,40,60,80,35,67]
if a%2==0:
   print(a)'''

'''a=[10,20,17,40,60,80,35,67]
for i in a:
    if i%2==0:
        print(i)

a=[10,20,17,40,60,80,35,67]
b=list(filter(lambda a:a%2==0,a))
print(b)

a=[10,20,17,40,60,80,35,67]
b=list(filter(lambda a:a%2!=0,a))
print(b)

a=[10,20,17,40,60,80,35,67]
b=tuple(filter(lambda i:i%2!=0,[10,20,17,40,60,80,35,67]))
print(b)'''

'''a=[[],(),set(),{},None," ",4,6.7,"python",5+9j,True,False]
b=list(filter(None,a))
print(b)'''

'''a=[[],(),set(),{},None," ",0+0j,4,6.7,"python",5+9j,True,False]
b=list(filter(None,a))
print(b)'''

'''a=int(input("a value:"))
b=int(input("b value:"))
c=lambda a,b:(a+b,a-b,a*b)
print(c(a,b))'''





