#a=0,1,2
#print(len(a))
#a=3j+5
#print(a)
'''  a=32
      print(a)'''
#LIST 
#a=[100,2.3,5j,'hi',[1,5],(2,5)]
#print(a[-3])
'''a.append(10)
print(a)
a.pop(-2)
print(a)'''
'''a=10
print(type(a))'''
'''a=10,20,30
print(type(a))'''
'''set={10,20,30}
print(set)'''
'''dict={'a':10}
print(dict)'''
'''a={'a':[10,20,30],'b':[40,50,60]}
print(a['b'][-1])'''
'''a='hello'
print(a[2:4:1])'''
'''a="good morning"
print(a[7:11])
print(a[-5:-1])
a='hello'
print(a[3:0:-1])
print(a[-2:-5:-1])
a='good morning'
print(a[1:5+1:2])
print(a[5:12:3])
print(a[-9::4])
print(a[-9:-2:4])'''
'''a=int(input("enter the number:"))
print(a)'''
'''a= int(input("enter the number:"))
if a%2==0:
     print("even")
else:
     print("odd")'''


'''l=eval(input("enter the number"))
if len(l)==5:
     print("length is 5")
else:
     print("lengthis not 5")'''

'''username=input("enter :")
if username=='hero':
    print("correct username")
    pw=input("enter the password:")
    if pw=='123456':
        print("sucessfully loggined in ...! ")
    else:
        print("password incorrect")
else:
    print("incorrect username")    '''

'''i=1
while i<=100:
    print(i)
    i+=1'''


'''print("Lowercase:")
for letter in "abcdefghijklmnopqrstuvwxyz":
    print(letter, end=" ")

print("\nUppercase:")
for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    print(letter, end=" ")'''

'''s=input("\nenter:")
rev =''
for i in s:
    rev=i+rev
    print(rev)'''

'''for i in range(1,6):    
    for j in range(1,6):
        if i<=j:
          print(1,end= "")
    else:
        print(" @ ",end="")
    print()'''
'''a='happy birthday'
print(a[-4:-7:-1])'''

#args with return values 
'''def convert (s,out):
    for i in s:
        if 'a' <= i <='z':
            out +=chr(ord(i)-32)
        else:
            out+=i
    return out
print(convert(input("enter the string:"),""))'''

# no arguments with return values 
'''def convert ():
    s=input("enter the string:")
    out=" "
    for i in s:
        if 'a' <= i <='z':
            out +=chr(ord(i)-32)
        else:
            out+=i
    return(out)
print(convert())'''

# arguments and with no return values
'''def convert(s):
    out = ""
    for i in s:
        if 'a' <= i <= 'z':
            out += chr(ord(i) - 32)
        else:
            out += i
    print(out)

s = input("Enter the string: ")
convert(s)

# no args no return values
def convert():
    s = input("Enter the string: ")
    out = ""
    for i in s:
        if 'a' <= i <= 'z':
            out += chr(ord(i) - 32)
        else:
            out += i
    print(out)

convert()'''

'''class col1ege:
    name=Gopalan
    location=Hoodi
S1=college'''

'''class college:
     cname="gcem"
     clocation="hoodi"

s1=college()
s1.name="harish"
s1.phone="5243534699"

s2=college()
s2.name="lucky"
s2.phone="2359353637"

print(s1.clocation)
s1.clocation="kr puram"
print("after changing" )
print(s1.clocation)

print(s2.clocation)
print(college.clocation)'''

class college :
     def __init__(self,name,phone,usn):
          self.name=name 
          self.phone=phone
          self.usn=usn

     def display(self):
          print(self.name,self.phone,self.usn)


     def change_name(self,new):
          self.name=new 

s1= college("harish","839748364","635437")
s2= college("girish","83974657","9565437")


s1.change_name("hareesh")
s1.display()
s2.display()
