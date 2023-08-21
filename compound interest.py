p=float(input("INPUT PRINCIPAL: "))
t=float(input("INPUT TIME: "))
r=float(input("INPUT RATE OF INTEREST: "))
a=p*(1+r/100)**t
c=a-p
print("SIMPLE INTEREST :",c)
