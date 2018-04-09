n=int(input("enter number:"))
a=list(map(int,str(n)))
b=list(map(lambda x:x**3,a))
if(sum(b)==n):
  print("it is armstrong")
else:
  print("it is not armstrong")
