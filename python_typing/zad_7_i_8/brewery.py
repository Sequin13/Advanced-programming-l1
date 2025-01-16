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
