# Temperature Converter

print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = input("Choose conversion (1 or 2): ")

if choice == "1":
    celsius = float(input("Temperature in Celsius: "))
    fahrenheit = celsius * 9 / 5 + 32
    print(f"Fahrenheit: {fahrenheit:.2f}")

elif choice == "2":
    fahrenheit = float(input("Temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5 / 9
    print(f"Celsius: {celsius:.2f}")

else:
    print("Invalid choice. Please enter 1 or 2.")
