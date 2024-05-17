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
inst_1 = storage.query(Institution).filter((Institution.name).like(
    'Lycee Qualifiant ALMANDAR ALJAMIL'),
                                           Institution.city.like(
                                               'Sal%')).first()
print('inst_1')
if not inst_1:
    exit(1)
inst_11 = storage.query(Institution).filter(Institution.name.like(
    'LYCEE OUHOUD'),
                                            Institution.city.like('SIDI KACEM')
                                            ).first()
print('inst_11')
if not inst_11:
    exit(1)
inst_2 = storage.query(Institution).filter(Institution.name.like(
    'Lycee Qualifiant JABER IBN HAYANE'),
                                           Institution.city.like('SAL%'
                                                                 )).first()
print('inst_2')
if not inst_2:
    exit(1)
inst_22 = storage.query(Institution).filter(Institution.name.like(
    'COLLEGE JABIR BNOU HAYYANE'),
                                            Institution.city.like('tanger%')
                                            ).first()
print('inst_22')
if not inst_22:
    exit(1)
inst_3 = storage.query(Institution).filter(Institution.name.like(
    'Lycee Qualifiant KADI AYAD'),
                                           Institution.city.like('salE')
                                           ).first()
print('inst_3')
if not inst_3:
    exit(1)
inst_33 = storage.query(Institution).filter(Institution.name.like
                                            ('Lycee Qualifiant EL KADI AYAD'),
                                            Institution.city.like('El Jadida')
                                            ).first()
print('inst_33')
if not inst_33:
    exit(1)
inst_4 = storage.query(Institution).filter(Institution.name.like
                                           ('Lycee Qualifiant AL MOUTANABI'),
                                           Institution.city.like('sal%')
                                           ).first()
print('inst_4')
if not inst_4:
    exit(1)


institution_list = [inst_1, inst_2, inst_3, inst_4, inst_11, inst_22, inst_33]
list_objects.extend(institution_list)


# Creating subjects.
PC = Subject(name='Physique-Chimie', abbr='PC')
PC.save()

SVT = Subject(name='Sciences de la Vie et de la Terre', abbr='SVT')
SVT.save()

MATH = Subject(name='Mathématiques', abbr='MATH')
MATH.save()

EN = Subject(name='Langue Anglaise', abbr='EN')
EN.save()

FR = Subject(name='Langue Française', abbr='FR')
FR.save()

AR = Subject(name='Langue et Littérature Arabe', abbr='AR')
AR.save()

ES = Subject(name='Langue Espagnole', abbr='ES')
ES.save()

HG = Subject(name='Histoire-Géographie', abbr='HG')
HG.save()

EI = Subject(name='Éducation Islamique', abbr='EI')
EI.save()

PH = Subject(name='Philosophie', abbr='PH')
PH.save()

EP = Subject(name='Éducation Physique', abbr='EP')
EP.save()

subject_list = [PC, SVT, MATH, EN, FR, AR, ES, HG, EI, PH, EP]
list_objects.extend(subject_list)

# Creating classes.
# High school
cc_english = Clas(name='Tronc commun (English)', alias='TC En')
cc_english.save()

cc_arabic = Clas(name='Tronc commun (Arabic)', alias='TC Ar')
cc_arabic.save()

cc_french = Clas(name='Tronc commun (French)', alias='TC Fr')
cc_french.save()

bac1_english = Clas(name='1ère année du Baccalauréat (English)',
                    alias='1BAC En')
bac1_english.save()

bac1_arabic = Clas(name='1ère année du Baccalauréat (Arabic)',
                   alias='1BAC Ar')
bac1_arabic.save()

bac1_french = Clas(name='1ère année du Baccalauréat (French)',
                   alias='1BAC Fr')
bac1_french.save()

bac2_english = Clas(name='2ème année du Baccalauréat (English)',
                    alias='2BAC En')
bac2_english.save()

bac2_arabic = Clas(name='2ème année du Baccalauréat (Arabic)',
                   alias='2BAC Ar')
bac2_arabic.save()

bac2_french = Clas(name='2ème année du Baccalauréat (French)',
                   alias='2BAC Fr')
bac2_french.save()


# Middle school
ac1 = Clas(name='1ère année du collège', alias='1AC')
ac1.save()

ac2 = Clas(name='2ème année du collège', alias='2AC')
ac2.save()

ac3 = Clas(name='3ème année du collège', alias='3AC')
ac3.save()


