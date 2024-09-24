# Main program for Ohm's Law Calculator
def ohms_law_calculator():
    print("Ohm's Law Calculator")
    
    # Ask the user what they want to calculate
    choice = input("What would you like to calculate? (V for Voltage, I for Current, R for Resistance): ").upper()
    
    # Calculate Voltage (V = I * R)
    if choice == 'V':
        current = float(input("Enter the current (I) in amperes: "))
        resistance = float(input("Enter the resistance (R) in ohms: "))
        voltage = current * resistance
        print(f"The voltage (V) is {voltage:.2f} volts.")
    
    # Calculate Current (I = V / R)
    elif choice == 'I':
        voltage = float(input("Enter the voltage (V) in volts: "))
        resistance = float(input("Enter the resistance (R) in ohms: "))
        if resistance != 0:
            current = voltage / resistance
            print(f"The current (I) is {current:.2f} amperes.")
        else:
            print("Error: Resistance cannot be zero.")
    
    # Calculate Resistance (R = V / I)
    elif choice == 'R':
        voltage = float(input("Enter the voltage (V) in volts: "))
        current = float(input("Enter the current (I) in amperes: "))
        if current != 0:
            resistance = voltage / current
            print(f"The resistance (R) is {resistance:.2f} ohms.")
        else:
            print("Error: Current cannot be zero.")
    
    else:
        print("Invalid choice. Please enter V, I, or R.")

# Run the program
ohms_law_calculator()
