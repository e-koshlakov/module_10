class Vehicle:

    def __init__(self, vehicle_name, vehicle_mileage):
        self.name = vehicle_name
        self.mileage = vehicle_mileage
        self.vehicle_types_dict = {
            2: 'Мотоцикл',
            3: 'Трицикл',
            4: 'Автомобиль'
        }

    def get_vehicle_type(self, wheels_quantity):
        if wheels_quantity in self.vehicle_types_dict:
            return f'Это {self.vehicle_types_dict[wheels_quantity]} марки {self.name} '
        else:
            return 'Я не знаю таких ТС.'

    def get_vehicle_advice(self):
        vehicle_mileage_dict = {
            (0, 50000): f"Неплохо {self.name} можно брать.",
            (50001, 100000): f"{self.name} надо внимательно проверить.",
            (100001, 150000): f"{self.name} надо провести полную диагностику.",
            (150000, 9999999999999): f"{self.name} лучше не покупать."
        }
        for mileage, advice in vehicle_mileage_dict.items():
            if self.mileage in range(mileage[0], mileage[1]+1):
                return advice

        return 'Проблемы с пробегом.'


vehicle_1 = Vehicle('BMW', 0)
vehicle_2 = Vehicle('Mercedes-Benz', 50001)
vehicle_3 = Vehicle('Audi', 100001)
vehicle_4 = Vehicle('Volkswagen', 150001)
vehicle_5 = Vehicle('Лада', 999999)

print("Количество колес: 1")
print(vehicle_1.get_vehicle_type(1))
print("\nКоличество колес: 2")
print(vehicle_2.get_vehicle_type(2))
print("\nКоличество колес: 3")
print(vehicle_3.get_vehicle_type(3))
print("\nКоличество колес: 4")
print(vehicle_4.get_vehicle_type(4))
print("\nКоличество колес: 5")
print(vehicle_5.get_vehicle_type(5))

print("\nСовет по пробегу:")
print(f'Пробег: {vehicle_1.mileage}')
print(vehicle_1.get_vehicle_advice())
print("\nПробег: 50001")
print(vehicle_2.get_vehicle_advice())
print("\nПробег: 100001")
print(vehicle_3.get_vehicle_advice())
print("\nПробег: 150001")
print(vehicle_4.get_vehicle_advice())
print("\nПробег: 999999")
print(vehicle_5.get_vehicle_advice())