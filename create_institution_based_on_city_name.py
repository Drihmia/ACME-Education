"""
Create institution based on city name
"""

from models.institution import Institution
from models.city import City
from models.subject import Subject
from models.clas import Clas
from models import storage


def create_institution_based_on_city_id(city_id, institution_name):
    """
    Create institution based on city name
    """
    city_obj = storage.query(City).filter(City.id == city_id).first()

    if city_obj is None:
        return None
    institution_obj = Institution(name=institution_name, city_id=city_obj.id, city=city_obj.name)
    if institution_obj is not None:
        institution_obj.save()
    return institution_obj


def find_institution_by_name_city_id(institution_name, city_id):
    """
    Find institution by name and city id
    """
    institution_obj = storage.query(Institution).filter(Institution.name == institution_name,
                                                        Institution.city_id == city_id).first()
    if institution_obj is not None:
        return institution_obj
    return None

def print_info_from_dict(Object_dict):
    """
    Print information from dictionary
    """
    for key, value in Object_dict.items():
        print("{}: {}".format(key, value))

def assign_subjects_to_institution(institution_obj, subjects):
    """
    Assign subjects to institution
    """
    for subject in subjects:
        institution_obj.subjects.append(subject)
    try:
        institution_obj.save()
    except Exception as e:
        print(e)
        return None

    return institution_obj.to_dict()

def assign_classes_to_institution(institution_obj, classes):
    """
    Assign classes to institution
    """
    for class_ in classes:
        institution_obj.classes.append(class_)
    try:
        institution_obj.save()
    except Exception as e:
        print(e)
        return None

    return institution_obj.to_dict()

if __name__ == "__main__":

    city_id_sale = "16694017-e108-4daa-a6ab-a1f77dbbd419"
    institution_name = "Ecole prive Anjad Alfikr"

    institution_obj = find_institution_by_name_city_id(institution_name, city_id_sale)
    if institution_obj:
        print("** Institution already exists **")
    else:
        print(" ** Institution Creation... **")
        institution_obj = create_institution_based_on_city_id(city_id_sale , institution_name)
        print("Institution created successfully")

    if institution_obj:
        print("Institution details: ")
        print_info_from_dict(institution_obj.to_dict())
    else:
        print("Failed to create institution")
        exit(1)

    # Assign subjects to institution
    subjects = [storage.query(Subject).filter(Subject.name == "Physique-Chimie").first()]
    assign_subjects_to_institution(institution_obj, subjects)

    # Assign classes to institution
    classes = [
        storage.query(Clas).filter(Clas.name == "Tronc commun (French)").first(),
        storage.query(Clas).filter(Clas.name == "1ère année du Baccalauréat (French)").first()
    ]
    assign_classes_to_institution(institution_obj, classes)

