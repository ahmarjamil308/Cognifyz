temp = float(input("Enter the temperature: "))
unit = input("Enter the unit (C/F): ").upper()

if unit == 'C':
    print(f"{temp}°C is {temp * 9/5 + 32}°F")
elif unit == 'F':
    print(f"{temp}°F is {(temp - 32) * 5/9}°C")
else:
    print("Invalid unit")
