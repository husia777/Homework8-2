import json


def load_students():
    """
    Считывает студентов из файла
    :return:Возвращает данные о студентах
    """
    with open('students.json', 'rt') as file:
        students = json.load(file)
        return students




def load_professions():
    """
    Считывает профессии из файла
    :return: Возвращает данные о профессиях
    """
    with open('professions.json', 'rt') as file:
        professions = json.load(file)
        return professions

def get_student_by_pk(pk, students):
    """
    :param pk:ID студента
    :param students: Студенты
    :return:Возвращает студента соответствующему данному ID
    """
    for i  in range(len(students)):
        if students[i]['pk'] == pk:
            return students[i]

def get_skill_student_by_name(name, students):
    """
    :param name: Имя студента
    :param students: Файл с информацией о студентах
    :return: Возвращает навыки студента
    """
    for i  in range(len(students)):
        if students[i]['full_name'] == name:
            return students[i]['skills']

def get_profession_by_title(title, professions):
    """
    :param title: Название профессии
    :param professions: Файл с профессиями
    :return: Возвращает необходимые навыки для профессии
    """
    for i in range(len(professions)):
        if professions[i]['title'] == title:
            return professions[i]['skills']


def check_fitness(student, profession):
    """
    :param student: Выбор студента
    :param profession: Выбор профессии
    :return: Возвращает проф пригодность в виде словаря
    """
    #Скиллы ученика
    skill_student = get_skill_student_by_name(student, load_students())
    #Скиллы профессии
    skill_profession = get_profession_by_title(profession, load_professions())
    student_skills = set(skill_student)
    profession_skills = set(skill_profession)
    has = profession_skills.intersection(student_skills)
    lacks = profession_skills.difference(student_skills)
    fit_persent = len(has) / len(profession_skills) * 100
    available_knowledge = {
        "has": 'Необходимых знаний нет' if len(has) == 0 else has,
        "lacks": 'Нужные знания получены' if len(lacks) == 0 else lacks ,
        "fit_percent": fit_persent
        }
    return available_knowledge






