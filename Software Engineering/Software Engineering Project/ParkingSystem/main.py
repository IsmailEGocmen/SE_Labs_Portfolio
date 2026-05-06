from ParkingSystem import ParkingSystem

def main():
    system = ParkingSystem()

    while True:
        print("\n1. View Spots")
        print("2. Reserve Spot")
        print("3. Pay")
        print("4. Cancel Reservation")
        print("5. Exit")

        choice = input("Choose: ")

        if choice == "1":
            system.show_available_spots()

        elif choice == "2":
            user = input("Enter your name: ")
            spot = int(input("Enter spot number: "))
            system.reserve_spot(user, spot)

        elif choice == "3":
            user = input("Enter your name: ")
            system.make_payment(user)

        elif choice == "4":
            user = input("Enter your name: ")
            system.cancel_reservation(user)

        elif choice == "5":
            break

        else:
            print("Invalid option")


if __name__ == "__main__":
    main()