from property import Property
from house import House
from flat import Flat

def main():
    house1 = House(225, 7, 1000000, "Sosnowiec, ul. Kwiatowa 53", 150)
    flat1 = Flat(100, 4, 700000, "Katowice, ul. Sosnowiecka 102/4", 4)

    print(house1)
    print(flat1)


if __name__ == "__main__":
    main()
