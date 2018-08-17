def numeroprimo(n): 
    if n<2:
       flag=False
    elif n==2:
       flag=True
    else: 
         flag=True
         for numerador in range (2,n-1):
          if n%numerador==0:
           flag= False
           break
    return flag
 
i=input("Dame un numero")
if numeroprimo(i):
   print( "primo")
else: 
   print ("no es primo") 
   
   
 
