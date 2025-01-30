##### ASSIGNMENT STARTS HERE #####


#%%
# First Assignment
'''
1: Please create a program which inputs two years and outputs the years as well as the difference
between them!

Your output should look like:

Year 1: 2025
Year 2: 2028
Difference: 3
'''

year1 = int(input("Enter first year: "))
year2 = int(input("Enter second year: " ))

difference = year2 - year1

print (f"year 1: {year1}")
print(f"Year 2: {year2}")
print(f"difference: {difference}")


#%%
# Second Assignment

'''
2: Please create a program which collects an input as fahrenheit and outputs the 
temperature in celsius

Your output should look like:

Fahrenheit: 25
Celsius: -3.89
'''

fahrenheit = float(input("Enter temperature in Fahrenheit: "))


celsisu = (fahrenheit - 32) * 5/9

print(f"Fahrenheit: {fahrenheit}")
print(f"Celsius: {celsius:.2f}")
#%%
# Third Assignment

'''

3: Please create a program which collects an input as US Dollars and converts the output to Euros 
given the exchange rate on 1/19/25 as 1 USD = 0.97 Euro

Your output should look like:
USD: 1
EU: 0.97

'''
usd = float(input("Enter amount in USD: "))

exchange_rate = 0.97
euro = usd * exchange_rate

print(f"USD: {usd}")
print(f"EU: {euro:.2f}")

##### ASSIGNMENT ENDS HERE #####
