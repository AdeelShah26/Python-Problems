d=int(input("Enter the decimal No."))
a=[]
b=[10,11,12,13,14,15]
while d>=16:
    hex=d%16
    d=d//16
    # return(hex)
    a.append(hex)
# return(1411%16)
def dectohex(num):
    if num==10:
        return 'A'
    elif num==11:
        return 'B'
    elif num==12:
        return 'C'
    elif num==13:
        return'D'
    elif num==14:
        return 'E'
    elif num==15:
        return'F'
    else:
        return num
        
# b=[]
c=dectohex(d)
print(c,end="")
for i in reversed(a):
    # return(i)
    d=dectohex(i)
    print(d,end="")
# print(b)
# for i in range