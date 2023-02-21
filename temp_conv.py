# Temperature converter for Celsius and Fahrenheit

# Stat menu
menu = "-----------------------------------------------\n"
menu += "c - converts Celsius to Fahrenheit\n"
menu += "f - converts Fahrenheits into Celsius\n"
menu += "q - to quit the convertor\n"
menu += "-----------------------------------------------\n"
print(menu)

# User input and validation
while True:

    choice = input("Which convertor do you whish to use? ").lower()

    if choice == "q":
        print("\n\tBye\n")
        break
# Calculation and a print out of Fahrenheit
    if choice == "c":
        cel = float(input("Enter temperature in Celsius: "))
        fah = (cel * (9 / 5)) + 32
        fah_r = round(fah,2)
        print(f"Your {cel} Celsius is equal to {fah_r} Fahrenheit.")
# Calculation and a print out of Celsius
    if choice == "f":
        fah = float(input("Enter temperature in Fahrenheit: "))
        cel = (fah - 32) * (5 / 9)
        cel_r = round(cel,2)
        print(f"Your {fah} Fahrenheit is equal to {cel_r} Celsius.")
    else:
        print("\nYou have not entered an appropriate choice.\n")
