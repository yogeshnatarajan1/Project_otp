import random
def otp(want):
    lists='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    tt=list(lists)
    ab=random.randrange(0,26)
    bb=random.randrange(0,26)
    num=random.randint(121454,989898)
    password=(f'{num}{tt[ab]}{tt[bb]}')
    print(password)
    return password
    
want=int(input('enter mob.no for otp : '))
ot=input("enter otp for otp : ").lower()
if (want.is_integer and ot=='otp'):
     rr=otp(want)
otpp=input('enter otp : ')
number=int(input("mobile number : "))
  
if rr==otpp and want == number:
    print('sucessful')
else:
    print('invalid')
    
    


