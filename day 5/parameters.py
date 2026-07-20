# parameters
a,b,c="ali","hassen","alaa"

def sayHello(name):
   
   print(f"Hello {name}")

sayHello(a)

  
# more task  

def additon(n1,n2):
   if not isinstance(n1, int) or not isinstance(n2, int):
      print('please enter number')
   else:
     return (n1)+(n2)
   
print(additon(1,2))


# more task

def full_name(frist,middle,last):

  return f"Hello {frist.strip().capitalize()} {middle[0].upper()} {last.capitalize()}"


print(full_name('ahmed','ramadan','rawy'))
  