class_list = [cc_english, cc_arabic, cc_french,
              bac1_english, bac1_arabic, bac1_french,
              bac2_english, bac2_arabic, bac2_french,
              ac1, ac2, ac3]
list_objects.extend(class_list)

# Creating teachers.
teacher_1 = Teacher(first_name='Redouane', last_name='DRIHMIA',
                    email='red1@gmail.com', password='red1',
                    institution=inst_1.name, city=inst_1.city, gender='M',
                    phone_number='+212683984948', main_subject=PC.name)
teacher_1.save()

teacher_2 = Teacher(first_name='DRIHMIA', last_name='Redouane',
                    email='red2@gmail.com', password='red2',
                    institution=inst_11.name, city=inst_11.city, gender='M',
                    phone_number='+2126123456452', main_subject=PH.name)
teacher_2.save()

teacher_3 = Teacher(first_name='OMER', last_name='Mohamed',
                    email='omer1@gmail.com', password='omer1',
                    institution=inst_1.name, city=inst_1.city, gender='M',
                    phone_number='+212698765432', main_subject=HG.name)
teacher_3.save()

teacher_4 = Teacher(first_name='OMER', last_name='OMER',
                    email='omer2@gmail.com', password='omer2',
                    institution=inst_2.name, city=inst_2.city, gender='M',
                    phone_number='+212610928374', main_subject=EN.name)
teacher_4.save()

# set relations with teacher's objects.
# With subjects
PC.teachers.extend([teacher_1, teacher_3])
PC.save()
MATH.teachers.extend([teacher_1, teacher_3])
MATH.save()
PH.teachers.extend([teacher_2])
PH.save()
PH.teachers.extend([teacher_2])
PH.save()
AR.teachers.extend([teacher_2, teacher_4])
AR.save()
SVT.teachers.extend([teacher_3, teacher_4])
SVT.save()
HG.teachers.extend([teacher_3])
HG.save()
EI.teachers.extend([teacher_3])
EI.save()
FR.teachers.extend([teacher_4])
FR.save()
EN.teachers.extend([teacher_4])
EN.save()

# With institutions
inst_1.teachers.extend([teacher_1, teacher_3])
inst_1.save()
inst_11.teachers.append(teacher_2)
inst_11.save()
inst_2.teachers.append(teacher_4)
inst_2.save()
# With classes
cc_french.teachers.extend([teacher_1, teacher_2])
cc_french.save()
bac1_french.teachers.extend([teacher_1, teacher_3, teacher_4])
bac1_french.save()
bac2_french.teachers.extend([teacher_2, teacher_4])
bac2_french.save()


teacher_list = [teacher_1, teacher_2, teacher_3, teacher_4]
list_objects.extend(teacher_list)


# Creating students.
Marwan = Student(first_name='student_1', last_name='marwan',
                 email='marwan@gmail.com', password='marwan',
                 institution_id=inst_1.id, class_id=cc_french.id,
                 institution=inst_1.name, city=inst_1.city,
                 teacher_email='red1@gmail.com',
                 gender='M')
Marwan.save()
Hicham = Student(first_name='student_2', last_name='hicham',
                 email='hicham@gmail.com', password='hicham',
                 institution_id=inst_1.id, class_id=cc_french.id,
                 institution=inst_1.name, city=inst_1.city,
                 teacher_email='red1@gmail.com',
                 gender='M')
Hicham.save()
Fatima = Student(first_name='student_3', last_name='fatima',
                 email='fatima@gmail.com', password='fatima',
                 institution_id=inst_1.id, class_id=bac1_french.id,
                 institution=inst_1.name, city=inst_1.city,
                 teacher_email='red1@gmail.com',
                 gender='F')
Fatima.save()
Yasmine = Student(first_name='student_4', last_name='yasmine',
                  email='yasmine@gmail.com', password='yasmine',
                  institution_id=inst_1.id, class_id=bac1_french.id,
                  institution=inst_1.name, city=inst_1.city,
                  teacher_email='red2@gmail.com',
                  gender='F')   # incomplete
Yasmine.save()

student_list = [Marwan, Hicham, Fatima, Yasmine]
list_objects.extend(student_list)

# set relations with student's objects.
# With teachers.
teacher_1.students.extend([Marwan, Hicham, Fatima])
teacher_1.save()
teacher_2.students.extend([Marwan, Fatima])
teacher_2.students.extend([Yasmine])
teacher_2.save()
# With subjects.
for sub in subject_list:
    sub.students.extend(student_list)
    sub.save()

