import math
n = int(input())

fibonacci = ((((1+(math.sqrt(5)))/2)**n) - (((1-(math.sqrt(5)))/2)**n))  /(math.sqrt(5))

print(f"{fibonacci:.1f}")