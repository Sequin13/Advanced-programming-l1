import argparse
import requests

from brewery import Brewery


def main(city):
    url = 'https://api.openbrewerydb.org/v1/breweries'
    r = requests.get(url)
    data = r.json()
    for el in data:
        if city == el['city'] or city is None:
            brewery = Brewery(el['id'], el['name'], el['brewery_type'], el['address_1'], el['address_2'],
                              el['address_3'],
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
