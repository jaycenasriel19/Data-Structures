import numpy as np
L=12 #length of beam in meters
w=10 #load intensity in kN/m
#a
#bending moment(M),shear force(V)when x=0
x=0
M=(w*(-6*x**2 + 6*L*x-L**2))/12
V=w*(L/2 - x)
m='The bending moment at x=o is'
n='The shear force at x=0 is'
print()
print('(a.1)' + m + str(M) + ' and ', n + str(V))

#bending moment(M),shear force(V),when x=L=12
x=L
M=(w*(-6*x**2 + 6*L*x-L**2))/12
V=w*(L/2-x)
a='bending moment at x=L is'
b='shear force at x=L is'
print()
print('(a.2)' + m + str(M) +' and ', n + str(V))


#b
#bending moment(M)=0 at the midspan of the beam
""" 
When bending moment is zero, we get an expression x**2 - Lx + L**2/6 = 0
"""
a=1
b=-L
c=L**2/6
discriminant = b**2 - 4*a*c
root_b1 = (-b + np.sqrt(discriminant))/2*a
root_b2 = (-b - np.sqrt(discriminant))/2*a
print()

#c
""" 
When the shear force is zero, x = L/2
"""
x = L/2
print()

#d
x=np.array(12,10)
M=(w*(-6*x**2 + 6*L*x-L**2))/12

#e
V = w*(L/2 - x)
print()

#f
"""
Let the absolute value of the bending moment array be AM
Also let the minimum AM be m_AM
"""
AM = abs(M)
m_AM = min(AM)
""" 
When the bending moment is m_AM, we get an expression x**2 - Lx + (L**2/6)+(2*m_AM)/w = 0
"""
#from the above expression 
a = 1
b = -L
c = (L**2/6)+(2*m_AM)/w
#Using the Almighty formula the two roots are;
discriminant = b**2 - 4*a*c
root_1f = (-b + np.sqrt(discriminant))/2*a
root_2f = (-b - np.sqrt(discriminant))/2*a
print()

#g
"""
Let the relative errors be r_e
"""
r_e1 = ((root_b1 - root_1f)/root_1b*100) 
r_e2 = ((root_2f - root_b2)/root_2f*100)

"""
Let the maximum bending moment be max_M and the minimum bending moment be min_M
"""
#for the maximum
max_M = max(M)
""" 
When the bending moment is max_M, we get an expression x**2 - Lx + (L**2/6)+(2*max_M)/w = 0
"""
a = 1
b = -L
c = (L**2/6)+(2*max_M)/w
#two roots:
discriminant = b**2 - 4*a*c
root_1 = (-b + np.sqrt(discriminant))/2*a
root_2 = (-b - np.sqrt(discriminant))/2*a
print()

#for the minimum
min_M = min(M)
""" 
When the bending moment is min_M, we get an expression x**2 - Lx + (L**2//6)+(2*min_M)/w = 0
"""
a = 1
b = -L
c = (L**2//6)+(2*min_M)/w

discriminant = b**2 - 4*a*c
root_1 = (-b - np.sqrt(discriminant))/2*a
root_2 = (-b + np.sqrt(discriminant))/2*a
print()

#github username:jaycenasriel19
 
