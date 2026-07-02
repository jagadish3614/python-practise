while True:
    print("\n VILLAGE DIGITAL ASSISTANT ")
    print("1. Crop Suggestion")
    print("2. Emergency Numbers")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        season = input("Enter Season (Summer/Rainy/Winter): ")

        if season.lower() == "summer":
            print("Suggested Crops: Groundnut, Sunflower")
        elif season.lower() == "rainy":
            print("Suggested Crops: Paddy, Cotton")
        elif season.lower() == "winter":
            print("Suggested Crops: Wheat, Bengal Gram")
        else:
            print("Season not found!")

    elif choice == "2":
        print("\nEmergency Numbers")
        print("Police : 100")
        print("Ambulance : 108")
        print("Fire : 101")

    elif choice == "3":
        print("Thank you!")
        break

    else:
        print("Invalid Choice!")