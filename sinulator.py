from math import factorial
pi = 3.14159265358979323846264338327950288419716
degorrad = int(input("Type 1 if you would like to take the sine of an angle in radians, type 2 if you would like to take the sine of an angle in degrees. (Default is radians)\n"))
x = float(input("Sineulator!\nInput your angle. (If in radians, don't add pi.)\n"))
if degorrad == 2:
  a = x/180
else:
  a = x
if a > 2 or a < -2:
  na = a % 2
#as sin(x) is a periodic function, the modulo by 2 will bring any input that is a real number into the radius of convergence of the Maclaurin Series
else:
  na=a
truex = pi*na
sinx = 0
for i in range(60):
  sinx += (((-1)**i)/factorial(2*i+1))*(truex**(1+2*i))
  #implementation of the partial sum of the Maclaurin series of sin(x) this uses the first 40 terms
fa=str(sinx)
print("Here is the sin of your angle!\n"+ fa)