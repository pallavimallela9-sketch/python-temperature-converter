temperature = float(input("Enter temperature: "))

print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = int(input("Enter your choice: "))

if choice == 1:
    fahrenheit = (temperature * 9 / 5) + 32
    print("Temperature in Fahrenheit:", fahrenheit)

elif choice == 2:
    celsius = (temperature - 32) * 5 / 9
    print("Temperature in Celsius:", celsius)

else:
    print("Invalid choice")
