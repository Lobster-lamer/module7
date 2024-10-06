def make_declension(number, declensions: tuple):
    if number % 10 == 1 and number // 10 != 1:
        return declensions[0]
    elif 5 > number % 10 > 1 != number // 10:
        return declensions[1]
    else:
        return declensions[2]


## Использование %:
# Переменные: количество участников первой команды (team1_num).
# Пример итоговой строки: "В команде Мастера кода участников: 5 ! "
team1_num = 5

declension = make_declension(team1_num, ("", "а", "ов"))

print("В команде Мастера кода %s участник%s!" % (team1_num, declension))

# Переменные: количество участников в обеих командах (team1_num, team2_num).
# Пример итоговой строки: "Итого сегодня в командах участников: 5 и 6 !"
team2_num = 6
declension = make_declension(team2_num, ("", "а", "ов"))

print("Итого сегодня в командах %s и %s участник%s!" % (team1_num, team2_num, declension))

## Использование format():
# Переменные: количество задач решённых командой 2 (score_2).
# Пример итоговой строки: "Команда Волшебники данных решила задач: 42 !"
score_2 = 42
declension = make_declension(score_2, ("у", "и", ""))

print("Команда Волшебники данных решила {0} задач{1}!".
      format(score_2, declension))

# Переменные: время за которое команда 2 решила задачи (team1_time).
# Пример итоговой строки: " Волшебники данных решили задачи за 18015.2 с !"
team1_time = 1552.512
team2_time = 2153.31451
print("Волшебники данных решили задачи за {:.1f}с!".
      format(team2_time))

## Использование f-строк:
# Переменные: количество решённых задач по командам: score_1, score_2
# Пример итоговой строки: "Команды решили 40 и 42 задач.”
score_1 = 40
print(f"Команды решили {score_1} и {score_2} задач{make_declension(score_2, ("у", "и", ""))}.")

# Переменные: исход соревнования (challenge_result).
# Пример итоговой строки: "Результат битвы: победа команды Мастера кода!"
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = "Победа команды Мастера кода!"
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = "Победа команды Волшебники Данных!"
else:
    challenge_result = "Ничья!"
print(f"Результат битвы: {challenge_result}")

# Переменные: количество задач (tasks_total) и среднее время решения (time_avg).
#  Пример итоговой строки: "Сегодня было решено 82 задач, в среднем по 350.4 секунды на задачу!."
tasks_total = score_1 + score_2
time_avg = (team1_time / score_1 + team2_time / score_2) / 2
print(f"Сегодня было решено {tasks_total} задач{make_declension(tasks_total, ("а", "и", ""))},"
      f" в среднем по {time_avg:.2f} секунды на задачу!.")

