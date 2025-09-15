import math

def area_of_circle(pi,radius):
    area_circle = pi * (radius**2)
    return area_circle

def total_money_due(money,tax_rate):
    total_due = money + (money*tax_rate)
    return total_due

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit-32) * 5/9
    return celsius

radius = float(input("Enter the radius of the circle: "))
print(f"Area of circle: {area_of_circle(math.pi,radius):.2f}")

money = float(input("Enter the amount of money: "))
tax_rate = float(input("Enter the tax rate: ")) / 100
print(f"Total money due: {total_money_due(money,tax_rate):.2f}")

fahrenheit = float(input("Enter temperature in fahrenheit: "))
print(f"Celsius: {fahrenheit_to_celsius(fahrenheit):.4f}")


