a = float(input("length of first side : "))
b = float(input("length of second side : "))
c = float(input("length of third side : "))
s= (a+b+c)/2
area = s*(s-a)*(s-b)*(s-c)**0.5
print("The area of the triangle is ",round(area, 2))