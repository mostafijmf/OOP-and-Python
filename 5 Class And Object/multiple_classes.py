class Student:
    def __init__(self, name, class_name, id):
        self.name = name
        self.class_name = class_name
        self.id = id

    def __repr__(self) -> str:
        return f'Student: {self.name}, Class: {self.class_name}, Id: {self.id}'

class Instructor:
    def __init__(self, name, subject, id):
        self.name = name
        self.subject = subject
        self.id = id

    def __repr__(self) -> str:
        return f'Instructor: {self.name}, Subject: {self.subject}, Id: {self.id}'
    
class Academy:
    def __init__(self, name):
        self.name = name
        self.instructors = []
        self.students = []

    def add_instructor(self, name, subject):
        id = len(self.instructors) + 1
        instructor = Instructor(name, subject, id)
        self.instructors.append(instructor)

    def enroll(self, name, fee):
        if fee < 6500:
            return 'Not enough fee'
        else:
            id = len(self.students) + 1
            student = Student(name, '4', id)
            self.students.append(student)
            return f'{name} is enrolled with id: {id}, extra money {fee - 6500}'
        
    def __repr__(self):
        print('Welcome to', self.name)

        print('-------- Our Instructors --------')
        for instr in self.instructors:
            print(instr)

        print('-------- Our Students --------')
        for student in self.students:
            print(student)
        return 'All done'
        


    
# student_data = Student('Mostafij', 'Batch-4', 1002)
# print(student_data)
# instr_data = Instructor('Jhankar', 'Python', 102)
# print(instr_data)

phitron = Academy('Phitron')
phitron.enroll('Mostafij', 7000)
phitron.enroll('Ismail', 8000)
phitron.enroll('Sabbir', 7500)

phitron.add_instructor('Jahnkar', 'Python')
phitron.add_instructor('Rahat', 'DSA')
phitron.add_instructor('Rahat2', 'C++')

print(phitron)