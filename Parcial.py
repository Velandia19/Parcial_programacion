
import numpy as np
import math
limite_1="Ingrese el límite inferior del intervalo : "
limite_2="Ingrese el límite superior del intervalo : "
intervalos="Ingrese el numero impar de intervalos: "
respuesta_1="introduzca un numero que sea impar:"
respuesta_2= "es impar, n="
respuesta_3="La aproximacion a la integral es: "
respuesta_4="n sub-intervalos:"
respuesta_5="lista impar de x_i:"
respuesta_6="Lista par de x_i:"
respuesta="Funcion a evaluar"

f= lambda x: math.sqrt(1+x**2)

#f= lambda x: x
print(f)
a = eval(input(limite_1))
b = eval(input(limite_2))
n = eval(input(intervalos))
suma = f(a)
n_1=(n-1)
h= (b-a)/n_1
N=1
x_1=a+(n*h)
while n%2==0:
    impar=eval(input(respuesta_1))
    if (impar%2!=0):
        break
    print(impar)
    
xi = a
for i in range(0,n-2,2):
    xi = xi + h
    suma = suma + 4*f(xi)
    xi = xi + h
    suma = suma + 2*f(xi)

xi = xi + h
suma = suma + 4*f(xi)
suma = suma + f(b)
integral = (h/3)*suma

print(respuesta_4, n)
print(respuesta_3, integral)
