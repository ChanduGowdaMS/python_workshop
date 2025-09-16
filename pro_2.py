'''
#day1  validate id and password 
id = "2211"
password = "12345"
if id == '2211':
    print("id is correct")
    if password=="12345":
        print("password is correct")
    else:
        print("incorrect password")
else:
    print("incorrect id")
'''
'''
m = int(input("enter the marks"))
if m >=0 and m<=100:
    if m >= 80 and m <= 100:
        print("A")
    elif m>=50 and m<=79:
        print("B")

    elif m >= 35 and m<=49:
        print ("c")

    else :
        print("file")

else:
    print("invalid")
'''
'''
#day2 to print even number between 10 and 20
i = 10
while i <= 20:
    if i%2==0:
        print(i)
    i+=1
'''
'''
#to print number 0 to 10
i=0
while i <=10:
    print(i)
    i+=1
'''
'''
i = 30
while i >= 12:
    if i%2==1:
        print(i)
    i-=1
'''

'''
a="CSISESYSS"
c=list(a)
i,b=0,''
while i<len(c):
    if i%2==1:
        b=b + c[i]
    i+=1
print(b)
'''
'''
a=[19,2,13,4,5,11,-1,-17]
i=0
c=0
while i < len(a):
    if a[i]> 0:
        if a[i]%2 == 1:
            c= c +a[i]
    i+=1
print(c)
'''
'''
a='AsD'
i=0
e=''
while i<len(a):
    if 'A'<=a[i]<='Z':
        b = ord(a[i])+ 32
        e+=chr(b)
    else:
        e+=a[i]
    i+=1
print(e)
'''
'''
a="prof123@gmail.com"
b,c,d='','',''
i=0
while i < len(a):
    if 'a'<=a[i]<='z' or 'A'<=a[i]<='Z':
        b=b+a[i]
    elif '0' <= a[i] <= '9':
        c=c+a[i]

    else:
        d+=a[i]
    i+=1
print(b)
print(c)
print(d)
'''

'''
#day 3 for loop
a='hello'
for i in a:
    print(i)
'''
''' 
a="12345"
for i in a:
    print('12345')
'''
'''
for i in range(6, 13):
    if i%2 ==0:
        print(i)
'''
'''
b='teachers'
c=0
for i in range(0, len(b)):
    if i%2==1:
        c+=i
print(c)
'''
'''
s= 'swapnodaya'
y=''
for i in range(len(s)):
    if i%2==0:
        y+=s[i]
print(y)

'''
'''
b = 'Swapnodaya Exskilence'
k=0
for i in b:
    if i in 'aeiou':
        k+=1

print(k)
'''

'''

b = 'Swapnodaya Exskilence'
k=0
for i in b:
    if i in 'aeiouAEIOU':
        k+=1

print(k)

'''
'''
b = 'Swapnodaya Exskilence'
k=0
i=0
while i < len(b):
    if b[i] in 'aeiou':
        k+=1
    i+=1
print(k)
    
'''
'''
b = 'Swapnodaya Exskilence'
k=0
i=0
while i < len(b):
    if b[i] in 'aeiouAEIOU':
        k+=1
    i+=1
print(k)
'''
'''
d=['hello', 52, 'hi']
e=[]
for i in d:
    c=0
    if type(i)==str:
        for j in i:
            c+=1
        e+=[c]

print(e)
'''
'''
d="Malayalam"
c,e,f='','',0
b=len(d)-1
for i in d:
    c+=d[b]
    b-=1
    if i=='a' and i not in e:
        e+=i
        f+=1
    elif i=='a':
        f+=1
e+=str(f)
print(c)
print(e)
'''

'''
d="malayalam"
a,z='','a'
c=0
for i in d:
    a=i+a
    if i==z:
        c+=1
z+=str(c)
print(z)
if a==d:
    print("palindrome")
else:
    print("not palindrome")

'''
'''
z ='aabbccc'
y=''
for i in z:
    c=0
    if i not in y:
        y+=i
        for j in z:
            if i==j:
                c+=1
        y+=str(c)
print(y)
'''
'''
i=0
while i<10:
    print(i)
    if i==4:
        break
    i+=1

'''
'''
for i in range(10):
    print(i)
    if i==4:
        break
'''
'''
for i in range(1,11):
    if i==6:
        continue
    print(i)
'''
'''
i=1
while i<= 10:
    if i==6:
        i+=1
        continue
    print(i)
    i+=1
'''
'''
l =[64,42,97,69]
c=0
for i in l:
    if c<i:
        c=i

print(c)
'''
'''
l=[-4,-6,-1,-9]
t=l[0]
for i in l:
    if i > t:
        t=i
print(t)
'''
'''
l =[64,42,97,69]
for i in l:
    for j in l:
        if j>i:
            i=j
    break

print(i)
'''
'''
l=[69, 88, 54, 75]
f=float('-inf')
s=float('-inf')
for i in l:
    if i>f:
        s=f
        f=i
    elif i>s:
        s=i
print(f)
print(s)
'''
'''
n=1
while n<=3:
    print(n, end = '')
    n+=1
    if n==2:
        continue
    print(n,end ='')
'''
'''
x=0
y=10
while x<y:
    x+=1
    y-=1
print(x, y)
'''
'''
n=0
while n<5:
    if n==3:
        break
    n+=1
else:
    n+=2
print(n)
'''
'''
sum=0
for i in range(5):
    sum+=i
print(sum)
'''
'''
x=1
for i in range(1,5):
    x*=i
print(x)
'''
'''
l=['hello','world','!']
s=''
for i in l:
    s+=i+' '
print(s.strip())
'''
'''
colors = ['red', 'green', 'bule']
for i in colors:
    if len(i)>4:
        break
    print(i, end =' ')
'''
'''
i = 0
while i<10:
    print(i, end=' ')
    i+=1
    if i==6:
        break
'''
'''
l=[1,2,3,4,5,6]
for i in l:
    if i%3==0:
        continue
    print(i,end=' ') 
'''
'''
a=[10,20,30,40,50]
i=0
while i <len(a):
    i+=1
    if a[i-1]==30:
        continue
    print(a[i-1], end =' ')
'''
'''
limit = 20
print(f"Fibonacci numbers less than {limit}:")
a = 0
b = 1

if limit > 0:
    
    if a < limit:
        print(a, end=" ")
    while b < limit:
        print(b, end=" ")
       
        a, b = b, a + b

print()
'''
