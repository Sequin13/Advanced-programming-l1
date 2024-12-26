class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self) -> bool:
        avg_marks = sum(self.marks) / len(self.marks)
        if avg_marks > 50:
            return True
        return False

    def __str__(self):
        return f"Student: {self.name}, którego oceny to: {self.marks}"
