import math
from math import sin, cos, exp, sqrt, pi, log

N=0
x=[]
Fncfile = 'Templates/2_test_sin.txt'
print(Fncfile)
with open(Fncfile) as f:
    f_x = f.readline()
    print(f_x)

x.append(pi)
y=eval(f_x)
print(y)

