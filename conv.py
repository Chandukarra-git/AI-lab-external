def celsius_to_fahrenheit(celsius_temperature):
    fahrenheit_temperature = (celsius_temperature * 9/5) + 32
    return fahrenheit_temperature
def is_below_freezing(celsius_temperature):
    return celsius_temperature < 0
celsius_temperature = float(input("Enter temperature in Celsius: "))
fahrenheit_temperature = celsius_to_fahrenheit(celsius_temperature)
print(f"{celsius_temperature}°C is equal to {fahrenheit_temperature}°F")
if is_below_freezing(celsius_temperature):
    print("The temperature is below freezing.")
else:
    print("The temperature is not below freezing.")
