import re
import random
l=["taehyung","suga","jin","namjoon","jimin","hope","kookie"]
input_string = random.choice(l)
new_string=""
for i in range(0,12):
  char=input("enter the character to find ").lower()
  replaced_string = re.sub('[^' + char + ']', '_', input_string)
  l=(list(replaced_string))
  if i!=0:
   if len(new_string)!=0:
    for j in range(0,len(l)):
        new_string=list(new_string)
        if l[j]=='_':
           if new_string[j]!='_':
              l.insert(j,new_string[j])
              l.pop(j+1)
   f=" "              
   print(f.join(l))            
   new_string=l
   x="_" in l
   if(x==False):
     print(f"you won your {input_string} oppa!! :)")
     break
  else:
     d=" "
     print(d.join(l)) 
     new_string=l
for i in l:
  if i=="_":
    print("you lost because the computer did not select you bias :( but never give up") 
    break    
     
         
