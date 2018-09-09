# Оценки
# Создать список с оценками учеников разных классов школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
# Посчитать и вывести средний балл по всей школе.
# Посчитать и вывести средний балл по каждому классу.

students = [{'school_class': '1a', 'scores': [3, 4, 4, 5, 2]}, {'school_class': '2a', 'scores': [5, 4, 3, 5, 4]},
            {'school_class': '2b', 'scores': [5, 3, 3, 5, 2]}, {'school_class': '3a', 'scores': [2, 4, 3, 3, 5]},
            {'school_class': '4a', 'scores': [5, 5, 5, 5, 4]}, {'school_class': '4b', 'scores': [3, 3, 5, 5, 2]}]
unit_in_school = 0
all_scores = []
for s in students:
    scores = s['scores']
    for score in scores:
        unit_in_school += 1
        all_scores.append(score)
result = sum(all_scores) / unit_in_school
print('The average score in all school:', round(result, 2))


for sch_class in students:
    unit_in_class = 0
    all_scores_in_class = []
    for score in sch_class['scores']:
        unit_in_class += 1
        all_scores_in_class.append(score)
    result = sum(all_scores_in_class) / unit_in_class
    print('The average score in class', sch_class['school_class'] + ':', round(result, 2))
