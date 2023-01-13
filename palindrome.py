### Program to print palindrome of any number
userinput=int(input())
while (userinput!=0):
    rem=userinput//10
    rem=userinput-rem*10
    userinput=userinput//10
    print(rem,end="")
