m=input("Enter maths mark : ")
c=input("Enter chem mark : ")
p=input("Enter phy mark : ")
b=input("Enter bio mark : ")
e=input("Enter english mark : ")
total=int(m)+int(c)+int(p)+int(b)+int(e)
per=total/5
print("Total marks: ",total)
print("Your percentage:",per)
if(per > 90):
   print("A+")
elif(per <= 90 and per >80 ): 
   print("A")  
elif(per <= 80 and per >70 ): 
   print("B")  
elif(per <= 70 and per >60 ): 
   print("C")    
else:
   print("FAIL")  