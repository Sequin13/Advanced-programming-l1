from property import Property


class Flat(Property):
    def __init__(self, area, rooms: int, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return (f"Mieszkanie o powierzchni {self.area} ma {self.rooms} pokoi, kosztuje {self.price}, znajduje się na "
                f"{self.floor} piętrze. Adres: {self.address}")
