# -*- coding: utf-8 -*-
"""
This program is to convert the inputted temperature to other units and display them

Created on Tue Aug  6 15:15:20 2024

@author: ajayk
"""

def Celsius_to_Kelvin(temperature): #this converts Celsius to Kelvin
    result = temperature+273.15
    return result;
def Kelvin_to_Celcius(temperature): #this converts Kelvin to Celcius
    result = temperature-273.15
    return result
def Celcius_to_Fahrenheit(temperature): #this converts Celcius to Fahrenheit
    result = temperature*9/5+32
    return result
def Fahrenheit_to_Celcius(tempurature): #this converts Fahrenheit to Celcius 
    result = (tempurature-32)*5/9
    return result
def Kelvin_to_Fahrenheit(tempurature): #this converts Kelvin to Fahrenheit
    result = Celcius_to_Fahrenheit(Kelvin_to_Celcius(tempurature))
    return result
def Fahrenheit_to_Kelvin(tempurature): #this converts Fahrenheit to Kelvin
    result = Celsius_to_Kelvin(Fahrenheit_to_Celcius(tempurature))
    return result

temperature = float(input(" Enter the value for Temperature : "))
unit = input(" Enter the unit of the temperature (C for Celsius, F for Fahrenheit, K for Kelvin): ").strip().upper()

if unit == 'C':
    fahrenheit = Celcius_to_Fahrenheit(temperature)
    kelvin = Celsius_to_Kelvin(temperature)
    print(f"\n {temperature}°C in other Temperature units \n\n Fahrenheit : {fahrenheit:.2f}°F \n Kelvin : {kelvin:.2f}K. ")
elif unit == 'F':
    celsius = Fahrenheit_to_Celcius(temperature)
    kelvin = Fahrenheit_to_Kelvin(temperature)
    print(f"\n {temperature}°F in other Temperature units \n\n Celcius : {celsius:.2f}°C \n Kelvin : {kelvin:.2f}K. ")
elif unit == 'K':
    celsius = Kelvin_to_Celcius(temperature)
    fahrenheit = Kelvin_to_Fahrenheit(temperature)
    print(f"\n {temperature}K in other Temperature units \n\n Celcius : {celsius:.2f}°C \n Fahrenheit : {fahrenheit:.2f}°F. ")
else:
    print("\n Invalid unit. Please enter C for Celsius, F for Fahrenheit, or K for Kelvin. ")