# Creating lessons.
# Commun Core
d1 = 'https://drive.google.com/file/d/1rnI4FRlHJxFqvNE_7M1o7jDDgfzJ782U/view'
cc_less_1 = Lesson(name='Periodic Classification of Chemical Elements',
                   download_link=d1,
                   description='lesson N6 for my student related to Chemistry',
                   subject_id=PC.id,
                   subject=PC.name,
                   teacher_id=teacher_1.id,
                   teacher=teacher_1.first_name + ' ' + teacher_1.last_name)
cc_less_1.save()


idd = '1n76fUTHscw7D-yjaAVaXFH8MY7bEDrkE/'
d2 = f'https://drive.google.com/file/d/{idd}view?usp=sharing'
cc_less_2 = Lesson(name='Direct electric current',
                   download_link=d2,
                   description='lesson N6 for my student related to Physics',
                   subject_id=PC.id,
                   subject=PC.name,
                   teacher_id=teacher_1.id,
                   public=False,
                   teacher=teacher_1.first_name + ' ' + teacher_1.last_name)
cc_less_2.save()

cc_lesson_list = [cc_less_1, cc_less_2]
list_objects.extend(cc_lesson_list)

# 1st year of the Baccalaureate
d1 = 'https://drive.google.com/file/d/14Ls7YwsYD9nFzYQ8KjlhGmi_E5wf61uM/view'
f_less_1 = Lesson(name='Magnetic Field Chapter',
                  download_link=d1,
                  description='lesson 11 for my 1st bac student',
                  subject_id=PC.id,
                  subject=PC.name,
                  teacher_id=teacher_1.id,
                  teacher=teacher_1.first_name + ' ' + teacher_1.last_name)
f_less_1.save()

idd = '14vaHIxaq3OdcLlphJkHV0mmnIriUUW8C'
d2 = f'https://drive.google.com/file/d/{idd}/view?usp=sharing'
f_less_2 = Lesson(name='Laplace\'s Force - out of the curriculum',
                  download_link=d2,
                  description='lesson 12 for my 1st bac student',
                  subject_id=PC.id,
                  subject=PC.name,
                  teacher_id=teacher_1.id,
                  public=False,
                  teacher=teacher_1.first_name + ' ' + teacher_1.last_name)
f_less_2.save()

f_lesson_list = [f_less_1, f_less_2]
list_objects.extend(f_lesson_list)

# Set relation with lesson's objects.
# With students
Marwan.lessons.extend(cc_lesson_list)
Marwan.save()
Hicham.lessons.extend(cc_lesson_list)
Hicham.save()
Fatima.lessons.extend(f_lesson_list)
Fatima.save()
Yasmine.lessons.extend(f_lesson_list)
Yasmine.save()
# With classes
cc_french.lessons.extend([cc_less_1, cc_less_2])
cc_french.save()
bac1_french.lessons.extend([f_less_1, f_less_2])
bac1_french.save()
# With institution.
inst_1.lessons.extend([cc_less_1, cc_less_2, f_less_1])
inst_1.save()
inst_2.lessons.extend([f_less_2])
inst_2.save()

# Setting general many to many relationship's information:
#  \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# Institution: ------------------------------
print("Do you wanna set the relationships now or latter")
print("Setting relationships takes triple time as the creating,")
print("Type anything to quit")
print("Note: You can do that using: ")
print("D='ACME' u='ur usr' h='ur host' p='ur pwd' python3 institution_relationship.py")
print("Wanna continue? Type 'yes'")
for_latter = 1
while(True):
    relation = input("")
    if  relation.strip().lower() == 'yes':
        break
    else:
        for_latter = 0
        break

if for_latter:
    print("""Setting relationship between institution \
          and thier classes and subjects""")
    count = 1
    institutions_db = storage.all(Institution).values()
    subjects_db = storage.all(Subject).values()
    classes_db = storage.all(Clas).values()
    number_institution = len(institutions_db)

    for institution in institutions_db:
        print(f"{(count/number_institution)*100:0.2f} of 100")
        institution.subjects.extend(subjects_db)
        institution.classes.extend(classes_db)
        institution.save()
        count += 1

# --------------------------------------------

# Commit al objects: ////////////////////////////////

# for obj in list_objects:
# obj.save()
storage.save()

# //////////////////////////////////////////////////


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
print("finished")
