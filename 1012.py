VALORES = input().split(" ")

A,B,C = VALORES

A = float(A)
B = float(B)
C = float(C)

TRIANGULO = (A * C) / 2
CIRCULO = 3.14159 * (C*C)
TRAPEZIO = ((A+B)/2)*C
QUADRADO = B*B
RETANGULO = A*B

print("TRIANGULO: %0.3f\nCIRCULO: %0.3f\nTRAPEZIO: %0.3f\nQUADRADO: %0.3f\nRETANGULO: %0.3f" % (TRIANGULO, CIRCULO, TRAPEZIO, QUADRADO, RETANGULO))
