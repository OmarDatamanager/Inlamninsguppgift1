
def create_student_register(students: list) -> dict:
    """
    Tar emot en lista med namn och ålder och returnerar en dictionary där namnet är nyckeln och åldern är värdet.
    """
    students_register = {name: age for name, age in students}
    return students_register

students = [("Alice", 24), ("Bob", 19), ("Charlie", 22)]
print(create_student_register(students))  # Output: {'Alice': 24, 'Bob': 19, 'Charlie': 22}

