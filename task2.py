'''
2. Пользователь вводит время в секундах. Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
'''

sec = int(input("Введите время в секундах: "))
sec = sec % (24 * 60 * 60)  # если количество секунд превышает сутки, убираем целые сутки
hours = sec // (60 * 60)  # определяем количество часов
sec = sec % (60 * 60)  # остаток после определения количества целых часов.
minutes = sec // 60  # определяем количество минут
sec = sec % 60  # секунды

print(f"Введённое время в формате чч:мм:сс соотвествует {hours:02}:{minutes:02}:{sec:02}")

