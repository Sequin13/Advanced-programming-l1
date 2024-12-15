import requests
import argparse


class Brewery:
    def __init__(self, brewery_id, name, brewery_type, address_1, address_2, address_3, city, state_province,
                 postal_code, country, longitude, latitude, phone, website_url, state, street):
        self.brewery_id = brewery_id
        self.name = name
        self.brewery_type = brewery_type
        self.address_1 = address_1
        self.address_2 = address_2
        self.address_3 = address_3
        self.city = city
        self.state_province = state_province
        self.postal_code = postal_code
        self.country = country
        self.longitude = longitude
        self.latitude = latitude
        self.phone = phone
        self.website_url = website_url
        self.state = state
        self.street = street

    def __str__(self):
        dividing_line = ''.join(f'_' for _ in range(1, 60))

        return (
            f'\n\nBrewery id: {self.brewery_id}\nName: {self.name} \nBrewery type: {self.brewery_type} \nAddress: {self.address_1}\nAdditional addresses: {self.address_2} {self.address_3}'
            f'\nCity: {self.city} \nState province: {self.state_province}\nPostal code: {self.postal_code}\nCountry: {self.country} \nLongitude: {self.longitude} \nLatitude: {self.latitude} '
            f'\nPhone number: {self.phone} \nWebsite: {self.website_url} \nState: {self.state} \nStreet: {self.street} \n{dividing_line}')


def main(city):
    url = 'https://api.openbrewerydb.org/v1/breweries'
    r = requests.get(url)
    data = r.json()

    for el in data:
        if city == el['city'] or city is None:
            brewery = Brewery(el['id'], el['name'], el['brewery_type'], el['address_1'], el['address_2'], el['address_3'],
                              el['city'], el['state_province'], el['postal_code'], el['country'], el['longitude'],
                              el['latitude'], el['phone'], el['website_url'], el['state'], el['street'])
            print(brewery)


if __name__ == "__main__":
    city = None
    parser = argparse.ArgumentParser()
    parser.add_argument("--city")
    args = parser.parse_args()

    if args.city:
        city = args.city
    main(city)
