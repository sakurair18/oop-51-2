from faker import Faker # Импортируем модуль из библиотеки

fake = Faker() # Создаем экземпляр модуля

print(fake.name())  # Вызываем экземпляр генерации имени
print(fake.address())  # Вызываем экземпляр генерации адреса

"""Это Python библиотека для генерации фальшивых данных таких как адреса, имена и т.д
Полезна для тестирования заполнения базы данных"""

