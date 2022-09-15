from functions import *

def main():
    while True:
        pk_input = input('Введите номер студента ')
        if pk_input == 'Выход':
            break
        try:
            numb_student, name_student, skills = get_student_by_pk(int(pk_input), load_students()).values()
            skills = ' '.join(skills)
            print(f'Студент {name_student}\nЗнает {skills}')
            prof_input = input(f'Выберите специальность для оценки студента {name_student} ')
            if prof_input == 'Выход':
                break
            try:
                get_profession_by_title(prof_input, load_professions())
                has, lacks, fit_percent = check_fitness(name_student, prof_input).values()
                print(f'Пригодность  {fit_percent} %')
                if has == 'Необходимых знаний нет':
                    print(f'{name_student}  {has}')
                else:
                    has = ' '.join(has)
                    print(f'{name_student} знает {has}')

                if lacks == 'Нужные знания получены':
                    print(f'{name_student}  {lacks}')
                else:
                    lacks = ' '.join(lacks)
                    print(f'{name_student} не знает {lacks}')
            except:
                print('У нас нет такой специальности')
        except:
            print('У нас нет такого студента')
            continue




if __name__ == '__main__':
    main()