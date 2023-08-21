#string

print("STRING")
s="abcdefghijklmnopqrstuvwxyz"        #string
for x in s:
    print("alphabets - ",x)
print(s[1])                            #access variable


#list

print("LIST")
l=['a','b',12,13,23+4j]                #list
l.append("hi")                         #add new element
for x in l:
    print(x)
l[2]=90                                 #change element
for x in l:
    print(x)
    

#tupple

print("TUPPLE")
tpl=(1,2,3,'hi','bye',23+4j)            #tupple
for i in tpl:                           
    print(i)


#dictionary

print("\t DICTIONARY\n")                    #dictionary
d={1701:'vishal',1702:'sarbjot',1703:'deepak'} 
print(d)
for x in d.keys():                           #to print keys
    print(" keys ",x)
for x in d.values():                         #to print values
    print("values  ",x)