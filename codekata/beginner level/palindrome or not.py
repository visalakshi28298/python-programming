n=int(raw_input())
temp=n
rev=0
while(n>0):
  dig=n%10
  rev=rev*10+dig
  n=n/10
if(temp==rev):
   print("it is palindrome")
else:
   print(it is not palindrome)

   
