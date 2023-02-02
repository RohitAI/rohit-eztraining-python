import random
l=list(map(str, input(). split()))
l1=[(random.randint(100,500)/500)*100  for i in range(len(l)) ]
dict={a:b for (a,b) in zip(l,l1)}          
print(dict)
