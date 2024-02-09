# programa para calcular el area y el perimetro de un circulo de radio R

import math

# input
R = input ("Ingrese el valor del radio del circulo:")
R = int(R)

# procesing
A = math.pi*R*R
P = 2*math.pi * R

# output
print("_ _ _ _ _  _ _ _ _ _ _ _ _ _ _ _ _ _ _")
print("El area del circulo es: " + str(A))
print(" El perimetro del circulo es: " + str(P))
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")
