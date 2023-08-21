a=[1,2,3,4,5,6,7]
a.append(8)     #append
print(a)

b=a.copy()     #copy
print(b)

b.clear()    #clear
print(b)
 
c=[1,1,1,23,5,6,7,1,1,3]    #count
print(c.count(1))

c.extend(a)     #extend
print(c)

print(c.index(23))   #index

print(c.pop())   #pop
print(c)

c.reverse()     #reverse
print(c)

print(c.sort())   #sort
print(c)

