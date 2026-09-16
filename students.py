"""Öğrenci kayıtlarının tutulduğu modül."""

students = []


def add_student(name, number):
    """Listeye yeni bir öğrenci ekler."""
    students.append({"name": name, "number": number})


def find_student(number):
    """Numaraya göre öğrenciyi bulur, yoksa None döner."""
    for student in students:
        if student["number"] == number:
            return student
    return None


def list_students():
    """Kayıtlı tüm öğrencileri döner."""
    return list(students)
