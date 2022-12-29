'''
Write a program that asks for the radio and calculates the area of a circle.
Knowing that area = pi*r^2
'''

radio = float(input("Give me the radio of the circle: "))
pi = 3.14

area = round(pi * pow(radio,2),2)

print(f"The area of the circle is: {area}")