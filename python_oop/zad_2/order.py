class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        books_str = ", ".join(str(book) for book in self.books)
        return (
            f"Zamówienie z {books_str}, złożone {self.order_date} "
            f"przez {self.student}. Książkę wydał {self.employee}"
        )
