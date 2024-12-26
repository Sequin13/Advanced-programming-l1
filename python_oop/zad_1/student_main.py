from student import Student


def main():
    student_1 = Student("Marek", [50, 100, 75, 88, 33, 99])
    student_2 = Student("Kamil", [1, 5, 50, 100, 2, 5])

    print(student_1.is_passed(), student_2.is_passed())


if __name__ == "__main__":
    main()
