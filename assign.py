# Celsius to Fahrenheit Temperature Converter

celsius = float(input("Enter temperature in Celsius: "))

# Convert Celsius to Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# Classify the temperature
if celsius < 15:
    level = "Cold"
elif celsius <= 30:
    level = "Normal"
else:
    level = "Hot"

# Display the results
print("Fahrenheit temperature:", round(fahrenheit, 2))
print("Temperature level:", level)
# ASCII String Encryption

text = input("Enter a string: ")

for i in range(len(text)):
    ascii_value = ord(text[i])

    if i % 2 == 0:
        modified_value = ascii_value + 2
    else:
        modified_value = ascii_value - 2

    modified_character = chr(modified_value)

    print("Modified ASCII value:", modified_value)
    print("Modified character:", modified_character)
    # Number Format Converter

num = int(input("Enter a positive integer with at least 3 digits: "))

# Validate the input
if num <= 0:
    print("Please enter a positive number.")
elif num < 100:
    print("Please enter a number with at least 3 digits.")
else:
    # Display the number in different formats
    print("Decimal:", num)
    print("Binary:", bin(num))
    print("Octal:", oct(num))
    print("Hexadecimal:", hex(num))

    # Display the last digit
    last_digit = num % 10
    print("Last digit:", last_digit)

    # Check whether the number is even or odd
    if num % 2 == 0:
        print("Number is Even")
    else:
        print("Number is Odd")