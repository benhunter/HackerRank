import math

AB = int(input())
BC = int(input())

atan = math.atan(BC/AB)  # Adjecent over opposite
# print(atan)

a = 90 - math.degrees(atan)
print(str(round(a)) + '°')
