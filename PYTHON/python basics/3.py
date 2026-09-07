while True:
    user_input = input("Enter a positive number (or negative to exit): ")
    number = float(user_input)
    
    print(f"You entered: {number}")
    
    
    if number < 0:
        print("Loop terminated.")
        break
