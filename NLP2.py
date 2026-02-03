import re
p=[("[0-9]","The student strenght is 31 but the perfection percentage is 100"),("[A-Z][a-z]+","Athi and meenashki handle the nlp."),("[aeiou]+","Natural language processing essentials."),("[a-z]+@[a-z]+\.com","Gmail id is person@gmail.com")]
for pa,t in p:
   print(pa)
   print(t)
   matches = re.findall(pa,t)
   if matches:
       print("matches")
   else:
       print("not found")
