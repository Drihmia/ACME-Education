#!/usr/bin/python3
""" Test file for ACME """

from models import storage
from models.institution import Institution
from models.subject import Subject
from models.teacher import Teacher
from models.lesson import Lesson
from models.clas import Clas
list_objects = []


# Creating institutions.
inst_1 = Institution(name='LYCEE ALMANDAR ALJAMIL', city='SALE', state='RSK')
inst_11 = Institution(name='LYCEE ALMANDAR ALJAMIL',
                      city='SIDI KACEM', state='RSK')
inst_2 = Institution(name='LYCEE JABIR IBN HAYANE', city='SALE', state='RSK')
inst_22 = Institution(name='LYCEE JABIR IBN HAYANE',
                      city='TANGER', state='TANGER-TETOUAN')
inst_3 = Institution(name='LYCEE QUADI AYAD', city='SALE', state='RSK')
inst_33 = Institution(name='LYCEE QUADI AYAD', city='JADIDA', state='SAFI')
inst_4 = Institution(name='LYCEE ALMOTANABI', city='SALE', state='RSK')

institution_list = [inst_1, inst_2, inst_3, inst_4, inst_11, inst_22, inst_33]
list_objects.extend(institution_list)


# Creating subjects.
PC = Subject(name='PC')
MATH = Subject(name='MATH')
EN = Subject(name='EN')
FR = Subject(name='FR')
AR = Subject(name='AR')

subject_list = [PC, MATH, EN, FR, AR]
list_objects.extend(subject_list)

# Creating classes.
cc = Clas(name='CC')
bac1 = Clas(name='1BAC')
bac2 = Clas(name='2BAC')

class_list = [cc, bac1, bac2]
list_objects.extend(class_list)

# Creating teachers.
teacher_1 = Teacher(name='Redouane')
teacher_2 = Teacher(name='DRIHMIA')
teacher_3 = Teacher(name='OMER')
teacher_4 = Teacher(name='Mohamed')

teacher_list = [teacher_1, teacher_2, teacher_3, teacher_4]
list_objects.extend(teacher_list)

# Creating lessons.
# Commun Core
d1 = 'https://drive.google.com/file/d/1rnI4FRlHJxFqvNE_7M1o7jDDgfzJ782U/view'
cc_less_1 = Lesson(name='Periodic Classification of Chemical Elements',
                   download_link=d1,
                   description='lesson N6 for my student related to Chemistry',
                   institution_id=inst_1.id,
                   subject_id=PC.id,
                   teacher_id=teacher_1.id)

idd = '1n76fUTHscw7D-yjaAVaXFH8MY7bEDrkE/'
d2 = f'https://drive.google.com/file/d/{idd}view?usp=sharing'
cc_less_2 = Lesson(name='Direct electric current',
                   download_link=d2,
                   description='lesson N6 for my student related to Physics',
                   institution_id=inst_1.id,
                   subject_id=PC.id,
                   teacher_id=teacher_1.id)

cc_lesson_list = [cc_less_1, cc_less_2]
list_objects.extend(cc_lesson_list)

# 1st year of the Baccalaureate
d1 = 'https://drive.google.com/file/d/14Ls7YwsYD9nFzYQ8KjlhGmi_E5wf61uM/view'
f_less_1 = Lesson(name='Magnetic Field Chapter',
                  download_link=d1,
                  description='lesson 11 for my 1st bac student',
                  institution_id=inst_1.id,
                  subject_id=PC.id,
                  teacher_id=teacher_1.id)
idd = '14vaHIxaq3OdcLlphJkHV0mmnIriUUW8C'
d2 = f'https://drive.google.com/file/d/{idd}/view?usp=sharing'
f_less_2 = Lesson(name='Laplace\'s Force - out of the curriculum',
                  download_link=d2,
                  description='lesson 12 for my 1st bac student',
                  institution_id=inst_2.id,
                  subject_id=PC.id,
                  teacher_id=teacher_1.id)


f_lesson_list = [f_less_1, f_less_2]
list_objects.extend(f_lesson_list)


# Setting many to many relationship's information:
#  \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# Institution: ------------------------------
for institution in institution_list:
    institution.subjects.extend(subject_list)
    institution.classes.extend(class_list)

inst_1.teachers.extend([teacher_1, teacher_2])
inst_2.teachers.extend([teacher_1, teacher_3])
inst_3.teachers.extend([teacher_3, teacher_2])
inst_4.teachers.extend([teacher_3, teacher_1])
inst_11.teachers.extend([teacher_1])
inst_22.teachers.extend([teacher_2])
inst_33.teachers.extend([teacher_3])

# --------------------------------------------


# Classes: ***********************************
for clss in class_list:
    if clss.name == 'CC':
        clss.lessons.extend(cc_lesson_list)
        clss.teachers.extend([teacher_1, teacher_2])
    elif clss.name == '1BAC':
        clss.lessons.extend(f_lesson_list)
        clss.teachers.extend([teacher_1, teacher_2])
    elif clss.name == '2BAC':
        clss.teachers.extend([teacher_3, teacher_4])
# **********************************************

for subject in subject_list:
    if subject.name == 'PC':
        subject.teachers.extend([teacher_1, teacher_2])
    elif subject.name == 'MATH':
        subject.teachers.extend([teacher_3, teacher_4])


# Commit al objects: ////////////////////////////////

for obj in list_objects:
    storage.new(obj)
storage.save()
# //////////////////////////////////////////////////

for obj in storage.all().values():
    if 'Institution' in str(obj):
        print('yes, in obj =>', obj, "\n*************************")
        for inst in obj.teachers:
            print(inst.name)
        print("-----------------")

print('statistics:')
stats = {
    'institutions': storage.count(Institution),
    'subjects': storage.count(Subject),
    'teachers': storage.count(Teacher),
    'lessons': storage.count(Lesson)
}
print(stats)
