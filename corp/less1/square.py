
#ax*2+bx+c = 0


import sys

a = int(sys.argv[1]) 
b = int(sys.argv[2])
c = int(sys.argv[3])

##
#Find "D"
D = b**2 - 4*a*c
print(f"D is {D}")

if D > 0:
    x1 = (-b - (D ** 0.5)) / 2 * a
    x2 = (-b + (D ** 0.5)) / 2 * a
    #print(x1,x2)
elif D == 0:
    x1 = x2 = -b*2*a

else:
    x1=x2=None

print(f"X1 = {x1}, X2 = {x2}")