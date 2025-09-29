def main():
    print("📏 Unit Converter")
    print("1. Kilometers → Miles")
    print("2. Miles → Kilometers")
    print("3. Celsius → Fahrenheit")
    print("4. Fahrenheit → Celsius")

    choice = input("choose an option(1-4): ")

    if choice == "1":
        km=float(input("Enter Kilometers:"))
        miles = km * 0.621371
        print(f"{km} km = {miles:.2f} miles")
    elif choice == "2":
        miles = float(input("Enter miles: "))
        km = miles / 0.621371
        print(f"{miles} miles = {km:.2f} km")
    elif choice == "3":
        c = float(input("Enter Celsius: "))
        f = (c* 9/5) +32
        print(f"{c}°C = {f:.2f}°F")
    elif choice == "4":
        f = float(input("Enter Fahrenheit: "))
        c = (f-32) * 5/9        
        print(f"{c} °F = {c:.2f}°C ")
    else:
        print("❌ Invalid choice")    

if __name__ == "__main__":
    main()
    