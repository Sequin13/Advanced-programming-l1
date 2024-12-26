class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return (f"Biblioteka na ulicy {self.street} w mieście {self.city} otwarta w godzinach {self.open_hours}. Nr. "
                f"telefonu: {self.phone}")