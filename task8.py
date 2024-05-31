class Sheet:
    def __init__(self, discipline_list, discipline, group):
        self.discipline_list = discipline_list
        self.discipline = discipline if discipline in discipline_list else None
        self.group = group
        self.students = {}

    def put(self, name, grade):
        self.students[name] = grade

    def get(self, name):
        return self.students.get(name, "Student not found")

    def change(self, name, new_grade):
        if name in self.students:
            self.students[name] = new_grade

    def delete(self, name):
        if name in self.students:
            del self.students[name]

    def result(self):
        grades = list(self.students.values())
        return grades.count("отлично"), grades.count("хорошо"), grades.count("удов"), grades.count("неуд")

    def __str__(self):
        return f"Discipline: {self.discipline}, Group: {self.group}, Students: {self.students}"

    def count(self):
        return len(self.students)

    def names(self):
        return list(self.students.keys())


# Создаем список дисциплин
discipline_list = ["Математика", "Физика", "Химия"]

# Создаем объект класса Sheet
sheet = Sheet(discipline_list, "Математика", "10-А")

# Добавляем оценки студентов
sheet.put("Иванов", "отлично")
sheet.put("Петров", "хорошо")
sheet.put("Сидоров", "удов")

# Получаем оценку студента
print(sheet.get("Иванов"))

# Изменяем оценку студента
sheet.change("Петров", "отлично")
print(sheet.get("Петров"))

# Удаляем студента из ведомости
sheet.delete("Сидоров")

# Получаем результаты экзамена
print(sheet.result())

# Выводим ведомость
print(sheet)

# Получаем количество студентов в ведомости
print(sheet.count())

# Получаем список фамилий студентов
print(sheet.names())
