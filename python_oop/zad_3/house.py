from property import Property


class House(Property):
    def __init__(self, area, rooms: int, price, address, plot: int):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return (f"Dom o powierzchni {self.area} posiada działkę o powiierzchni: {self.plot}, "
                f"a także ma {self.rooms} pokoi, kosztuje {self.price}. Adres: {self.address}")
