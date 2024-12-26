from library import Library
from book import Book
from employee import Employee
from python_oop.zad_1.student import Student
from order import Order


def main():
    library_1 = Library("Czeladź", "1 Maja", "41-250", "9-18", "+48123456789")
    library_2 = Library("Katowice", "Kwiatowa", "40-000", "7-19", "+48987654321")

    book_1 = Book(library_1, "12.12.2012", "Kamil", "Grzanka", "250")
    book_2 = Book(library_2, "1.05.1995", "Adam", "Soćko", "123")
    book_3 = Book(library_1, "25.06.2003", "Wiktoria", "Sikora", "96")
    book_4 = Book(library_2, "08.09.2077", "Johnny", "Silverhand", "911")
    book_5 = Book(library_1, "9.9.1999", "Jan", "Kowalski", "12")

    employee_1 = Employee("Mario", "Super", "12.12.2015", "15.04.1974", "Dziwnów", "Kolorowa", "30-325",
                          "+481324354667")
    employee_2 = Employee("Luigi", "Super", "12.12.2015", "5.01.1974", "Dziwnów", "Kolorowa", "30-325", "+481324354668")
    employee_3 = Employee("Marcin", "Najman", "12.12.2015", "14.12.1970", "Warszawa", "Tulipanowa", "31-325",
                          "+48153354667")

    student_1 = Student("Karol", [12, 13, 100, 54])
    student_2 = Student("Maciej", [66, 0, 100, 42])
    student_3 = Student("Jakub", [12, 64, 13, 59])

    order_1 = Order(employee_1, student_3, [book_4, book_1], "15.12.2024")
    order_2 = Order(employee_3, student_1, [book_2, book_3, book_5], "21.12.2024")

    print(order_1)
    print(order_2)


if __name__ == "__main__":
    main()
