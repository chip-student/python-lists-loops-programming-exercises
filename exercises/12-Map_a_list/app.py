Celsius_values = [-2,34,56,-10]


Fah = 0
def fahrenheit_values(x):
# the magic go here:
   Fah = x * (9/5) + 32
   return Fah

result = list(map(fahrenheit_values, Celsius_values))
print(result)
