import math

a = int(input("length of first side"))
b = int(input("length of second side"))
c = int(input("length of third side"))

#s=sum of all sides(perimeter of triangle)

s=(a+b+c)/2

print("perimeter of triangle/2:",s)
area = math.sqrt(s*(s-a)*(s-b)*(s-c))
print("area is:",area)
