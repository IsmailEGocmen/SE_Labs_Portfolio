class ParkingSystem:
    def __init__(self):
        self.spots = {
            1: "available",
            2: "available",
            3: "available"
        }
        self.reservations = {}

    def show_available_spots(self):
        print("\nAvailable Spots:")
        for spot, status in self.spots.items():
            if status == "available":
                print(f"Spot {spot}")

    def reserve_spot(self, user, spot_id):
        if self.spots.get(spot_id) == "available":
            self.spots[spot_id] = "reserved"
            self.reservations[user] = spot_id
            print(f"Spot {spot_id} reserved for {user}")
        else:
            print("Spot not available")

    def make_payment(self, user):
        if user in self.reservations:
            print("Payment successful")
            print("Reservation confirmed")
        else:
            print("No reservation found")

    def cancel_reservation(self, user):
        if user in self.reservations:
            spot_id = self.reservations[user]
            self.spots[spot_id] = "available"
            del self.reservations[user]
            print("Reservation cancelled")
        else:
            print("No reservation to cancel")