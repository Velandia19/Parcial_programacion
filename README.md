# Parcial_programacion
Documentos del Parcial.py de programacion donde se realizo un programa que evaluara una integral definida de una funcion cualquiera, en este caso es la funcion raiz(1+x^2) pero con la sumatoria de sus segmentos y tramos, en conclusion por la regla de Simpson.
Primero se realizo el llamado de la libreria numpy y se le dio un nombre "np", tambien la libreria math.
Se le asignaron variables a todas las preguntas y respuestas que se le iban a dar al usuario.
Se asigno una variable a la funcion, donde se escribio con el comando de lambda y math, luego se le preguntara al usuario los limites de la integral.
Se le pide al usuario un numero n impar, que sera el numero de tramos que tendra nuestra integral.
Cuando la integral tiene intervalos, este se divide en varios segmentos y en este caso como se describio en el ejercicio cada segmento tendra dos tramos.
En este caso se esta utilizando la regla de Simpson de 1/3 donde se define que los tramos deben ser pares, pero como se le pide al usuario impares entonces mas abajo.
Se vuelve a redefinir n como n_1, el cual se convierte en par para asi realizar la respectiva sumatoria de segmentos, como se explico en la guia.
Para obenet n impares, se utilizo un ciclo while que comienza cuando n es par y se corta cuando el usuario ingresa un n impar. 
Luego se utilizo un for i in range(0, n-2,2), esto es para que crear un generador que sume las funciones, es decir, la funcion evaluada en dichos puntos.
Donde el rango es porque la sumatoria es de cada segmento pero cada dos tramos, como se explico anteriormente verificando que sean pares y que cada segmento tiene dos tramos.
Luego se realizo la suma del ultimo segmento, para asi multiplicar todo eso por (h/3), esto por definicion de la regla de simpson.
Luego se imprime el numero de n usados y el resultado de la integral evaluada en esos limites, donde se observa que entre mayor sea el valor de n, mayor sera la aproximacion.

