[a,b,c] = list(map(float, input().split()))

triangulo = (a*c)/2
circulo = c * c * 3.14159
trapezio = (a + b)/2 * c
quadrado = b * b
retangulo = a * b

print("TRIANGULO: %0.3f"%triangulo)
print("CIRCULO: %0.3f"%circulo)
print("TRAPEZIO: %0.3f"%trapezio)
print("QUADRADO: %0.3f"%quadrado)
print("RETANGULO: %0.3f"%retangulo)