#!/usr/bin/python3
""" Test file for ACME """

from models import storage
from models.institution import Institution
from models.subject import Subject
from models.teacher import Teacher
from models.student import Student
from models.lesson import Lesson
from models.clas import Clas
from models.state import State
from models.city import City
list_objects = []


# Creating states.
RSK = State(name='RSK')
RSK.save()
# try:
    # RSK = State(name='RSK')
    # RSK.save()
# except Exception as e:
    # storage.rollback()
    # RSK = State(name='RSK')
    # RSK.save()
    # print(e)

SAFI = State(name='SAFI')
SAFI.save()
T_T = State(name='TANGER-TETOUAN')
T_T.save()

# Creating cities.
SALE = City(name='SALE', state_id=RSK.id)
SALE.save()
S_K = City(name='SIDI KACEM', state_id=RSK.id)
S_K.save()
TANGER = City(name='TANGER', state_id=T_T.id)
TANGER.save()
JADIDA = City(name='JADIDA', state_id=SAFI.id)
JADIDA.save()

list_objects.extend([RSK, SAFI, T_T, SALE, S_K, TANGER, JADIDA])


# Creating institutions.
inst_1 = Institution(name='LYCEE ALMANDAR ALJAMIL', city=SALE.name, state=RSK.name)
inst_1.save()
inst_11 = Institution(name='LYCEE ALMANDAR ALJAMIL',
                      city=S_K.name, state=RSK.name)
inst_11.save()
inst_2 = Institution(name='LYCEE JABIR IBN HAYANE', city=SALE.name, state=RSK.name)
inst_2.save()
inst_22 = Institution(name='LYCEE JABIR IBN HAYANE',
                      city=TANGER.name, state=T_T.name)
inst_22.save()
inst_3 = Institution(name='LYCEE QUADI AYAD', city=SALE.name, state=RSK.name)
inst_3.save()
inst_33 = Institution(name='LYCEE QUADI AYAD', city=JADIDA.name, state=SAFI.name)
inst_33.save()
inst_4 = Institution(name='LYCEE ALMOTANABI', city=SALE.name, state=RSK.name)
inst_4.save()

# set many to many relationship between cities and institutions.
# important note:
# for many to many, the assignement of the relationship must be done
# +manually as bellow, but it needs to be done only by one side.
SALE.institutions.extend([inst_1, inst_2, inst_3, inst_4])
JADIDA.institutions.extend([inst_33])
S_K.institutions.extend([inst_11])
TANGER.institutions.extend([inst_22])

# print('inst_1', inst_1)
# print('inst_1.cities', inst_1.cities)
# print('SALE\n', SALE.institutions)
# print('JADIDA\n', JADIDA.institutions)
# print('S_K\n', S_K.institutions)
# print('TANGER\n', TANGER.institutions)


# inst_1.cities.append(SALE)
# print('RSK\n', RSK.cities)
# print('SAFI\n', SAFI.cities)
# print('T_T\n', T_T.cities)

institution_list = [inst_1, inst_2, inst_3, inst_4, inst_11, inst_22, inst_33]
list_objects.extend(institution_list)


# Creating subjects.
PC = Subject(name='PC')
PC.save()

MATH = Subject(name='MATH')
MATH.save()

EN = Subject(name='EN')
EN.save()

FR = Subject(name='FR')
FR.save()

AR = Subject(name='AR')
AR.save()

subject_list = [PC, MATH, EN, FR, AR]
list_objects.extend(subject_list)

# Creating classes.
cc = Clas(name='CC')
cc.save()

bac1 = Clas(name='1BAC')
bac1.save()

bac2 = Clas(name='2BAC')
bac2.save()


class_list = [cc, bac1, bac2]
list_objects.extend(class_list)

# Creating teachers.
teacher_1 = Teacher(name='Redouane')
teacher_1.save()

teacher_2 = Teacher(name='DRIHMIA')
teacher_2.save()

teacher_3 = Teacher(name='OMER')
teacher_3.save()

teacher_4 = Teacher(name='Mohamed')
teacher_4.save()


teacher_list = [teacher_1, teacher_2, teacher_3, teacher_4]
list_objects.extend(teacher_list)


# Creating students.
Marwan = Student(name='Marwan', institution_id=inst_1.id, class_id=cc.id)
Marwan.save()
Hamid = Student(name='Hamid', institution_id=inst_1.id, class_id=cc.id)
Hamid.save()
Samir = Student(name='Samir', institution_id=inst_1.id, class_id=bac1.id)
Samir.save()
Fatima = Student(name='Fatima', institution_id=inst_1.id, class_id=bac1.id)   # incomplete
Fatima.save()

# Creating lessons.
# Commun Core
d1 = 'https://drive.google.com/file/d/1rnI4FRlHJxFqvNE_7M1o7jDDgfzJ782U/view'
cc_less_1 = Lesson(name='Periodic Classification of Chemical Elements',
                   download_link=d1,
                   description='lesson N6 for my student related to Chemistry',
                   institution_id=inst_1.id,
                   subject_id=PC.id,
                   teacher_id=teacher_1.id)
cc_less_1.save()


idd = '1n76fUTHscw7D-yjaAVaXFH8MY7bEDrkE/'
d2 = f'https://drive.google.com/file/d/{idd}view?usp=sharing'
cc_less_2 = Lesson(name='Direct electric current',
                   download_link=d2,
                   description='lesson N6 for my student related to Physics',
                   institution_id=inst_1.id,
                   subject_id=PC.id,
                   teacher_id=teacher_1.id)
cc_less_2.save()

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
f_less_1.save()

idd = '14vaHIxaq3OdcLlphJkHV0mmnIriUUW8C'
d2 = f'https://drive.google.com/file/d/{idd}/view?usp=sharing'
f_less_2 = Lesson(name='Laplace\'s Force - out of the curriculum',
                  download_link=d2,
                  description='lesson 12 for my 1st bac student',
                  institution_id=inst_2.id,
                  subject_id=PC.id,
                  teacher_id=teacher_1.id)
f_less_2.save()

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
# print(class_list[-1])
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
    obj.save()

# //////////////////////////////////////////////////

for obj in storage.all().values():
    if 'Institution' in str(type(obj)):
        for inst in obj.cities:
            print(inst.name)
            print("-----------------")

print('statistics:')
stats = {
    'states': storage.count(State),
    'cities': storage.count(City),
    'institutions': storage.count(Institution),
    'subjects': storage.count(Subject),
    'classes': storage.count(Clas),
    'teachers': storage.count(Teacher),
    'lessons': storage.count(Lesson)
}
print(stats)
